# The Ladder never reads input files

The *call me maybe* subject ships `data/input/functions_definition.json` and
`data/input/function_calling_tests.json`, and a teaching repository for that assignment would
naturally read them. This one deletes the `data/` directory entirely: every function **Name**,
every request, and every structure on the **Ladder** is a literal in a **Rung**'s source.

The reason is that the **Ladder** hands the **Climber** working code, so the only thing standing
between them and a copy-pasted submission is the *shape* of that code. A **Rung** that loads
names from a file at runtime is a skeleton for the assignment. A **Rung** with three names
hardcoded in a list is a lab bench — it cannot be lifted, because the assignment's names are
unknown until the reviewer supplies them. Making the firewall physical rather than a rule we
remember to follow means it cannot erode as **Rungs** get added.

## Consequences

- Hardcoded literals become **Knobs**. The **Climber** edits names by hand, which is the point.
- A **Climber** who finishes the **Ladder** has never seen **Constrained Decoding** applied to
  anything but a fixed set of **Names**. Typed **Arguments** — where the **Allowed Set** stops
  being a prefix match over strings and becomes a state machine over digits, quotes and escapes —
  is a harder idea, and they meet it alone. This is accepted, not overlooked.
- The repository cannot be run against the assignment's own test data to check whether the
  technique works at the required scale. That confidence has to come from the **Climber**'s own
  project.
