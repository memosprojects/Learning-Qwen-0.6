"""Rung 06 — The allowed set.

Instead of hoping the model behaves, filter its scores. The first token of the
name must start one of the legal names; every other token is illegal. Build that
allowed set and pick the best token inside it, overriding the model's favourite.
"""
from llm_sdk import Small_LLM_Model


def build_prefix(request: str, names: list[str]) -> str:
    """The context: the request, plus the JSON opened up to the name value."""
    return (
        f"You can call these functions: {', '.join(names)}.\n"
        f"Request: {request}\n"
        "Reply with JSON only.\n"
        '{"name": "'
    )


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    # KNOB: the legal function names. The allowed set is built from these.
    names = ["fn_add_numbers", "fn_greet", "fn_reverse_string"]
    # KNOB: the request. It steers which allowed token scores highest.
    request = "What is the sum of 40 and 2?"

    # The allowed FIRST token: the first token id of each name's encoding.
    allowed_first = sorted({model.encode(n)[0].tolist()[0] for n in names})

    prefix_ids = model.encode(build_prefix(request, names))[0].tolist()
    logits = model.get_logits_from_input_ids(prefix_ids)

    wanted = max(range(len(logits)), key=lambda i: logits[i])
    allowed_pick = max(allowed_first, key=lambda i: logits[i])

    print(f"REQUEST: {request!r}\n")
    print("Allowed first tokens (what may legally start the name):")
    for token_id in allowed_first:
        print(f"    id={token_id:<8} {model.decode([token_id])!r}  "
              f"score={logits[token_id]:.3f}")
    print()
    print(f"Model WANTED : id={wanted:<8} {model.decode([wanted])!r}  "
          f"score={logits[wanted]:.3f}")
    print(f"We ALLOW     : id={allowed_pick:<8} "
          f"{model.decode([allowed_pick])!r}  score={logits[allowed_pick]:.3f}")
    print("\nWe overrode the model. Its favourite was never a candidate.")


if __name__ == "__main__":
    main()
