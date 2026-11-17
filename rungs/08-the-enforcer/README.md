# Rung 08 — The enforcer

**Idea:** put Rungs 06 and 07 in a loop. At every step, score the tokens, keep
only the allowed-next set, pick the best one, append it, repeat — until the name
is complete. Then close the JSON yourself.

The result is a function call that is **valid every single time**, no matter what
the model would have done on its own. This is constrained decoding.

## Run it

```bash
uv run python rungs/08-the-enforcer/rung.py
```

## What you should see

The name being built one allowed token at a time, then the final string:

```
{"name": "fn_add_numbers"}
```

Guaranteed valid JSON. Guaranteed one of your names. Compare this to Rung 04,
where the same model, asked the same thing, gave you fenced, invented, looping
garbage. Same model. The only difference is that here *you* decided what was
allowed at each step.

Look back at Rung 05: in the costume, the model's strongest instinct was to emit
`<think>`. The enforcer does not care what the model wants. It overrides even
that. The guarantee comes from the structure you impose, not from the model's
cooperation.

## Turn the knobs

- `request` — change it and watch which name gets built. The allowed set is the
  same three names every time; the *request* is what makes the scores favour one.
- `names` — change the legal set. The output is always a valid call to one of
  whatever you list here.

You are done when you can explain how looping the allowed set guarantees valid
output, and why the request still controls *which* valid output you get.
