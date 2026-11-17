# Rung 00 — First contact

**Idea:** get the model onto your machine and prove the whole stack works,
*before* any real lesson depends on it.

The first time you load the model, it downloads about 1.4 GB from Hugging Face.
This rung exists so that download — and any setup problem — happens here, in a
folder that expects it, instead of ambushing you on the first real lesson.

## Before you run

Make sure you did the two things from the top-level README:

- You are working inside `sgoinfre`, not your home directory.
- You have set `HF_HOME` into `sgoinfre`:
  ```bash
  export HF_HOME=/sgoinfre/$USER/huggingface
  ```

If you skip the second one, the download goes to your home directory and will
blow past your quota with a confusing disk error.

## Run it

```bash
uv run python rungs/00-first-contact/rung.py
```

The first run is slow (downloading). Later runs are fast (loading from cache).

## What you should see

A few lines confirming the model loaded, the device it runs on (`cpu`), and a
tiny sanity check that encoding a word gives back a list of numbers.

If you got here, everything downstream will run. Move to `01-tokens`.
