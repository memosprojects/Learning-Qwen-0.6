import json
from pathlib import Path
from llm_sdk import Small_LLM_Model


model = Small_LLM_Model(device="cpu")

vocab_path = Path(model.get_path_to_vocab_file())
with vocab_path.open("r", encoding="utf-8") as file:
    vocab = json.load(file)

id_to_token = {token_id: token for token, token_id in vocab.items()}

prompt = '{"name":"name","type":"'
input_ids = model.encode(prompt)[0].tolist()
logits = model.get_logits_from_input_ids(input_ids)

top_ids = sorted(
    range(len(logits)),
    key=lambda token_id: logits[token_id],
    reverse=True,
)[:10]

print("PROMPT:", repr(prompt))
print("ENCODED IDS:", input_ids)
print()

for rank, token_id in enumerate(top_ids, start=1):
    vocab_token = id_to_token.get(token_id, "<not found>")
    decoded_piece = model.decode([token_id])
    score = logits[token_id]

    print(
        f"{rank:>2}. id={token_id:<8} "
        f"logit={score:>12.4f} "
        f"vocab={repr(vocab_token):<20} "
        f"decode={repr(decoded_piece)}"
    )