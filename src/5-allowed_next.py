from llm_sdk import Small_LLM_Model


model = Small_LLM_Model(device="cpu")

text = "fn_"

current_ids = model.encode(text)[0].tolist()
current_text = model.decode(current_ids)

allowed_names = [
    "fn_add_numbers",
    "fn_greet",
    "fn_reverse_string",
]

matches = [
    name for name in allowed_names
    if name.startswith(current_text)
]
print("Matches found:")
for match in sorted(matches):
    print(f"{match}")
