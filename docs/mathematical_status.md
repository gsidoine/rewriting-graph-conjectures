# Mathematical Status Ledger

**Audit date:** 12 July 2026  
**Rule:** a claim is authoritative only at the status written here.  Historical prose in `archive/original_files/` is not automatically endorsed.

## Berge–Fulkerson programme

| Claim | Status | Audit note |
|---|---|---|
| Replacement identity \(\Delta Q=w_i(N)-w_i(M_i)\) | **THEOREM — independently verified** | Checked algebraically edge by edge and by randomized exact tests. |
| At a one-coordinate local minimum, \(S_i\le n/3\) | **THEOREM — independently verified** | Uses \(\frac13\mathbf1\) in the perfect-matching polytope of a loopless bridgeless cubic multigraph. Connectedness is unnecessary. |
| If \(Q>2n\), one coordinate strictly decreases \(Q\) | **THEOREM — independently verified** | Follows from \(\sum_iS_i=Q\). |
| At most \(5n\) strict moves reach \(Q\le2n\) | **THEOREM — independently verified** | \(Q\le12n\), \(Q\) is even, and every strict move lowers it by at least two; at most \(30n\) weighted-matching calls. |
| Residue-dependent cyclic barrier | **THEOREM — independently verified after proof repair** | The relative-interior contradiction must exclude equality for each individual \(S_i=n/3\), not only the simultaneous equality case. The audited paper contains the corrected argument. |
| Defect support alternates on even cycles when \(m(e)\in\{1,2,3\}\) | **THEOREM — independently verified** | Local multiplicity triples are exactly \((2,2,2)\) or \((1,2,3)\). |
| Every alternating defect 4-cycle is one-coordinate repairable | **THEOREM — independently verified** | Membership-set argument checked. |
| Every nonzero local minimum in a simple cubic graph has \(Q\ge6\) | **THEOREM — independently verified** | Includes the case of an edge with \(|d(e)|\ge2\). |
| In the \(\{1,2,3\}\) regime, \(Q=6\) is one alternating 6-cycle | **THEOREM — independently verified** | The total-intersection criterion certifies a direct alternating-cycle flip, not every conceivable replacement. |
| Petersen: all 462 sextuple-multiset states normalize | **COMPUTATIONAL RESULT — reproducible** | Independent Python rerun; six perfect matchings and one target. |
| Flower snark \(J_5\): all 2,324,784 states normalize | **COMPUTATIONAL RESULT — reproducible** | Fresh C++17 rerun; 32 perfect matchings, 132 targets, zero unresolved. |
| Random bridgeless cubic and bipartite logs | **COMPUTATIONAL RESULT — historical log only** | Inputs/seeds are partly encoded in the logs, but no complete independent generator/checker reconstruction was supplied. |
| Every bridgeless cubic graph normalizes to \(Q=0\) | **CONJECTURE** | This would imply Berge–Fulkerson. The current theorem only enters a low-defect region. |

## 3-Decomposition programme

| Claim | Status | Audit note |
|---|---|---|
| \(b(T)=0\) iff the tree extends to a 3-decomposition | **THEOREM — independently verified** | Cotree components have maximum degree two. |
| Exact defect identity \(|D(T)|=2b(T)\) | **THEOREM — independently verified** | Verified theoretically and in tests. |
| Endpoint leaf-slide is non-increasing | **THEOREM — independently verified** | Audited proof gives all possibilities for the cotree degree of the receiving vertex. |
| Tail-peel is non-increasing | **THEOREM — independently verified** | Audited proof supplies the missing component-merger cases. |
| Monotone Exchange Conjecture | **CONJECTURE** | Stronger than 3-Decomposition because it asks for monotone normalization from every spanning tree. |
| All connected simple cubic graphs through order 10 satisfy the plateau-exit statement | **COMPUTATIONAL RESULT — reproducible** | 27 isomorphism classes, 30,619 spanning trees, 152,120 safe rewrites, zero closed positive plateau SCCs. |
| Unrestricted One-Defect Conjecture | **CONJECTURE** | The cycle part may change. |
| Fixed-cycle blossom-to-bridge lemma | **DISPROVED** | Explicit 16-vertex counterexample. |
| Counterexample counts: 1,448 size-5 matchings, 105 good; 615 size-6 matchings, zero tree complements | **COMPUTATIONAL RESULT — reproducible** | Independent exhaustive Python verifier. |
| Near-Unicyclic Matching Decycling under the stated promises is NP-complete | **THEOREM — independently verified after source-promise clarification** | The source reduction constructs a Hamiltonian fairly cubic graph with an explicit Hamiltonian cycle; the extra promise is inherited from the construction, not literally part of the cited theorem statement. |
| Fixed-cycle one-defect repair in bridgeless cubic graphs is NP-complete | **THEOREM — independently verified** | Triangle completion preserves the required correspondence; audited paper spells out both directions. |
| The 3-Decomposition Conjecture | **OPEN GAP** | Not solved here. |

## Barnette programme

| Claim | Status | Audit note |
|---|---|---|
| Classical dual equivalence with two induced trees | **THEOREM — established literature** | Not new; fully credited. |
| Exact identity \(\Phi=z+2(t-1)\) | **THEOREM — independently verified** | Valid for nontrivial binary colourings in the stated simple plane-dual setting. Nested cycles still create exactly \(t+1\) regions on the sphere. |
| \(\Phi=0\) iff the primal even subgraph is Hamiltonian | **THEOREM — independently verified** | Immediate from the identity and nontriviality. |
| Radius-two connected-patch normalization fails on a 36-vertex example | **COMPUTATIONAL RESULT — reproducible** | A fresh complete reverse-reachability run over all \(2^{20}\) colourings leaves exactly six radius-two traps, all with \(\Phi=2\); radius three reaches every state. The six masks and independent C++ verifier are archived. |
| Selected 30 generated 22-dual-vertex instances: two pair-flip failures, both resolved by triples | **COMPUTATIONAL RESULT — reproducible** | Fresh C++ output exactly matches `steps8res.txt`. |
| Historical 48-vertex/six-mask trap certificate | **COMPUTATIONAL RESULT — historical log only / inconsistent** | On the supplied `step10.txt` graph, the six masks have potentials 14,20,18,18,20,14 rather than the implied value 2 and are not locally closed. Do not cite as verified. |
| More than \(10^8\) colourings tested without a radius-three obstruction | **COMPUTATIONAL RESULT — historical log only** | Large input/result files are preserved, but the complete run was not independently repeated in this audit. |
| Three-Face Normalization Conjecture | **CONJECTURE** | Stronger than Barnette; no proof claimed. |
| Every \(\Phi=2\) state escapes with a connected triple | **CONJECTURE** | Principal theorem-sized frontier. |
| Barnette's Conjecture | **OPEN GAP** | Not solved here. |

## Tutte 5-flow branch

All supplied claims in this directory are classified as **HEURISTIC** or **OPEN GAP** unless a theorem is explicitly repeated in an audited paper.  The residual-network and polarized-cut ideas remain exploratory.

## Open Problem Garden search

The repository inspected several two- and three-star graph-theory problems and selected 3-Decomposition as the final target because the programme already yields a verified obstruction theorem and an NP-completeness result directly constraining a natural proof strategy.  **No listed open problem was completely solved.**
