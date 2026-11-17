# Rung 09 — Function calling

**Idea:** this is what "function calling" actually means. The enforcer from Rung
08 always produces a valid call — but the *point* is that a **different request
produces a different call**, from the exact same code and the exact same list of
names.

Choosing the right function *is* the whole job. There is no function body here,
nothing gets executed. Picking the name in response to the request is the entire
act — that is all *call me maybe* asks the model to do for the name.

## Run it

```bash
uv run python rungs/09-function-calling/rung.py
```

## What you should see

Several requests, each run through the same enforcer, printed side by side:

```
"What is the sum of 40 and 2?"   ->  {"name": "fn_add_numbers"}
"Greet shrek"                    ->  {"name": "fn_greet"}
"Reverse the string 'hello'"     ->  {"name": "fn_reverse_string"}
```

The output for any single request looks just like Rung 08 — a JSON string. The
lesson is only visible in the *comparison*: same code, same allowed set, and yet
the chosen name tracks the request. That is the logits doing their job inside the
structure you enforce. The allowed set guarantees the *shape*; the request
decides *which* shape.

## Turn the knobs

- `requests` — add your own. Try one that is ambiguous ("do something with
  numbers and a name") and see which function it lands on. Try one that matches
  no function well and watch it pick the closest anyway — the enforcer always
  returns *some* valid name, even when none truly fits.

## Where the ladder ends

You now understand: tokens, encoding/decoding, logits, generation as a loop, why
the model cannot be trusted to self-format, and how constraining the allowed set
guarantees valid structured output that still responds to the request.

That is the onramp. From here, *call me maybe* is yours to design.
