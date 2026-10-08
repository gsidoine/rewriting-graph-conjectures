# Resistance as the exact cost of residual-kernel realization

**Research status: proved in a complete four-page mathematical draft; two explicit certified examples; external originality not verified.** See [the paper](../applications/berge_fulkerson/plateau/resistance_paper/main.tex), its [PDF](../applications/berge_fulkerson/plateau/resistance_paper/main.pdf) and [standalone construction code](../applications/berge_fulkerson/plateau/resistance_kernel_lift.py).

## Main theorem

For any finite simple **3-edge-connected cubic** graph `K`, let `r(K)` be the minimum cardinality of a set of edges whose deletion leaves a properly 3-edge-colourable graph. There exists a finite simple 3-edge-connected cubic graph `G` with an FR-triple `F=(M1,M2,M3)` with:

- the cubic kernel of `2G-(M1+M2+M3)` (after suppressing the doubled residual edges) is `K`;
- precisely `r(K)` edges of `G` are uncovered by the three matchings;
- `|V(G)|=|V(K)|+2r(K)`;
- neither the uncovered count nor host order can be improved for a prescribed kernel `K`.

If `r(K)=2`, the constructed host `G` is **3-edge-colourable**, although the specified FR-triple is nonextendable when `K` is a snark.

The existence proof starts with a minimum proper partial 3-edge-colouring of `K`, splits each deleted edge into a length-three path, and connects the newly created half-edge ports in pairs of the *same* missing colour. The two new edge types are respectively uncovered and doubly covered by the frozen triple. The key constraints are a parity count for the three port colours and minimum-deletion optimality, which prohibits equal colours at opposite ends of any deleted edge.

The converse says: for **any** prescribed FR-triple on a simple cubic host whose residual has a nonempty kernel `K`, `r(K)` is bounded above by the number of uncovered edges. To see this, remove from the kernel all edges whose representing residual chains pass through a doubled residual edge; the rest inherit a proper 3-edge-colouring from the original matching indices. At most one kernel edge is charged to each uncovered host edge.

## Computational examples

| Kernel | Order of K | Resistance | Realized host order | Host 3-edge-colourable? |
|---|---:|---:|---:|---|
| Petersen | 10 | 2 | 14 | yes |
| Flower snark J5 | 20 | 2 | 24 | yes |

There are 75 deleted-edge pairs of Petersen admitting a dangling proper colouring. Choosing one canonical dangling colouring per pair yields three nonisomorphic host graphs. All generated hosts have edge-connectivity three.

Tests: `tests/test_resistance_kernel_lift.py`. These include an independent networkx edge-connectivity check, exact kernel equality and absence of a colourability solution after only one edge deletion in either snark.

## Importance and limits

The result *connects* certificate-coordination (prescribed FR-triple), a graph-theoretic structural obstruction (kernel), and a classical distance-to-feasibility invariant (resistance) with an exact minimax formula. It is not an algorithm solving the Berge–Fulkerson conjecture and does not prove monotone normalization for arbitrary matching tuples. The classification of which optimal lifts are themselves class one beyond resistance two remains open in this program.

This research note is not a substitute for a targeted literature audit of previously known snark resistance lifts, and is not being declared publication-novel.
