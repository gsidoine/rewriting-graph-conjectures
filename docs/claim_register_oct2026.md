# Claim register — October 8, 2026 research integration

This **supplements**, rather than overwrites, the [July audited status ledger](mathematical_status.md). The repository records discovery history and hypotheses, not an assertion that the external open conjectures have been solved.

**Classification key**

- **Proof draft + executable checks**: complete-looking human argument in LaTeX, finite examples checked; **not** Lean-verified, journal-refereed, or independently vetted for novelty.
- **Finite computational result**: an enumeration or tested finite instance with source and reproduction instructions, not a universal proof.
- **Failed/limiting lemma**: an explicit example invalidating a stronger local normalization strategy, not the original open conjecture.
- **Open**: no proof/disproof claimed.

| Claim or direction | Classification | Canonical sources |
|---|---|---|
| Sharp order-14 nonextendability of a prescribed FR-triple despite a bridgeless residual, plus all-even-order 3-edge-connected lifts and a one-coordinate strict escape | Complete reduction proof + explicit minimal witness + independent PM enumeration; external novelty **not vetted** | [`formal manuscript`](../applications/berge_fulkerson/plateau/fr_extension_paper/main.tex), [`FR extension proof`](../applications/berge_fulkerson/plateau/FR_EXTENSION_OBSTRUCTIONS_20261008.md), [`certificate`](../applications/berge_fulkerson/plateau/fr_n14_petersen_kernel.json), [`verifier`](../applications/berge_fulkerson/plateau/fr_extension_core.py) |
| Finite cut-response algebra: 3-port compatibility from parity; incompatible locally colourable 4-ports on Petersen | Classical parity deduction + independently reproduced finite certificate; no novelty claimed | [`cut-signature proof`](../theory/cut_signature_factorization_2026-10-08.md), [`boundary enumerator`](../shared/three_colour_boundaries.py) |
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

## Subsequent theory note — uniform collision hypergraphs

- **Statement:** for bipartite `k`-fold perfect-matching multicovers, direct repair width equals the transversal number of the uniform `(k+1)`-coordinate collision hypergraph, without a unit-defect assumption. **Status:** elementary proof from König factorization, independently brute-force tested; novelty not audited.
- **Algorithm:** implicit `(k+1)`-branching gives FPT time in repair budget for each fixed `k`. **Status:** proof + executable implementation; standard bounded-rank Hitting Set technique.
- **Complexity separation:** variable `k` yields W[2]-hardness in the repair budget via the v8 complete-bipartite realization. **Status:** reduction argument based on the v8 proof, not independently refereed.
- **Nonbipartite limitation:** the triangular prism has collision hitting number 2 but true direct repair width 3, due to residual odd-cycle factorization obstruction. **Status:** elementary proof + exhaustive standalone checker.

Sources: [`theory/parameterized_collision_repair_2026-10-08.md`](../theory/parameterized_collision_repair_2026-10-08.md), [`collision_hypergraph.py`](../certificate_coordination/collision_hypergraph.py), [`test_collision_hypergraph.py`](../tests/test_collision_hypergraph.py), [`test_nonbipartite_factorization.py`](../tests/test_nonbipartite_factorization.py).

## 2026-10-08 resistance--kernel universality (research draft)

- **Proved claim, pending independent novelty audit:** every simple connected bridgeless cubic graph `K` has a simple connected bridgeless FR-triple host (3-edge-connected if `K` is) with residual kernel `K`, exactly `res(K)` uncovered edges and precisely `2 res(K)` additional vertices; these costs are minimal.
- **Resistance-two refinement:** constructed hosts are themselves 3-edge-colourable, despite failure of extension of the *specified* frozen triple when `K` is a snark.
- **Exact certificates:** Petersen (10 to 14 vertices), flower snark `J5` (20 to 24 vertices), plus an 18-vertex host for a 2-edge-connected Petersen--K4 join; 75 Petersen edge-pair realizations yield three isomorphism classes under the deterministic port-colour choice.
- **References/limitations:** established literature on colouring resistance and defect is extensive. Do not claim novel general lifting without comparison to resistance-2 critical snark and 3-array bicontraction literature; the Berge--Fulkerson/Fan--Raspaud existence conjectures remain unresolved.
- **Sources:** `theory/resistance_kernel_realization_2026-10-08.md`, `applications/berge_fulkerson/plateau/resistance_paper/`, `applications/berge_fulkerson/plateau/resistance_kernel_lift.py`, `tests/test_resistance_kernel_lift.py`.


## Theorem-first reconfiguration integration (8 October, later update)

The [cycle double-cover application](../applications/cycle_double_cover/README.md) archives compression, direct-descent obstructions, six-step neutral escape and small-order counts. **The proof-status ledger for that application is [CLAIM_STATUS.md](../applications/cycle_double_cover/CLAIM_STATUS.md)**; do not upgrade historical finite claims lacking in-repository certificate JSON to CI-reproduced results.

Two new mathematical notes address genuinely cross-application questions:

- [Three-cut neutral-switch synchronization and the exact typed fiber-product reduction](../theory/three_cut_synchronized_reconfiguration_2026-10-08.md): mathematical proof note, finite tests on the triangular prism, classical ingredients and originality not vetted.
- [K3,3 disconnected neutral fibers](../theory/k33_neutral_fiber_obstructions_2026-10-08.md): exact classification for three-sheet CDC and six-matching double-cover systems (fiber types 1+1 and 1+8+1), proofs plus exhaustive test. This **falsifies unqualified boundary-signature-only neutral reachability**.

The research priorities and stop/pivot conditions are recorded in [theorem-first programme](theorem_first_reconfiguration_program_2026-10-08.md). Full 5-CDC, Berge–Fulkerson and Fan–Raspaud remain open here; no release is claimed to settle them.

## 2026-10-08 unbounded uphill FR reconfiguration barriers

- **Structural theorem candidate, complete combinatorial proof draft:** for every `t >= 0` there is a simple, 3-edge-connected, 3-edge-colourable cubic graph on `10*5**t` vertices and an FR-triple with `u=3**(t+1)` such that every one-coordinate FR-preserving normalization must reach `u >= 4*3**t`; a normalization path exists. The necessary absolute increase is at least `3**t`.
- **Exact finite witness:** on 10 vertices there are six PMs and 23 unordered FR triples; a specified `u=3` triple has exactly six distinct legal neighbours, all at `u=4`, and an explicit `3->4->3->0` normalization path. An independent 24-vertex class-one host has a 36-state sublevel-3 component disconnected from the `u=0` states.
- **Proof mechanism:** balanced all-vertex `K_{3,2}` expansion projects every PM onto an original PM, preserves 3-edge-connectivity and class one, satisfies `u_expanded >= 3*u_projected` for all FR triples, and admits equality-attaining lifts. An arbitrary base FR path can be lifted from any preimage. An earlier triangle-expansion argument was **discarded** because it allowed extra all-three-external perfect matchings and did not give projection.
- **Scope:** this is a theorem about one-coordinate reconfiguration of existing FR triples, not a disproof of FR or Berge–Fulkerson. Unlike the variable-degree complexity results, it concerns **cubic graphs of fixed degree**. The novelty claim is unverified outside this research programme; see the cited matching reconfiguration/colouring defect literature.
- **Sources:** [`paper/main.tex`](../applications/berge_fulkerson/plateau/energy_barriers/paper/main.tex), [`standalone_audit.py`](../applications/berge_fulkerson/plateau/energy_barriers/standalone_audit.py), [`balanced_lift.py`](../applications/berge_fulkerson/plateau/energy_barriers/balanced_lift.py), [`ten_vertex_witness.json`](../applications/berge_fulkerson/plateau/energy_barriers/ten_vertex_witness.json), [`theory note`](../theory/fr_uphill_barriers_2026-10-08.md).
