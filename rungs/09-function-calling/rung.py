"""Rung 09 — Function calling.

The enforcer always produces a valid call. The point of this rung is that a
different request produces a different call, from the same code and the same
names. Choosing the name in response to the request is the whole act.
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
        if not allowed:
            break
        logits = model.get_logits_from_input_ids(prefix_ids + chosen)
        chosen.append(max(allowed, key=lambda token_id: logits[token_id]))

    return f'{{"name": "{model.decode(chosen)}"}}'


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    names = ["fn_add_numbers", "fn_greet", "fn_reverse_string"]  # KNOB
    # KNOB: add your own requests, including ambiguous ones.
    requests = [
        "What is the sum of 40 and 2?",
        "Greet shrek",
        "Reverse the string 'hello'",
    ]

    print("Same code, same names, different requests:\n")
    for request in requests:
        result = enforce_name(model, request, names)
        print(f"    {request!r:<38} ->  {result}")


if __name__ == "__main__":
    main()
