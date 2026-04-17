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


prefix = '{"name":"'
prefix_ids = model.encode(prefix)[0].tolist()

current_name_ids: list[int] = []

for step in range(10):
    input_ids = prefix_ids + current_name_ids
    logits = model.get_logits_from_input_ids(input_ids)

    allowed_ids = allowed_next_name_token_ids(current_name_ids)
    if not allowed_ids:
        break

    next_id = max(allowed_ids, key=lambda token_id: logits[token_id])
    current_name_ids.append(next_id)

    print("STEP:", step + 1)
    print("NEXT TOKEN:", next_id, repr(model.decode([next_id])))
    print("NAME NOW  :", repr(model.decode(current_name_ids)))
    print()
