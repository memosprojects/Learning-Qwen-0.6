from llm_sdk import Small_LLM_Model


model = Small_LLM_Model(device="cpu")

text = 'What is the sum of 2 and 3?'
ids = model.encode(text)[0].tolist()

print("FULL TEXT:", repr(text))
print("FULL IDS :", ids)
print()

current_ids = []
for token_id in ids:
    current_ids.append(token_id)
    piece = model.decode([token_id])
    partial = model.decode(current_ids)

    print(
        f"id={token_id:<8} piece={repr(piece):<20} partial={repr(partial)}"
    )