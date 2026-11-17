"""Rung 08 — The enforcer.

Loop the allowed set: at each step keep only tokens that continue a legal name,
pick the best-scoring one, append, repeat until the name is complete, then close
the JSON. The output is a valid function call every single time.
"""
from llm_sdk import Small_LLM_Model


def build_prefix(request: str, names: list[str]) -> str:
    return (
        f"You can call these functions: {', '.join(names)}.\n"
        f"Request: {request}\n"
        "Reply with JSON only.\n"
        '{"name": "'
    )


def enforce_name(model: Small_LLM_Model, request: str,
                 names: list[str]) -> str:
    """Constrained-decode exactly one legal name and return valid JSON."""
    name_to_ids = {name: model.encode(name)[0].tolist() for name in names}
    prefix_ids = model.encode(build_prefix(request, names))[0].tolist()

    def allowed_next(chosen: list[int]) -> set[int]:
        allowed = set()
        for ids in name_to_ids.values():
            if ids[:len(chosen)] == chosen and len(chosen) < len(ids):
                allowed.add(ids[len(chosen)])
        return allowed

    chosen: list[int] = []
    while True:
        allowed = allowed_next(chosen)
        if not allowed:  # no name extends further: the name is complete.
            break
        logits = model.get_logits_from_input_ids(prefix_ids + chosen)
        best = max(allowed, key=lambda token_id: logits[token_id])
        chosen.append(best)
        print(f"    +{best:<8} {model.decode([best])!r:<16} "
              f"-> {model.decode(chosen)!r}")

    name = model.decode(chosen)
    return f'{{"name": "{name}"}}'


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    names = ["fn_add_numbers", "fn_greet", "fn_reverse_string"]  # KNOB
    request = "What is the sum of 40 and 2?"  # KNOB: change the request.

    print(f"REQUEST: {request!r}")
    print("Building the name, one allowed token at a time:")
    result = enforce_name(model, request, names)
    print()
    print(f"VALID FUNCTION CALL: {result}")


if __name__ == "__main__":
    main()
