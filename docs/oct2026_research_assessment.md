# October 8, 2026 — adversarial assessment of the coordinated matching research branch

## Source boundary

The private GitHub repository was read using the connected GitHub integration on 8 October 2026: it is private, uses default branch `main`, and retains the older July ledger and lacks the new plateau directory. No GitHub file or visibility mutation was performed. The user's private GitHub ZIP (`rewriting-graph-conjectures-main.zip`) was a **July 2026** state (11 existing tests), lacking the October 2026 Fan–Raspaud work. The new work is in `berge_fulkerson/plateau/` only, with new regression tests under `tests/test_plateau_oct2026.py`. Historical notebooks, pre-existing status ledger and manuscripts have not been altered.

## Main claims and assurance

| Claim | Status | Exact verification / proof mechanism |
|---|---|---|
| For 0<Q<=10, two-coordinate strict descent on cubic bipartite graphs; for 0<Q<=38, three-coordinate strict descent | **Analytic proof + exact finite hitting-set check** | Oriented defect cycles and hitting sets; all 15,504 five-triple families of six colors certified pair-hittable |
| For any fixed two coordinates, best simultaneous correction is polynomial-time computable on cubic bipartite graphs | **Analytic min-cost-flow reduction** | Integral convex-cost transportation network; agrees with exhaustive optima in 12 random 18-vertex states |
| Arbitrary cubic Q=6 direct pair correction criterion | **Elementary characterization** | Two selected colors hit three surplus edges, with even cycles in the residual 2-factor |
| Q=6 can require two matching-coordinate changes even in 3-edge-connected cubic bipartite graphs | **Proof + complete finite certificate** | 18-vertex 27-edge graph, six labelled perfect matchings, six 18-vertex assignment dual potentials, stand-alone dual checker; 47 PM enumerated independently |
| Every cubic bipartite Q=6 sextuple has a two-coordinate completion | **Analytic proof in manuscript** | Degree/defect structure: alternating 6-cycle; 3 three-subsets of six colors admit a 2-element transversal; freeze remaining 4 and use König |
| Infinite 3-edge-connected bipartite graphs of orders 18+4k with strict one-coordinate Q=6 traps | **Analytic lifting lemma + first three instances checked** | Balanced K3,2 substitution at a defect-free vertex, projection of arbitrary replacement; 18,22,26,30 vertices checked |
| High-girth bridgeless bipartite strict local minima with Q/n=1/3 | **Analytic covering lemma relying on standard residual finiteness of free groups** | Lift bipartite LP assignment dual potentials; explicit girth-6 connected 36-vertex cover verified |
| Four-coordinate joint correction to exact Q=0 on cubic bipartite graphs | **CLASSICAL CONSEQUENCE** | Freeze any 2 perfect matchings; residual 4-regular bipartite multigraph decomposes into 4 matchings by König |
| Finite 84-state 3-edge-cut boundary composition | **Standard exact reduction, toy case checked** | Unique boundary patterns 0,1,2,ALL; 84 multisets of six; triangular-prism exact test |
| All other bridgeless cubic graphs normalize under two-coordinate moves | **NOT PROVED, NOT CLAIMED** | Bipartiteness crucial for residual edge-colouring |
| October Fano-shore 22/28-vertex traps | **Not audited here** | Raw instances/scripts not present in July ZIP |
| Lean kernel-verified proofs | **NOT COMPLETED** | `lean` and `lake` unavailable |

## Why this differs from the classical results

König's theorem guarantees a one-step 4-coordinate solution and was already known; this is not a novel existence result. The bounded-range descent theorem and exact two-coordinate flow optimizer broaden the potential contribution, but neither establishes global two-coordinate convergence. The specific *sharp 1 vs 2 coordinate* threshold at the very first potential obstruction Q=6, infinite 3-edge-connected lifting, and the LP-dual cover stability are the plausible new contributions. Publication novelty **not yet established**; a stronger literature survey and external specialist review must precede public release.

Close neighbouring work:
- Bonamy et al., *The Perfect Matching Reconfiguration Problem* (2019), DOI `10.4230/LIPIcs.MFCS.2019.80`: **4-cycle flips** of a single perfect matching, quite different moves.
- Mori, Motomura, Ohsugi, Tsuchiya, *Toric ideals of matching polytopes and edge colorings* (2026), DOI `10.1112/mtk.70099`: at most **three-colour neutral transformations** connecting fixed multiplicity fibres for bipartite edge-colourings. Relevant, needs careful comparison.
- Luo, Hao, Luo, Zhang, Zhou, *Berge–Fulkerson Conjecture, Perfect Matching Partial Coverings and Odd Dividers* (2026), DOI `10.1002/jgt.70097`: different partial-covering approach.

## Research quality gate

This is a **candidate Level-2 structural finding** under the project's internal categories in the sense of an explicit theorem with an infinite family, but the standalone journal significance is **moderate and not yet certified**. It is not a Level-3 solution. Before public release:

1. Ask an outside graph-theory/combinatorial-optimization researcher to scrutinize both the proof and whether similar plateau examples / balanced expansions were previously known.
2. Complete a Lean implementation of the finite dual checker and preferably of the abstract lifting argument.
3. Consider improving to a theorem in a non-bipartite class or showing a sharp obstruction for a 2- or 3-coordinate rule, which would substantially strengthen publication prospects.
4. Only after the above, amend `docs/mathematical_status.md`, canonical paper inventory and public README; keep July versions until then.

## October continuation: falsification attempts

- `transversal_boundary.py` checks all 15,504 five-triple families and exhibits a six-triple family blocking all 15 coordinate pairs. This is a **formal set-system obstruction to the proof method**, not a graph-realized trap.
- `flow_optimize_two.py` computes globally optimal paired replacements by min-cost flow (rather than sampling replacements). Its outputs matched full pair enumeration on 12 independently seeded six-matching states of the 18-vertex graph.
- A separate exploratory search sampled 24 states on connected random cubic bipartite graphs of orders 24, 36, 48 and 72, using exact best-pair flow optimization at every step. Every sampled state reached Q=0 in one or two improving steps. **No exhaustive general-size conclusion follows.**
- A theorem-strength open problem remains: whether a strictly improving two-coordinate replacement exists from every positive defect on every cubic bipartite graph. The low-defect result proves this for Q<=10, not in general.

## Follow-on discovery: exact direct-repair coordination hierarchy (2026-10-08)

**New theorem candidate (independently certifiable, not externally refereed):**
On cubic bipartite graphs, the minimum number of whole perfect matchings
that must be replaced to obtain Q=0 in one step is exactly a finite
multicover hitting number. In the unit-defect regime m(e) in {1,2,3},
this becomes a 3-uniform hypergraph transversal number on six matching
labels. The least positive Q requiring direct repair widths 2,3,4 are
exactly 6,12,40. The latter two bounds have NEW 3-edge-connected cubic
bipartite certificate graphs on 18 and 40 vertices, checked by independent
standard-library scripts. See `docs/oct2026_exact_coordinate_hierarchy.md`
for proofs, explicit verification commands and novelty limitations.

**Important:** A four-coordinate *exact* direct-repair requirement does
NOT imply a three-coordinate strict-descent obstruction. The Q40 graph
admits a strict two-coordinate improvement 40->10. The kappa hierarchy
is a new and more precise structural parameter; it does not resolve
any major open graph conjecture or the all-Q strict two-coordinate
conjecture. The elementary criterion relies on Kőnig edge colouring;
only the sharp realizability constructions are potential novelty claims.
Do not merge this branch to main without external specialist review.

**Further exploratory nonbipartite check:** An independently compiled
C++ routine exhaustively enumerated all 2,040 Q=6 six-matching multiset
states in the 20-vertex flower snark J5. All admit exact two-coordinate
repair under the degree-two residual even-cycle test. This is finite
negative evidence for odd-cycle obstructions at Q=6 in that one graph,
not a universal nonbipartite theorem. Source and edge-order mapping are
archived at `berge_fulkerson/plateau/j5_q6_pair_audit.cpp` and
`j5_edges.txt`.
