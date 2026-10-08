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
