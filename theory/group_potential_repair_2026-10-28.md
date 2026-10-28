# Exact repair and neutral components for group-potential certificates

**Status (2026-10-28):** self-contained elementary theorem and independently audited executable implementation. **No Lean kernel verification, specialist novelty confirmation or new Erdős problem resolution.** The mathematics is closely related to classical gain graphs, switching/potential theory, group synchronization and coset decoding. This is a synthesis for the certificate-coordination program, not an originality claim.

## Certificate setup

Let H be a finite group, not necessarily abelian, with identity 1. On a finite graph G, fix an orientation of each constraint edge u→v, with prescribed gain g_e∈H. A feasible certificate is a vertex labeling x:V→H satisfying

    x_v = g_e x_u.

We allow multiple edges and loops in the *constraint* multigraph; a graph may have inconsistent edge data. Start with an old edge system E₀ and a known feasible labeling x⁰. Add any multiset of constraints E₁. Each vertex v has a nonnegative integral edit weight w_v (unweighted: all 1). The repair cost is Σ_v w_v [x_v≠x⁰_v]. We seek the minimum among labelings satisfying E₀∪E₁, or a proof of infeasibility.

**Important sidedness:** all edge gains multiply on the LEFT; the component degrees of freedom multiply on the RIGHT. This avoids assuming H commutative.

## Theorem A — exact group-potential repair

Let C₁,...,C_k be the connected components of (V,E₀), and let W_i=Σ_{v∈C_i}w_v. Define a quotient multigraph Q with one vertex i per old component and an edge i→j for every added constraint u→v between these components. This edge is labeled

    h_e = (x⁰_v)^(-1) g_e x⁰_u.

A loop is allowed when both endpoints lie in one old component. The problem is feasible iff every directed closed walk in Q has gain product equal to 1 (using inverse labels when traversing edges backward). Equivalently, the quotient transport equations

    t_j = h_e t_i

are consistent. (For noncommutative H, path gains are composed in traversal order on the left.)

For each connected quotient block B, choose a root. Consistency gives well-defined h_i∈H by path transport from that root, so that every solution has

    x_v = x⁰_v (h_i t_B),   v∈C_i,

where t_B is a single arbitrary right multiplier.

**Exact optimum:**

    R = Σ_{quotient blocks B} [
          Σ_{i∈B} W_i
          - max_{a∈H} Σ_{i∈B : h_i=a} W_i
        ].

A maximizing modal weight a is implemented by choosing t_B=a^(-1). This is an explicit optimal certificate, not just a bound.

### Proof

On an old edge u→v, both x and x⁰ satisfy the same relation. Hence

    (x⁰_v)^(-1)x_v
      = (g_e x⁰_u)^(-1)(g_e x_u)
      = (x⁰_u)^(-1)x_u.

By connectedness, the right multiplier t_i=(x⁰_v)^(-1)x_v is constant on every old component C_i. Substituting x_v=x⁰_v t_j and x_u=x⁰_u t_i into a new edge gives t_j=h_e t_i. Transport round a closed walk must return the original multiplier, and left multiplication is free, forcing the product of the h_e to be 1. Conversely if all closed walks are balanced, define h_i by path transport from a root and obtain every feasible solution by choosing t_B independently.

As right multiplication is free, a vertex in component C_i is unchanged **iff** h_i t_B=1, i.e. h_i=t_B^(-1). Therefore the unchanged weight in B is the total weight of precisely one class of equal h_i. Choosing the maximum-weight class gives the formula. QED.

The quotient traversal and weighted-mode choices give an algorithm using one component search, one gain-propagation search, and weighted counting; for fixed finite H it is linear in the input size (up to dictionary operations).

## Theorem B — exact strict-feasibility reconfiguration components

Consider a single *consistent* edge system E and a move that changes at most r vertex labels while retaining every edge equation. Let the connected components of the underlying graph have sizes s₁,...,s_k. Then the graph of feasible certificates with edges for any nonzero Hamming change of size ≤r has exactly

    |H| ^ #{i : s_i>r}

connected components, and each component contains

    |H| ^ #{i : s_i≤r}

certificates.

**Proof.** Every feasible certificate is an independently chosen right-multiplier per graph component. Two feasible certificates differ on *all* vertices of a component if their multipliers differ, and on none if equal. Thus changing a component of size >r is impossible in one move, and all such multipliers are invariants along any sequence. Each component of size ≤r can be changed to any other multiplier in one feasible move, independently of the other components. This gives exactly the claimed product of complete graphs and component formula. QED.

**Distinguish two notions:** minimum repair distance from an old certificate after adding constraints, versus minimum size of a feasible-to-feasible move on the fully augmented graph. In the two-path example these are m and 2m, respectively.

## Theorem C — sharp linear repair barriers on paths

For any finite group |H|=q≥2 and m≥1, take q vertex-disjoint paths each of m vertices; all old gains are 1 and the old labeling is all 1. Enumerate the group elements as a₀=1,a₁,...,a_(q-1). Add q-1 new edges connecting successive paths, with gains a_(i+1) a_i^(-1). The augmented graph is **a single path** (maximum degree 2) and the quotient offsets are exactly a₀,...,a_(q-1), each occurring at weight m.

Therefore Theorem A gives

    R = qm - m = (q-1)m = (1-1/q)n.

The all-distinct offsets ensure the bound is exact, and the family exists for all m. Theorem B also says that the fully augmented graph's q feasible states are mutually isolated under all strict-feasibility moves of arity <n, although the minimum old-to-new repair cost is only (1-1/q)n.

The case q=2 has **just one added constraint** between two m-vertex paths: it forces changing at least m vertex labels. For H=S₃ (noncommutative, q=6) five new constraints force 5m changes on a 6m-vertex path.

## Audits and reproducibility

Run at repository root:

    python -m pytest -q tests/test_gauge_repair.py

Independent brute-force checks cover:
- 200 randomized binary systems on ≤7 vertices;
- 120 randomized ternary systems on ≤6 vertices;
- 55 randomized nonabelian S₃ systems on ≤4 vertices;
- arbitrary weighted vertex edit costs, inconsistent loops/cycles and multiedges;
- complete enumeration of feasible-state reconfiguration graphs for random binary systems on ≤6 vertices;
- sharp barriers for Z₂, Z₃ and S₃, and both sides of the binary threshold.

The brute-force oracle never invokes the quotient solver to evaluate an optimum. All test instances are finite; the all-n theorem is proved above, not inferred from the tests.

## Position in the certificate-rewriting program

The old certificate graph is an exact **constraint core**. Each connected component is a rigid *gauge coordinate*; newly added constraints are compatibility conditions between coordinates. The quotient holonomy is an exact obstruction: pairwise-compatible interfaces need not be globally compatible if a cycle has nonidentity gain. The weighted-mode formula gives the exact direct-repair width and Theorem B gives the complete neutral-move quotient.

This is a second certificate system, conceptually distinct from the diameter-two *private-distance witness* repair theorem in \`applications/murty_simon/\`. One is governed by torsor transport and a coset leader, the other by pairwise path-repair charges. **A universal repair theorem for all certificate systems has NOT been established.**

### Related literature and novelty warning

- Gain graphs, switching equivalence, balanced circles and potential functions are classical; see https://doi.org/10.1016/j.jctb.2016.05.008
- The standard balanced-gain switching criterion is discussed at https://doi.org/10.1515/spma-2022-0169
- Color-reconfiguration and Kempe-component moves have a substantial existing literature; see https://doi.org/10.1016/j.tcs.2020.05.033 and https://doi.org/10.1016/j.aam.2023.102556
- In the abelian setting the optimization is related to syndrome decoding / minimum-weight coset leaders.

The main theorem is intentionally presented as a transparent structural derivation rather than claimed novel. Any publication would require a specialized comparison to gain-graph and reconfiguration theory.
