# Compression via auxiliary edge-coloring — draft proof

**Status:** human proof draft with independent finite examples in the original October 8 research archive. **Novelty not established.**

Let G be cubic, and let C_1,...,C_q be even edge sets covering every edge exactly twice. Select a set Q of r>=3 sheet coordinates and put k(e)=sum_{i in Q} 1[e in C_i], so k(e) is in {0,1,2}.

Every vertex of the positive support k>0 has degree 0,2 or 3. For degree 3 the multiset of positive multiplicities is either (1,1,2) or (2,2,2). For degree 2 the multiplicities are either (1,1) or (2,2). (The total is even because all original sheets are even.)

Form H_Q by deleting k=0 edges and isolated vertices, suppressing the degree-2 paths, and discarding isolated cycle components. For supports of cycle-double-cover selections H_Q is a bridgeless cubic multigraph, possibly disconnected.

**Theorem.** The r selected sheets can be replaced by *at most* three even sheets, preserving each edge's exact multiplicity, if and only if H_Q is properly 3-edge-colorable.

**Forward direction.** Given output sheets X,Y,Z, color every support edge with k=1 by the unique output sheet containing it, and every edge k=2 by the unique output sheet *omitting* it. At degree 2 the two colors must agree (parity of all three sheets); at degree 3 the three colors must be distinct (check the two multiplicity possibilities above). Thus colors continue along suppressed paths and induce a proper coloring of H_Q.

**Reverse direction.** Extend a proper coloring of H_Q constantly along each suppressed path; color any isolated support cycle constantly. Put a k=1 edge in the output sheet indicated by its color and a k=2 edge in the *other* two sheets. At each vertex, all three output degrees are even by the same local parity analysis. Each edge has exactly k(e) output memberships. Empty outputs may be dropped. QED.

**Direct obstruction count.** For a selected quartet Q, let b(Q) count positive-support vertices of degree 3 (equivalently, vertices with at least two active selected labels). A noncolorable H_Q contains a noncolorable bridgeless cubic component, which must have at least 10 vertices, by the classical Petersen-minimum fact. Consequently any obstructed quartet has b(Q)>=10.

At every cubic vertex there are exactly three active labels. The number of four-label selections Q that contain at least two of the three is
`A_q=3*binom(q-3,2)+(q-3)`.
Therefore
`sum_{|Q|=4} b(Q)=|V(G)| A_q`.
If every quartet is obstructed, necessarily
`|V(G)| >= 10*binom(q,4)/A_q`.

For q=8 and n=20, equality would force all seventy b(Q)=10. Fix any label a, let d_a be the number of local active triples containing a. Sum b(Q) over the thirty-five quartets containing a. Such a triple contributes 25, and a triple not containing a contributes 13, yielding
`350=25*d_a+13*(20-d_a)=260+12*d_a`.
Thus d_a=7.5, impossible. This proves the **eight-sheet, at-most-20-vertex direct quartet compression guarantee**. For n<=18 averaging already suffices.

The original research archive contains related q=6,7,9,10 counts and a sharp local 22-vertex witness; these remain outside this condensed proof pending an independent proof-line audit.

**Caution:** This is a theorem about a selected *certificate*, not a new graph-existence result. It does not resolve the five-cycle double cover conjecture, and is not a publication novelty claim.
