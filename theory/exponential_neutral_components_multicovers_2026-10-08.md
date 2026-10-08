# Exponentially many neutral components in regular perfect-matching multicovers

**2026-10-08 | Mathematical proof draft, independently checked small cases | Novelty not established.**

## Statement

Fix positive integers \(m,n\). Let \(\mathcal C_m(G)\) be the set of **labelled** tuples
\[
  (M_1,\ldots,M_{3m})
\]
of perfect matchings of a cubic graph \(G\), where every edge belongs to exactly \(m\) matchings. Repetitions are permitted. A *neutral two-coordinate switch* selects distinct indices \(a,b\) and toggles membership in \(M_a,M_b\) along **one connected component of their symmetric difference**, necessarily an alternating even cycle. Let \(R_m(G)\) be the resulting reconfiguration graph.

Define \(G_n\) recursively. Start with \(K_{3,3}\), and designate two distinct, nonadjacent vertices \(u,v\) in the same bipartition class. To append another \(K_{3,3}\), delete the currently designated right-end vertex \(v\) and the new tile's designated left-end vertex \(u'\), and join corresponding members of their three neighborhoods by three new edges. Keep the original left endpoint \(u\) and the new right endpoint \(v'\) marked. The port ordering is fixed but arbitrary.

**Theorem (multicover neutral-component amplification).**

1. \(G_n\) is a connected, simple, cubic, bipartite, 3-edge-connected graph of order \(4n+2\).
2. \(R_m(G_n)\) has exactly \((m+1)^n\) connected components, indexed by vectors \(t=(t_1,\ldots,t_n)\in\{0,\ldots,m\}^n\).
3. Let \(s\) prescribe, for each of the three edges incident with the marked left-end vertex, the subset of matching-coordinate labels covering that edge. Thus \(s\) is an ordered partition of \([3m]\) into three sets of size \(m\). Within the subgraph of \(R_m(G_n)\) induced by certificates having **exactly this fixed signature**, there are still exactly \((m+1)^n\) connected components, indexed by the same \(t\).
4. Write
\[
  S_m=\frac{(3m)!}{(m!)^3},\quad w_m(t)=\binom mt^3,\quad
  F_m=\sum_{t=0}^m\binom mt^3
\]
(\(F_m\) is a Franel number). For each vector \(t\), the corresponding full neutral component has precisely
\[
  S_m\prod_{i=1}^n w_m(t_i)
\]
labelled states, and its intersection with any fixed left-end signature \(s\) is one connected component of size \(\prod_{i=1}^n w_m(t_i)\). Consequently
\[
  |\mathcal C_m(G_n)|=S_m F_m^n.
\]

In particular, at the fixed multiplicity \(m=2\), **six perfect-matching double covers** of connected, bipartite, 3-edge-connected cubic graphs have precisely \(3^n=3^{(|V|-2)/4}\) neutral components; **every fixed three-edge boundary signature also has \(3^n\) neutral-fiber components.**

## Proof

### 1. Perfect matchings of one tile

Identify \(K_{3,3}\) with the three-by-three bipartite grid. Each perfect matching is a permutation in \(S_3\), so there are six. Partition them into three even permutations \(P_1,P_2,P_3\) and three odd permutations \(Q_1,Q_2,Q_3\).

**Fact 1.** Each of the nine edges belongs to exactly one even matching and exactly one odd matching, and every pair \((P_i,Q_j)\) intersects in exactly one edge. This follows by inspecting the parity of the relative permutation: an odd permutation of three objects is a transposition, with exactly one fixed point. Therefore the nine edges biject with the nine ordered pairs \((P_i,Q_j)\).

Let a labelled \(m\)-fold multicover use \(x_i\) copies of \(P_i\) and \(y_j\) copies of \(Q_j\). Covering each edge \((P_i,Q_j)\) exactly \(m\) times means
\[
  x_i+y_j=m\quad\text{for all }i,j.
\]
Hence all \(x_i\) equal some \(t\in\{0,\ldots,m\}\), and all \(y_j\) equal \(m-t\). **This \(t\) is the unique local type** of the unordered multiset of matching coordinates.

Fix a star signature at one distinguished vertex. Each of its three edges has precisely \(m\) coordinate labels, forming one group of size \(m\). Within that group there are precisely two matching choices, one even and one odd. Exactly \(t\) labels in each group must use the even choice. Thus, for every prescribed signature and every type \(t\), there are
\[
  w_m(t)=\binom mt^3
\]
local certificates. Since the \(S_m\) possible signatures are equipotent, the total number of local certificates is \(S_m F_m\).

**Fact 2 (local exchange rigidity).** The symmetric difference of any two distinct perfect matchings of \(K_{3,3}\) is **one** alternating 4-cycle or 6-cycle. Indeed their relative permutation is a transposition or a 3-cycle. Accordingly, if an unordered pair of local matchings is replaced by another pair with the same integer edgewise sum, that pair can only remain unchanged or be interchanged. One proves this by deleting shared edges and observing that the unique alternating cycle admits only the two alternating matchings.

**Fact 3 (local connected fiber).** Fix a star signature and type \(t\). If two coordinate labels belong to the same incident cut-edge group but use different local perfect matchings, their symmetric difference is a 4-cycle **avoiding the distinguished vertex**. Switching it exchanges their even/odd choices. For each group, the \(t\)-subsets of an \(m\)-set are connected under exchanges; independently over the three groups, the local neutral graph is \(J(m,t)^3\), with the convention that \(J(m,0)\) and \(J(m,m)\) are singletons. The entire local fixed-signature/type fiber is therefore connected.

Without a fixed star signature, any two labelled certificates of the same local type have the same unordered multiset of perfect matchings, so differ by a permutation of coordinate labels. Any coordinate transposition can be executed by switching along the unique connected symmetric-difference cycle (or does nothing for identical matchings). The unrestricted local type fiber is connected as well.

### 2. Restriction and gluing at a three-edge cut

At any three-edge cut of a cubic graph bearing a \(3m\)-matching \(m\)-multicover, every matching crosses an odd number of cut edges, so either one or three. The total number of matching incidences on the cut is \(3m\) (three edges, multiplicity \(m\)), equal to the number of matching coordinates. Thus **each matching crosses exactly one cut edge**.

We can therefore replace the three cut edges on each shore with three spokes to an artificial cap vertex. Every global matching restricts to a perfect matching on each capped shore. Conversely, two collections of capped-shore matchings glue to global matchings exactly when their three-edge membership signatures agree coordinate by coordinate.

Repeat this operation successively to recover perfect-matching coordinates on each original \(K_{3,3}\) tile, even for tiles with two capped ports.

### 3. The local types are global neutral invariants

Fix two coordinate labels \(a,b\) and a global neutral switch in \(G_n\). For every original edge, the integer sum of its memberships in \(M_a,M_b\) is unchanged. The same is true after restricting to each original \(K_{3,3}\): every artificial spoke corresponds to one physical three-cut edge, whose membership sum is preserved.

By Fact 2 the unordered pair of local \(K_{3,3}\) perfect matchings for \(a,b\) can only be unchanged or swapped. All other coordinates are untouched. Therefore each tile's **entire unordered matching multiset**, and hence its type \(t_i\), is invariant under every neutral switch.

Thus there are **at least** as many neutral components as realized type vectors.

### 4. Every type vector is realized; exact state counts

At \(n=1\), every type \(t_1\) is realized for every marked-star signature, in \(w_m(t_1)\) different ways.

Suppose a certificate exists on \(G_{n-1}\), with a specified vector \(t_1,\dots,t_{n-1}\). The right-end three-edge signature partitions its \(3m\) labels into three size-\(m\) groups. By Fact 1, there are precisely \(w_m(t_n)\) compatible local \(K_{3,3}\) certificates of any prescribed new type \(t_n\). Gluing gives distinct global certificates. Thus every type vector is realized, and for a **fixed marked left-end signature** \(s\), it has exactly
\[
  \prod_{i=1}^n w_m(t_i)
\]
states. Summing over the \(S_m\) possible left-end signatures gives the full type-vector count \(S_m\prod_i w_m(t_i)\).

### 5. Connectivity within each fixed-signature/type class

We prove the *stronger* fixed-left-signature connectivity statement by induction on \(n\).

For \(n=1\), it is Fact 3.

For the inductive step, cut off the rightmost tile, thereby restoring a cap at the right end of \(G_{n-1}\). Let \(A,B\) be two global certificates with the same left-end signature and the same type vector. Their restrictions \(A_0,B_0\) to \(G_{n-1}\) share that left-end signature and the first \(n-1\) types. By induction there is a neutral path from \(A_0\) to \(B_0\) that **preserves the left-end signature at every step**.

Every move in this path can be lifted while maintaining a compatible certificate on the new tile:

* If the switched alternating cycle in \(G_{n-1}\) avoids its artificial right cap, it survives unchanged as a global neutral cycle; leave the new tile untouched.
* If the cycle uses the cap, it traverses two cap spokes corresponding to two different boundary ports. The same pair of matching coordinates on the new \(K_{3,3}\) necessarily differs on those two ports. Their unique alternating local cycle also goes through the cap. Delete the two artificial cap vertices and join their boundary-to-boundary paths through the two physical cut edges. This is one global alternating cycle. Switching it performs the desired move on \(G_{n-1}\) and swaps the corresponding two local matchings on the new tile, preserving its local type by Fact 2.

Because each lifted move projects exactly to its prescribed \(G_{n-1}\) move, it also preserves the **original marked left-end signature**.

At the end, the remainder equals \(B_0\). The current last-tile certificate has the same incoming three-edge signature as the last-tile part of \(B\), and has the same local type \(t_n\). Fact 3 supplies a path of neutral switches in the final tile **avoiding its incoming cap**, so these switches lift to genuine global neutral cycles wholly inside the final tile. They do not affect the remainder or the marked left endpoint. We have reached \(B\).

Thus every fixed-signature/type fiber is connected. Global connectivity of each type vector follows as well: any global permutation of coordinate labels can be performed by sequentially switching all components of the symmetric difference for the transposed pair, so all \(S_m\) boundary signatures are mutually accessible without changing the local type vector. By Step 3 distinct type vectors cannot connect. The theorem follows. \(\square\)

### 6. Basic graph properties

Each three-edge sum deletes two vertices and introduces three edges while preserving cubic degree, hence \(|V(G_n)|=6n-2(n-1)=4n+2\). Using nonadjacent marked vertices avoids multiple edges; all cut edges join distinct tiles, so the graph is simple. Flipping the bipartition of each newly appended tile if necessary makes every new cut edge bipartite, so \(G_n\) is bipartite.

For 3-edge-connectivity, consider a putative edge cut of size at most two in a three-edge sum \(H=H_1\oplus_3H_2\) of 3-edge-connected cubic graphs. Write its partition restrictions to the two punctured shores as \(U_1,U_2\). If either restriction is empty or the whole punctured shore, transfer that shore's cap status to the other and obtain a cut of size at most two in the other capped graph, unless the original cut is empty. If both restrictions are nonempty proper, each punctured shore has at least two crossing *internal* edges: otherwise capping either inside or outside would produce a cut of size at most two in that original graph (one of the two capped cuts uses at most one cap edge). Hence the global cut has at least four edges, a contradiction. Induction from \(K_{3,3}\) gives 3-edge-connectivity.

## Immediate corollaries and boundary of significance

* **Known specialization:** \(m=1\) gives exactly \(2^n\) edge-Kempe classes of ordinary three-edge-colorings, equivalently three-sheet CDCs under edgewise complement. This is a specialization of the cubic edge-Kempe equivalence theory of Belcastro--Haas (2014); **it is not novel**.
* **Fulkerson-cover specialization:** \(m=2\) gives exactly \(3^n\) neutral components of six perfect-matching double covers. Already with 10 vertices (\(n=2\)), there are 9000 labelled covers forming exactly nine components of sizes 90,720,90,720,5760,720,90,720,90 depending on the local type vector.
* **No bounded fiber-state shortcut:** For fixed \(m=2\), fixed six matching coordinates, fixed three-edge cut, and one prescribed complete boundary signature, the number of internal neutral components equals \(3^n\). Hence no uniform bound depending *only* on boundary size and coordinate count can bound the number of neutral-component refinements of that signature in an arbitrary large shore. A compositional factorized representation may still remain efficient.
* **Not a Berge--Fulkerson result:** These are explicit cubic bipartite graphs already known to possess six-match double covers. The result characterizes **reconfiguration**, not existence of such covers in arbitrary bridgeless cubic graphs.

## Independent reproducibility

1. \`tests/test_k33_multicover_types.py\`: independent local multiplicity-\(m\) enumeration for \(m=1,2,3\), including exhaustive brute-force agreement for \(m=1,2\) and direct validation of all 94080 multiplicity-three local certificates.
2. \`repro_runs/k33_two_block_multicover_components.py\`: exhaustive two-block six-matching case: 9000 labelled certificates, 151200 directed neutral switch transitions, exactly nine global connected components; for one fixed marked signature, exactly nine components of sizes \(1,8,1,8,64,8,1,8,1\).

## Novelty review

The \(m=1\) result and the three-edge-sum idea have substantial priority in:
- S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, Discrete Mathematics 325 (2014), 77–84, DOI: [10.1016/j.disc.2014.02.014](https://doi.org/10.1016/j.disc.2014.02.014).
- J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, Discrete Mathematics 345 (2022), 112963, DOI: [10.1016/j.disc.2022.112963](https://doi.org/10.1016/j.disc.2022.112963).

The \(m\ge2\) exact extension and fixed-signature formula **may be a new observation** but are **not yet proved novel** relative to edge-Kempe classes of regular multigraphs and 1-factorization interchange theory. Do not promote to a publication claim before a specialist literature audit.
