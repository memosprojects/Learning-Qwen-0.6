# Rung 06 — The allowed set

**Idea:** stop asking the model to behave. Instead, look at its scores and simply
**refuse every token you don't want.**

You have three legal function names. Whatever the first token of the name is, it
must be the first token of *one of those names*. Every other token in the 150,000
is illegal right now. That set of legal token ids is the **allowed set**.

This rung does one step: it builds the allowed set for the *first* token of the
name, and picks the highest-scoring token **inside that set** — ignoring the
model's actual favourite.

## Run it

```bash
uv run python rungs/06-the-allowed-set/rung.py
```

## What you should see

Two things, side by side:

- The token the model *wanted* most (its top logit). It is usually junk from the
  model's point of view of your task — a fence, a space, a quote.
- The token you *allowed* it to have: the highest-scoring token that actually
  starts one of your names.

You just overrode the model. It wanted one thing; you forced it into your set and
took the best option available there. Nothing here can produce an illegal first
token, because illegal tokens were never candidates.

## Turn the knobs

- `names` — change the list. The allowed set is rebuilt from whatever you put
  here. Add a name, remove one, watch the allowed first-tokens change.
- `request` — the request sits in the prompt, so it still steers *which* allowed
  token scores highest. Ask for a greeting and see if the allowed pick shifts.

You are done when you can explain what "allowed set" means and how filtering the
logits is different from prompting.
