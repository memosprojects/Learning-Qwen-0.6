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

name_to_ids = {
    name: model.encode(name)[0].tolist()
    for name in allowed_names
}


def allowed_next_name_token_ids(current_name_ids: list[int]) -> set[int]:
    allowed_next = set()

    for name, ids in name_to_ids.items():
        if ids[:len(current_name_ids)] == current_name_ids:
            if len(current_name_ids) < len(ids):
                allowed_next.add(ids[len(current_name_ids)])

    return allowed_next


tests = [
    [],
    name_to_ids["fn_add_numbers"][:1],
    name_to_ids["fn_add_numbers"][:2],
]

for current in tests:
    next_ids = allowed_next_name_token_ids(current)

    print("CURRENT IDS:", current)
    print("CURRENT TXT:", repr(model.decode(current)))
    print("ALLOWED NEXT:")
    for token_id in sorted(next_ids):
        print("   ", token_id, repr(model.decode([token_id])))
    print()