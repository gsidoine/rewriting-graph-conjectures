# The complete component-enriched three-cut relation algebra for neutral graph certificates

**8 October 2026 — mathematical proof with exact computational illustrations.**
The reduction is *exact* for every three-edge sum in the specified models, without pair-rigidity, transparency, or connected signature fibers. It is elementary as an abstract graph-quotient theorem; its originality and algorithmic novelty **are not established**.

## 1. State systems and complete separator signatures

Let \(G=A\oplus_3 B\) be the three-edge sum of finite cubic graphs, obtained by deleting a designated degree-three vertex of each side and joining the three pairs of neighbors. The two original graphs \(A,B\), with those cap vertices restored, are the *capped shores*.

We consider either of the following labelled certificate spaces:

* **PM6:** six labelled perfect matchings with each edge covered twice, and neutral moves switching two coordinate matchings along **one connected alternating cycle** of their symmetric difference.
* **Padded CDCq, \(q\ge3\):** \(q\) labelled even edge sets, **including empty coordinates**, with each edge covered twice, and neutral moves switching two coordinates along **one connected cycle** of their symmetric difference.

Every global state corresponds to a unique pair of capped-shore states with **exactly matching full boundary signature**: the signatures record the complete labelled membership subsets on each of the three cap spokes. In PM6 this is an ordered partition of six labels into three groups of two (90 possible signatures). In CDCq the three cut edges carry the pairs \(\{a,b\},\{a,c\},\{b,c\}\) for three distinct active coordinate labels (a total \(6\binom q3\) formal signatures).

Call a local neutral switch **internal** if it preserves the complete cap signature, and **crossing** otherwise. Every crossing switch uses exactly two cap spokes; its *move type* is
\[
 \tau=(\{i,j\},\{p,r\}),
\]
where \(i,j\) are the two distinct selected coordinate labels, and \(p,r\) the two cap-spoke indices (from \(\{1,2,3\}\)). All other neutral switches are internal. For a given source complete signature \(s\) and type \(\tau\), the resulting complete signature \(s'\) is uniquely determined by exchanging membership of \(i,j\) on \(p,r\). An impossible type creates no transition.

## 2. Build the component-enriched local response algebra

For each shore \(X=A,B\), let \(\mathcal S_X\) be its finite state set, with complete signature map \(\sigma_X\), and let \(\Gamma_X\) be its graph of local neutral switches.

For each signature \(s\), take the connected components of the **induced subgraph** \(\Gamma_X[\sigma_X^{-1}(s)]\) consisting only of signature-preserving switches. These are the *internal neutral fiber components*.

Each such component is one **local response state**
\[
 U=(s,\alpha),\qquad \omega_X(U)=|U|.
\]
Thus unlike a signature-only abstraction, multiple disconnected local components having the same boundary signature remain distinct.

Insert a typed, undirected *boundary transition*
\[
 U\xleftrightarrow{\tau}U'
\]
if there exist local certificate states \(x\in U\), \(x'\in U'\) connected by one **crossing** neutral switch of move type \(\tau\). Record the exact coordinate labels and port pair in \(\tau\); forgetting either can invent global moves.

Write \(\mathcal R_A,\mathcal R_B\) for the resulting finite *weighted typed response graphs*. They need not be bounded in size as the shores grow.

## 3. Main theorem — exact synchronized product after fiber enrichment

Define the product-node set
\[
 V(Q)=\{(U,V):U\in \mathcal R_A,\ V\in\mathcal R_B,\
                     \sigma_A(U)=\sigma_B(V)\}.
\]
Give every node the positive integer weight
\[
 \omega(U,V)=\omega_A(U)\,\omega_B(V).
\]
Join two product nodes \((U,V)\) and \((U',V')\) by a quotient edge **if and only if there exists one common move type \(\tau\)** with
\[
 U\xleftrightarrow{\tau}U'
 \quad\text{and}\quad
 V\xleftrightarrow{\tau}V'.
\]

**Theorem (exact component-enriched relation product).** The neutral connected components of the global graph \(\Gamma_G\) are in natural bijection with the connected components of the finite quotient graph \(Q\). Moreover, for every quotient connected component \(D\),
\[
 \boxed{
 |\text{the corresponding global component}|
   =\sum_{(U,V)\in D}\omega_A(U)\,\omega_B(V).
 }
\]
The quotient therefore gives **both exact neutral-reachability and exact component cardinalities** for every three-edge sum, without any assumption of local pair-rigidity or boundary-fiber connectivity.

The precise quotient statement remains true if one restricts the global state graph to a fixed complete boundary signature at a **different marked vertex** in one shore, provided that signature is carried as additional data in the local response states and in the definition of internal components. It is **not** valid to forget such an external constraint before computing responses.

### Proof

The global state space is the disjoint union over common signatures \(s\) of the Cartesian products
\[
 \sigma_A^{-1}(s)\times\sigma_B^{-1}(s).
\]
Consider only global neutral moves that do **not** change the gluing signature. A switching cycle meeting no cut edge lies wholly in one shore, so these are exactly the unilateral local internal moves in the left or right coordinate. Therefore the connected components of the internal-move graph at a fixed signature are **precisely the Cartesian products** \(U\times V\) of local internal fiber components. Each such block is connected, contains exactly \(|U||V|\) global states, and is disjoint from every other block. These are exactly our quotient nodes with the claimed weights.

A global neutral move changing the gluing signature switches two coordinate labels along a cycle crossing the three-edge cut in exactly two edges, since any cycle meets a cut evenly. Capping each shore completes its boundary-to-boundary path into a local switching cycle using precisely those two cap spokes, and with **the same coordinate pair on both shores**. Thus every global crossing neutral move yields a pair of local typed transitions of the same type \(\tau\), so projects to an edge of \(Q\).

Conversely, suppose the local response components \(U,U'\) and \(V,V'\) admit crossing transitions of the same type \(\tau\). Choose witnesses \(x\to x'\) and \(y\to y'\) for those two local transitions. Because \(\sigma_A(U)=\sigma_B(V)=s\), \((x,y)\) is a compatible global certificate. The two matching typed crossing cycles pass through the **same** cut ports with the **same** pair of labels. Delete their two cap vertices and join the resulting alternating paths by the corresponding cut edges. The result is one connected neutral switching cycle of \(G\). Switching it realizes the global transition \((x,y)\to(x',y')\). The initial point \((x,y)\) is reachable from **any** point in \(U\times V\) by internal moves, because that block is a Cartesian product of two connected local fiber components; similarly, all of \(U'\times V'\) is reachable afterwards. Therefore **every edge of \(Q\)** represents a valid way to pass between the corresponding internally connected global blocks.

Contracting each internally connected block gives exactly the quotient's connected-component structure. Summing disjoint block weights proves the formula. QED.

### Key distinction from our earlier hypothesis

The prior signature-only synchronization lemma assumed every fixed-signature local fiber was connected. That fails already on \(K_{3,3}\) (both for the three-sheet CDC and six-matching double cover). The present theorem **needs no such hypothesis**: it refines a signature by its true local neutral-component index. It is a universally correct *finite* exact algorithm, but **not** a uniform finite-state bound or a polynomial-time algorithm for arbitrary inputs.

## 4. How the other two theorems arise as specializations

**Pair-rigid product algebra:** On \(K_{3,3}\) the fixed-signature PM6 fiber has three components of sizes \(1,8,1\) indexed by the local integer type \(t=0,1,2\). Typed crossing moves never change this invariant. Iterating the exact quotient thus gives the earlier \((m+1)^n\) multiplicative count of neutral classes for pair-rigid chains.

**Neutral-transparent insertion:** For a transparent tile \(T\) each complete-signature local fiber is one response state. Every host crossing move has a compatible \(T\) transition, and every complete signature is represented. Consequently the synchronized quotient collapses to the host's neutral components, with all state weights multiplied by \(w_T\) when its fiber weights are constant. The cube \(Q_3\), although non-pair-rigid, has exactly this property for PM6 and for padded CDCq for all \(q\ge3\).

The two earlier theorems therefore fit into one **typed separator-response formalism**.

## 5. Exact test cases

We independently constructed all local PM6 certificate states, fixed-star components and typed crossing transitions for the following tiles:

| Tile | PM6 local certificates | Fiber-component nodes | Distinct typed crossing transitions |
|---|---:|---:|---:|
| \(K_{3,3}\) | 900 | 270 (three per each of 90 signatures) | 3,240 |
| Cube \(Q_3\) | 4,320 | 90 (one per signature) | 1,080 |
| Petersen | 720 | 90 (one per signature) | 1,080 |

Forming the **product quotient**, without enumerating global certificate states, gives:

| Three-edge sum | Quotient nodes | Weighted global components | Total global states |
|---|---:|---|---:|
| \(K_{3,3}\oplus_3 Q_3\) | 270 | 4,320; 4,320; 34,560 | 43,200 |
| Petersen \(\oplus_3 Q_3\) | 90 | 34,560 | 34,560 |
| \(K_{3,3}\oplus_3 K_{3,3}\) | 810 | four of size 90, four of size 720, one of size 5,760 | 9,000 |
| \(Q_3\oplus_3 Q_3\) | 90 | 207,360 | 207,360 |

These agree with **independently enumerated global neutral graphs** for the first three cases in our prior research, and give a new prediction for the two-cube sum. In the first case, the quotient has **270 nodes instead of 43,200**, a 160-fold reduction; in the two-cube case it has **90 instead of 207,360**, a 2,304-fold reduction.

See [exact typed quotient verifier](../repro_runs/verify_typed_cut_quotient.py), which recomputes local PM6 states, all internal fiber components, all typed crossing transitions and the weighted synchronized product from scratch.

## 6. Importance and limitations

**What is proved:** an exact, functorial-looking but elementary decomposition of neutral-reachability and component counts across a 3-edge cut for two distinct graph-certificate models, including arbitrary non-pair-rigid shores. The theorem shows exactly how much extra boundary information is necessary beyond signatures.

**What is not proved:** a uniformly bounded number of response states. Indeed our previously verified \(K_{3,3}\)-chain has exponentially many connected components **within a fixed signature fiber**, so bounded interface size and coordinate count do not bound the number of enriched states.

**Algorithmic question now worth researching:** can these enriched response graphs be represented *symbolically* by compact tensor, semiring, or automaton operations for a broad class of shores without enumerating their exponential number of components? This is not answered by the elementary exact quotient alone. More substantive next results would classify cases with bounded algebraic generators, prove nontrivial complexity separations, or give an exact symbolic representation that supports strict-escape queries.

**Novelty:** Path-lifting and graph-contraction principles are standard; the exact typed quotient may overlap known graph-reconfiguration transfer and graph-algebra literature. Do **not** promote it as a new journal-level result before independent comparison with Kempe equivalence, 1-factorization interchange and finite-state reconfiguration algorithms. It does not solve the 5-CDC or Berge–Fulkerson conjecture.

## Background

- S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, Discrete Mathematics 325 (2014), 77–84; DOI [10.1016/j.disc.2014.02.014](https://doi.org/10.1016/j.disc.2014.02.014).
- J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, Discrete Mathematics 345 (2022), 112963; DOI [10.1016/j.disc.2022.112963](https://doi.org/10.1016/j.disc.2022.112963).
- [Neutral-transparent cube and arbitrary padded CDCq](neutral_transparent_cube_substitution_2026-10-08.md).
