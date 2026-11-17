"""Rung 00 — First contact.

Load the model and prove the whole stack works. Running this the first time
downloads ~1.4 GB; that is the point of doing it here and now.
"""
from llm_sdk import Small_LLM_Model


def main() -> None:
    # We force CPU everywhere on this ladder. School machines have no usable
    # GPU, and CPU + full precision gives identical results on every machine,
    # so what a README promises is what you actually see.
    print("Loading the model (first time downloads ~1.4 GB)...")
    model = Small_LLM_Model(device="cpu")
    print("Model loaded.")

    # A tiny sanity check: text goes in, numbers come out.
    word = "mellow hello"  # KNOB: try any word here.
    ids = model.encode(word)[0].tolist()
    print(f"encode({word!r}) -> {ids}")
    decoded = model.decode(ids)
    print(f"decoded: {decoded}")

    print("\nIf you can read this line, everything downstream will run.")


if __name__ == "__main__":
    main()
