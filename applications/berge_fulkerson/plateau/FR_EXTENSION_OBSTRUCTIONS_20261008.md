# A sharp order-14 obstruction to extending Fan–Raspaud triples

**October 8, 2026 — original research draft, computationally certified finite base and complete reduction proof.**

This note concerns **extension of a *specified* triple** of perfect matchings to a Fulkerson cover. It does not assert a counterexample to Berge–Fulkerson (indeed the base graph is 3-edge-colourable), nor does it claim literature novelty without specialist review.

## Setup and exact reduction

Let `G` be a simple cubic graph, and let `F=(M1,M2,M3)` be a triple of perfect matchings with empty common intersection (an FR-triple). Put `f(e)=|{i:e in Mi}|` and let `R=2G-(M1+M2+M3)` be the 3-regular multigraph with edge multiplicities `r(e)=2-f(e)`.

**Proposition 1 (extension criterion).** `F` can be extended by three further perfect matchings to cover each edge of `G` exactly twice **iff** `R` is 3-edge-colourable. This is immediate by subtracting the already fixed three matchings from the prescribed double cover.

At every vertex the triple's three matching incidences have multiplicity pattern `(1,1,1)` or `(2,1,0)`. Hence the uncovered edges `E0={e:f(e)=0}` and the doubly covered edges `E2={e:f(e)=2}` are matchings having exactly the same vertex set. Their union is a vertex-disjoint collection of even circuits alternating `E0` and `E2`. If `u=|E0|`, either `u=0` or (for simple `G`) `u>=2`.

**Proposition 2 (doubled-edge kernel).** Suppress in `R` every pair of parallel copies of an edge in `E0`: remove its two endpoints and the incident single edges, replacing the latter by one edge joining their other ends. Continue along any resulting degree-two paths. Components consisting only of alternating doubled/single edges can be discarded, because each has an explicit 3-edge-colouring. Denote the remaining cubic pseudograph by `K(F)`. Then

    R is 3-edge-colourable  <=>  K(F) is 3-edge-colourable.

If `R` is bridgeless, `K(F)` is loopless and bridgeless. Its vertex count is `n-2u` (possibly zero).

*Proof.* Every doubled edge in a proper 3-edge-colouring uses two colours; at both endpoints the unique single incident edge must use the same third colour. We may therefore replace the entire path by one edge of that third colour. Conversely, a colour `c` on the replacement edge uniquely specifies the two remaining colours for the doubled pair, while both incident single edges receive `c`. Iterating this bijection proves the equivalence. A cubic kernel loop would have a third incident edge that is a bridge, and a kernel bridge expands to a bridge along the corresponding single-edge path in `R`. Hence these cannot occur if `R` is bridgeless. An all-degree-two component consists of an even alternating circuit and can be 3-coloured separately. QED.

The transformation is a *reduction of the residual factorization problem*, not an assertion that a general cubic graph is 3-edge-colourable.

## The sharp 14-vertex example

**Theorem 3 (sharp obstruction and infinite lifting family).** There exists a simple 3-edge-connected, 3-edge-colourable cubic graph on **14 vertices** with an FR-triple `F` such that:

1. `u=2`: exactly two edges are uncovered by `F`, the least positive uncovered count allowed by simplicity.
2. `R=2G-F` is bridgeless, and hence all its odd cuts have at least three edges counting multiplicity.
3. `K(F)` is isomorphic to the **Petersen graph**, so `R` is not 3-edge-colourable and `F` does not extend to a Fulkerson cover.
4. **One change repairs the obstruction:** replacing only `M1` by the complementary matching to `M2 ∪ M3` yields an exact 3-edge-colouring of the host, and therefore a (different) Fulkerson cover. The direct-extension failure is not a local-reachability failure.

Moreover, for **every even order `n>=14`**, there exists such a graph and triple, maintaining `u=2` and 3-edge-connectivity of the host. Among simple cubic graphs with an FR-triple and a bridgeless but non-3-edge-colourable residual, 14 is the minimum possible order.

*Proof.* The 14-vertex example is explicitly given in `fr_n14_petersen_kernel.json`. The dependency-free checker `fr_extension_core.py` verifies its 21 distinct edges, degree three, edge-connectivity at least three (all deletions of one or two edges), three original perfect matchings with empty common intersection, a separate proper 3-edge-colouring of the host (as three further disjoint perfect matchings), and bridgelessness of `R`. It constructs `K(F)` and verifies an explicitly supplied isomorphism to the standard Petersen graph. Independently, it enumerates all six perfect matchings of `K(F)` and shows that none has an even-cycle complementary 2-factor, confirming it is not 3-edge-colourable. Thus the finite witness proves assertions 1--3. For assertion 4, the supplied `M2` and `M3` are disjoint and their complement is the matching `{(0,5),(1,11),(2,8),(3,7),(4,9),(6,10),(12,13)}`; replacing `M1` by it takes the three-matching quadratic defect from `4` directly to `0`. The checker verifies all three resulting perfect matchings.

For the order bound, suppose `R` is bridgeless but cannot be 3-edge-coloured. By Proposition 2, `K(F)` is a bridgeless, loopless, cubic multigraph that cannot be 3-edge-coloured. The smallest such graph has at least ten vertices (the classical Petersen minimum; parallel-edge digons can be suppressed without affecting colourability). The value `u` cannot be zero, since in that case the supplied triple already forms a 3-edge-colouring. As `G` is simple, `u>=2`. Therefore `|V(G)|=|V(K(F))|+2u >= 10+4=14`.

For infinite lifting, choose a vertex where the triple covers all three incident edges once (such a vertex exists in the base example). Replace this vertex by a triangle, attaching its original three neighbours to three different triangle vertices. For each of the three frozen matchings, retain its chosen external incident edge and add the triangle edge connecting the two unused triangle vertices. This extends each perfect matching and preserves `u=2` and the FR property. Apply the analogous extension to an independently supplied 3-edge-colouring of `G` to prove the expanded host remains 3-edge-colourable. Vertex-to-triangle expansion preserves simple cubicity and 3-edge-connectivity. In the residual, this replaces a degree-three vertex by a triangle with all six incidences of multiplicity one. It preserves bridgelessness. Any 3-edge-colouring of the expanded residual restricts to a 3-edge-colouring of the original residual, because each of the three colours meets the three-edge separating cut exactly once (the cubic parity lemma). Thus nonextension persists. Newly introduced triangle vertices also have multiplicity pattern `(1,1,1)` and can be expanded again, giving all even orders `14+2j`. The checker reproduces the first four expansions. QED.

## Independent computations and other examples

* Flower snark `J5` (20 vertices, 32 perfect matchings): all 2010 unordered collision-free triples were independently tested. 1680 extend and 330 do not, but *every one of the 330 failures has a bridge in the residual*. Thus `J5` alone cannot witness this stronger bridge-free obstruction.
* The 14-vertex base and its first four triangle expansions are checked in standard-library tests without a SAT solver or optimisation backend.
* The Petersen graph itself has 20 collision-free unordered triples of perfect matchings; all 20 extend (tested separately).
* A random search also found 20- and 32-vertex bridge-free nonextendable triples; their witnesses are nonminimal and omitted from the main source tree. The 14-vertex example supersedes them.

The full direct residual colouring test and the suppressed-kernel criterion agree on **all 2010** collision-free triples on `J5`.

## Scope, novelty and research questions

There is a general small-defect escape lemma: if a triple with empty intersection leaves exactly two uncovered edges in a simple cubic graph, then exactly two edges are doubly covered. Among the three unordered pairs of the three matchings, at least one pair is never doubly covered, so those two matchings are disjoint. Their edge complement is a perfect matching. Hence **every such triple can be normalized to a proper 3-edge-colouring by replacing at most one coordinate**, even though our certificate shows that its original three coordinates may not permit direct completion to a Fulkerson cover.

Every uncovered edge in the residual has multiplicity two. The cut surrounding its two endpoints contains only two residual single-edge copies, so its residual cannot be 3-edge-connected when `u>0`. This is why the example is stated as **bridgeless residual** plus **3-edge-connected host**, not as a 3-edge-connected residual.

This theorem describes *failure of extension of a fixed FR-triple*, not nonexistence of some FR-triple or a full Berge--Fulkerson cover. In the base graph a Fulkerson cover exists because the host itself is 3-edge-colourable.

The notions of triple cores/regular defect and existing nonextension examples are established literature. Especially relevant are Kardoš–Máčajová–Zerafa (JCTB 2023) and Karabáš–Máčajová–Nedela–Škoviera (EJC 2024). The **exact minimum 14**, explicit Petersen-kernel reduction, odd-cut separation and infinite lifting merit specialist novelty checks; do not advertise as a new published theorem without them.

Possible continuation: classify the realizable cubic kernels `K(F)` for FR-triples with small `u`; in particular characterize exactly which snarks arise with `u=2` and determine how separator signatures affect the reachability of an *alternative* extendable FR-triple.

## Reproduction

```bash
python -m applications.berge_fulkerson.plateau.fr_extension_core
python -m pytest -q tests/test_fr_extension_core.py
```

References:
- Kardoš, Máčajová, Zerafa, *Disjoint odd circuits in a bridgeless cubic graph can be quelled by a single perfect matching*, JCTB 160 (2023) 1–14, https://doi.org/10.1016/j.jctb.2022.12.003.
- Karabáš, Máčajová, Nedela, Škoviera, *Cubic Graphs with Colouring Defect 3*, Electronic J. Combin. 31 (2024), #P2.6, https://doi.org/10.37236/12333.
- Inoue, Kawarabayashi, Miyashita, Mohar, Sonobe, *Three-edge-coloring projective planar cubic graphs*, arXiv:2405.16586 (context for Petersen-like cubic graphs).
