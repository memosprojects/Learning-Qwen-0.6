"""Rung 02 — Logits.

Give the model a prompt; it scores every token in the vocabulary as a possible
next token. Here we look at the ten highest-scoring ones.
"""
from llm_sdk import Small_LLM_Model


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    # KNOB: change the prompt and see how the ranking of next tokens changes.
    prompt = "The capital of France is"

    input_ids = model.encode(prompt)[0].tolist()
    logits = model.get_logits_from_input_ids(input_ids)

    # Rank every token id by its score, highest first, and keep the top ten.
    top_ids = sorted(
        range(len(logits)),
        key=lambda token_id: logits[token_id],
        reverse=True,
    )[:10]

    print(f"PROMPT      : {prompt!r}")
    print(f"VOCAB SIZE  : {len(logits)} tokens were all scored")
    print()
    print("Top 10 candidates for the next token:")
    for rank, token_id in enumerate(top_ids, start=1):
        piece = model.decode([token_id])
        score = logits[token_id]
        print(f"    {rank:>2}. id={token_id:<8} score={score:>10.3f}  "
              f"{piece!r}")


if __name__ == "__main__":
    main()
