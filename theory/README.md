# Track A — General certificate-coordination theory

**Purpose.** Study exact repair width, strict/neutral reconfiguration, obstruction hypergraphs, and finite separator interfaces independently of particular open graph conjectures.

The generic implementation is under `certificate_coordination/`. Application-specific code is located under `applications/` and can be imported with the `applications.<problem>` prefix. The theoretical index links to both without duplicating code.

| Workstream | Code and certificates | Paper and status |
|---|---|---|
| Multiplicity-2 six-matching repair/plateaux | [`berge_fulkerson/plateau/`](../applications/berge_fulkerson/plateau) | [paper source](../applications/berge_fulkerson/plateau/paper/main.tex), [readme](../applications/berge_fulkerson/plateau/README.md) |
| Sharp direct-repair thresholds / local drift | [`berge_fulkerson/plateau/next_phase/`](../applications/berge_fulkerson/plateau/next_phase) | [notes](../applications/berge_fulkerson/plateau/next_phase/README.md) |
| Three-cut gluing, componentwise corrections | [`berge_fulkerson/plateau/next_phase/continuation_20261008/`](../applications/berge_fulkerson/plateau/next_phase/continuation_20261008) | [claim status](../applications/berge_fulkerson/plateau/next_phase/continuation_20261008/CLAIM_STATUS.md) |
| Obstruction conflicts, variable-degree systems | [`certificate_coordination/`](../certificate_coordination) | [v7 proof](../certificate_coordination/paper/main.tex), [status](../certificate_coordination/RESEARCH_STATUS.md) |
| Complete-bipartite hypergraph universality, multiplicity `k`, width-DP | [`certificate_coordination/v8/`](../certificate_coordination/v8) | [v8 proof](../certificate_coordination/v8/paper/main.tex), [status](../certificate_coordination/v8/README.md) |


- **New October 8 theorem-first branch:** [Three-edge-cut synchronization](three_cut_synchronized_reconfiguration_2026-10-08.md) proves a typed neutral-move gluing principle for both cycle double covers and six-matching multicovers. [K3,3 neutral-fiber obstructions](k33_neutral_fiber_obstructions_2026-10-08.md) exhibits disconnected fixed-signature fibers in both systems, requiring component-enriched boundary states. Proof status and novelty limitations are stated in each note.


## Uniform-multiplicity amplification theorem (8 October)

[Exact neutral components of m-fold matching multicovers on K3,3 chains](exponential_neutral_components_multicovers_2026-10-08.md) proves that the `3m`-matching reconfiguration graph of a connected 3-edge-connected bipartite cubic chain of `n` K3,3 tiles has exactly `(m+1)^n` components. The theorem gives exact component sizes, Franel-number total counts, and **(m+1)^n components even in each fixed three-edge boundary fiber**. Independent small-case enumeration includes all 94,080 multiplicity-3 local states and 9,000 two-block multiplicity-2 states. The case `m=1` is classical edge-Kempe theory; **novelty for m>=2 is not yet vetted**.


## Pair-rigid tile normal form and mixed Petersen chains (8 October)

[Pair-rigid matching multicover composition](pair_rigid_tile_multicover_algebra_2026-10-08.md) extends the previous K3,3 calculation to **arbitrary three-edge-sum chains of cubic tiles whose pairs of perfect matchings differ on a single alternating cycle**. The neutral components are indexed exactly by the local integer matching-multiplicity solutions `A_T x=m1`, with explicit product-size formulas and a constructive fixed-signature path bound. For chains of `a` K3,3 and `b>=1` Petersen tiles, the graph is non-3-edge-colorable; odd-m multicovers do not exist; even-m multicovers have precisely `(m+1)^a` neutral components. The cube Q3 is a sharp non-rigid obstruction. On K3,3 + Petersen, three-coordinate exact trades connect the three binary-neutral components. Independent finite global enumerations are in `repro_runs/verify_mixed_pair_rigid.py`. **Novelty not established; proof remains a research draft.**


## Cross-certificate port-coherence theorem (8 October)

[Port-coherent neutral-reconfiguration gluing](port_coherent_neutral_reconfiguration_2026-10-08.md) extends the pair-rigid theorem to **both labelled cycle double covers and perfect-matching multicovers**, requiring only that each local neutral orbit be connected **inside every fixed full boundary signature**. It gives a bijection between global components and products of local orbits, exact component-size products, and additive fixed-boundary neutral-path diameter bounds. The non-pair-rigid cube Q3 satisfies the hypothesis for 3-sheet CDC and 6-matching double-cover certificates by independent exhaustive enumeration. Combining cubes, K3,3 and Petersen tiles yields exact non-3-edge-colorable examples in the matching system. Classic 3-edge-coloring/Kempe consequences are **not novel**; the general abstract theorem remains a research proof draft pending literature audit.
## Pair-rigid tile product theorem — 8 October continuation

[Exact component algebras for pair-rigid cubic tiles](pair_rigid_tile_multicover_algebra_2026-10-08.md) extends the K3,3 multicover theorem to a family of 3-edge-sum chains built from arbitrary pair-rigid cubic tiles, including Petersen and triangular-prism tiles. The local types are feasible integer solutions to the tile perfect-matching incidence equations, and both the global and fixed-signature neutral components factor exactly. Mixed Petersen/K3,3 chains are non-3-edge-colorable and retain `(m+1)^a` components when `m` is even (no covers when `m` is odd). The note includes a sharp **binary-vs-three-coordinate** trade threshold on the mixed 14-vertex graph. The cube invalidates the local multiset invariant without pair rigidity. **Status: unrefereed proof draft, independent finite tests; novelty not established.**


## General neutral-transparent cube substitution (8 October, later)

[Exact three-cut component-preserving insertion theorem](neutral_transparent_cube_substitution_2026-10-08.md) **removes the pair-rigidity requirement**. A tile with connected fixed-boundary neutral fibers induces a bijection of neutral-reconfiguration components upon attachment to any cubic host; uniform fiber sizes multiply the certificate counts, with additive diameter overhead. The cube `Q3` is neutral-transparent for six-perfect-matching double covers (**48 extensions per boundary signature, diameter 4**) and for **padded q-sheet cycle double covers for all q>=3**, with exact extension factor `4+28(q-3)+6*C(q-3,2)+6*C(q-3,3)` and fixed-fiber diameter at most 19 for all q. Finite base lemmas for q=3,4,5,6 and PM6 are checked exhaustively by CI tests; a separate verifier reproduces two mixed insertion examples with 77,760 states and 1,645,920 directed neutral switches. This is a theorem with **computer-assisted finite ingredients**, not a vetted novelty or 5-CDC proof.



## Exact component-enriched typed three-cut algebra (8 October 2026)

[Complete typed boundary-response quotient](component_enriched_three_cut_relation_2026-10-08.md) eliminates both the pair-rigidity and connected-fiber assumptions from neutral reconfiguration **across any three-edge cut**. The response state is a full boundary signature *plus an internal neutral-component index*; transitions are typed by the coordinate pair and the two cut ports used. The global neutral connected components are **exactly** those of the synchronized typed product; each component size is the sum of products of local component weights. This provides a unifying theorem for six-perfect-matching double covers and padded q-sheet cycle double covers. Reproducible quotient tests include K3,3, cube and Petersen in PM6, and K3,3/cube in the three-sheet CDC model. The theorem is mathematically exact but does **not** imply bounded-state or polynomial-time computation for arbitrary graphs; novelty relative to transfer/reconfiguration literature remains unvetted.


## Exact finite-group certificate repair (28 October 2026)

[Group-potential quotient-holonomy and weighted coset-mode repair](group_potential_repair_2026-10-28.md) gives an exact feasibility and minimum-edit formula for finite-group edge-potential certificates, including noncommutative groups, a sharp universal repair bound `floor((1-1/|H|)n)`, and an exact count of strict-feasibility reconfiguration components for bounded-coordinate moves. The included [independent brute-force tests](../tests/test_gauge_repair.py) cover Z2, Z3 and S3. **These are elementary combinations of classical gain-graph/switching ideas; no originality, Lean verification, or general graph-conjecture solution is claimed.**

## Primary definitions

For a tuple of `kd` perfect matchings in a `d`-regular bipartite graph, the target is multiplicity `k` on every edge, with defect `Q_k = sum_e (m(e)-k)^2`. **Direct-repair width** is the fewest labelled coordinates replaced at once to reach zero. **Strict reconfiguration distance** is the shortest sequence of one-coordinate changes strictly decreasing `Q_k` at every move; infinity is allowed. These parameters are not interchangeable.

## Research integrity

- Proofs in October 2026 manuscripts are **research drafts**, with independently executable finite checks but no formal Lean kernel checking, journal refereeing, or comprehensive specialist novelty audit.
- Statements proved by finite code are **finite computational results**, not infinite theorems.
- Results for variable degree (and `kd` coordinates) must **not** be projected to the fixed cubic six-matching conjectures.
- To reproduce: run `python -m pytest -q`; then follow the `README.md` in each workstream for independent certificate programs.

See [current claim register](../docs/claim_register_oct2026.md) for a cross-project classification.

## New parameterized consequence (October 8)

[Uniform collision hypergraphs and the parameter boundary for exact repair](parameterized_collision_repair_2026-10-08.md): fixed cover multiplicity gives an implicit bounded-depth FPT search in repair width, while variable multiplicity inherits W[2]-hardness from the v8 complete-bipartite realization. The note also isolates the independent nonbipartite factorization obstruction on the triangular prism. **This is a theoretical research note, not an externally refereed novelty claim.**

## New residual-factorization and separator branch (October 8)

- [Cut-signature factorization and 3-versus-4 port compatibility](cut_signature_factorization_2026-10-08.md): a finite response algebra for residual edge-colourings, with an exact Petersen 4-pole incompatibility. The cut parity ingredient is classical.
- [Sharp 14-vertex nonextendable Fan–Raspaud triple](../applications/berge_fulkerson/plateau/FR_EXTENSION_OBSTRUCTIONS_20261008.md): a nonbipartite residual factorization obstruction despite odd-cut feasibility, suppressed to a Petersen cubic kernel; explicit one-coordinate escape and all-even-order expansions.

## Resistance as an exact obstruction-realization cost

[Resistance--kernel theorem and complete proof status](resistance_kernel_realization_2026-10-08.md): a general bridge from proper partial edge colourings to frozen perfect-matching covers and their residual kernels (with sharp vertex/defect cost).

## Non-monotone reconfiguration: an unbounded barrier theorem (October 8)

[Exact uphill FR-triple barriers](fr_uphill_barriers_2026-10-08.md) show that even class-one, 3-edge-connected cubic graphs do not admit universally non-increasing normalization of arbitrary FR-triples. A 10-vertex seed, a `K_{3,2}` lifting theorem and dependency-free exact verifier yield an infinite family with barrier at least `3**t` on `10*5**t` vertices. This is a proof draft with finite certificates; specialist novelty review remains outstanding.

## Exact FR triple transfer operator and component preservation (October 8)

- [Three-pole defect polynomial, component-preserving projection, minimum-defect scaling and universal entropy](fr_three_pole_renormalization_2026-10-08.md). The proof counts local cube/six-cycle phase fibres and verifies the operator by full small-graph enumeration. Does not prove any open matching-cover conjecture; originality unreviewed.
