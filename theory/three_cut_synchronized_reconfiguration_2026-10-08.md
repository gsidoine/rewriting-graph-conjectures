# Three-edge-cut synchronization of graph-certificate reconfiguration

**Date:** 2026-10-08. **Status:** theorem proofs in this note; independently checked finite examples; **no literature novelty claim or Lean certification**.

## Conventions

All graphs here are finite, loopless and cubic. Let `F={e_1,e_2,e_3}` be an edge cut separating nonempty vertex shores `U,W`. The *cap* of either shore is obtained by adjoining one vertex incident with the three cut half-edges, in the original order. We keep certificate coordinates labelled. Allow locally empty even subgraphs in a capped-shore cycle cover; global final sheets can be required nonempty.

A labelled `q`-cycle double cover (CDC) is a vector of even edge sets `(C_1,...,C_q)` with each edge in exactly two coordinates. A six-perfect-matching double cover is a vector `(M_1,...,M_6)` of perfect matchings, each edge present exactly twice. A neutral **two-coordinate switch** toggles the selected coordinates on one connected component of their symmetric difference. Since the graph is cubic, this component is a simple cycle, and the result is again a valid labelled cover. In the perfect-matching case, the cycle is alternating.

## Theorem A — exact three-cut response alphabets

1. For a labelled `q`-CDC, exactly three coordinate labels occur across the cut; each occurs on two cut edges. Consequently, for distinct labels `a,b,c`, the three cut-edge membership sets are `{a,b},{a,c},{b,c}` in some order. The number of possible *formal* boundary signatures for `q>=3` is `6*binom(q,3)`.
2. For a six-perfect-matching double cover, every matching crosses `F` in exactly one edge, and every cut edge belongs to two matchings. Thus the signature is a partition of six labelled coordinates into three ordered, size-two groups, one group per cut edge. There are `6!/(2!^3)=90` formal signatures.
3. Compatible labelled certificates on the two capped shores glue to a certificate on the original graph **if and only if** their complete cut-edge membership signatures agree. Restriction of a global certificate to either cap gives the inverse operation.

**Proof.** Every even edge set meets every cut in an even number of edges (sum its degrees on one shore modulo two). For a three-cut this is zero or two. There are six membership incidences across the three cut edges, so exactly three sheet labels occur twice. As each cut edge has two distinct labels, their incidences form a triangle on the three active labels.

For a perfect matching `M`, `3|U|=2|E(U)|+3` implies `|U|` odd. Hence `|M cap F|` is odd, either one or three. The six matchings contribute exactly six cut incidences in total. Each contributes at least one, so each contributes exactly one.

For gluing, identify the three cap half-edges on the two shores. Signature equality gives exactly two memberships per restored edge; every original vertex retains its even or degree-one constraint, respectively. Conversely restriction preserves local constraints at all old vertices; the parity facts supply the required constraint at the new cap vertex. These procedures are mutually inverse with fixed labels and a fixed ordering of ports. QED.

## Theorem B — synchronized neutral cycles

For any two certificate coordinates `a,b` in either system, let `Z=C_a symmetric_difference C_b`, or `Z=M_a symmetric_difference M_b`. Every connected component of `Z` is a cycle. It meets the three-edge cut `F` in **zero or exactly two edges**. In the two-edge case, there is exactly one crossing cycle; after capping, it decomposes into a path in each shore joining the same two boundary ports, completed in each cap by the two artificial spokes.

A global two-coordinate switch on that crossing cycle is exactly a *synchronized pair* of capped-shore switches using the **same coordinate pair and the same two boundary ports**. Conversely, any such compatible shore switches glue into the global crossing-cycle switch. Switches meeting no cut edge act inside one shore.

**Proof.** In a cubic graph, the symmetric difference of any two even subgraphs has degree zero or two everywhere. The same holds for two perfect matchings, with alternating edges on each nontrivial component. Thus `Z` is a disjoint union of simple cycles. Each cycle meets every edge cut evenly; since `|F|=3`, it crosses in zero or two edges. There cannot be two distinct crossing cycles, as they would require four cut edges. Cutting the unique crossing cycle along its two cut edges yields one simple boundary-to-boundary path on each shore. Adding the cap vertex completes these into cycles. Toggling the two labels on corresponding paths changes both signatures identically, hence glues, and is exactly the original global switch. The reverse construction is immediate. QED.

**Warning.** Two shore switches with *different* coordinate pairs or port choices need not glue to one neutral global move, even if the resulting untyped boundary states happen to coincide. Boundary transitions must retain the move type `tau=(coordinate pair, two ports)`.

## Theorem C — neutral fiber-product reduction

Let `X_A,X_B` be finite undirected local neutral-move graphs with signature maps `sigma_i:X_i -> S`. Moves are either internal (signature unchanged) or typed boundary moves `tau`. Define the global synchronized product

`X = {(x,y):sigma_A(x)=sigma_B(y)}`

with internal moves on one side while holding the other fixed, and paired boundary moves of the same type `tau` simultaneously on the two sides. Assume:

* for every signature `s` appearing on both sides, the graph induced by `sigma_i^{-1}(s)` is connected, separately for `i=A,B`;
* all globally allowed neutral moves are precisely the unilateral internal moves and synchronized typed boundary moves above.

Define `H_i` to have a typed edge `(s,t,tau)` whenever some local `tau`-move connects its two nonempty signature fibers. Let `H=H_A intersect H_B`, intersecting **typed edges**.

Then the connected components of `X` correspond bijectively to connected components of `H`. More strongly, the minimum possible number of signature-changing moves along a global neutral path from signature `s` to signature `t` equals the graph distance `dist_H(s,t)` (allowing any number of internal moves at zero boundary-change cost).

**Proof.** Projection of any global path maps each internal move to a stationary signature and each synchronized move to an edge in both `H_i`, necessarily with the same type. It gives a walk in `H`, proving the lower bound and necessity. Conversely a common typed edge `(s,t,tau)` has witnesses `x_s--x_t` and `y_s--y_t`. Connectedness of the two signature fibers allows us to move internally from any current global state at `s` to `(x_s,y_s)`, then perform the paired move to `(x_t,y_t)`. Iterating over a shortest path in `H` proves the upper bound and sufficiency. Each global signature fiber is a Cartesian product of connected graphs, hence connected, proving the component statement. QED.

**Corollary (neutral-before-strict escape).** If a strict improving operation is enabled at some global state in a signature fiber `s`, and internal moves can reach all states in that fiber, then the smallest number of signature-changing *neutral* moves needed to reach any strict move is

`min_{s in E} dist_H(s0,s)`,

where `E` is the set of signatures supporting at least one strict move. The number of internal neutral moves is **not** bounded by this formula.

**Limitations.** Fiber connectedness is a substantive, possibly false hypothesis; its failure requires refining the boundary state by fiber components. Availability of one local transition on each shore is sufficient only because connected fibers let us align witness representatives. Neither the theorem nor the corollary implies polynomial-time construction of the local transition graphs. Reconfiguration is known to be PSPACE-hard in many bounded-bandwidth settings.

## Research implications and falsification targets

- For `q=8` CDCs the *formal* three-cut signature space has at most 336 states; for six-matching double covers it has 90. These bounds do not control the number of components *inside* a signature fiber.
- Search first for disconnected signature fibers under two-coordinate switches. Record a certified minimal example if found: it falsifies unqualified separator-state compression.
- If fibers disconnect, replace each boundary state `s` by a pair `(s, component-index)`; seek a bounded response algebra, rather than claiming a constant number of states from cut size alone.
- Study whether neutral plateau escape depth can be computed by an exact synchronized response automaton on 3-edge-sum families. Explicitly compare against established Kempe equivalence and reconfiguration complexity results.

## Independent test

Run `python tests/test_three_cut_synchronization.py`. It exhaustively checks labelled CDCs and six-matching double covers of the triangular prism, all available pair-cycle switches, parity of their cut crossings, and an illustrative finite synchronized-product calculation.

## Background and novelty boundary

This theorem combines standard parity of even subgraphs, alternating-cycle switching, and elementary Cartesian/fiber-product graph arguments. **No originality is asserted for Theorems A–C individually.** The research objective is to obtain a nontrivial new bound or classification of fiber components for a natural certificate system.

Related reading: Marcin Wrochna, *Reconfiguration in bounded bandwidth and tree-depth*, JCSS 93 (2018), DOI 10.1016/j.jcss.2017.11.003; Chakraborty–Feghali–Mahmoud, *Kempe equivalent list colorings revisited*, JGT 107 (2024), DOI 10.1002/jgt.23142; Liu–Hao–Luo–Zhang, *5-Cycle Double Covers, 4-Flows, and Catlin Reduction*, SIAM JDM 37 (2023), DOI 10.1137/22M1472425.
