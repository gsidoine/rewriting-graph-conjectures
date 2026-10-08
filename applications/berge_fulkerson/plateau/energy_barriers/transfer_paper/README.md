# Exact Fan–Raspaud triple renormalization under the balanced three-pole

**Research status:** complete five-page mathematical proof draft, exhaustively tested small examples; no independent novelty/referee certification (8 October 2026).

- `main.tex`: editable manuscript (authoritative).
- `main.pdf`: compiled rendering.
- `../transfer_operator.py`: local phase enumeration, polynomial transfer, numerical pressure, and independent perfect-matching enumeration.
- `../../../../../tests/test_fr_transfer_operator.py`: eight additional unit tests, including independent brute-force expansion checks.
- `../../../../../theory/fr_three_pole_renormalization_2026-10-08.md`: theorem status and research implications.

## Principal theorems

1. Local FR phase graphs are `Q3` (eight configurations) or `C6` (six configurations).
2. Projection from `T(G)` to `G` induces a bijection of full one-coordinate FR reconfiguration connected components; any base move can be lifted from any preimage; the phase-fibre diameter is at most `3|V(G)|`.
3. The exact polynomial transform is `Z_T(z) = (2+6z²)^n Z_G(z³ ((z+2)/(1+3z²))²)` for ordered FR-triples counted by uncovered edges.
4. Minimum defect scales by `3^t` under `t` substitutions; minimizer multiplicities are given in closed form.
5. For any seed graph possessing an FR-triple, a universal limiting weighted triple entropy and mean defect density exist, independent of the seed.

## Reproduce

From repo root:

```bash
python applications/berge_fulkerson/plateau/energy_barriers/transfer_operator.py
python -m pytest -q tests/test_fr_transfer_operator.py
```

This is a theorem about the exact substituted family, not a proof of Fan–Raspaud or Berge–Fulkerson on arbitrary cubic graphs. MultipoIe substitution and colouring-defect invariants have extensive established literatures; claim originality only after an external specialist review.
