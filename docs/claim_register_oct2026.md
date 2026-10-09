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


## Exact multiplicity-m neutral-component amplification (8 October, later)

- **Theorem:** on a cubic bipartite 3-edge-connected chain of `n` copies of K3,3, the `3m`-matching multiplicity-`m` certificate reconfiguration graph has exactly `(m+1)^n` neutral components. Same exact count occurs with any prescribed complete signature at one exposed three-edge star. Individual component sizes are `(3m)!/(m!)^3 * product_i binom(m,t_i)^3`; the fixed-signature components have sizes `product_i binom(m,t_i)^3`.
- **Status:** complete human proof draft plus exhaustive finite sanity checks, **not** Lean certified or specialist-refereed. Historical m=1 case is covered by Belcastro--Haas (2014); novelty of m>=2 is not established.
- **Sources:** [theorem and complete proof](../theory/exponential_neutral_components_multicovers_2026-10-08.md), [local test](../tests/test_k33_multicover_types.py), [two-block full replay](../repro_runs/k33_two_block_multicover_components.py).
- **Why this matters:** disproves any hope that bounded interface size and fixed coordinate count alone bound the number of neutral connected components in an *entire boundary fiber*. A compositional/factorized representation is still possible.

- **Additional corollary (same proof):** neutral equivalence on the K3,3 chain is decidable by equality of the local type vector in O(nm) input work; within a fixed boundary signature each component has a constructive diameter bound 3*sum_i min(t_i,m-t_i); unrestricted diameter <= n(3m-1)+that term. Exhaustive n=2,m=2 fiber BFS shows the fixed-signature bounds are attained there. The general bound is a proof draft, not externally reviewed.

## Exact FR three-pole renormalization and component theorem (October 8, 2026)

- **Mathematical proof draft (not peer-reviewed):** the `K_{3,2}` all-vertex expansion projects full ordered FR reconfiguration onto the original graph, every projected edge lifts from any preimage, and each fibre has a connected spanning product of `Q3`/`C6`; connected components correspond bijectively.
- **Exact polynomial:** `Z_{T(G)}(z)=(2+6z^2)^n Z_G(z^3 ((z+2)/(1+3z^2))^2)`. Component-wise versions hold. Minimal defect scales as `3^t`, with a closed formula for minimizing-state multiplicities. Iterated normalized log counts have a universal limit independent of the cubic seed, conditional on at least one FR-triple.
- **Independent exhaustive checks:** 156 locally valid phase states, 828 projected-port transitions, exact polynomial coefficients for all 47,904 ordered FR-triples on `T(K4)`, complete reconfiguration connectedness on that graph; Petersen seed has `Z=120z^3`. Eight new targeted local tests.
- **Novelty caution:** the generic multipole/graph-polynomial substitution paradigm is classical; this exact FR transfer and dynamical statement has not been externally checked for originality. Does not settle Fan–Raspaud or Berge–Fulkerson.
- **Sources:** [theory status](../theory/fr_three_pole_renormalization_2026-10-08.md), [paper](../applications/berge_fulkerson/plateau/energy_barriers/transfer_paper/), [transfer code](../applications/berge_fulkerson/plateau/energy_barriers/transfer_operator.py), [tests](../tests/test_fr_transfer_operator.py).


## Pair-rigid tile algebra and mixed non-3-colorable chains (8 October, next phase)

- **Proof draft:** [pair-rigid tile composition theorem](../theory/pair_rigid_tile_multicover_algebra_2026-10-08.md). For cubic tiles with one alternating symmetric-difference cycle for every distinct perfect-matching pair, binary-neutral components factor exactly as products of local integer multiplicity-vector sets `X_m(T)={x>=0:A_T x=m1}`. Fixed-star signature fibers retain the same component indexing, with explicit multinomial weights and a constructive path bound `<=3L(m-1)` for a chain of L tiles.
- **Corollary:** any three-edge-sum chain of `a` K3,3 tiles and `b>=1` Petersen tiles is non-3-edge-colorable. There are no matching m-multicovers for odd m; for even m exactly `(m+1)^a` binary-neutral classes, with exact component sizes.
- **Finite verification:** 14-vertex K3,3+Petersen (7200 labelled six-matching certificates, three neutral components), 18-vertex Petersen+Petersen (5760 certificates, one component), 14-vertex Petersen+K3,3 (same three components); complete enumeration and local cube non-rigid obstruction. On the 14-vertex mixed graph, three-coordinate exact replacements are necessary and sufficient to pass between neutral classes (width-three threshold).
- **Status:** human proof draft plus independent finite verification; claims of new literature priority are **not justified** without a specialized audit. The underlying Petersen matching configuration and 3-edge-cut parity are classical; the earlier all-K3,3 m=1 case is covered by Belcastro–Haas (2014). No conjecture about Fulkerson covers is solved.


## Port-coherent orbit gluing across CDC and matching systems (8 October, newest)

- [Shared gluing theorem](../theory/port_coherent_neutral_reconfiguration_2026-10-08.md): **human proof draft** for *two distinct* certificate systems, `CDC(q)` even-subgraph sheets (empty sheets allowed), and `PM(m)` m-fold matching multicovers. If every tile's neutral orbit has a connected induced fixed-boundary-signature fiber, global neutral components are indexed by products of local orbit indices; both component sizes and fixed-boundary diameter bounds factor/add.
- [Cube local neutral-fiber test](../tests/test_cube_port_coherence.py): **exact finite computational lemma**: cube has 24 3-sheet CDC states (one orbit, six signature fibers of four connected states each) and 4320 6-matching double-cover states (one orbit, 90 fibers of 48 connected states each), despite failing pair-rigidity.
- [Mixed global 3-sheet CDC verification](../tests/test_cdc_k33_cube_gluing.py): K3,3+cube has 48 states, two components of size24 and fixed-signature components of size4 each. **This specialization falls under classical edge-Kempe composition and is not novel.**
- [Mixed matching global verification](../repro_runs/verify_mixed_pair_rigid.py): K3,3+cube 43200 states (components 4320/34560/4320) and Petersen+cube 34560 states (one component); independently built neutral graphs.
- **Publication limits:** no unconditional claim for arbitrary tiles, no proof of any major conjecture; cube hypothesis currently computationally exhausted rather than human-classified; general novelty not established.
## Pair-rigid tile factorization (2026-10-08, evening)

- **Exact factorization theorem (proof draft):** a chain of simple, cubic, 3-edge-connected, pair-rigid tiles has neutral-connected components indexed precisely by a product of local integer perfect-matching multiplicity solution sets. Exact fixed-signature and global component sizes are multinomial products, with a constructive `3L(m-1)` fixed-fiber switch bound. [Full proof](../theory/pair_rigid_tile_multicover_algebra_2026-10-08.md).
- **Mixed Petersen/K3,3 corollary (proof draft):** if there are `a` K3,3 and `b>=1` Petersen tiles, for even `m`, both global and fixed-signature neutral component counts are `(m+1)^a`. No m-cover for odd `m`. This is on non-3-edge-colorable cubic graphs, but **not** cyclically 4-edge-connected graphs.
- **Sharp coordinate-arity observation (finite witness and short proof):** in a 14-vertex K3,3-Petersen chain, no two-coordinate exact trade changes the local K3,3 type, while three-coordinate trades connect types 0->1->2, even within a fixed complete boundary signature.
- **Independent finite audits:** six-matching mixed chains KP, PK, PP have 7200, 7200, 5760 states and 3, 3, 1 neutral components; cube has nine perfect matchings, 4320 double covers and a neutral trade changing the unordered matching multiset.
- **Novelty qualification:** component product formulas draw on classical 3-cut matching parity and Kempe arguments; the specialization `m=1` is known. No claim of a major open conjecture resolution or specialist-vetted novelty.


## Neutral-transparent cubic substitution (8 October, evening)

- **General theorem:** gluing any neutral-transparent cubic tile onto a cubic host through a three-edge cut preserves the host's neutral-component graph **on connected components**; if every local boundary fiber has size w and diameter <= d, each component's cardinality multiplies by w and its diameter increases by at most d. **Status:** full mathematical proof, classical path-lifting ingredients, novelty not audited. See [theorem](../theory/neutral_transparent_cube_substitution_2026-10-08.md).
- **PM6 cube:** Q3 fixed-boundary fiber is connected with **48** labelled states and diameter **4**; all 4,320 labelled certificates and 90 signatures enumerated. **Status:** exhaustive finite lemma + CI test.
- **Padded CDCq cube:** for every q>=3 the fixed-boundary fiber is connected of size `w_q=4+28(q-3)+6*C(q-3,2)+6*C(q-3,3)`; finite q=3,4,5,6 bases have exact fiber diameters 2,6,6,7, and general q>=7 has bound 19 by neutral relocation of extra labels. **Status:** general proof conditional on fully enumerated finite q<=6 lemmas; computer-assisted, not pure symbolic proof.
- **Mixed two-block verifier:** cube plus K3,3 (12 vertices, 43,200 PM6 certificates, components 4,320/34,560/4,320); cube plus Petersen (16 vertices, 34,560 certificates, one component); 1,645,920 directed switches checked. **Status:** exact finite certificate computation, full code in repro_runs.
- **Crucial scope:** coordinates of a padded CDC are allowed to be empty locally. This does **not** prove existence of nonempty 5-cycle double covers. No full graph conjecture resolved, and no journal-level originality claim made.


## General component-enriched typed-cut response theorem (8 October, later)

- **Theorem (full mathematical proof):** for any three-edge sum of cubic graphs, in either six-perfect-matching multiplicity-2 covers or padded q-sheet cycle double covers, partition each local fixed-signature fiber into *its own internal neutral-connected components*. Label each signature-changing transition by both the coordinate pair and cut port pair. The weighted **synchronized typed product** has exactly the neutral connected components of the global certificate graph, with global component sizes equal to sums of local-fiber product weights. [Proof](../theory/component_enriched_three_cut_relation_2026-10-08.md).
- **Finite independent tests:** PM6 local state spaces K3,3 (900 states, 270 response nodes), cube (4,320 states, 90 response nodes), Petersen (720, 90 nodes); exact product quotient yields all correct components for K3,3+cube, Petersen+cube, K3,3+K3,3 and cube+cube. Three-sheet CDC complement-coloring tests separately reproduce K3,3+cube (two size-24 components), cube+cube (96 states, one component), K3,3+K3,3 (four size-6 components).
- **Status:** exact elementary theorem + enumerated finite checks; classical quotient/path-lifting ingredients; independent literature novelty review **not completed**. This does not yield a uniform finite-state bound because local neutral-component counts can grow exponentially even for a fixed signature.
- **Next novelty target:** compressed algebraic or symbolic representations of the weighted typed response objects, beyond explicit enumeration; strict-escape queries on the resulting exact quotient.


### Novelty correction: existing degree-three toric/edge-coloring theory

The 2026 paper by Mori–Motomura–Ohsugi–Tsuchiya, *Toric ideals of matching polytopes and edge colorings*, Mathematika 72 e70099, DOI [10.1112/mtk.70099](https://doi.org/10.1112/mtk.70099), recalls the *classical* theorem that proper edge-colorings of bipartite multigraphs are connected by changes involving at most three colors. Thus three-coordinate **exact** matching-multicover connectivity on bipartite cubic graphs is established prior work. Preserve the K3,3 width-three witness as an example, **not** as a novel global theorem. The research frontier considered here is binary-neutral **single-cycle** reconfiguration topology, component-enriched typed separator composition, and strict-escape behavior. Novelty of the exact quotient itself still needs a transfer-algebra literature audit.


### Padded five-sheet CDC validation and all-q K3,3 local classification

The exact component-enriched quotient was independently applied to **direct padded q=5 cycle double covers**, not just the three-sheet complement-coloring case: K3,3 has 840 local states, 60 complete signatures and 480 enriched response nodes; cube has 3,960 local states, 60 signatures and 60 nodes. Their 3-edge sum yields precisely 55,440 padded five-sheet certificates in **eight** components (two size 3,960 and six size 7,920). A separate all-q K3,3 classification follows from the fact that any two of its even subgraphs have connected symmetric difference: the unordered multiset of sheets is binary-neutral invariant; with q>=4 there are exactly eight global classes, and with q=3 exactly two. The q=3/4 finite enumeration is a computer-assisted base, extended symbolically for all q. See [theorem and source](../theory/component_enriched_three_cut_relation_2026-10-08.md). Do not interpret these padded spaces as an existence proof for nonempty-sheet 5-CDC.
