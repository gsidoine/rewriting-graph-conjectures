# October 2026: sharp matching-coordinate plateaux — research branch

**Status: rigorous draft + reproducible finite certificates; NOT externally refereed or Lean-verified.**

This folder is an additive research branch; it does not silently overwrite the July 2026 authoritative ledger or change the public repository claims. An external novelty audit is still needed before submitting or publishing.

## New mathematical results

1. **Sharp frontier at defect `Q=6`.** Every sextuple of perfect matchings on a finite simple cubic **bipartite** graph with `Q=6` can be completed to `Q=0` by changing **at most two matchings**. An explicit 18-vertex, 3-edge-connected cubic bipartite graph has a `Q=6` state in which *no single perfect-matching replacement* decreases `Q`. Hence the `1` versus `2` coordination gap at `Q=6` is exact.
2. **New low-defect guaranteed descent.** On EVERY cubic bipartite graph, `0<Q<=10` implies a strictly improving **two-coordinate** replacement; `0<Q<=38` implies a strictly improving **three-coordinate** replacement. This follows by orienting the defect edges and hitting the surplus edges on a directed alternating cycle. A counting/parity lemma on subsets of six matching indices is the precise ingredient. The first possible hitting-set obstruction for two colors appears at `Q>=12`, NOT a certified graph-state obstruction.
3. **Exact minimum-cost-flow pair optimizer.** For each fixed pair of matching positions, minimize the quadratic potential over all jointly replaced pairs in polynomial time, using a 2-regular bipartite residual multigraph and marginal-cost flow. Its output agrees with exhaustive pair enumeration on the 18-vertex graph. Random sampled 24--72 vertex bipartite examples also normalized under this exact two-block optimizer, but this does not prove a global two-coordinate normalization conjecture.
4. **Nonbipartite parity criterion at Q=6.** A two-coordinate correction to zero exists iff the selected pair covers all three surplus edges and the residual degree-two multigraph has only even-cycle components. This isolates an important difference from the bipartite proof.
5. **Arbitrarily large 3-edge-connected sharp obstructions.** A balanced `K_(3,2)` vertex expansion preserves an optimal one-coordinate plateau and defect, yielding graphs on `18+4k` vertices with the same exact `Q=6` obstruction and a lifted `Q:6->6->0` path.
6. **Covering stability + unbounded girth.** Bipartite assignment dual certificates lift along all finite graph coverings. Standard residual finiteness of free groups provides connected finite covers with arbitrarily large girth, giving locally optimal positive-defect states of density `Q/|V|=1/3` on arbitrarily high-girth connected bridgeless cubic bipartite graphs.
7. **Elementary bipartite frozen-factor completion.** In a `d`-regular bipartite graph, any fixed collection of matchings can be completed to a uniform edge multiplicity `t` iff no fixed edge multiplicity exceeds `t`. This follows directly from Kőnig's edge-colouring theorem. In particular, four of six perfect matchings may always be jointly replaced to obtain `Q=0`. This is supporting methodology, **not** the novelty claim.
8. **Exact 84-state 3-cut composition formula.** A perfect matching crosses a 3-cut in one of three single-edge modes or all three edges. Six ordered matching responses modulo permutation are indexed by `C(9,3)=84` signature multisets. The graph-global minimum of the quadratic defect has an exact min-plus composition through these signatures. Checked on the triangular prism. This is an expected boundary-DP identity, not yet a new theorem-level contribution.

## How to reproduce

From the repository root:

```bash
python applications/berge_fulkerson/plateau/standalone_checker.py
python -m applications.berge_fulkerson.plateau.sharp_trap
python -m applications.berge_fulkerson.plateau.dual_certificate
python -m applications.berge_fulkerson.plateau.cover_lifting
python -m applications.berge_fulkerson.plateau.bounded_coordinate_descent
python -m applications.berge_fulkerson.plateau.three_cut_profile
python -m applications.berge_fulkerson.plateau.flow_optimize_two
python -m applications.berge_fulkerson.plateau.general_q6_pair
python -m applications.berge_fulkerson.plateau.transversal_boundary
pytest -q
```

The pure-Python standalone checker requires **no third-party dependencies** and reads the supplied integer dual witnesses. It checks:

- cubic, simple, bipartite graph of order 18;
- connectivity after all zero-, one-, and two-edge deletions (379 cases);
- six exact perfect matching masks at each step of `Q=[6,6,0]`;
- six vertex-potential duals, each verified by 27 elementary inequalities and matching equalities, certifying one-coordinate optimality against **all** perfect matchings.

The independent enumeration additionally finds 47 perfect matchings, checks all `6 × 47 = 282` replacements, and lifts to 22, 26, 30 vertices (94, 188, 376 perfect matchings, respectively). The explicit 36-vertex connected double cover has girth 6 and an inherited local minimum `Q=12`.

## Papers and notes

- `paper/main.tex`, `paper/main.pdf`: **six-page research draft, not publication-ready**.
- `../../../docs/oct2026_research_assessment.md`: novelty, proof trust boundary, and proposed next experiments.
- `../../../docs/oct2026_lean_plan.md`: Lean verification roadmap; no Lean checked proof is currently claimed.

## Important cautions

- The four-coordinate complete bipartite normalization is a direct corollary of Kőnig, not a major advance on Berge–Fulkerson.
- The exact two-coordinate `Q=6` theorem and sharp infinite obstructions are the strongest potential new results. A limited web search did **not** prove novelty; an expert literature audit is mandatory.
- The October Fan–Raspaud six-line Fano obstruction computations reported in chat are **not contained in the supplied July ZIP**; no claims about their independent verification are included here.
- No theorem extends the normalization result to general *nonbipartite* bridgeless cubic graphs.

## Continuation: exact one-step coordination hierarchy (October 8)

New **independent structural theorem**: for any cubic bipartite graph,
the minimum number `kappa` of coordinates needing simultaneous replacement
to *reach Q=0 directly* is the minimum number of matching labels whose
removal brings every frozen edge's multiplicity down to at most 2. This
follows from König's theorem, and differs from the weaker requirement of a
strict improvement. In the unit-defect regime `m(e) in {1,2,3}`, it is a
3-uniform hypergraph transversal number. The optimal positive-Q thresholds
for `kappa >= 2,3,4` are respectively **6, 12, 40**. The latter two sharp
thresholds are witnessed by explicit 3-edge-connected cubic bipartite
graphs with **18** and **40** vertices; the former was already audited in
the original 18-vertex example. Each witness was checked using small,
third-party-free code.

See `docs/oct2026_exact_coordinate_hierarchy.md`,
`q12_cycle_blocker_18.json`, `q40_cycle_blocker_40.json`, and
`q12_standalone_checker.py`, `q40_standalone_checker.py`.

**Do not confuse kappa >= 4 with an obstruction to strict 2-coordinate
descent.** The Q=40 certificate admits a pair replacement Q=40 -> 10.
Novelty not yet independently refereed.
