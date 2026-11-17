# Rung 01 — Tokens

**Idea:** the model cannot see text. It only ever sees numbers. Turning text
into those numbers is **encoding**; turning them back is **decoding**.

A token is not a letter and not a word. It is a chunk — sometimes a whole word,
sometimes a piece of one, and it often carries a leading space with it. The
tokenizer decides the chunks; you do not.

## Run it

```bash
uv run python rungs/01-tokens/rung.py
```

## What you should see

For each text: its token ids, the text you get back by decoding them, and then a
token-by-token breakdown so you can see exactly where the tokenizer cut.

The second half feeds the tokens in one at a time and decodes the growing list,
so you can watch the text rebuild itself piece by piece. This is why you need
both directions constantly: you *encode* to talk to the model, and you *decode*
to read what its numbers mean.

## Turn the knobs

The `texts` list is the knob. Some things worth discovering:

- Put in the same word twice, once with a leading space (`"hello"` vs
  `" hello"`). Same ids? Why might a leading space matter to the model?
- Try upper and lower case.
- Try a long rare word and a short common one. Which one splits into more tokens?
- Try a number like `"40"` and a bigger one like `"4020"`.

You are done with this rung when you can say, in your own words, why the model
needs encoding and decoding at all.
