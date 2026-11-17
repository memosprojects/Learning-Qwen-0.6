# Rung 04 — The model can't be trusted

**Idea:** now we ask the model to do the actual *call me maybe* job — read a
request and reply with a function call as JSON — and we watch it fail.

This is the most important rung on the ladder. Everything after it is a fix for
what you see here. So look carefully at *how* it fails.

## Run it

```bash
uv run python rungs/04-the-model-cant-be-trusted/rung.py
```

## What you should see

The model does **not** cleanly give you `{"name": ...}`. Watch for all of these:

- It wraps the JSON in markdown fences (```` ```json ````). That is prose around
  the JSON — not valid JSON on its own.
- It invents keys that were never asked for: `"result"`, `"sum"`, and the like.
- It just **answers the question** — it returns `42` — when the whole point of a
  function call is to say *which function to call*, not to compute the answer.
- Under greedy decoding it often gets stuck repeating the same block forever.

Here is the trap: the model is not stupid. It usually gets the *answer* right.
It simply cannot be trusted to produce the exact *structure* you need. Knowing
the answer and emitting a valid function call are two different things, and the
model is only good at the first.

## Turn the knobs

- `request` — try the sum, a greeting, a string reversal. Does any phrasing make
  it reliably produce clean, schema-correct JSON? (It won't.)
- `n_tokens` — let it run longer and watch it ramble or loop.

You are done when you can state precisely what goes wrong. "It's bad at JSON" is
too vague. Name the specific failures: fences, invented keys, answering instead
of naming, repetition.
