# Exact edge-repair arity for diameter-two graphs of girth at least five

**Status (28 October 2026):** full elementary mathematical proof draft, exact constructive verifier and independent finite audits. **Not Lean kernel verified**, specialist novelty review not completed, and **does not settle Erdős #742**.

## Statement

Let G be a finite simple graph with diameter <=2, minimum degree >=2 and no triangles or 4-cycles. Fix uv in E(G), and put p=d(v)-1 and q=d(u)-1. Consider *new* edge sets F not containing uv, disjoint from E(G), such that H=G-uv+F has diameter <=2. Define r_G(uv)=min |F|. Then

    r_G(uv) = p+1          if p=q,
              max(p,q)    if p != q.

In particular, for every d-regular such graph, r_G(uv)=d for **every** edge. For C5, Petersen, and Hoffman–Singleton the exact repair costs are 2, 3 and 7.

This separates **one-swap isolation** from **coordinated edit repair**. A single edge swap never suffices. The high-girth diameter-two graphs are the diameter-two Moore graphs (a classical area); this theorem does not assert the existence of any new Moore graphs.

## Step 1: exact broken pairs after deleting uv

Let X=N(v)\{u}, Y=N(u)\{v}; |X|=p, |Y|=q, both nonempty. No triangle implies X and Y are disjoint independent sets. No four-cycle implies that every two vertices at distance two have a *unique* common neighbor. Consequently the pairs whose distance increases beyond two after deleting uv are exactly

    B(uv) = {{u,v}} ∪ {{u,x}: x∈X} ∪ {{v,y}: y∈Y}.

There are exactly p+q+1 broken pairs.

## Step 2: charging lemma / lower bound

For any feasible F, construct an injection f_X:X→F by choosing a length-≤2 u–x route in H:

* If ux∈F, charge ux (always prefer the direct edge).
* Otherwise choose a length-two u–z–x route. It must contain an added edge. If zx∈F, charge zx; otherwise charge uz∈F.

These charges are injective. To see this, note that each charge is incident to u or to its particular x. If different x,x' charge the same edge incident to u, then it is either a direct ux (which cannot be charged for x' because X is independent), or uz with z an original neighbor of both x,x', yielding a forbidden quadrilateral v–x–z–x'–v. If the shared edge is not incident to u, it would have to be xx'; its use as a charged edge for x requires the other route edge ux' to exist, which would make x' choose its direct edge instead. The mixed cases are impossible because the relevant charges have different endpoint types.

Analogously, construct an injection f_Y:Y→F, using routes from v to y. Hence |F|≥max(p,q).

If p=q=r, suppose |F|=r. Both injections must then be bijections. But restoring the pair {u,v} requires that F contain an edge ux with x∈X, or vy with y∈Y (the reinserted edge uv itself is forbidden). An edge ux has endpoints disjoint from {v}∪Y, so cannot be charged by f_Y; symmetrically vy cannot be charged by f_X. Contradiction: |F|≥r+1.

This lower bound does **not** assume paths with two new edges are forbidden; the charge explicitly handles them.

## Step 3: matching construction / upper bound

Choose arbitrary bijectively paired elements (x_i,y_i) for i=1..min(p,q) and add edges x_i y_i. These edges were absent in G: otherwise u–v–x_i–y_i–u is a 4-cycle. The pairs {u,x_i} and {v,y_i} are now both repaired through u–y_i–x_i and v–x_i–y_i.

If p>q, add ux_i for every remaining unpaired x_i; if q>p, add vy_i for every remaining unpaired y_i. If p=q, add one extra ux_1. All these edges are absent in G by triangle-freeness. The extra edge restores the u–v pair via the original opposite neighbor. Thus every broken pair is repaired and all other pairs remain at distance <=2 because we only *added* edges to G-uv.

The number added is exactly max(p,q) when unequal, and p+1 when equal, matching the lower bound. QED.

## Audits

Run from repository root:

    python -m pytest -q tests/test_murty_simon_moore_repair.py

The new test file independently checks the hypotheses, all edge deletions and all output repairs on C5 (5 edges), Petersen (15), and Hoffman–Singleton (175), i.e. 195 complete edge-repair certificates. It independently enumerates all candidates of smaller cardinalities for C5 and Petersen. The general theorem uses a mathematical charging proof, **not exhaustive enumeration**.

## Relationship to existing work

The Moore-graph degree/girth/diameter theory is classical; graph-diameter repair and augmentation have an established literature. The present exact local deletion/augmentation formula, in this particular form, is an unrefereed research observation and **its novelty is not established**. It strengthens the reconfiguration/escape-arity evidence in this repository but yields no new edge-density bound for diameter-two-critical graphs, and so is not a proof of the Murty–Simon conjecture.
