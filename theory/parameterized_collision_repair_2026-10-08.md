# Uniform collision hypergraphs and parameterized exact repair

**Research note — October 8, 2026.** The reduction is proved here from König's bipartite edge-colouring theorem and standard parameterized Hitting Set results. This is **not** a claim of external publication-level novelty. It sharpens the interpretation of the v8 obstruction-hypergraph machinery and separates the bipartite and nonbipartite cases.

## Setup

Let \(G\) be a finite \(d\)-regular bipartite graph, let \(k\ge1\), and let \(M_1,\dots,M_t\), \(t=kd\), be **labelled** perfect matchings, with repetitions permitted. The target is an exact \(k\)-fold edge cover. For an edge \(e\), write \(S_e=\{i:e\in M_i\}\subseteq[t]\). Selecting coordinates \(I\subseteq[t]\) means that only matching positions indexed by \(I\) may change; all other matchings must remain literally unchanged. Let \(\kappa\) be the minimum size of such an \(I\) that permits exact repair.

Define the **uniform collision hypergraph** \(\mathcal C_k(\mathcal M)\) on ground set \([t]\) by

\[
\mathcal C_k(\mathcal M)=\bigcup_{e\in E(G)}\binom{S_e}{k+1}.
\]

This includes all \((k+1)\)-element subsets of heavily covered edges, **even if** \(|S_e|>k+1\). It is distinct from the v8 presentation that keeps quota constraints \(|I\cap S_e|\ge |S_e|-k\).

## Theorem A — exact equivalence

\[
\boxed{\kappa(G,\mathcal M)=\tau(\mathcal C_k(\mathcal M)).}
\]

**Proof.** Freeze \(F=[t]\setminus I\) and let \(f_e=|S_e\cap F|\). It is necessary that \(f_e\le k\) for all \(e\). Conversely, if these inequalities hold, prescribe residual multiplicities \(r_e=k-f_e\ge0\). At every vertex \(v\),

\[
\sum_{e\ni v}r_e=kd-|F|=|I|.
\]

Thus the residual multigraph is \(|I|\)-regular and bipartite. König's line-colouring theorem decomposes it into \(|I|\) perfect matchings, which replace the selected coordinates and yield exact multiplicity \(k\). Finally, \(f_e\le k\) holds precisely when \(I\) intersects every \((k+1)\)-subset of every \(S_e\). This is the hypergraph hitting-set condition. \(\square\)

The theorem is valid for arbitrarily large initial edge multiplicities. No restriction to unit-defect states, cubic graphs, or connected graphs is needed.

## Theorem B — fixed-multiplicity parameterized algorithm

For every **fixed** \(k\), deciding whether \(\kappa\le r\) and constructing an optimal direct repair is fixed-parameter tractable with parameter \(r\). A simple deterministic branching algorithm uses

\[
O((k+1)^r\,\operatorname{poly}(|E(G)|,t))
\]

time for a given budget \(r\). It can avoid explicitly constructing \(\mathcal C_k\).

**Proof.** Suppose some current choice \(I\) leaves an edge with more than \(k\) frozen occurrences. Choose any \(k+1\) of those indices. Every valid extension of \(I\) must select at least one of them. Branch on the \(k+1\) choices and reduce the remaining budget. The depth is at most \(r\); all feasibility checks are polynomial. Iterative deepening from \(0\) to the optimum returns the exact minimum and witnesses. \(\square\)

For \(k=1\), \(\mathcal C_k\) is a graph and direct repair is exactly **Vertex Cover** on the collision graph. For \(k=2\), the problem is **3-uniform Hitting Set**, even if some edges appear in four or more original matchings. Classical constant-rank Hitting Set kernelization therefore also supplies polynomial kernels for every fixed \(k\); that kernelization is not a new contribution of this work.

## Theorem C — parameter boundary when multiplicity is variable

When \(k\) is part of the input, deciding \(\kappa\le r\) is **W[2]-hard parameterized by \(r\)**, even for hosts that are complete bipartite graphs \(K_{D,D}\) with their maximum possible edge-connectivity.

**Reduction sketch with exact preservation.** Given any Hitting Set instance \(\mathcal H\), pad each nonempty hyperedge with fresh private elements to obtain a common cardinality \(p\ge2\). This preserves the minimum transversal number: an initially chosen private element can be replaced by any original element of the same padded edge. Set \(k=p-1\) and apply the explicit polynomial-size complete-bipartite realization from `certificate_coordination/v8/complete_bipartite_realization.py`. In each diagonal block, one surplus edge family has \((k+1)\)-coordinate signature equal to a padded hyperedge. Every other edge has multiplicity at most \(k\), and the remaining coordinates supply exact regular factorization. Theorem A yields \(\kappa=\tau(\mathcal H)\) with the parameter \(r\) unchanged. Since unrestricted Hitting Set is W[2]-complete in its solution size, the stated hardness follows. \(\square\)

**Scope warning.** This proves W[2]-*hardness*, not membership or completeness for the general repair problem with variable \(k\). Nor does it show hardness for fixed cubic degree or a fixed number of matching coordinates.

## Nonbipartite correction — the factorization obstruction

For an arbitrary \(d\)-regular (possibly nonbipartite) graph, hitting \(\mathcal C_k\) remains **necessary**. It is no longer sufficient: after fixing \(F\), the residual \(|I|\)-regular multigraph must actually admit an \(|I|\)-edge-colouring (decomposition into perfect matchings). For \(|I|=2\), this means that every cycle component of the residual 2-regular multigraph has even length (counting parallel-edge 2-cycles).

The **triangular prism** demonstrates a strict gap even when the underlying cubic graph *is* 3-edge-colourable. Take \(k=1\), \(t=3\), and all three original matchings equal to the three vertical edges. The collision graph is a triangle on the three matching indices, so its vertex-cover number is \(2\). Freezing one vertical matching leaves two vertex-disjoint odd triangles, which cannot decompose into two perfect matchings. Thus two-coordinate exact repair is impossible. However, replacing all three matchings can yield a proper 3-edge-colouring; the true repair width is \(3>2\).

This supplies a natural **two-layer obstruction theory**:

1. Coordinate collision constraints, encoded by \(\mathcal C_k\).
2. Residual edge-factorization constraints (vanishing automatically on bipartite graphs, but not on general regular graphs).

## Reproducibility

```bash
python -m pytest -q tests/test_collision_hypergraph.py tests/test_nonbipartite_factorization.py
```

`certificate_coordination/collision_hypergraph.py` provides a standalone implicit branching solver and explicit hypergraph generator. The tests compare against exhaustive coordinate subsets on random incidence families, actual matching tuples, and the v8 complete-bipartite realization; a separate checker enumerates every perfect matching of the triangular prism.

## Closest established results / intellectual boundary

- König's line-colouring theorem provides residual factorization, and the exact-repair theorem is an application of it.
- Hitting Set parameterized by solution size is W[2]-complete; fixed-rank Hitting Set is FPT and admits polynomial kernels. See, for example, Bérczi et al., *Fixed-Parameter Algorithms for Fair Hitting Set Problems*, MFCS 2023, https://doi.org/10.4230/LIPIcs.MFCS.2023.55.
- Perfect-matching reconfiguration by alternating-cycle flips is a **different move system**; see Ito et al., *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, SIAM J. Discrete Math. (2022), https://doi.org/10.1137/20M1364370.

Novelty here, if any, is the **coordination-language formulation and the realization inside a specific matching-certificate family**, not the classical graph-colouring or parameterized Hitting Set machinery. Specialist novelty review remains outstanding.
