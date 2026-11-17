# Rung 02 — Logits

**Idea:** you hand the model a sequence of tokens, and it hands back a **score
for every single token in its vocabulary** — its opinion about what should come
next. Those scores are called *logits*.

The vocabulary is huge (about 150,000 tokens). The model does not pick one for
you here. It just scores all of them. A higher score means "more likely to come
next, given everything so far."

## Run it

```bash
uv run python rungs/02-logits/rung.py
```

## What you should see

Your prompt, and then the ten highest-scoring next tokens, each with its id, its
score, and the text it decodes to. The top token is the model's single best
guess for what comes next.

## Turn the knobs

The `prompt` is the knob.

- Try `"The capital of France is"`. Is the top token what you expect?
- Try `"2 + 2 ="`.
- Try just `"The"` versus a long, specific sentence. Do the top scores get more
  confident (spread further apart) as the prompt gives more to go on?

Notice: the model scores *the same* set of tokens no matter what you type. What
changes is the *ordering*. That ordering is the only place your prompt's meaning
shows up — a fact that becomes the whole game a few rungs from now.

You are done when you can explain what a logit is and what "the model's next-token
distribution" means.
