# Claim register — October 8, 2026 research integration

This **supplements**, rather than overwrites, the [July audited status ledger](mathematical_status.md). The repository records discovery history and hypotheses, not an assertion that the external open conjectures have been solved.

**Classification key**

- **Proof draft + executable checks**: complete-looking human argument in LaTeX, finite examples checked; **not** Lean-verified, journal-refereed, or independently vetted for novelty.
- **Finite computational result**: an enumeration or tested finite instance with source and reproduction instructions, not a universal proof.
- **Failed/limiting lemma**: an explicit example invalidating a stronger local normalization strategy, not the original open conjecture.
- **Open**: no proof/disproof claimed.

| Claim or direction | Classification | Canonical sources |
|---|---|---|
| Exact repair-width criterion for bipartite matching multicovers via frozen multiplicities and regular factorization | Proof draft + executable checks | [`certificate_coordination/v8/paper/main.tex`](../certificate_coordination/v8/paper/main.tex) |
| Sharp six-matching plateau and direct-repair thresholds (including multiplicity unrestricted) | Proof drafts + exact examples | [`berge_fulkerson/plateau/`](../applications/berge_fulkerson/plateau), [`next_phase/`](../applications/berge_fulkerson/plateau/next_phase) |
| Quadratic high-defect averaging, three-cut splicing and defect-component localization | Proof draft + executable checks | [`continuation_20261008/`](../applications/berge_fulkerson/plateau/next_phase/continuation_20261008) |
| Conflict-graph realization: simultaneous width and shortest strict paths encode vertex cover | Proof draft + sample certificates | [`certificate_coordination/paper/main.tex`](../certificate_coordination/paper/main.tex) |
| Hypergraph-transversal realization for every fixed covering multiplicity on complete bipartite hosts | Proof draft + exact sample cases | [`certificate_coordination/v8/paper/main.tex`](../certificate_coordination/v8/paper/main.tex) |
| High-connectivity `Q=4` one-coordinate strict plateaux | Proof draft + assignment dual certificates | [`certificate_coordination/v8/`](../certificate_coordination/v8) |
| Obstruction-primal-width dynamic program for direct repair | Algorithmic derivation + tests; based on standard elimination | [`obstruction_width_dp.py`](../certificate_coordination/v8/obstruction_width_dp.py) |
| Fixed-tree bridge-cover CNF and at-most-two-literal 2-SAT case | Proof / routine algorithmic corollary | [`edge_partitioning/RESEARCH_FINDINGS.md`](../applications/edge_partitioning/RESEARCH_FINDINGS.md) |
| K7 triple-tree completion assertion | Exhaustive finite result | [`k7_packed_tree_exhaustive.cpp`](../applications/edge_partitioning/k7_packed_tree_exhaustive.cpp) |
| High connectivity alone forces completion of arbitrarily frozen two-tree scaffolds | **False** (explicit counterexamples) | [`edge_partitioning/RESEARCH_FINDINGS.md`](../applications/edge_partitioning/RESEARCH_FINDINGS.md) |
| Full edge-connectivity partitioning conjecture (2,2) for 6-edge-connected graphs | **Open** | [`edge_partitioning/`](../applications/edge_partitioning) |
| General two-coordinate strict descent for cubic bipartite six-matching states | **Open** | [`berge_fulkerson/plateau/`](../applications/berge_fulkerson/plateau) |
| Berge–Fulkerson, Fan–Raspaud, Barnette | **Not solved here** | [applications index](../applications/README.md) |

## Important limits

1. Reproducible Python/C++ tests are valuable **checks**, not formal verification of all symbolic claims.
2. No October manuscripts have been independently reviewed by a specialist. Novelty statements are provisional, especially relative to Latin square completion and matching/edge-colouring reconfiguration.
3. Historical contaminated or inconsistent material remains marked under `archive/`; it is not reinstated by this integration.
4. Git history is preserved. Deletion of generated caches from the working tree does not erase commits or old releases.
5. Historical root checksum snapshots have moved to `archive/historical_manifests/`. For the relocated layout, see `docs/sha256_current_tree_2026-10-08.txt`. Earlier manifests are kept only as provenance.
