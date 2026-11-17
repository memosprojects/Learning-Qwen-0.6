# Rung 05 — The costume

**Idea:** Rung 04 talked to the model as raw text. But Qwen3 was *trained* to be
chatted with in a specific format — special tokens that mark where the user's
turn starts and where the assistant should answer. Think of it as a costume the
model expects to wear:

```
<|im_start|>user
...your request...<|im_end|>
<|im_start|>assistant
```

The obvious hope is: put it in its proper costume and it will finally behave.
This rung tests that hope. **It does not work** — and *how* it fails to work is
the lesson.

## Run it

```bash
uv run python rungs/05-the-costume/rung.py
```

## What you should see

With the costume on, the very first thing the model wants to do is **think out
loud** — it emits a `<think>` block and reasons to itself instead of answering.
It is a reasoning model; that is its strongest instinct.

Even if you suppress the thinking, it still does not give you a valid function
call. It answers the question with invented keys (`{"sum": 42}`,
`{"greet_shrek": ...}`) and never emits the `name` schema you need. Compared to
raw text it is arguably **worse** — at least raw mode sometimes named the
function.

The takeaway: **prompting is not the lever.** Talking to the model more
correctly does not buy you guaranteed structure. If you want a guarantee, you
have to stop asking nicely and start controlling which tokens are even allowed.
That is the next rung.

> One gotcha you will hit: `decode()` hides special tokens. If you decode a
> sequence containing `<|im_start|>`, those markers vanish from the output. Your
> instruments quietly lie to you — keep that in mind whenever the decoded text
> looks shorter than you expected.

## Turn the knobs

- `use_costume` — flip between raw text and the chat format. Compare the outputs.
- `close_thinking` — inject an empty `<think></think>` to skip the reasoning and
  see what the model does when forced to answer immediately.
- `request` — try all three kinds of request in both modes.

You are done when you can explain why better prompting (even the official chat
format) still cannot guarantee valid output.
