# Pivot: two-tree bridge-cover completion and 6-edge-connectivity

**Date:** 2026-10-08. **Status:** mathematical exploration and reproducible finite theorem; not a solution of the DeVos--Johnson--Seymour conjecture and not a submission-ready paper. No GitHub branch has been modified.

## 1. Problem statement and literature

DeVos--Johnson--Seymour ask whether every `(a+b+2)`-edge-connected graph admits an edge partition into an `a`-edge-connected and a `b`-edge-connected spanning subgraph. In particular, the `(2,2)` case asks whether every 6-edge-connected graph admits an edge partition into two bridgeless connected spanning subgraphs. The classical Nash-Williams--Tutte spanning-tree-packing theorem gives the assertion from 8-edge-connectivity by packing four edge-disjoint spanning trees and taking two unions of two trees. [Source](https://garden.irmacs.sfu.ca/op/partitioning_edge_connectivity).

This research attempts the 6-edge-connected case via tree scaffolds, fundamental cuts, exact SAT, and local exchanges. It did **not** prove the conjecture.

## 2. The exact two-tree bridge-cover reduction (proved)

Let `G=(V,E)` be a finite loopless multigraph admitting two edge-disjoint spanning trees `T_R` and `T_B`. Write `R=E\(T_R ∪ T_B)`. For an edge `e` in a spanning tree `T`, removing `e` defines a bipartition of `V`; write `D_T(e)` for the set of edges of `R` crossing this fundamental cut.

Assign each `r∈R` to red (Boolean `x_r=true`) or blue (`x_r=false`). Consider the two colored spanning graphs:

`H_R = T_R ∪ {r∈R : x_r=true}`, and `H_B = T_B ∪ {r∈R : x_r=false}`.

**Exact equivalence.** `H_R` and `H_B` are both 2-edge-connected if and only if the following CNF is satisfied:

- For every `e∈T_R`, the clause `∨_{r∈D_{T_R}(e)} x_r`;
- For every `e∈T_B`, the clause `∨_{r∈D_{T_B}(e)} ¬x_r`.

**Proof.** Both graphs are connected because they contain spanning trees. A non-tree edge lies on its fundamental cycle and hence cannot be a bridge. A tree edge is a bridge after adding the residual assigned edges exactly when no assigned edge crosses its fundamental cut. This is equivalent clause by clause. QED.

**Algorithmic corollary.** If every fundamental-cut clause contains at most two residual edges, the existence of a completion can be decided, and a solution constructed, in polynomial time by 2-SAT. Empty clauses are correctly treated as contradictions. The supplied standalone `bridge_completion.py` implements an implication-graph/SCC solver with no external dependencies. This is a straightforward application of classical 2-SAT rather than a claim of novelty.

More generally the reduction exposes a precise *cut-cover SAT* obstruction which can be combined with tree exchanges. It is not known here whether every 6-edge-connected graph admits *some* pair of trees whose formula is satisfiable.

## 3. A sharp warning: arbitrary scaffolds fail at arbitrarily high connectivity (proved)

For each `n≥7`, consider the complete graph `K_n` on vertices `0,…,n−1` and fix:

`T_R = {(0,1),(2,3)} ∪ {(0,j): 3≤j≤n−1}`;

`T_B = {(0,2)} ∪ {(1,j): 2≤j≤n−1}`.

Both sets are edge-disjoint spanning trees. In **every** edge partition extending these trees, red degree at vertex 1 equals 1 (its incident edge `(0,1)` is red, all `(1,j),j≥2`, are frozen blue), so the red graph cannot be 2-edge-connected. Symmetrically, blue degree at 0 equals 1. Thus the fixed-tree formula is unsatisfiable even though `λ(K_n)=n−1` is unbounded.

Meanwhile `K_n` admits two edge-disjoint Hamilton cycles for every `n≥7`. One is the step-1 cycle on `Z_n`, and another uses a step `s` coprime to `n` with `s≠1,n−1`. For `n≥7` such an `s` exists; the cycles have disjoint edges. Assign the remaining edges arbitrarily. Thus it is **tree freezing**, not the existence of a 2-edge-connected edge partition, that fails.

This disqualifies any proof strategy asserting arbitrary two-tree completion merely from high edge connectivity. This is an elementary explicit construction, not claimed as a major new graph theory theorem.

## 4. Exhaustive computational theorem on K7 (certified finite statement)

**Statement.** Let `T_R,T_B` be any ordered pair of edge-disjoint spanning trees of `K_7`. If `K_7−(T_R∪T_B)` is connected (equivalently, contains a third edge-disjoint spanning tree), the exact CNF in Section 2 is satisfiable. Thus both trees extend to a partition into two 2-edge-connected spanning subgraphs.

**Exhaustive certificate and coverage.** The supplied dependency-free `k7_packed_tree_exhaustive.cpp` enumerates all `7^(7−2)=16,807` spanning trees bijectively via Prüfer words. For every ordered pair, it tests disjointness. For each disjoint pair it tests connectivity of the nine residual edges using union--find. It computes both families of fundamental-cut clauses, and tests their conjunction against all `2^9=512` Boolean assignments in exact 512-bit sets. It prints:

```text
FINAL trees=16807 disjoint_pairs=27351240 three_tree_packings=24585120 unsatisfiable=0
```

The algorithm uses integer and bitwise operations; it does not rely on numerical tolerances, random search, or a general MILP solver. On the test machine it compiled with `g++ -O3 -std=c++17` and took ~5.66 seconds. The mathematical scope is **K7 only**. A kernel-checked Lean formalization has not been completed.

This finite statement is useful evidence for the conjecture that *carefully chosen and exchangeable* spanning-tree scaffolds could yield a proof, but it does not imply the 6-edge-connected problem.

## 5. Another infinite 6-edge-connected class (proved constructive closure)

Define a **six-edge vertex splice** of two simple 6-regular graphs as follows: delete a chosen vertex from each, leaving six dangling stubs on either side, and join the stubs in an arbitrary perfect matching. The resulting graph is simple and 6-regular.

**Connectivity lemma.** If both inputs are 6-edge-connected, so is the splice. To see this, consider any cut `S` in the splice and its intersections `X,Y` with the two shores. When both shores are proper nonempty vertex subsets after vertex deletion, each shore contributes at least 3 internal crossing edges: if `a` is the number of crossing edges within one shore and `q` its number of stubs on the `X` side, the two cuts in the original 6-edge-connected graph with its deleted vertex outside/inside show `a+q≥6` and `a+(6−q)≥6`; hence `a≥max(q,6−q)≥3`. If one shore is empty or full, one of the original cuts gives at least six combined internal/cross-splice edges; if the cut consists of the whole first shore against the empty second shore, it consists of exactly six splice edges. Every proper cut thus has size at least six. Regularity makes the edge-connectivity exactly six.

**Hamiltonian-splice closure.** `K7` decomposes into three edge-disjoint Hamilton cycles (the step-1, 2, and 3 cycles on `Z7`). Given any previously constructed 6-regular graph with such a decomposition and any six-edge splice with a fresh `K7`, one can permute the six neighbors of the deleted `K7` vertex to match the three pairs of Hamilton-cycle stubs at the old vertex. Each old Hamilton path then joins the corresponding `K7` Hamilton path through two splice edges, forming a new Hamilton cycle. The three cycles remain disjoint and cover every edge.

Consequently **every iterated six-edge vertex splice obtained by adjoining copies of `K7`**, with arbitrary choice of splice vertices and arbitrary stub matching, is 6-edge-connected, 6-regular, and decomposes into three Hamilton cycles. It therefore satisfies the `(2,2)` edge-partition conjecture (choose one Hamilton cycle red, the other two blue). It gives an explicit infinite class in the six-edge-connected, non-eight-edge-connected regime. This follows from established Hamilton-decomposition and splicing ideas and is not claimed to be an independently publishable advance.

The supplied `hamiltonian_splice.py` constructs/checks examples on 7, 12, 17 and 22 vertices.

## 6. Experiments and independent checks

- All `1,140` ordered pairs of disjoint spanning trees of `K5` independently checked by enumerating *all* assignments of the remaining two edges: exact CNF agrees with the bridge-free graph property in all cases. Of these, 300 pairs have completions and 840 do not.
- `1,250` random small 2-SAT instances checked against brute-force truth assignments, including unsatisfiable formulas and repeated literals.
- The six infinite-family counterexamples at `n=7,…,12` were checked for tree-validity, explicit unextendability and disjoint Hamilton cycles.
- Exact cut-constraint MILP feasibility and cut-defect one-edge local search on 16 *specified test instances* (several are repeated isomorphic models) found a valid `(2,2)` partition in every instance and no positive local optimum in twelve seeded greedily descended states per test instance. These are **not** an exhaustive classification of all 6-edge-connected graphs.
- On the cocktail-party graph `K8` minus a perfect matching, 20,913 out of 25,000 randomly attempted tree pairs left a connected residual graph, and all 20,913 admitted CNF completions. An earlier smaller run also included 213 eligible pairs of a 6-regular 9-vertex example, 199 of order 10, and 172 of order 12. These samples do not prove any statement beyond their individual tested cases.
- The exhaustive `K7` theorem covers 24,585,120 connected-residual ordered pairs, with no exceptions.

## 7. Literature-status correction: friendly partitions

The second pivot, 5-regular friendly/internal partitions, is less attractive for our main campaign than it looked initially. Zuo--Chen's October 2025 preprint abstract explicitly states a result for all 5-regular graphs of order at least 14 ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5558295)). Their final article in *Graphs and Combinatorics* **42**, article 58 (published June 20, 2026; DOI `10.1007/s00373-026-03051-7`) has an abstract which **does not repeat** that stronger result, while retaining a minimum-cut theorem. Therefore this work must be audited at the full-paper level before anyone treats the degree-five problem as settled or chooses it for a new attack. No claim about the validity of the earlier preprint is made here.

The related Bärnkopf--Nagy--Paulovics paper (2024) develops internal-partition methods and Cayley graph results. Any claimed new min-cut argument must be checked against Zuo--Chen 2026.

## 8. Current research verdict and next decisive target

**No general open problem was solved in this run.** The mathematically sound new output is a reusable exact fundamental-cut SAT reduction, a verified 24.6-million-case finite theorem on `K7`, and explicit positive/negative infinite classes distinguishing *arbitrary frozen scaffolds* from *tree-packing-compatible scaffolds*. The construction/algorithmic novelty is unassessed and likely modest. These findings help identify which potential rewriting proofs are too strong; they do not yet meet the program's publication-grade major-breakthrough standard.

The new, precisely posed research question is:

> For every 6-edge-connected graph, does there exist a triple of edge-disjoint spanning trees `T1,T2,T3` such that the cut-cover CNF for `T1,T2` is satisfiable? More ambitiously, is it satisfiable for **every** triple? If false, what are the minimal finite obstruction signatures, and what tree-exchange moves remove them?

The *existential* version would imply the DeVos--Johnson--Seymour `(2,2)` conjecture and is therefore difficult. The *universal* version is stronger and must be treated adversarially, not presumed true. The tree-exchange / unsatisfiable-core viewpoint seems more promising than another unconstrained defect threshold search.

### Reproduction

```bash
python bridge_completion.py
python test_bridge_completion.py
python hamiltonian_splice.py
python partition_lab.py
python third_tree_random_search.py
# Full exact K7 theorem:
g++ -O3 -std=c++17 k7_packed_tree_exhaustive.cpp -o /tmp/k7check
/tmp/k7check keep
```

`partition_lab.py` and `third_tree_random_search.py` additionally require NetworkX, NumPy and SciPy; all other Python proof-certificate scripts use the standard library only. The scripts operate read-only on other repository branches.
