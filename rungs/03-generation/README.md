# Rung 03 — Generation

**Idea:** generating text is not magic and not a single step. It is a loop:

1. Score every possible next token (Rung 02).
2. Pick the highest-scoring one.
3. Append it to the sequence.
4. Go back to step 1.

That's it. Always picking the single best token is called **greedy** decoding.
Everything a chatbot says is this loop, run over and over.

## Run it

```bash
uv run python rungs/03-generation/rung.py
```

This is the first rung that is genuinely slow. Each step re-reads the whole
sequence to score the next token, and it does that once per token generated.
Watching it grind is the point: now you know what "the model is typing" actually
costs.

## What you should see

The prompt, then each generated token printed as it is chosen, then the full
continuation the model produced.

## Turn the knobs

- `prompt` — start it with `"Once upon a time"` and let it tell a story.
- `n_tokens` — how many steps the loop runs. Bigger is slower. Keep it modest.

Try a factual prompt and watch it stay coherent, then a strange one and watch it
wander. Greedy always takes the top token, so the same prompt always gives the
same output — run it twice and check.

You are done when you can explain generation as a loop over next-token
prediction, and say what "greedy" means.
