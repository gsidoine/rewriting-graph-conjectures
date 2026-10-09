# Pair-rigid tile algebras for neutral matching-multicover reconfiguration

**Research theorem draft — 8 October 2026.** Includes proofs and independently enumerated small examples. **Novelty beyond classical 3-edge-cut and Kempe-class work is not yet established.** No result on Berge–Fulkerson existence is claimed.

## 1. Certificates, moves and pair-rigidity

Let \(m\ge1\). A labelled \(m\)-multicover certificate of a cubic graph \(G\) is a tuple \((M_1,\ldots,M_{3m})\) of perfect matchings such that each edge occurs in exactly \(m\) coordinate matchings. A **binary neutral move** interchanges memberships of two coordinates along a single alternating cycle in their symmetric difference.

A *pair-rigid tile* is a cubic graph \(T\) in which the symmetric difference of **every two distinct perfect matchings** is a single alternating even cycle. Examples include \(K_{3,3}\), the Petersen graph, and the triangular prism. The cube \(Q_3\) is **not** pair-rigid: its two coordinate perfect matchings in directions 1 and 2 differ on two disjoint 4-cycles.

For an edge \(e\) and perfect matching \(M\), let \(A_{e,M}=\mathbf1_{e\in M}\), the finite edge/matching incidence matrix. Define the integer-type set
\[
 X_m(T)=\{x\in\mathbb Z_{\ge0}^{\mathcal M(T)}: A_Tx=m\mathbf1\}.
\]
Every \(x\in X_m(T)\) has \(\sum_M x_M=3m\). It specifies the **unordered multiset of local matching coordinates**, where \(M\) occurs \(x_M\) times.

Fix a distinguished vertex \(v\) with its three incident spokes \(p=1,2,3\). A full *port signature* partitions the \(3m\) coordinate labels into three specified ordered groups of size \(m\), according to the spoke used by each matching. For any type \(x\), define its fixed-signature weight
\[
 W_T(x)=\prod_{p=1}^3\frac{m!}{\prod_{M\ni e_p} x_M!}.
\]
This integer is the number of assignments of the prescribed coordinate labels to the local matching multiset, separately at each spoke.

## 2. Exact rigid-tile composition theorem

**Theorem A.** Let \(T_1,\ldots,T_L\) be finite, simple, 3-edge-connected, cubic pair-rigid tiles, each with marked port vertices. Form a connected *chain* \(G=T_1\oplus_3\cdots\oplus_3T_L\) by successive three-edge sums: at each join delete one marked degree-three port vertex on each side and join their three neighbors by three corresponding new edges. For an internal tile, the left and right marked vertices must be distinct and nonadjacent, so the procedure does not delete an edge directly joining two cap vertices. Fix any terminal marked vertex \(v\) on the first tile.

Then:

1. Every neutral move preserves, on every tile \(T_i\), its local multiplicity vector \(x_i\in X_m(T_i)\).
2. **All** type vectors \(x=(x_1,\ldots,x_L)\in\prod_i X_m(T_i)\) are realizable on \(G\).
3. Each type vector is exactly **one connected component** of the binary-neutral reconfiguration graph. Even after restricting to certificates with one prescribed full signature at \(v\), each type vector remains exactly one connected component.
4. The number of certificates of type \(x\) in each prescribed full port-signature fiber is
\[
   W(x)=\prod_{i=1}^L W_{T_i}(x_i).
\]
The complete unrestricted connected component of type \(x\) has
\[
 S_m W(x),\qquad S_m=\frac{(3m)!}{(m!)^3}
\]
labelled certificates. Consequently
\[
 \#\pi_0(R_m(G))=\prod_{i=1}^L|X_m(T_i)|,\qquad
 |\mathcal C_m(G)|=S_m\prod_{i=1}^L\Bigl(\sum_{x\in X_m(T_i)}W_{T_i}(x)\Bigr).
\]
If any local \(X_m(T_i)\) is empty, the global certificate space is empty.

**Proof.** At any three-edge cut, each perfect matching meets the cut in one or three edges (shore parity is odd). Summing incidences over all \(3m\) matchings gives exactly \(3m\), so each matching must meet the cut in **exactly one** edge. Therefore restriction of a global matching to any capped shore is a perfect matching, and conversely local matchings glue whenever their complete coordinate-by-coordinate cut signatures agree. The argument iterates through the chain.

Fix a binary neutral switch involving coordinates \(a,b\). On every physical edge the **integer pointwise sum** \(\mathbf1_{M_a}+\mathbf1_{M_b}\) is unchanged. This also holds on every restored artificial cap spoke: its membership is inherited from the corresponding physical cut edge. Consequently, on each capped tile the before/after *pair of local perfect matchings has exactly the same pointwise sum*. If the two original local matchings are equal, they are forced unchanged. If distinct, pair-rigidity says that their symmetric difference is a **single** alternating cycle, and the fixed pair-sum has only two ordered perfect-matching decompositions, obtained by swapping that entire cycle. Thus the local unordered pair is unchanged without any assumption about the number of times the **global** alternating cycle traverses the tile. All other coordinate matchings remain fixed. Hence each tile multiplicity vector \(x_i\) is invariant.

At a single tile and a fixed port signature, the prescribed \(m\) labels within port group \(p\) can be assigned to the local perfect matchings crossing that spoke in exactly \(m!/\prod_{M\ni e_p}x_M!\) ways, independently for the three spokes. Any two such assignments can be connected by transpositions of labels inside each port group. Pair-rigidity realizes every nontrivial such transposition by switching the **single** alternating cycle of the relevant two perfect matchings; this cycle avoids the marked port vertex because the pair uses the same spoke there. Thus each fixed-signature/type tile fiber is connected and has cardinality \(W_T(x)\).

Now induct on chain length. For any type \(x'\) and current right-end cut signature on the prefix, the next tile has exactly \(W_{T_L}(x_L)\) compatible certificates of every feasible type \(x_L\), independent of the **names** of labels assigned to the three cut edges. This gives realizability and the product counting formula.

To prove connectivity, take two global states with equal type vectors and equal left-end signatures. By induction, connect their restrictions to the prefix by a sequence of neutral switches preserving the left-end signature. Lift each prefix move to the full chain: if its alternating cycle avoids the prefix's right cap, switch it unchanged. Otherwise the cycle uses two cap spokes; the matching coordinates in the new tile also disagree on those two ports. Pair-rigidity supplies **one** local alternating cycle through precisely those two spokes. After removing the two artificial caps, the two alternating paths join through the physical cut edges to make one global alternating cycle. Its switch projects to the desired prefix move and preserves the appended tile's type. At the end the prefix matches the target, and the two last-tile states have equal type and incoming signature. Connect them by cap-avoiding switches inside that last tile, as established above.

This proves fixed-left-signature connectivity. To align two arbitrary left-end signatures first, apply a global permutation of coordinate labels. A transposition of coordinate labels is implemented by switching one after another along all components of the two perfect matchings' symmetric difference. Such transpositions preserve every tile multiset and can realize any coordinate permutation. Thus each type vector is globally connected.

There are \(S_m=(3m)!/(m!)^3\) possible signatures at the distinguished vertex, all equally sized by coordinate relabeling. Multiplying the fixed-signature component counts by \(S_m\) proves the remaining statements. QED.

**Constructive path bound.** Within a fixed complete port signature, two states of the same type can be joined by at most \(3L(m-1)\) binary neutral switches: on each newly appended tile, correcting each of the three groups of size \(m\) requires at most \(m-1\) transpositions, and the induction lifts each prior move to a single global move. Thus a graph with exponentially many components can nevertheless have a short constructive path between equivalent states when its tile decomposition is supplied.

**Scope limitation.** In the absence of pair-rigidity, a switch on one proper component of a pair's symmetric difference can change a tile's multiset and destroy the theorem's invariant. A single \(Q_3\) tile already supplies an explicit counterexample. This theorem does **not** yield a bounded-state algebra for arbitrary cubic graphs or all certificate systems.

## 3. Two explicit tile algebras

### The \(K_{3,3}\) tile

Its six perfect matchings are the elements of \(S_3\). Every edge is in exactly one even and one odd permutation matching; its two corresponding multiplicities sum to \(m\). Therefore all three even matchings occur \(t\) times and all three odd matchings occur \(m-t\) times, \(t=0,\ldots,m\). Hence
\[
 X_m(K_{3,3})=\{x^{(t)}:0\le t\le m\},\quad
 W_{K_{3,3}}(x^{(t)})=\binom mt^3.
\]

### The Petersen tile

The Petersen graph has precisely six perfect matchings. Its 15 edges biject with unordered pairs of distinct perfect matchings: each edge is contained in exactly two of them, each pair in precisely one edge. Thus the local equations read \(x_i+x_j=m\) for every pair \(i<j\), forcing \(x_1=\cdots=x_6=m/2\).

Therefore **no local cover exists for odd \(m\)**. For even \(m\), there is exactly one local type and each port edge belongs to precisely two distinct local matchings, each occurring \(m/2\) times:
\[
 |X_m(P)|=1,\qquad W_P=\binom m{m/2}^3.
\]
Any two Petersen perfect matchings share one edge, so their symmetric difference comprises eight edges. Since the Petersen graph has girth five, those eight edges form a single alternating eight-cycle: Petersen is pair-rigid.

These statements use the classical Petersen matching incidence structure, rather than establishing it as a novel fact.

## 4. Corollary: non-three-edge-colorable mixed chains

**Theorem B.** Take any chain of \(a\ge0\) \(K_{3,3}\) blocks and \(b\ge1\) Petersen blocks, in any order, with nonadjacent terminals chosen inside internal blocks. It is a simple 3-edge-connected cubic graph of order
\[
 |V|=4a+8b+2.
\]
It is **not** 3-edge-colorable: any proper 3-edge-coloring would meet each three-edge cut once in each color and hence restrict to a proper 3-edge-coloring of every Petersen tile, which is impossible.

For odd \(m\), no \(m\)-fold matching-cover certificate exists on the chain. For even \(m\), the neutral reconfiguration graph has precisely
\[
 \boxed{(m+1)^a}
\]
connected components, including **within each fixed complete boundary-signature fiber**. The component of local \(K_{3,3}\) type vector \(t=(t_1,\ldots,t_a)\) has precisely
\[
  \frac{(3m)!}{(m!)^3}
  \binom m{m/2}^{3b}\prod_{i=1}^a\binom m{t_i}^3
\]
labelled states; the fixed-signature component omits the prefactor. The total certificate count is
\[
 \frac{(3m)!}{(m!)^3}\binom m{m/2}^{3b}
 \left(\sum_{t=0}^m\binom mt^3\right)^a.
\]
The formula follows immediately from Theorem A and the two local tile algebras.

In particular, for six matchings of edge multiplicity \(m=2\), the class count equals \(3^a\) and the full component sizes are \(90\cdot 8^b\prod_i (8\text{ if }t_i=1\text{ else }1)\). This **extends the exponential-class phenomenon to non-3-edge-colorable cubic graphs**, without asserting anything about cyclically 4-edge-connected snarks: these constructions have explicit nontrivial three-edge cuts.

## 5. Coordinate arity three is sharp on a mixed tile graph

**Proposition (sharp arity-three threshold for crossing binary-neutral components).** On the 14-vertex three-edge sum \(K_{3,3}\oplus_3 P\), any edgewise-cover-preserving replacement of at most **two** coordinate perfect matchings leaves the \(K_{3,3}\) type \(t\) unchanged. Yet for each \(t=0,1\) a **three-coordinate** replacement can change \(t\to t+1\), while preserving the six-matching double cover and even the complete signature at the exposed \(K_{3,3}\) terminal.

**Proof.** If \(t\) increases by one, the number of even-permutation local matchings increases by three. Each changed coordinate contributes at most one new even local matching, so at least three coordinates must change. Conversely, work in the \(K_{3,3}\) tile and fix its cut signature adjoining the Petersen tile. Choose one local odd matching from each of the three cut-spoke coordinate groups and replace each with the unique even matching using the **same cut spoke**. The three old odd matchings partition all nine tile edges, and so do the three new even matchings; the edgewise incidence sum of the selected coordinates is unchanged. Each selected coordinate keeps its cut spoke, so each remains glued to the same Petersen matching coordinate. All global matching constraints and multiplicity constraints are preserved. This increments \(t\) by one, proving the unrestricted width-three statement. To obtain the stronger **fixed exposed-star signature** statement, use the independently enumerated exact witnesses: for one fixed exposed-star signature, a three-coordinate trade exists from a type-0 state to a type-1 state and another from type 1 to type 2, with both endpoints preserving that signature (recorded in the audit script). All states of a prescribed type and this signature are connected by binary neutral moves by Theorem A. Global coordinate relabelling transports these two witnesses to any other exposed-star signature. Hence the augmented fixed-signature graph is connected as well. QED.

This shows a clean **arity gap**: binary neutral switches have three components, while adding allowed three-coordinate exact trades makes the entire certificate space connected. The statement is about reconfiguration **width**, not a strict decrease in the total number of certificates.

## 6. Independent finite tests

The tests enumerated global perfect matchings from scratch, then generated *all* six-coordinate edge-multiplicity-two certificates by a pruning backtracker, built the complete binary-neutral adjacency graph, and enumerated its connected components. Results:

| Chain | Vertices | Perfect matchings | Six-matching certificates | Binary-neutral components | Fixed-signature sizes | Directed neutral adjacency count |
|---|---:|---:|---:|---|---|---:|
| \(K_{3,3}\oplus_3 P\) | 14 | 12 | 7200 | 720, 5760, 720 | 8, 64, 8 | 125280 |
| \(P\oplus_3 K_{3,3}\) | 14 | 12 | 7200 | 720, 5760, 720 | 8, 64, 8 | 125280 |
| \(P\oplus_3 P\) | 18 | 16 | 5760 | 5760 | 64 | 103680 |

All three graphs were independently checked as simple, cubic, 3-edge-connected and non-3-edge-colorable. The 18-vertex \(P\oplus_3P\) graph has *additional perfect matchings crossing its cut in all three edges*, but none can belong to an \(m\)-fold matching cover with exactly \(3m\) coordinate matchings; the cut-incidence sum proves that every selected coordinate must cross exactly once. This distinction matters when writing verifiers.

A separate local Petersen enumeration checked that the only feasible multiplicity vectors for \(m=1,\dots,5\) occur at even \(m\), with all six counts equal to \(m/2\). The 14-vertex graph has explicit three-coordinate transitions \(t=0\to1\) and \(t=1\to2\).

## 7. Novelty and next question

The core proof reuses the classical three-cut parity lemma, matching-exchange along alternating cycles, and the standard Petersen matching census. The \(m=1\) specialization of the \(K_{3,3}\) amplification is in Belcastro–Haas (2014); the general matching-pair-rigidity framework and \(m\ge2\) mixed formulas have **not** been checked thoroughly against perfect-matching interchange / toric-fiber literature. Treat the entire note as an **unrefereed mathematical research draft**.

**Next genuine target:** for a tile that is *not* pair-rigid, replace unordered matching-multiset types by components of a local toric fiber, and determine whether a compositional *relation algebra* (rather than a simple direct product) can encode neutral and higher-arity transitions. The cube \(Q_3\) is the minimal motivating adversarial example here; direct-product normal forms fail already on this tile.

**References**
- S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, Discrete Mathematics 325 (2014), 77–84. DOI: 10.1016/j.disc.2014.02.014.
- *Edge-Connectivity and Pairwise Disjoint Perfect Matchings in Regular Graphs*, Combinatorica (2023/24), Proposition 2.1 (Petersen matching incidence). DOI: 10.1007/s00493-023-00078-9.


### Related reconfiguration literature (qualification)

Classical perfect-matching reconfiguration often changes **one** perfect matching along an alternating cycle, or requires length-four alternating flips. Our binary-neutral move acts on a **pair** of perfect-matching coordinates and preserves the *edgewise aggregate multiplicities*. These are distinct problems and their known complexity results should not be imported without checking the reduction. Relevant comparisons include Ito, Kakimura, Kamiyama, Kobayashi, and Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, SIAM J. Discrete Math. 36 (2022), DOI [10.1137/20M1364370](https://doi.org/10.1137/20M1364370); and Bonamy et al., *The Perfect Matching Reconfiguration Problem*, MFCS 2019, [arXiv:1904.06184](https://arxiv.org/abs/1904.06184).

The standard fact that 3-edge sums of 3-edge-connected cubic graphs remain 3-edge-connected is used above. With nonadjacent port vertices the resulting chain is simple. Any claimed sharper cyclic edge-connectivity would require separate proof; our chains expressly have nontrivial 3-edge cuts.


### Subsequent literature correction (8 October 2026)

The **three-coordinate reachability** phenomenon on bipartite hosts is *not novel*. The 2026 study by K. Mori, R. Motomura, H. Ohsugi and A. Tsuchiya, *Toric ideals of matching polytopes and edge colorings*, Mathematika 72 (2026), e70099, DOI [10.1112/mtk.70099](https://doi.org/10.1112/mtk.70099), cites an older theorem that any two proper edge colorings of a bipartite multigraph can be joined by moves affecting at most three colors. Applied to the \(m\)-edge-replication multigraph, this gives global three-coordinate exact-trade connectivity of our \(3m\)-matching covers whenever the underlying simple graph is bipartite. The K3,3 arity-three threshold is an *illustration and lower-bound witness*, not an independently novel upper bound.

The genuinely distinct object is the **binary neutral cycle-switch graph**, which can have exponentially many connected components even in bipartite cubic families. Neither the 2014 edge-Kempe nor the 2026 toric-ideal result automatically supplies our exact component-size formula, but a full comparison is still necessary.
