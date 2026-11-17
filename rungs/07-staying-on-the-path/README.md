# Rung 07 — Staying on the path

**Idea:** one allowed token is not enough. After you pick the first token of the
name, you are *partway into* a name, and the allowed set has to shrink to only
the tokens that continue a real name from where you are.

Think of the names as paths. `fn_` is the shared start. After it, `add_numbers`,
`greet`, and `reverse_string` branch off. Once you have committed to enough
tokens that only one path matches, the rest is forced.

This rung does not generate anything yet. It shows you how to compute, for any
partial name-so-far, which token ids may legally come next.

## Run it

```bash
uv run python rungs/07-staying-on-the-path/rung.py
```

## What you should see

For several "partial name" states — nothing yet, one token in, two tokens in —
the set of tokens allowed to come next, and which names still match. Watch the
allowed set start wide and collapse as the path commits to a single name.

## How it works

Each name is encoded once into a list of token ids. Given the tokens chosen so
far, a name is still reachable if its id list *starts with* those tokens. The
allowed-next set is the next id from every still-reachable name.

> Note: this compares token *ids*, not the letters. That means it only allows the
> one canonical way each name is tokenized. It is good enough here because your
> names are a small fixed list. When you design your own solution and the names
> come from a file you have not seen, you will have to think harder about this.

## Turn the knobs

- `names` — change the list and watch how the branch points move. Add two names
  that share a long prefix and see where the allowed set finally splits.

You are done when you can describe how the allowed set narrows as a name is built
token by token.
