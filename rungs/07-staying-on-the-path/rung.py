"""Rung 07 — Staying on the path.

After the first token you are partway into a name. The allowed set must shrink
to only the tokens that continue a still-reachable name. This rung computes the
allowed-next set for any partial name; it does not generate yet.
"""
from llm_sdk import Small_LLM_Model


def main() -> None:
    model = Small_LLM_Model(device="cpu")

    # KNOB: the legal names. Try adding names that share a long prefix.
    names = ["fn_add_numbers", "fn_greet", "fn_reverse_string"]

    # Encode each name once into its list of token ids.
    name_to_ids = {name: model.encode(name)[0].tolist() for name in names}

    def still_reachable(chosen: list[int]) -> list[str]:
        """Names whose id list starts with the tokens chosen so far."""
        return [
            name for name, ids in name_to_ids.items()
            if ids[:len(chosen)] == chosen
        ]

    def allowed_next(chosen: list[int]) -> set[int]:
        """The next token id from every still-reachable name."""
        allowed = set()
        for ids in name_to_ids.values():
            if ids[:len(chosen)] == chosen and len(chosen) < len(ids):
                allowed.add(ids[len(chosen)])
        return allowed

    # Walk a few partial states: empty, then the prefix of fn_add_numbers.
    add_ids = name_to_ids["fn_add_numbers"]
    states = [[], add_ids[:1], add_ids[:2], add_ids[:3]]

    for chosen in states:
        print(f"CHOSEN SO FAR : {chosen}  ({model.decode(chosen)!r})")
        print(f"STILL MATCHES : {still_reachable(chosen)}")
        print("ALLOWED NEXT  :")
        for token_id in sorted(allowed_next(chosen)):
            print(f"    id={token_id:<8} {model.decode([token_id])!r}")
        print()


if __name__ == "__main__":
    main()
