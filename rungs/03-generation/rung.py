"""Rung 03 — Generation.

Generating text is a loop: score the next token, take the best one, append it,
repeat. Taking the single best token every time is "greedy" decoding.
"""
from llm_sdk import Small_LLM_Model


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    # KNOB: the starting prompt.
    prompt = "Once upon a time"
    # KNOB: how many tokens to generate. Bigger = slower (this runs on CPU).
    n_tokens = 20

    ids = model.encode(prompt)[0].tolist()
    start = len(ids)

    print(f"PROMPT: {prompt!r}")
    print("Generating (one token per step):")

    for step in range(1, n_tokens + 1):
        logits = model.get_logits_from_input_ids(ids)
        # Greedy: the next token is simply the highest-scoring one.
        next_id = max(range(len(logits)), key=lambda i: logits[i])
        ids.append(next_id)
        print(f"    step {step:>2}: +{next_id:<8} {model.decode([next_id])!r}")

    print()
    print(f"CONTINUATION: {model.decode(ids[start:])!r}")


if __name__ == "__main__":
    main()
