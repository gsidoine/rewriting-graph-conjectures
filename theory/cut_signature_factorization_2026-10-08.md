# Separator responses for exact residual matching factorization

**Research note, October 8, 2026.** This is an exact gluing lemma for residual edge-colouring with an independently reproduced Petersen obstruction. The colour-parity lemma and multipole boundary patterns are classical; no newness is asserted for their use in isolation.

Let `R` be an `r`-regular (loopless) multigraph, here obtained by freezing some matching coordinates of a cubic simple host `G` and taking the residual multiplicity. A proper `r`-edge-colouring of `R` is exactly the missing factorization of the residual into `r` perfect matchings.

For an edge cut `delta_G(X)` of size `c`, split every residual copy of a crossing edge into two half-edges. A **boundary response** is an assignment of distinct colours from `[r]` to these half-edge copies at the shore, so that every shore vertex is incident once with every colour and the copies of an underlying crossing edge receive distinct colours. Treat global permutations of the `r` colours as equivalent.

**Cut-signature gluing theorem.** `R` admits an `r`-edge-colouring if and only if each shore admits a boundary response and the two sets of responses contain compatible representatives (the colour assignment on each crossing copy agrees). This is immediate by restricting/gluing a proper edge-colouring; its force is that the boundary state space depends only on `r` and `c`, not on the sizes of the shores. It admits a finite-state, bottom-up separator algorithm for any fixed `r,c` and a supplied decomposition, with the complete response sets stored at each interface.

## Cuts of size at most three in cubic hosts

A cubic host's proper three-edge cut separates odd-order shores. For every perfect-matching colour factor, the number of crossing copies is therefore odd, hence one or three. If the three underlying cut edges have residual multiplicities `m1,m2,m3` and `a` colour factors cross all three, the other `r-a` colour factors cross exactly one, where

    a = (m1+m2+m3-r)/2.

The response is completely described by a set of `a` colours on all three ports and three disjoint sets of respective sizes `m_i-a` assigned individually to the ports. Thus any two boundary responses with the same cut multiplicities are equivalent under a single permutation of the `r` colour labels. **Three-edge cuts introduce no extra incompatibility beyond local feasibility.** For one- and two-edge cuts the analogous statement follows from parity and is still simpler (in a two-port even cut each factor crosses either both ports or neither).

This is a classical parity-lemma consequence but is essential to the vertex-to-triangle lifting theorem in `applications/berge_fulkerson/plateau/FR_EXTENSION_OBSTRUCTIONS_20261008.md`.

## Four ports are genuinely different

For `r=3` and four single-copy crossing ports in a cubic graph, every colour appears on zero, two, or four ports. Up to colour renaming, the possible patterns are `0000`, `0011`, `0101`, `0110`. A shore may realize only a strict subset of these responses; the other shore may realize a disjoint subset.

**Explicit sharp incompatibility:** Let `G` be the Petersen graph with conventional vertices `0,...,9`. Split off the shore `{0,1}`, where `01` is an edge. Its four crossing edges, sorted as `04,05,12,16`, have local response set `{0101,0110}` (colour permutations identified). The remaining eight vertices have response set `{0000,0011}`. Both shores admit proper 3-edge-colourings as open poles, but they cannot be glued to a proper 3-edge-colouring of the Petersen graph. The exact DFS enumerator `shared/three_colour_boundaries.py` checks all possible assignments; the result is tested in `tests/test_fr_extension_core.py`.

This identifies the first cut size at which *realizable boundary-signature incompatibility* can obstruct residual factorization despite local colourability: at most three ports always align up to colour permutation, while four need not.

For general `r`, the finite boundary algebra is naturally a Boolean semiring under union of response sets and matching/intersection of gluable colour assignments. Tracking minimum defect or weighted transitions requires additional states and is **not** proved by the direct-factorization gluing lemma.

## Research frontier

1. Derive economical *reachable-state* (not merely feasible-state) separator algebras under single- and two-coordinate moves, with explicit transition labels and potential corrections.
2. Classify precisely which factorization kernels can occur for three frozen matchings on bridgeless cubic graphs.
3. Use the four-port signature sets to prove an infinite-class reconfiguration theorem on 4-edge-sum decompositions that goes beyond classical colourability tests.
