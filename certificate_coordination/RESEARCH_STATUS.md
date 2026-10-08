# Certificate coordination research — 8 October 2026 (v7)

**Scope:** additive research branch, not the authoritative July theorem ledger. The main theorems below have full informal mathematical proofs and reproducible independent checks. They are **not** Lean-certified and their novelty has **not** been independently refereed.

## New results

1. **Exact multicover repair criterion.** In a `d`-regular bipartite graph with `kd` perfect matchings targeting multiplicity `k`, changing coordinates `I` can yield an exact cover if and only if `|I ∩ S_e| >= |S_e|-k` for every edge. This follows directly from bipartite one-factorization; not individually novel.
2. **Exact conflict-graph theorem at k=1.** With `d` matchings on a `d`-regular bipartite graph, the direct exact repair width is the vertex-cover number of the conflict graph on matching indices, where an edge means the two matchings overlap.
3. **High-connectivity universality.** For any input finite graph `H` and any prescribed edge-connectivity `c`, construct a simple connected `d`-regular bipartite graph `G` with `lambda(G)>=c` and an explicitly listed tuple of `d` perfect matchings. The conflict graph equals `H` plus isolated indices. Both the direct repair width and the **minimum number of strictly improving one-coordinate replacements** needed to reach the exact cover equal `tau(H)`. The initial defect is `Q=2d|E(H)|`. Proof in `paper/main.tex`.
4. **Complexity corollary.** Direct-repair-width and shortest strict one-coordinate normalization are NP-complete for this generalized matching certificate problem, even on connected, arbitrarily prescribed edge-connected regular bipartite graphs. The shortest-path problem remains hard on a family explicitly guaranteed to admit strictly improving normalization. APX-hardness follows from the exact optimum-preserving reduction from bounded-degree vertex cover.
5. **Separator/signature splice.** Switching two edges with identical membership signatures between disjoint regular bipartite certificate systems preserves all matching constraints and the union of their edge signature multisets. Multiple singleton splices connect the vertex-cover gadgets while maintaining a prescribed edge-connectivity lower bound. This is a compositional mechanism for obstruction hypergraphs.
6. **Maximally connected constant-defect traps.** For every `d>=8`, `K_(d,d)` (edge connectivity `d`) admits a `d`-perfect-matching tuple at the *smallest possible positive defect* `Q=4`, and no single-coordinate strict improvement exists. Explicit integral bipartite assignment duals prove this uniformly in `d`. An explicit neutral-then-strict path `Q:4 -> 4 -> 0` exists for every constructed instance. The same phenomenon holds for `K_(4,4)`.
7. **Asymptotic separation.** Taking input `H=K_h`, `c=floor(sqrt(h))`, gives increasingly edge-connected graphs with direct repair width `kappa/d -> 1`. Thus arbitrarily high ordinary edge-connectivity cannot force a uniformly submaximal relative coordination width in this generalized setting.

These theorems apply to the **generalized one-fold target (`d` matchings of a `d`-regular graph)**. They do *not* solve the original six-matchings/two-fold-cover Berge–Fulkerson problem, and they do not prove the DeVos–Johnson–Seymour edge partition conjecture.

## Independent computational passes

- A general constructor and separate checker validate matching validity, degree, signature conflict graph, vertex-cover equality, and actual networkx edge connectivity for P4, C5, K5 at c=2 or c=4; recorded in `verification.log`.
- The strict-path checker verifies every matching and each strict Q decrease, including C5 on 120 vertices (Q history `120,72,48,0`), P4 on 36 vertices and K5 on 240 vertices.
- An exhaustive campaign ran every nonempty labelled graph on four vertices at c=1,2,4, totaling 189 host instances, and checked exact shortest paths on the constructed family.
- A dependency-free checker verifies *all* integer optimality dual inequalities for K_(d,d), with d in {8,9,10,12,16,24,32}. Independent scipy Hungarian minimization gives identical results.
- A separate exhaustive enumeration on K_(4,4) found 144 one-coordinate strict local minima at positive defect among the 17,526 positive-defect four-matching multisets (4 perfect matchings total). The lexicographically first Q=4 trap has an explicit neutral-then-strict escape and an exact two-coordinate repair.
- A separate spanning-tree campaign found that merely packing three edge-disjoint spanning trees does not ensure two bridgeless colour classes in an arbitrary sparse graph. The seven-vertex witness has a vertex of degree three, which is a straightforward obstruction. This **does not** meaningfully affect the six-edge-connected partition conjecture; see `edge_partitioning` v6.

## Mathematical significance and limitations

The result is a genuine structural and complexity **Level-2 theorem candidate**, not a resolution of a classical open conjecture. It joins a universal exact characterization to an explicit connectivity-preserving realization and an optimum-preserving hardness reduction. The K_(d,d) dual construction independently rules out connectivity-based strict local normalization, even at minimum defect.

Novelty remains provisional. Prior work on shortest alternating-cycle reconfiguration of a *single* perfect matching proves NP-hardness (Ito, Kakimura, Kamiyama, Kobayashi, Okamoto, SIAM J. Discrete Math., DOI 10.1137/20M1364370); our tuple-coordinate and strict quadratic descent move system is different. Bonamy et al.'s MFCS 2019 matching reconfiguration paper is also relevant. A specialist reviewer must compare the precise problem definitions and the connectivity-strengthened construction before claiming priority.

## Reproducibility commands

```bash
python certificate_coordination/realize_conflict.py
python certificate_coordination/check_strict_paths.py
python certificate_coordination/exhaustive_host_check.py
python certificate_coordination/high_connectivity_traps.py
python certificate_coordination/k44_trap_certificate.py
python -m pytest -q
cd certificate_coordination/paper && latexmk -pdf main.tex
```

`realize_conflict.py` imports `networkx` only for the *optional* independent exact-connectivity audit. Core construction, strict paths, Kdd duals, and every infinite-family proof use no MILP, SAT, external solver, or numerical tolerance. `k44_trap_certificate.py` uses only Python stdlib.

## Next directions

1. Recheck novelty against prescribed-matching-set packing, monotone reconfiguration, and graph conflict realization beyond the papers identified so far.
2. Formalize the exact repair criterion, singleton-signature edge splice, and four small integer dual witnesses in Lean (not installed in the current runtime).
3. Parameterize exact coordination by **obstruction graph treewidth** (for k=1, ordinary vertex cover) rather than graph connectivity. Determine the structural compatibility constraints for general k>1.
4. Return to the six-matching, two-fold-cover case only if the obstruction-hypergraph framework reveals a new decomposition or a non-trivial exchange bound beyond known factorization theorems.
5. Preserve the independent edge-cut partition branch; the v6 three-tree CNF hypothesis remains blocked by unproved structural compatibility in the 6-edge-connected setting.
