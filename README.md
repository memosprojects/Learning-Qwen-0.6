# Learning Qwen

A hands-on onramp to the 42 project *call me maybe*.

This repository does **not** solve *call me maybe*. It teaches the ideas the
project rests on, one small runnable step at a time, so that by the end you can
sit down and design your own function-calling solution and defend every line of
it.

## What you will learn

By running (and changing) the code here, you will understand:

- **Tokens** — why a language model cannot see text, only numbers.
- **Encoding and decoding** — the round trip between text and those numbers, and
  why you constantly need both.
- **Logits** — the score the model assigns to every possible next token.
- **Generation** — that producing text is just picking a token, appending it,
  and asking again.
- **Constrained decoding** — forcing the model to stay inside a structure you
  choose, by filtering those scores before you pick.

Everything is built on the `Small_LLM_Model` wrapper in [`llm_sdk/`](llm_sdk/) —
the same SDK the assignment gives you. You will only ever use its public methods:
`encode`, `decode`, `get_logits_from_input_ids`, and `get_path_to_vocab_file`.

## How it is structured

The repository is a **ladder**. Each folder under [`rungs/`](rungs/) is one step
that introduces exactly one idea. Climb them in order:

| Rung | Idea |
|------|------|
| `00-first-contact`        | Load the model. Make the download happen. |
| `01-tokens`               | Text becomes numbers and comes back. |
| `02-logits`               | One question, a score for every token. |
| `03-generation`           | Pick, append, ask again — that's all it is. |
| `04-the-model-cant-be-trusted` | Ask for a function call. Watch it fail. |
| `05-the-costume`          | Try the proper chat format. Watch it still fail. |
| `06-the-allowed-set`      | Forbid every token except the ones you allow. |
| `07-staying-on-the-path`  | Allow only what continues a real name. |
| `08-the-enforcer`         | Loop it. Get valid output every single time. |
| `09-function-calling`     | Swap the request, watch the choice change. |

Each folder has a `README.md` (read it first) and a `rung.py` (run it, then
change it). Look for `# KNOB:` comments in the code — those mark the places you
are meant to change to see what happens.

## Running it

> **This is slow, on purpose.** The ladder runs on 42 school computers, which
> have no usable GPU, so everything runs on CPU in full precision. That keeps the
> results identical on every machine — what a README says you should see is what
> you will actually see. A generation loop grinding out one token at a time is
> part of the lesson about what generation costs.

The model is about 1.4 GB. On a 42 machine your home directory quota cannot hold
that plus the Python environment, so work inside `sgoinfre`:

```bash
# clone into sgoinfre, not your home directory
cd /sgoinfre/$USER
git clone <this-repo> learning-qwen
cd learning-qwen

# send the model download to sgoinfre too (this is the step people forget:
# the download location is decided by HF_HOME, not by where you cloned)
export HF_HOME=/sgoinfre/$USER/huggingface

# install dependencies
uv sync

# climb the first rung
uv run python rungs/00-first-contact/rung.py
```

The first run downloads the model and takes a few minutes. That is normal —
nothing is wrong.

## Resources

- Qwen3-0.6B model card: https://huggingface.co/Qwen/Qwen3-0.6B
- Hugging Face tokenizer summary: https://huggingface.co/docs/transformers/tokenizer_summary
- A visual guide to BPE tokenization: https://tiktokenizer.vercel.app/
