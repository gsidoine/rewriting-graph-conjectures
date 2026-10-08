# Exact one-step coordination hierarchy for six perfect matchings

**Status (8 October 2026):** New theorem/proof and independently checkable finite certificates, not externally refereed, novelty not established, no Lean formalization. This is an additive research note. Existing July status ledger remains unchanged.

## 1. Distinguish two questions

For a sextuple of perfect matchings on a cubic graph, define
`Q = sum_e (m(e)-2)^2`, and call a *one-step k-coordinate exact repair*
replacement of at most k whole perfect matchings after which Q=0.
Define `kappa` as its minimum k, if any.

This differs from **strict k-coordinate descent**, which merely requires
Q to decrease. The Q=40 example below has kappa=4 but has a strict
2-coordinate descent Q=40 -> Q=10. It is NOT a two-coordinate local minimum.

## 2. Exact general completion criterion (elementary König consequence)

Let G be d-regular bipartite, and take `dt` perfect matchings whose ideal
edge-multiplicity is `t`. For each edge e let `S_e` be its matching-index
membership set. Replacing coordinates in `I` to reach the exact t-fold
cover is possible **if and only if**

    |I intersection S_e| >= max(0, |S_e|-t)  for every e.

Necessity: more than t frozen copies of an edge cannot be repaired.
Sufficiency: the residual demand `r(e)=t - #frozen occurrences` is a
nonnegative integer vector, with degree `dt-(dt-|I|)=|I|` at each vertex.
König's bipartite multigraph edge-coloring decomposes it into |I| perfect
matchings. This provides a polynomial-time exact construction after a
constant-size subset test for fixed d,t.

For cubic d=3,t=2, there are six matching coordinates, any four suffice,
and the formula for kappa is a multicover hitting-set problem on six labels.

## 3. Unit-defect hierarchy

Assume all multiplicities belong to {1,2,3}; let F be the family of
three-element sets `S_e` over surplus edges `m(e)=3`. Deficits have `m(e)=1`.
Then `kappa = transversal_number(F)`, with kappa=0 for Q=0. Also
`Q = 2 * |F|`, counting repeated edge-set memberships with multiplicity.

Among positive unit-defect states on finite simple cubic bipartite graphs:

| Required direct-repair width | Smallest Q for which kappa >= width | Certificate |
|---|---:|---|
| 2 | 6 | Earlier 18-vertex sharp one-coordinate trap |
| 3 | 12 | New 18-vertex 3-edge-connected graph |
| 4 | 40 | New 40-vertex 3-edge-connected graph |

Why these thresholds are minimal:
- Q<6: existing alternating-4-cycle lemma finds a single-coordinate
  correction. All unit-defect Q=4 states are an alternating 4-cycle.
- For fewer than six surplus triples (Q<=10), every family of up to
  five 3-subsets of [6] admits a hitting pair. Five complements each
  contain three pairs of [6]; if they covered all 15 pairs, they would
  partition edges of K6 into five triangles, impossible as K6 has odd
  degrees.
- For fewer than twenty surplus triples (Q<=38), some
  three-element set meets every surplus triple. Each 3-subset I misses
  exactly one 3-subset: its complement. Blocking all 20 choices I requires
  each of the 20 possible three-subsets to occur.
- All three bounds are attained by supplied explicit verified graphs.

In fact, **for any unit-defect state with Q<=10, two replacements reach
Q=0 directly**, and **for any unit-defect state with Q<=38, three
replacements reach Q=0 directly**. These are stronger than the earlier
strict-improvement guarantees within this multiplicity regime.

## 4. Q=12 witness (18 vertices)

`berge_fulkerson/plateau/q12_cycle_blocker_18.json` gives 27 edges,
per-edge subsets of six matching coordinates, and three six-matching states
with Q path 12 -> 4 -> 0. It is cubic, simple, bipartite and 3-edge-connected.
Six positive edges form one alternating 12-cycle and carry the blocker:

    012, 013, 234, 045, 145, 235

No pair of labels meets all six triples, whereas some triple does, hence
kappa=3. A completely independent stdlib-only checker enumerates all 54
perfect matchings, exhausts all two-coordinate replacements and confirms
that the smallest possible resulting Q under a pair change is 4.
The construction repeats on 18+4k vertices via a balanced vertex expansion
at a defect-free vertex, maintaining Q=12 and kappa=3. (The independent
expansion test checks the first four instances; the general argument is the
balanced-vertex expansion lemma already given in the paper.)

Verification:

    python applications/berge_fulkerson/plateau/q12_standalone_checker.py
    python -m applications.berge_fulkerson.plateau.q12_cycle_blocker

## 5. Q=40 witness (40 vertices)

`berge_fulkerson/plateau/q40_cycle_blocker_40.json` gives 60 edges and
memberships in an explicit 3-edge-connected simple cubic bipartite graph.
Its 40-cycle defect core has 20 surplus edges, with membership triples
running over **all 20 triples on six labels**, each exactly once.
Consequently kappa=4. The JSON includes a genuine four-coordinate Q=0
witness and a separate two-coordinate Q=10 improvement witness.

The graph can be described succinctly: left vertices `u_i=i` and right
vertices `v_i=20+i` for i=0,...,19; plus edges `(u_i,v_i)` with triple
labels `T_i`; minus edges `(v_i,u_(i+1 mod 20))` with singleton labels
`{d_i}`; and neutral edges `(u_i,v_pi(i))` with exactly two labels.
All data `T_i,d_i,pi(i)` are in JSON and the manuscript table. The
neutral pair is `([6]\\T_i)\\{d_(i-1)}`. A pure-stdlib verifier checks all
60 matching memberships and 1,831 possible zero-/one-/two-edge deletion sets,
the entire triple family, and the explicit replacement masks.

Verification:

    python applications/berge_fulkerson/plateau/q40_standalone_checker.py

## 6. Novelty and significance boundary

The general criterion is an elementary consequence of König's theorem;
we **do not** claim it as an entirely new theorem. The new contribution
candidate is the sharp extremal *realizability* hierarchy at Q=6, 12, 40
inside 3-edge-connected cubic bipartite graphs, with exact finite
certificates, and the mechanism-level distinction between direct repair
and monotone strict descent. Specialist literature review is required.
These results do not solve Berge-Fulkerson or the all-Q two-coordinate
strict-descent conjecture. Their role is a mathematically rigorous Level-2
candidate, not a Level-3 conjecture solution.

## 7. Remaining theorem-sized targets

1. Does every positive-Q six-matching state of a cubic bipartite graph admit
   a strictly improving replacement of at most two coordinates? The Q=12
   and Q=40 states emphatically do not disprove this.
2. Classify realizable 3-uniform membership hypergraphs of unit-defect
   sextuples on 3-edge-connected cubic bipartite graphs. Which hypergraphs
   can occur with a **unique** alternating defect cycle?
3. Extend frozen-factor completion to nonbipartite bridgeless cubic graphs
   using parity/odd-cut feasibility of the residual regular multigraph.
4. Formalize the elementary hitting-set bounds and the dependency-free
   certificate checker in Lean 4; no kernel-verified proof is claimed yet.

## 8. Independent nonbipartite exploratory boundary check

The direct-repair criterion is **not** claimed for nonbipartite graphs.
For a selected pair of coordinates, the residual multiplicities after
freezing the other four form a degree-two spanning multigraph if they
are nonnegative. A direct pair correction exists precisely when its
cycles are all even. A new standalone C++17 test enumerated every one
of the 2,040 six-matching **multisets** with Q=6 in the flower snark J5
(20 vertices, 32 perfect matchings). Each admits an exact two-coordinate
completion. This is a finite computational observation, not a theorem
for all snarks or a proof of Berge-Fulkerson.

Reproduce from repository root:

    g++ -O3 -std=c++17 berge_fulkerson/plateau/j5_q6_pair_audit.cpp -o /tmp/j5_q6_pair_audit
    /tmp/j5_q6_pair_audit berge_fulkerson/instances/j5/j5_input.txt berge_fulkerson/plateau/j5_edges.txt

Expected stderr: `Q6 total=2040 kappa2possible=2040 no_kappa2=0`.
