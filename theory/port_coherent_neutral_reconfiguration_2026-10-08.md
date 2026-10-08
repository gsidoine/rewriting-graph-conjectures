# Port-coherent neutral reconfiguration: a common separator algebra for cycle covers and matching multicovers

**8 October 2026 — mathematical proof draft with exact finite component enumerations. Novelty unverified.**

## 1. Two different graph-certificate systems

Throughout, the host graphs are finite, simple and cubic. We consider either of the following *labelled*, multiplicity-constrained systems.

**Matching multicover** \(\mathsf{PM}(m)\): \(3m\) labelled perfect matchings \(M_1,\ldots,M_{3m}\) cover every edge exactly \(m\) times. A binary neutral switch swaps two matching coordinates on **one connected alternating cycle** of their symmetric difference.

**Cycle double cover** \(\mathsf{CDC}(q)\): \(q\ge3\) labelled even edge sets \(C_1,\ldots,C_q\) cover every edge exactly twice. Empty even edge sets are **allowed** to keep the certificate space closed under the reconfiguration operations; this is a relaxed labelled model and is not identical to requiring every cover sheet to be nonempty. A binary neutral switch exchanges two coordinates on one component of their symmetric difference, which is an even cycle since the graph is cubic.

Both switches preserve all local parity constraints and exact edge-cover multiplicities.

Let \(T\) be a cubic tile equipped with one designated degree-three *port vertex* \(v\) and with its three incident edges ordered. The full signature \(\sigma_v(S)\) records **which coordinate labels are present on each of these three edges**. Let \(R(T)\) be the finite binary-neutral reconfiguration graph of the appropriate certificate system. Its connected components are called *local neutral orbits* and denoted \(\Omega(T)\).

A local orbit \(\omega\in\Omega(T)\) is **port-coherent at \(v\)** if, for every realized full signature \(s\), the subgraph induced by
\[
  F(\omega,s)=\{S\in\omega:\sigma_v(S)=s\}
\]
is connected under binary-neutral moves *which preserve that full signature at every step*. A tile with two cut ports must satisfy port coherence for each port used for a join. This condition is **not** the assertion that the entire fixed-signature certificate space is connected; it may have multiple different local orbits.

The signature alphabet sizes are
\[
 S_{\mathsf{PM}(m)}=\frac{(3m)!}{(m!)^3},
 \qquad S_{\mathsf{CDC}(q)}=6\binom q3.
\]
For \(\mathsf{PM}(m)\), the labels partition into three ordered groups of size \(m\), since each coordinate crosses a 3-edge cut exactly once. For \(\mathsf{CDC}(q)\), exactly three labels are locally active; each occurs on two spokes, so the spokes are labelled by the three unordered pairs of these active labels, in some order.

Every neutral orbit realizes **every** formal signature: arbitrary coordinate-label transpositions are achieved by switching all components of the two coordinates' symmetric difference, and these transpositions act transitively on all formal star signatures. By label symmetry, the number
\[
 w_T(\omega)=|F(\omega,s)|
\]
is independent of \(s\). Under port coherence this is also the size of a single fixed-signature neutral component belonging to \(\omega\).

## 2. Exact port-coherent gluing theorem

**Theorem A (two certificate systems, one neutral component algebra).**
Let \(T_1,\ldots,T_L\) be finite simple 3-edge-connected cubic tiles, each with designated left/right port vertices (nonadjacent and distinct where both are used). Form a chain
\[
 G=T_1\oplus_3T_2\oplus_3\cdots\oplus_3T_L
\]
by deleting adjacent port vertices at every join and matching their three neighbors through three new cut edges. Fix a terminal vertex \(v\) on \(T_1\) as the exposed left boundary. Suppose **each tile is port-coherent at every port used for a join and at the exposed left boundary** for the certificate system under study.

Then:
1. Every global neutral move preserves the local neutral-orbit index \(\omega_i\in\Omega(T_i)\) obtained by restricting a global certificate to the capped tile \(T_i\).
2. Every orbit vector \(\omega=(\omega_1,\ldots,\omega_L)\) occurs, and **any two global certificates with the same orbit vector are neutrally connected**.
3. The same statement holds **within a prescribed full exposed-boundary signature**: for each \(s\) and \(\omega\), the certificates of signature \(s\) and orbit vector \(\omega\) form one connected induced subgraph of cardinality
\[
  \prod_{i=1}^L w_{T_i}(\omega_i).
\]
4. Globally, that neutral component has cardinality
\[
 S\prod_{i=1}^Lw_{T_i}(\omega_i),
\]
where \(S\) is the appropriate signature alphabet size above, and
\[
 \#\pi_0(R(G))=\prod_i|\Omega(T_i)|,\qquad
 |R(G)|=S\prod_i\left(\sum_{\omega_i\in\Omega(T_i)}w_{T_i}(\omega_i)\right).
\]
5. If \(D_i(\omega_i)\) is the maximum (over signatures) **diameter of the induced connected fixed-signature fiber** for orbit \(\omega_i\), then any two global certificates of the same orbit vector and the same exposed signature can be connected by at most
\[
 \sum_{i=1}^L D_i(\omega_i)
\]
binary-neutral switches.

**Proof.**

**Cut parity and exact restriction.** In a cubic graph, every shore of a 3-edge cut has odd vertex count: \(3|U|=2|E(U)|+3\). Each perfect matching meets the cut in one or three edges. Since a \(\mathsf{PM}(m)\) certificate has \(3m\) matchings and exactly \(3m\) total cut-edge incidences, every coordinate meets the cut **exactly once**. For \(\mathsf{CDC}(q)\), each even subgraph meets the cut in zero or two edges. Six total sheet incidences across the cut force exactly three active sheet labels, each appearing twice, with the triangle pair pattern. Thus the coordinate-by-coordinate cut signature uniquely prescribes restriction to matching/even-subgraph states on each *capped* shore, and matching signatures suffice to glue local states. This works at each successive chain cut.

**Orbit invariance under a global move.** A binary global switch toggles one component \(Z\) of the symmetric difference of two coordinate sheets. It crosses each 3-edge cut in zero or two edges. In any tile, restore the deleted cut spokes and consider the part of \(Z\) in the tile. It is an even edge subset of the two restricted coordinates' symmetric difference, hence decomposes into a (possibly empty) disjoint union of alternating cycles in the matching system, or ordinary symmetric-difference cycles in the even-subgraph system. Performing the local switches on these cycles reproduces the restricted effect of the global switch. Therefore each restricted state remains in the **same local neutral orbit**. Pair-rigidity is *not required* for this argument.

**Counting and realization.** Fix one global exposed signature \(s\) and an orbit vector. The first tile has \(w_{T_1}(\omega_1)\) choices. Each prefix certificate determines the exact signature of the next 3-edge cut. Since every orbit realizes every signature and its fiber has the same size \(w_{T_i}(\omega_i)\), the next tile has exactly that many compatible states. Iteration gives \(\prod_iw_{T_i}(\omega_i)\) certificates in the prescribed exposed signature. All type vectors are realized.

**Constructive connectivity and path bound.** Proceed by induction on chain length. Let \(A,B\) have the same exposed signature and orbit vector. Inductively connect their restrictions to the prefix while preserving the exposed signature. Lift each neutral switch in this prefix path to the full chain. If its alternating/symmetric-difference cycle avoids the prefix's artificial right cap, the switch is internal and lifts unchanged. If it meets the cap, it contains exactly **two** of its spokes; the corresponding two coordinates on the next tile also disagree on those two spokes. Exactly **one** component of their local symmetric difference contains both cap spokes. Remove the artificial caps and join the two shore paths along the same two physical cut edges; their union is one global alternating/symmetric-difference cycle. Its switch induces the original prefix move on the prefix and a valid local move on the appended tile, preserving that tile's orbit.

At the end the prefix matches \(B\). The last-tile restriction is in the desired local orbit and now shares the *entire incoming signature* with the target. By port coherence it can be corrected through a path that **never changes the incoming signature**, so each such move avoids the deleted cap and is an ordinary cycle entirely in the last tile. This establishes global fixed-signature connectivity. Each lifted prefix move costs one global move, and the last-tile correction costs at most \(D_L(\omega_L)\), giving the sum-of-diameters bound by induction.

Finally, arbitrary coordinate-label permutations are implementable by switches on all cycles in each transposed pair's symmetric difference. This aligns any two exposed signatures without changing the local orbit indices, so there is exactly one unrestricted global component per orbit vector. There are \(S\) possible signatures, all equipotent by label symmetry. Multiplication by \(S\) gives the global component size and total count. QED.

**What this theorem does *not* say.** Port coherence is a genuine hypothesis, not a consequence of fixed separator size or local orbit connectivity. It can fail on other tiles. We do not assert a finite uniform bound on the number of **global** orbit vectors: exponentially many global components are compatible with a constant-size local alphabet. The theorem does not yield strict-descent reachability unless the strict moves are separately encoded.

## 3. Local orbit algebras in two systems

**Exact classifications on three small tiles, with proof or independently replayed finite enumeration:**

| Tile | Certificate system | Global local neutral orbits | Fixed-port sizes \(w_T\) |
|---|---|---:|---|
| \(K_{3,3}\) | \(\mathsf{CDC}(3)\) | 2 | \(1,1\) |
| Cube \(Q_3\) | \(\mathsf{CDC}(3)\) | 1 | \(4\) |
| \(K_{3,3}\) | \(\mathsf{PM}(2)\) | 3 | \(1,8,1\) |
| Cube \(Q_3\) | \(\mathsf{PM}(2)\) | 1 | \(48\) |
| Petersen \(P\) | \(\mathsf{PM}(2)\) | 1 | \(8\) |

For \(K_{3,3}\) and Petersen, port coherence is proved algebraically in [pair-rigid tile algebra](pair_rigid_tile_multicover_algebra_2026-10-08.md). Cube is **not** pair-rigid, but exact enumeration on its **nine** perfect matchings establishes port coherence for the two listed certificate systems: in \(\mathsf{PM}(2)\), all 4320 labelled states form one orbit, and every one of the 90 full-port signatures contains 48 states forming one connected subgraph; in \(\mathsf{CDC}(3)\), all 24 states form one orbit, and each of six signatures contains four connected states. The finite enumeration is a computer-verified lemma; it should be replaced with an independent human proof for a standalone theoretical publication.

**Corollary B (shared \(K_{3,3}\)-cube chain phenomenon).** For any three-edge-sum chain of \(a\) \(K_{3,3}\) tiles and \(c\) cubes, all distinct/nonadjacent ports suitably chosen:

- In \(\mathsf{CDC}(3)\), there are exactly \(2^a\) neutral components; each has \(6\cdot4^c\) labelled states, and every fixed boundary signature meets it in exactly \(4^c\) states. The result is equivalent to established cubic edge-Kempe class composition and **not claimed as novel**.
- In \(\mathsf{PM}(2)\), there are exactly \(3^a\) neutral components indexed by \(t\in\{0,1,2\}^a\). Each has
\[
 90\cdot48^c\prod_{i=1}^a (8\text{ if }t_i=1\text{ else }1)
\]
labelled states, with the factor 90 omitted in a fixed boundary fiber. The total is \(90\cdot10^a\cdot48^c\).

**Corollary C (non-3-edge-colorable extensions).** For a chain of \(a\) \(K_{3,3}\), \(b\ge1\) Petersen, and \(c\) cube tiles in arbitrary order, \(\mathsf{PM}(2)\) has exactly \(3^a\) neutral components, with sizes
\[
 90\cdot8^b\cdot48^c\prod_{i=1}^a(8\text{ if }t_i=1\text{ else }1).
\]
The graph is simple 3-edge-connected and non-3-edge-colorable (the Petersen block prevents a 3-edge-coloring by the parity lemma). This gives a **three-tile, non-pair-rigid, non-three-edge-colorable extension** of the initial rigid-tile result.

## 4. Independent global enumerations

| Joined graph | System | States | Connected components | Fixed-boundary component sizes | Directed neutral adjacency entries |
|---|---|---:|---|---|---:|
| \(K_{3,3}\oplus_3 Q_3\) | \(\mathsf{CDC}(3)\) | 48 | \(24,24\) | \(4,4\) | independently enumerated |
| \(K_{3,3}\oplus_3 Q_3\) | \(\mathsf{PM}(2)\) | 43200 | \(4320,34560,4320\) | \(48,384,48\) | 902880 |
| \(Q_3\oplus_3 K_{3,3}\) | \(\mathsf{PM}(2)\) | 43200 | \(4320,34560,4320\) | \(48,384,48\) | 902880 |
| \(P\oplus_3 Q_3\) | \(\mathsf{PM}(2)\) | 34560 | \(34560\) | \(384\) | 743040 |

Enumerators reconstruct global perfect matchings, exact edgewise multiplicities and complete binary-neutral adjacency graphs; global classes are obtained by graph traversal, not by assuming the product formula.

The numerical local cube calculation is exhaustively finite and reproducible, but not a Lean-certified proof. Do not extend the cube orbit claim to arbitrary \(m\) or arbitrary \(q\) without checking.

## 5. Research implications

This resolves a structural false dichotomy from the earlier work: **pair rigidity is sufficient but not necessary** for exact neutral-component factorization. The correct concept is *port coherence of each orbit's fixed-signature fiber*. It applies across two different certificate systems, although the 3-sheet CDC specialization is largely classical Kempe-equivalence theory.

The next substantial target is to characterize port coherence itself. An elementary or structural characterization that handles non-rigid tiles without exhaustive enumeration could become more valuable than a further product formula. In parallel, define a *typed component-enriched relation algebra* for **non-port-coherent** tiles and test whether its action under 3-edge sums predicts terminal strongly connected components and escape under higher-arity trades.

**Relevant priority boundaries:** Belcastro and Haas (2014), *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, DOI 10.1016/j.disc.2014.02.014; Ito et al., *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, SIAM J. Discrete Math. 36 (2022), DOI 10.1137/20M1364370; classical three-edge-cut parity and matching factorization. No unverified originality claim is made for this abstract product theorem.
