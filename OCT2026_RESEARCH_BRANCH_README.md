# October 2026 independent research branch — not public-release ready

This ZIP is an **additive research snapshot** of the user's privately hosted
`rewriting-graph-conjectures` project. It does **not** edit or publish the
live GitHub repository, and it preserves the original July mathematical
status ledger and manuscript archive.

## New and verified mathematically

A theorem characterizes the minimum number of matching coordinates that
must be simultaneously replaced to obtain an exact twice-cover on a cubic
bipartite graph. It is a consequence of frozen-factor completion by
Kőnig edge coloring. In the unit-defect regime, this minimum is the
transversal number of a hypergraph of surplus-edge membership triples.
The smallest positive defect values at which this minimum can be at least
2, 3, and 4 are sharply **Q=6,12,40**. Explicit 3-edge-connected bipartite
cubic graph certificates of orders 18,18,40 realize these thresholds.

**It does not prove an unrestricted two-coordinate strict-descent theorem**;
it does not resolve Berge-Fulkerson or Fan-Raspaud. Exact direct repair
is different from strict improvement.

## Reproduce from repository root

```
python berge_fulkerson/plateau/standalone_checker.py
python berge_fulkerson/plateau/q12_standalone_checker.py
python berge_fulkerson/plateau/q40_standalone_checker.py
python -m berge_fulkerson.plateau.q12_cycle_blocker
pytest -q
cd berge_fulkerson/plateau/paper && latexmk -pdf main.tex
```

## Research documents

- `berge_fulkerson/plateau/paper/main.pdf`: 8-page expanded manuscript.
- `docs/oct2026_exact_coordinate_hierarchy.md`: theorem and proof status.
- `docs/oct2026_research_assessment.md`: ongoing research and novelty cautions.
- `docs/oct2026_lean_plan.md`: not formally verified in Lean.

The release preserves the earlier 6-page research draft source as
`berge_fulkerson/plateau/paper/main_previous_plateau_v2.tex`.

## Releasing publicly

Before publication: independently referee the mathematical claims and the
novelty relative to bipartite edge-colouring and matching reconfiguration;
formalize the strongest finite lemmas in Lean if possible; update the July
status ledger and root README only after accepting the new claims. The
original `SHA256SUMS.txt` was a July snapshot; use
`SHA256SUMS_OCT2026_ADDITIONS.txt` for added files in this branch.
