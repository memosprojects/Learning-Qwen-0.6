"""Rung 01 — Tokens.

Text becomes numbers (encoding) and comes back (decoding). A token is a chunk,
not a letter and not a word. Watch where the tokenizer cuts.
"""
from llm_sdk import Small_LLM_Model


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    # KNOB: change these. Try the same word with and without a leading space,
    # different cases, numbers of different sizes.
    texts = [
        "hello",
        " hello",
        "Hello",
        "What is the sum of 2 and 3?",
    ]

    for text in texts:
        ids = model.encode(text)[0].tolist()
        decoded = model.decode(ids)
        print(f"TEXT   : {text!r}")
        print(f"IDS    : {ids}")
        print(f"DECODE : {decoded!r}")
        print("TOKENS :")
        for token_id in ids:
            piece = model.decode([token_id])
            print(f"    {token_id:<8} -> {piece!r}")
        print()

    # Watch the text rebuild itself one token at a time. This is the whole
    # reason both directions exist: encode to speak to the model, decode to
    # read it back.
    print("=" * 60)
    print("Rebuilding one token at a time:")
    sentence = "What is the sum of 2 and 3?"  # KNOB: change this too.
    ids = model.encode(sentence)[0].tolist()
    growing: list[int] = []
    for token_id in ids:
        growing.append(token_id)
        piece = model.decode([token_id])
        partial = model.decode(growing)
        print(f"    +{token_id:<8} piece={piece!r:<14} so far={partial!r}")


if __name__ == "__main__":
    main()
