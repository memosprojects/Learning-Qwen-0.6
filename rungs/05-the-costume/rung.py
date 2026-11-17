"""Rung 05 — The costume.

Qwen3 expects a chat format (the "costume"): special tokens marking the user
and assistant turns. Putting the model in its costume does not fix Rung 04 — it
wants to think out loud, and even silenced it still won't emit valid structure.
The lesson: prompting is not the lever.
"""
from llm_sdk import Small_LLM_Model


def greedy(model: Small_LLM_Model, input_ids: list[int], n: int) -> str:
    ids = list(input_ids)
    for _ in range(n):
        logits = model.get_logits_from_input_ids(ids)
        ids.append(max(range(len(logits)), key=lambda i: logits[i]))
    return model.decode(ids[len(input_ids):])


def build_prompt(request: str, names: list[str], use_costume: bool,
                 close_thinking: bool) -> str:
    """Build either a raw prompt or the chat-format ("costume") prompt."""
    instruction = (
        f"You can call these functions: {', '.join(names)}. "
        f"Reply with JSON only. {request}"
    )
    if not use_costume:
        return instruction + '\n{"name": "'

    prompt = (
        f"<|im_start|>user\n{instruction}<|im_end|>\n"
        "<|im_start|>assistant\n"
    )
    if close_thinking:
        # An empty think block tells the model it is done reasoning.
        prompt += "<think>\n\n</think>\n\n"
    return prompt


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    names = ["fn_add_numbers", "fn_greet", "fn_reverse_string"]
    request = "What is the sum of 40 and 2?"  # KNOB: change the request.
    use_costume = True      # KNOB: False = raw text, True = chat format.
    close_thinking = False  # KNOB: True = silence the <think> block.

    prompt = build_prompt(request, names, use_costume, close_thinking)

    print(f"use_costume={use_costume}  close_thinking={close_thinking}")
    print(f"REQUEST: {request!r}")
    print(f"PROMPT:\n{prompt!r}\n")
    print("MODEL OUTPUT:")
    print(greedy(model, model.encode(prompt)[0].tolist(), 40))


if __name__ == "__main__":
    main()
