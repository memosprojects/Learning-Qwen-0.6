from llm_sdk import Small_LLM_Model


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    texts = [
        "hello",
        " hello",
        "Hello",
        "What is the sum of 2 and 3?",
        '{{}"name":"fn_greet"}',
    ]

    for text in texts:
        encoded = model.encode(text)
        ids = encoded[0].tolist()
        decoded = model.decode(ids)
        print("TEXT   :", repr(text))
        print("IDS    :", ids)
        print("DECODE :", repr(decoded))
        print("TOKENS :")

        for token_id in ids:
            token_text = model.decode([token_id])
            print(f"  {token_id:<8} -> {token_text}")

        print()


if __name__ == "__main__":
    main()
