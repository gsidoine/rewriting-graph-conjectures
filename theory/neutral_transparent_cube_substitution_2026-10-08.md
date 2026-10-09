# Neutral-transparent cubic tiles: exact three-cut substitution for two certificate systems

**Date:** 8 October 2026  
**Status:** mathematical gluing proof + computer-assisted finite cube classification; independently checked small mixed graphs. **No claim of novelty, Lean formalization, or major-conjecture resolution.**

This note supersedes the idea that pair rigidity is necessary for exact separator composition. The cube \(Q_3\) is **not** pair-rigid, but has connected fixed-boundary neutral fibers for both six-perfect-matching double covers and arbitrary padded \(q\)-sheet cycle double covers.

## 1. Two certificate systems

All graphs are finite, loopless, simple, and cubic. A **three-edge sum** \(H\oplus_3 T\) deletes one degree-three vertex from each of \(H,T\) and joins their three remaining neighbors in a prescribed bijection. The three newly added edges form a distinguished cut. Unless otherwise stated, \(H\) is connected and 3-edge-connected; the three-edge sum remains so.

### Matching double covers (PM6)

A state is an ordered 6-tuple of perfect matchings \((M_1,\ldots,M_6)\), each edge lying in exactly two matchings. Neutral moves switch **two** selected matchings along **one connected alternating cycle** of their symmetric difference. Their complete star signature at a degree-three vertex is an ordered partition of six labels into three groups of two. There are 90 signatures.

### Padded cycle double covers (CDCq)

For fixed \(q\ge3\), a state is an ordered \(q\)-tuple \((C_1,\ldots,C_q)\) of **even edge sets**, allowed to be empty on individual graph pieces, with each edge in exactly two coordinates. A neutral move chooses two coordinates and exchanges their memberships along one cycle of their symmetric difference. At every degree-three vertex exactly three sheet labels are locally active (each appears on two incident edges), giving \(6\binom q3\) formal complete signatures.

**Nonemptiness qualification.** Here *padded* coordinates may be empty. This is essential for restriction to a shore: a globally nonempty sheet may restrict to an empty tile sheet. Our component and counting statements apply to padded labelled certificate spaces. They must not be silently converted into claims for the usual “all sheets nonempty” state space, or into a proof of 5-CDC existence.

## 2. General neutral-transparent substitution theorem

Call a cubic tile \(T\) **neutral-transparent** in a chosen certificate system if:

1. every formal complete star signature is realized by a certificate of \(T\);
2. for each such signature \(s\), the subgraph of neutral switches induced by the certificates having signature \(s\) is **connected**.

Write \(w_T(s)\) for the number of local certificates in signature fiber \(s\), and \(d_T(s)\) for that induced graph's diameter.

**Theorem A (component-conservative three-edge substitution).** Fix either certificate system. Let \(H\) be any cubic graph carrying at least one certificate, and let \(T\) be a neutral-transparent tile of the same certificate system. Form \(G=H\oplus_3 T\). For a global certificate \(\gamma\), let \(\pi(\gamma)\) be its restriction to the \(H\)-shore, with its three cut half-edges capped by a new cubic vertex.

Then:

1. \(\pi\) is a surjection onto the entire labelled certificate space of \(H\).
2. \(\pi\) maps neutral moves either to neutral moves or to stationary steps, and every neutral move in \(H\) lifts to a **single** neutral move in \(G\), starting at any extension of its initial state.
3. Every point fiber \(\pi^{-1}(h)\) is connected by neutral moves that project to stationary steps; it has exactly \(w_T(s(h))\) states, where \(s(h)\) is the complete signature at the cap of \(H\).
4. Consequently \(\pi\) induces an **exact bijection of neutral connected components** between \(G\) and \(H\). More precisely, the preimage of each neutral connected component of \(H\) is exactly one connected component of \(G\).
5. If \(w_T(s)=w\) is independent of signature, every global component of \(G\) has **exactly \(w\) times as many states** as the corresponding component of \(H\), and likewise for every signature-restricted component measured at any marked star in the \(H\)-shore.
6. If \(d_T(s)\le d\) for all signatures, and \(C\) is a neutral component of \(H\), then the corresponding component in \(G\) has diameter at most \(\mathrm{diam}(C)+d\). The same bound holds in any prescribed exterior star-signature fiber located entirely in \(H\).

**Proof.** Every sheet of a CDC is even, so it meets a three-edge cut in zero or two edges. Each perfect matching of a PM6 state crosses that cut in exactly one edge: the cut has six total coordinate-edge incidences; each of the six matchings crosses an odd, positive number, hence exactly one. Thus restriction and gluing are inverse operations between global states and pairs of capped-shore states with equal **complete** signatures.

A neutral switching cycle meets a three-edge cut in either zero or two edges. If it meets zero, it lies in one shore and projects either to an unchanged \(H\) state or to a single neutral \(H\) switch. If it meets two, its intersection with each shore is one boundary-to-boundary alternating path; capping the two half-edges completes it to one local switching cycle. It therefore projects to one neutral \(H\) switch.

Conversely, take any local neutral cycle in \(H\). If it avoids the cap, perform it unchanged in \(G\). Otherwise, it uses two cap spokes at which its selected coordinate pair has different membership. The **same** two cut edges have different memberships in the corresponding two coordinates on \(T\), so the symmetric difference of that coordinate pair in \(T\) contains **a unique** cycle through the cap, using precisely those two spokes. Splice the two capped cycles along their two shared ports; the result is **one** alternating cycle in \(G\). Switching on that cycle lifts the desired \(H\) move regardless of which extension of the initial \(H\) state we chose. No pair-rigidity assumption was used.

At fixed \(h\), compatible \(T\)-states are exactly the complete signature fiber \(s(h)\). Every \(T\)-switch preserving that signature avoids the cap (the active coordinate pair cannot change any cap spoke), so it lifts unchanged into the \(T\)-shore of \(G\) and keeps \(h\) fixed. Neutral transparency makes the point fiber connected.

Now lift any path between \(h,h'\) starting from an arbitrary \((h,t)\). The terminal lifted state has host restriction \(h'\). Move inside the connected point fiber to the prescribed extension \((h',t')\). This proves component equivalence and the diameter bound. Counting follows from the uniform point-fiber cardinality. QED.

**Important:** A fixed-boundary signature fiber can be *disconnected* for a different tile, as shown by \(K_{3,3}\). Neutral transparency is a **verified hypothesis about the attached tile**, not a property of arbitrary cubic shores.

## 3. Two exact cube classifications

The cube is **not pair-rigid**: some two perfect matchings differ on two disjoint 4-cycles, so switching one cycle changes their unordered multiset. Nevertheless the following finite classifications hold.

### Theorem B — PM6 cube

For \(T=Q_3\), there are **4,320** labelled PM6 states, split equally among **90** complete star signatures. For every signature the corresponding **48 states form one neutral connected component of diameter exactly 4**.

Thus for every cubic host \(H\) admitting a PM6 certificate, inserting a cube preserves its neutral components and multiplies the size of **every** component by **48**, with neutral diameter increase at most **4**. Iterating \(k\) cube insertions multiplies each component size by \(48^k\) and increases its diameter by at most \(4k\).

The finite classification is checked by a complete backtracking enumeration of six-tuples of the cube's nine perfect matchings, edgewise cover verification, and BFS in the induced fixed-star-signature switching graph. No sampling is used.

### Theorem C — padded CDCq cube, **all \(q\ge3\)**

For every integer \(q\ge3\), all \(6\binom q3\) complete signatures are realized on the cube. Every fixed-signature neutral fiber is **connected** and has exact cardinality
\[
 w_q=4+28(q-3)+6\binom{q-3}{2}+6\binom{q-3}{3}.
\]
The resulting full cube certificate space has
\[
 6\binom q3\,w_q
\]
states and just **one** neutral connected component. For \(q=3,4,5,6\), the fixed-signature diameters are respectively **2, 6, 6, 7**; for all \(q\ge7\), the induced fixed-signature diameter is **at most 19**, independently of \(q\).

**Finite part of proof.** A cube even subgraph is a union of edge-disjoint cycles and has at least four edges if nonempty. Each of a \(q\)-CDC's three labels active at the chosen star contains at least four edges. The cube has 12 edges, each covered twice (24 total memberships). Therefore there are at most **three nonempty inactive coordinates** in addition to the three active coordinates.

For \(q=3,4,5,6\), enumerate all 32 even edge sets of \(Q_3\), all their labelled \(q\)-tuples of edge multiplicity exactly two, and every single-component two-sheet switch. The induced signature fibers are connected and have respective sizes \(4,32,66,112\), with diameters \(2,6,6,7\). For one fixed signature with exactly three additional inactive labels, the 112 states have **4**, **84**, **18**, and **6** states with respectively 0, 1, 2, and 3 *nonempty* inactive sheets. By symmetry of the three inactive labels these counts give respectively \(4\), \(28\), \(6\), \(6\) completions for a **prescribed** set of 0, 1, 2, 3 extra nonempty labels. This proves the displayed formula for any \(q\ge3\).

**Infinite reduction.** For \(q>6\), pick six predetermined labels comprising the three star-active labels and any three of the remaining inactive labels. There can be at most three nonempty inactive sheets in total. Whenever a nonempty inactive sheet occupies a label *outside* the predetermined six, there is an **empty** inactive label inside them. Since the nonempty sheet is a disjoint union of at most two cycles (cube has only eight vertices and girth four), switch its entire content, one connected cycle at a time, from the outside label into the empty target label. This takes at most **two** neutral moves and preserves the star signature. There are at most three such relocations, hence at most six moves.

After relocation, only the predetermined six labels can be nonempty. Regard them as a padded six-sheet cube cover with the same boundary signature. The verified six-sheet fiber is connected with diameter seven. Carry out its path while holding all other labels empty. Reversing relocations to reach the second target gives a total path bound \(6+7+6=19\). This proves connectedness and the uniform diameter bound for **all \(q>6\)**. QED.

In particular,
\[
  w_3=4,\quad w_4=32,\quad w_5=66,\quad
  w_6=112,\quad w_7=176,\quad w_8=264.
\]

## 4. Non-pair-rigid infinite families

**Corollary D.** For every cubic host \(H\) and every \(k\ge0\), attach \(k\) copies of the cube by iterated three-edge sums at accessible degree-three vertices. Provided the initial certificate space is nonempty:

- In PM6, the resulting neutral-component set is in natural bijection with that of \(H\); each component's number of labelled certificates is multiplied by \(48^k\).
- In padded CDCq, the same holds with multiplier \(w_q^k\), for **every** \(q\ge3\).
- If the host is 3-edge-connected, these graphs remain 3-edge-connected. If the host is not 3-edge-colorable, the resulting graphs remain not 3-edge-colorable because a three-edge-coloring of the three-sum would induce one on the capped host.
- If there is a known neutral equivalence test and constructive path algorithm for \(H\), they extend to the cube-inserted family. For PM6 the extra path overhead is at most \(4k\); for CDCq it is at most \(19k\).

For example, a \(K_{3,3}\) host with \(k\) attached cubes has exactly **three** PM6 neutral components, with sizes \(48^k(90,720,90)\). A Petersen host with \(k\) attached cubes is **non-3-edge-colorable** and has a **single** PM6 neutral component containing \(720\cdot48^k\) labelled certificates.

This extends exact reconfiguration classification beyond pair-rigid pieces. It does **not** claim a new 5-cycle double-cover existence result.

## 5. Independent exact checks and reproduction

- [Unit tests: cube neutral transparency](../tests/test_cube_neutral_transparency.py). Complete counts, connectivity, and diameters for PM6 and padded CDCq, \(q=3,4,5,6\); check local state-completion coefficients.
- [Full two-block exact audit](../repro_runs/verify_cube_neutral_substitution.py). The \(Q_3\oplus_3 K_{3,3}\) graph has 12 vertices, 18 global perfect matchings, and **43,200** PM6 states split into components \((4,320,4,320,34,560)\), with fixed-exposed-star components \((48,48,384)\). The \(Q_3\oplus_3\mathrm{Petersen}\) graph has 16 vertices, 18 perfect matchings, and **34,560** PM6 states forming a single component, with 384 states in each fixed-signature fiber. All **1,645,920 directed neutral transitions** across both global enumerations preserve the predicted graph, and all component sizes were checked.
- [Prior pair-rigid and cube notes](pair_rigid_tile_multicover_algebra_2026-10-08.md).

**Audit boundary.** The general lifting result is a short mathematical proof. Cube local transparency and diameters for \(q\le6\) and PM6 use finite exhaustive verification; these are **computer-assisted finite lemmas**, not symbolic human classifications yet. The theorem for all \(q\ge3\) is conditional on these fully reproducible finite checks. Specialist novelty audit against Kempe-equivalence, 1-factorization reconfiguration, and 3-edge-sum transfer methods remains outstanding.

## 6. Stop condition and next theorem

This theorem solves the **neutral-transparent tile insertion** problem, but does not give a complete compositional theory when **both** shores have disconnected fixed-signature fibers.

The next substantive target is a **typed relation algebra** of connected-fiber boundary transitions under arbitrary three-edge sums; it must recover the pair-rigid product and transparent-tile projection theorems as distinct specializations, and specify when the boundary transition abstraction yields spurious reachability. Test first on \(K_{3,3}\oplus_3 Q_3\oplus_3 K_{3,3}\) and mixed perfect-matching and CDC configurations; do not chase more isolated small-order bounds.

## Selected prior art

- S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, Discrete Mathematics 325 (2014), 77–84; DOI [10.1016/j.disc.2014.02.014](https://doi.org/10.1016/j.disc.2014.02.014). Already treats edge-Kempe 3-cut decomposition and planar bipartite cubic colorings.
- J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, Discrete Mathematics 345 (2022), 112963; DOI [10.1016/j.disc.2022.112963](https://doi.org/10.1016/j.disc.2022.112963).
- Perfect-matching 1-factorization and Markov-basis literature is pertinent; this note does not claim the general component-projection lemma is novel.
