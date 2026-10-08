# Obstruction-hypergraph universality (October 2026, v8)

**Status: mathematical research draft.** Proofs are complete in the supplied LaTeX manuscript, finite certificates were independently checked, but no Lean formalization or external peer review has occurred. Do not call these statements established literature until an outside novelty/referee audit.

## Main new claims

1. **Complete-bipartite universality:** For every uniformity `k+1`, and every hypergraph `H` of that uniformity, a tuple of `kD` perfect matchings on the complete bipartite `K_(D,D)` has `direct-repair width = shortest strictly decreasing single-coordinate path = transversal(H)`.
2. **Exact defect landscape:** The canonical families of states have quadratic defect `2*d*(number of hyperedges not hit yet)`. A selected coordinate fixes every newly hit hyperedge in one strict step.
3. **Complexity on maximally edge-connected hosts:** For each fixed `k>=1`, direct repair and shortest strict normalization are NP-complete/APX-hard on explicitly supplied tuples whose host is complete bipartite; strict normalization is promised to exist in the reduction family.
4. **Positive separator-width algorithm:** Direct repair is computable in `2^(w+1)*poly(input size)` when a width-`w` elimination order of the obstruction-primal graph is supplied. This is a standard constraint-programming technique, not a separately claimed novel algorithm.
5. **All-multiplicity minimal plateaux:** For each `k>=1` and each `d>=8` (also d=4), `K_(d,d)` has a `kd`-matching state of the smallest positive defect `Q_k=4` with no strict one-coordinate move, but an explicit neutral then strict route `4 -> 4 -> 0`.

The older v7 matching-coordination and plateau results remain preserved. The new construction improves the prescribed-connectivity version to complete bipartite graphs and covers every multiplicity k. The existing canonical July 2026 mathematical ledger is not changed.

## Reproduce

From this directory (Python 3.10+, standard library):

```bash
python complete_bipartite_realization.py
python hypergraph_realization.py
python obstruction_width_dp.py
python all_multiplicity_plateaux.py
python test_exhaustive.py
python independent_verify.py
```

Compile the five-page paper with `cd paper && latexmk -pdf main.tex`.

The standalone `independent_verify.py` reads archived JSON files and does not import the discovery/construction algorithms. It checks every perfect matching, all edge multiplicities, the exact transversal optimum in the sample, the entire strict path, and every integer assignment-dual inequality in the plateau sample.

The `tests/test_coordination_v8.py` integration tests are included in the repository's standard `pytest` run.

## Do not overclaim

- Completeness and complexity statements are about **variable degree** complete bipartite graphs. For the original six-matching cubic case the coordinate set has only six elements, so direct repair width has a trivial finite enumeration algorithm.
- The obstruction-width dynamic program calculates **direct repair**, not the shortest strict descent path for arbitrary input certificates. Equality is proven for the specially realized family.
- The family-of-states formulation is deliberately non-unique: globally assigning a single state to every subset of hypergraph labels does not preserve every possible one-coordinate transition.
- Latin-square completion and edge-precolouring extension hardness on complete bipartite graphs are classical; a specialist must decide whether the specific tuple-coordinate strict-path hardness and complete-bipartite construction are sufficiently novel to publish.
- No active GitHub branch has been changed by this artifact preparation.
