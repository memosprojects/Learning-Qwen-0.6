# Learning Qwen — Onramp to "call me maybe"

A teaching repository. It exists to carry a 42 student from "I have never touched an
LLM" to "I understand constrained decoding well enough to design my own function-calling
solution". It is deliberately **not** a solution to the *call me maybe* project.

## Language

### The teaching structure

**Ladder**:
The ordered sequence of **Rungs** that makes up this repository.
_Avoid_: course, tutorial, curriculum, exercises

**Rung**:
One step of the **Ladder** — introduces exactly one new idea and nothing else.
Ships as working code that runs against the model, plus the **Knobs** to turn on it.
_Avoid_: lesson, chapter, module, exercise

**Knob**:
A marked place in a **Rung**'s code the **Climber** is invited to change in order to see
the model behave differently. Turning a **Knob** is the unit of learning on this
**Ladder** — not writing code from scratch. A **Knob** is free-form: it names the place
to change and what it controls, and leaves what to try to the **Climber**.
_Avoid_: parameter, variable, setting, TODO

**Onramp**:
The scope of the whole **Ladder** — enough understanding to *begin* the project, not the project itself.
_Avoid_: solution, implementation

**Climber**:
The person working through the **Ladder**. Assumed to have written Python but never touched an LLM.
_Avoid_: student, user, learner, friend

### The subject domain

**Function Call**:
The structured output the *call me maybe* project must produce — a function **Name** plus its **Arguments**.
_Avoid_: tool call, invocation, response

**Name**:
One of the fixed strings the model may choose, e.g. `fn_reverse_string`. A **Name** has no body
and is never executed — choosing it *is* the whole act of calling.
_Avoid_: function, tool, handler

**Constrained Decoding**:
Choosing the next token only from the set the target structure permits, by filtering logits before selection.
_Avoid_: guided generation, structured output, grammar sampling

**Allowed Set**:
The set of token ids that are legal at the current generation step.
_Avoid_: mask, valid tokens, whitelist

**Costume**:
The `<|im_start|>role … <|im_end|>` chat format Qwen3 was trained on. Wearing it makes the
model behave as an assistant answering a request; without it the model is a raw continuation
engine finishing a fragment.
_Avoid_: chat template, prompt format, system prompt

## Relationships

- The **Ladder** is an ordered list of **Rungs**
- A **Rung** teaches exactly one idea, and ends where the **Climber** can state that idea in their own words
- A **Rung** carries one or more **Knobs**; the **Climber** turns them and watches the model's output change
- The order of the **Rungs** is the order the repository's author learned these ideas themselves — it is
  validated by having worked once, not derived from first principles
- The **Ladder** ends at the **Onramp** boundary — the **Climber** leaves it to write their own **Function Call** system
- **Constrained Decoding** at each step computes an **Allowed Set**, then picks the highest-logit member of it
- The **Allowed Set** decides *what is legal*; the logits decide *which legal thing is chosen*.
  Only the logits carry the **Climber**'s request, so the request must be in the context —
  otherwise every prompt yields the same **Function Call**

## Example dialogue

> **Climber:** I turned the **Knob** on the last **Rung** and asked it to reverse a string, but
> it still called `fn_add_numbers`. Is the **Allowed Set** broken?
>
> **Author:** No — the **Allowed Set** is doing its job. It only decides which tokens are *legal*,
> and all three **Names** were legal there. What picks between them is the logits, and the logits
> come from what's in the context. Did you change the request, or just the **Name** list?
>
> **Climber:** So a wrong **Name** is still a valid **Function Call**?
>
> **Author:** Exactly. **Constrained Decoding** guarantees the shape, never the choice. That's
> the whole split — structure is yours to enforce, correctness is the model's to get right.

## Flagged ambiguities

- "the project" was used to mean both this teaching repository and the 42 assignment
  *call me maybe*. Resolved: this repository is the **Ladder**; the assignment is always
  written *call me maybe* in italics.

## Decisions so far

- **Reversed.** An earlier decision made the **Ladder** a set of stubs the **Climber**
  implements. It is instead **working code the Climber changes**. The **Climber** is not
  being taught to code — they already can. They are being taught what an LLM does, and
  that is learned by turning a **Knob** and watching the output move, not by writing a
  function from an empty file.
- Every **Rung** forces CPU and float32, never the SDK's auto-selected `mps`/float16. This is
  not primarily a trade-off — the **Ladder** is climbed on 42 school computers, which have no
  usable GPU, so CPU is the target hardware rather than a choice. Forcing it explicitly rather
  than letting the SDK auto-select also keeps the **Ladder** reproducible: a `README.md` that
  describes what the **Climber** should see stays true on any machine, where half-precision on
  Metal would reorder near-tied logits and read as "I broke it". Being slow is therefore a fact
  about the environment to state plainly, not a defect to apologise for.
- Each **Rung** is a folder holding a `README.md` and one runnable script, and the prose is in
  English. The explanation and the **Knob** markers are split deliberately: prose answering
  "why does the model need numbers at all?" is read once and closed, while a marker saying
  "this list is a **Knob**" must be visible on every re-run, so it lives in the source as a
  comment. A long comment header was rejected because it pushes the code below the fold until
  the **Climber** stops seeing it; a single root document was rejected because it separates the
  words from the thing they describe. Folder-per-**Rung** also means browsing `rungs/` on
  GitHub renders the **Ladder** in order.
- **Knobs** are free-form, not directed probes. The **Ladder** marks the place to change
  and says what it controls; it does not prescribe values to try or ask the **Climber**
  to predict the result first. Rationale: the **Climber** is a 42 student, and 42's
  pedagogy is self-direction and peer learning by design. A prediction worksheet fights
  that culture and reads as condescending to someone who has already passed the Piscine.
  Accepted cost: a **Climber** who turns a **Knob** carelessly can learn less than one
  who probes deliberately. That risk is theirs to run.
- A **Rung** teaches the **Costume** — the `<|im_start|>` chat format Qwen3 was trained on —
  with a **Knob** toggling between raw continuation and templated input so the **Climber** can
  compare the logit ordering. Chosen over hiding the format because of what it buys: right after
  the assistant turn opens, this model's strongest preference is to emit `<think>`, and watching
  **Constrained Decoding** override that instinct and still produce valid output is the most
  convincing demonstration of the technique available in the project. Accepted cost: one **Rung**
  spent on plumbing, and `<think>` is a rabbit hole.
  - The **Costume** does **not** improve reliability, and the **Rung** must not claim it does
    (an earlier note said "better, still not guaranteed" — falsified by probing). Measured on
    Qwen3-0.6B, greedy: raw continuation primed with `{"name":"` at least picks the right
    **Name**, whereas the **Costume** omits the **Name** entirely and answers the question
    (`{"sum": 42}`, `{"greet_shrek": ...}`, `{"result": "olleh"}`), each wrapped in markdown
    fences. The lesson is therefore "prompting harder — even the proper chat format — is not the
    lever; only forcing the tokens is", which is a cleaner motivation than the original framing.
- The **Climber**'s request sits in the context from the **Rung** where the model first fails
  onward, and the final **Rung** swaps it to show the same code choosing a different **Name**.
  The author's own scripts fed the model a bare `{"name":"` fragment with no request in the
  context at all, so the **Function Call** they produced was caused by the model's prior over
  JSON text rather than by any user need — running them a hundred times gives the same **Name**
  a hundred times. Teaching this as its own **Rung** was considered and rejected as a lecture;
  it lands better as the punchline of the last one.
- The root `README.md` states the purpose — hands-on learning of what tokens, encoding, decoding
  and **Constrained Decoding** actually are, using the functions `llm_sdk` exposes — and says
  plainly that it is slow because it runs on school computers with CPU only. The author's
  original eight scripts are deleted rather than kept alongside the **Ladder**: they are
  preserved in commit `ff14415`, and a teaching repository cannot afford ambiguity about which
  file the **Climber** is meant to be looking at.
- The **Ladder** opens with a **Rung** that only loads the model and prints one line, so the
  1.4 GB download and any platform breakage happen in a folder that expects them rather than
  landing on the tokens **Rung** and being filed as "tokens are confusing and slow".
- The **Ladder** is cloned into `sgoinfre`, not the **Climber**'s home directory, because 42
  home quotas cannot hold a 1.4 GB model plus a torch virtualenv. The first **Rung** must also
  set `HF_HOME` into `sgoinfre`: the download location is decided by that variable and not by
  the working directory, so a **Climber** who only clones into `sgoinfre` still fills their
  home quota and gets a disk error that names none of this.
- The **Ladder** is nine **Rungs** in three acts: *how generation works* (tokens, logits, the
  greedy loop), *how it breaks* (ask for a **Function Call**, watch the model ramble; try the
  **Costume**, watch it still be unreliable), *how it is fixed* (**Allowed Set** for one step,
  then tracking position inside a **Name**, then the enforcer loop, then swapping the request).
  The author's own scripts contained only the third act, so **Constrained Decoding** arrived as
  a procedure rather than as a fix for a failure the **Climber** had witnessed.
- The **Climber** must watch the model *fail* to produce a **Function Call** unaided. This is
  the load-bearing **Rung**; without it the rest is a magic trick performed on a problem they
  were told about but never met. **Verified** on Qwen3-0.6B (CPU, greedy): it fails reliably,
  but not by being stupid — it produces the *right answer* in the *wrong shape*. It wraps output
  in markdown fences, invents a different key every time (`result`, `sum`, `greet_shrek`), never
  emits the required `name`/`parameters` schema, and under greedy decoding loops the same block
  forever. It returns `42` — exactly what the subject says a **Function Call** must not do. The
  **Rung**'s point is therefore "the model knows the answer but cannot be trusted with the
  structure", which is a stronger motivation than "the model is wrong".
- The **Ladder** ends by swapping the request and watching the same code choose a different
  **Name**. Nothing is executed. Because the output looks identical to the previous **Rung**'s,
  the final **Rung** must show several requests side by side — the progression lives in the
  comparison, not in the output.
- The **Ladder** ends at a working enforcer that produces a complete, valid **Function Call**
  for a fixed set of **Names**. Stopping one loop short of that payoff was considered and
  rejected: it protects nothing a 42 student cannot rewrite in five minutes, and it withholds
  the moment the technique visibly works.
- The **Allowed Set** is built by matching token ids against `encode()`d **Names**, not by
  reading `vocab.json`. This is knowingly weaker — it permits only the canonical tokenisation of
  each **Name**, so a token the model prefers can be forbidden even though it leads somewhere
  valid — and it contradicts a hint in the subject. Chosen anyway: byte-level BPE (`Ġ`, `Ċ`,
  mojibake) is a difficulty spike late on the **Ladder**, and the **Onramp** does not require it.
  The **Climber** meets this limitation during the assignment instead.
- The `data/` directory is deleted and the **Ladder** never reads input files.
  See [ADR 0001](docs/adr/0001-the-ladder-never-reads-input-files.md).
- The **Ladder** ends at the last **Rung**. There is no closing document inventorying what the
  **Climber** still has to learn, and no warning against submitting the **Ladder**'s code as
  their own. Consistent with the **Knobs** being free-form: the **Climber** is a peer who is
  trusted to work out where they stand. Accepted cost: they step off the top without being told
  that everything they learned covers the **Name** and nothing else — **Arguments**, typed and
  constrained differently, are unmentioned.
- The **Ladder** is still not a submittable solution. Handing over a solution would
  actively harm the **Climber**: the assignment fails anyone who cannot defend code they
  did not write.
- The **Ladder** stops at the **Onramp**: constraining generation to a fixed set of
  function **Names**, fully understood. Typed **Arguments**, file IO, CLI, and error
  handling are left for the **Climber** to design.
