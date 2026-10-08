# Exact 84-profile composition through a 3-edge cut

**Status:** direct elementary composition lemma with an independently checked six-matching example. Intended as future dynamic-programming machinery; **not claimed new**.

Let a bridgeless cubic graph `G` be separated into two 3-poles `H_L`, `H_R` by a 3-edge cut `e_0,e_1,e_2`. Because a cubic shore incident with exactly three cut edges has an odd number of vertices, every perfect matching of `G` crosses the cut in an odd number of edges: **exactly one or all three**.

Encode its boundary mode by `0`,`1`,`2` (which sole cut edge is used), or `*` (all three are used). For a *six-tuple* of perfect matchings, rearranging the labels makes only the counts of the four boundary types relevant:

```
a_0 + a_1 + a_2 + b = 6, a_j >= 0, b >= 0.
```

There are `C(9,3)=84` such profiles.

Define `F_H(a_0,a_1,a_2,b)` as the minimum sum of squared interior-edge multiplicity deviations from 2 among all six *partial* perfect matchings on the shore with the given boundary-mode counts. A partial matching covers each internal vertex either via an internal edge or through the recorded exposed terminal port. If no such configuration exists, let `F_H=+infinity`.

**Exact composition identity:**

\[
\min_{\mathcal M\text{ a six-tuple of PMs of }G}Q_G(\mathcal M)
=\min_{a_0+a_1+a_2+b=6}
\left[F_{H_L}(a_0,a_1,a_2,b)+F_{H_R}(a_0,a_1,a_2,b)+
\sum_{j=0}^{2}(a_j+b-2)^2\right].
\]

**Proof.** Each global six-tuple induces the same six boundary modes on both shores. Its interior potential splits across the shores. Each cut edge `e_j` occurs in the `a_j` matchings of mode `j` and the `b` matchings of mode `*`, so its contribution is `(a_j+b-2)^2`. This proves the left side is at least the right side. Conversely choose, for each shore, a six-tuple achieving its finite response cost at any specified count-vector. Since the color labels of a six-tuple are arbitrary, permute one shore's matching labels so that all six modes match coordinate-by-coordinate. Glue the matching pairs along the cut, obtaining six global perfect matchings of the stated total defect. Take the minimum over all profiles.

**Specialization at zero defect.** When all three cut edges have multiplicity two, the equations `a_j+b=2` give `a_0=a_1=a_2=2-b`. Summing the profile counts gives `6=3(2-b)+b=6-2b`, hence `b=0`. Thus a perfect twice-cover cannot use the all-three crossing mode at a 3-cut; it must have exactly two of each single-edge mode. This is the key 3-cut signature constraint, not an obstruction discovered by computation.

**Reproducible toy case:** glue two triangular 3-poles to form the triangular prism. A triangle shore of mode `j` uses the internal edge opposite `j`, and mode `*` uses none. Its response cost is `F_H=Σ_j(a_j-2)^2`, so the formula is exact for all 84 profiles. `python -m applications.berge_fulkerson.plateau.three_cut_profile` verifies the identity over all six-matching multiset states of the prism.

**Research direction:** enriching `F_H` with reachability/neutral-plateau information rather than only minimum potential may produce an interface theory genuinely different from ordinary bounded-cut dynamic programming. A finite response algebra *for minimum Q alone* is not a proof of neutral normalization.
