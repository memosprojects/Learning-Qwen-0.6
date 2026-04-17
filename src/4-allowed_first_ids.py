from llm_sdk import Small_LLM_Model


model = Small_LLM_Model(device="cpu")

allowed_names = [
    "fn_add_numbers",
    "fn_greet",
    "fn_reverse_string",
]

allowed_first_ids = set()

for name in allowed_names:
    ids = model.encode(name)[0].tolist()
    if ids:
        allowed_first_ids.add(ids[0])

print("ALLOWED FIRST TOKEN IDS:", allowed_first_ids)

for token_id in sorted(allowed_first_ids):
    print(token_id, repr(model.decode([token_id])))
