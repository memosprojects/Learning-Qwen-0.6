"""Rung 04 — The model can't be trusted.

Ask the model to produce a function call as JSON and watch it fail: markdown
fences, invented keys, answering the question instead of naming a function, and
greedy repetition. This failure is the reason the rest of the ladder exists.
"""
from llm_sdk import Small_LLM_Model


def greedy(model: Small_LLM_Model, input_ids: list[int], n: int) -> str:
    """Generate n tokens greedily and return only the new text (Rung 03)."""
    ids = list(input_ids)
    for _ in range(n):
        logits = model.get_logits_from_input_ids(ids)
        ids.append(max(range(len(logits)), key=lambda i: logits[i]))
    return model.decode(ids[len(input_ids):])


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    names = ["fn_add_numbers", "fn_greet", "fn_reverse_string"]
    # KNOB: change the request. No phrasing makes the output reliably valid.
    request = "What is the sum of 40 and 2?"
    # KNOB: let it run longer to watch it ramble or loop.
    n_tokens = 40

    prompt = (
        f"You can call these functions: {', '.join(names)}.\n"
        f"Request: {request}\n"
        'Reply with JSON only, like {"name": ...}.\n'
    )

    print(f"REQUEST: {request!r}")
    print(f"PROMPT:\n{prompt}")
    print("MODEL OUTPUT:")
    print(greedy(model, model.encode(prompt)[0].tolist(), n_tokens))
    print()
    print("Look at what went wrong. That is this rung's whole lesson.")


if __name__ == "__main__":
    main()
