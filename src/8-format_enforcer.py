import json
from pathlib import Path
from llm_sdk import Small_LLM_Model


model = Small_LLM_Model(device="cpu")

allowed_names = [
    "fn_add_numbers",
    "fn_greet",
    "fn_reverse_string",
]

name_to_ids = {
    name: model.encode(name)[0].tolist()
    for name in allowed_names
}

prefix = '{"name":"'
suffix = '"}'


def get_name_matches(current_name_ids: list[int]) -> list[str]:
    matches = []

    for name, full_ids in name_to_ids.items():
        if full_ids[:len(current_name_ids)] == current_name_ids:
            matches.append(name)

    return matches


def allowed_next_name_token_ids(current_name_ids: list[int]) -> set[int]:
    allowed_next = set()

    for full_ids in name_to_ids.values():
        if full_ids[:len(current_name_ids)] == current_name_ids:
            if len(current_name_ids) < len(full_ids):
                allowed_next.add(full_ids[len(current_name_ids)])

    return allowed_next


def is_name_complete(current_name_ids: list[int]) -> bool:
    for full_ids in name_to_ids.values():
        if full_ids == current_name_ids:
            return True
    return False


def completed_name(current_name_ids: list[int]) -> str | None:
    for name, full_ids in name_to_ids.items():
        if full_ids == current_name_ids:
            return name
    return None


def main() -> None:
    prefix_ids = model.encode(prefix)[0].tolist()
    suffix_ids = model.encode(suffix)[0].tolist()

    current_name_ids: list[int] = []

    print("PREFIX:", repr(prefix))
    print("PREFIX IDS:", prefix_ids)
    print()

    step = 0

    while True:
        step += 1

        if is_name_complete(current_name_ids):
            final_ids = prefix_ids + current_name_ids + suffix_ids
            final_text = model.decode(final_ids)

            print(f"STEP {step}")
            print("NAME COMPLETE:", repr(completed_name(current_name_ids)))
            print("ADDING SUFFIX:", repr(suffix))
            print("FINAL TEXT   :", repr(final_text))
            break

        input_ids = prefix_ids + current_name_ids
        logits = model.get_logits_from_input_ids(input_ids)

        allowed_ids = allowed_next_name_token_ids(current_name_ids)
        if not allowed_ids:
            print("No valid next tokens. Dead end.")
            break

        next_id = max(allowed_ids, key=lambda token_id: logits[token_id])
        current_name_ids.append(next_id)

        print(f"STEP {step}")
        print("CURRENT NAME IDS :", current_name_ids)
        print("CURRENT NAME TEXT:", repr(model.decode(current_name_ids)))
        print("MATCHES          :", get_name_matches(current_name_ids))
        print("NEXT TOKEN       :", next_id, repr(model.decode([next_id])))
        print()


if __name__ == "__main__":
    main()
