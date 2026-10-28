# Erdős #742 (Murty–Simon): exact private witnesses and a rewrite trap

**Claim status:** mathematical identity proved below; finite atlas audits passed; no new extremal bound, no Lean kernel checking, and no claim of novelty. **Does not resolve Erdős #742.**

[Erdős #742](https://www.erdosproblems.com/742): every diameter-two-critical graph on n vertices is conjectured to have at most floor(n²/4) edges. The result is known for sufficiently large n, but the finite gap is open.

## The private-witness identity

Let G be a finite simple graph with all pairwise distances at most two. Fix an edge uv, and write B(uv) for the unordered vertex pairs whose distance becomes larger than two (including disconnection) after deleting uv. Let N(x) be the open neighborhood in G. Then B(uv) is the disjoint union:

1. {{u,v}} if N(u) ∩ N(v) is empty; otherwise the empty set.
2. All {u,x} with x∈N(v)\{u}, ux absent, and N(u)∩N(x)={v}.
3. All {v,x} with x∈N(u)\{v}, vx absent, and N(v)∩N(x)={u}.

**Proof.** Any path of length at most two destroyed by deleting uv must use uv, so its endpoints must include u or v. The pair {u,v} is lost iff it lacks an alternative two-step path. For a pair {u,x}, its only possible uv-containing shortest route is u–v–x, and this is the unique route of length at most two exactly when ux is absent and N(u)∩N(x)={v}. The other case is symmetric. Conversely, deleting uv destroys all paths of length at most two for precisely these pairs. The three families are disjoint. QED.

**Corollary.** G is edge-minimal subject to diameter ≤2 iff every edge e has at least one private witness in B(e). The size |B(e)| is the *exact* sensitivity of the pair-distance defect under deletion of e.

This is a valid local obstruction-certificate interpretation, not by itself a bound on |E(G)|.

## Exact C5 one-edge-swap barrier

C5 is diameter-two-critical. On deleting its edge 01 (using cyclic order 0,1,2,3,4), the remaining path is 0–4–3–2–1 and its broken pairs are {0,1},{0,2},{1,4}. A single new edge capable of repairing pair {0,1} must be 01 (undo), 02, or 14. Adding 02 still leaves d(1,4)=3, while adding 14 still leaves d(0,2)=3. Thus no delete-one/add-one move to a different graph preserves diameter at most two, even if the destination need not be critical.

Nevertheless K₂,₃ is also diameter-two-critical on five vertices and has six edges, versus five for C5. In any labeling, K₂,₃ shares at most four edges with C5 because every bipartition of an odd cycle cuts at most four of its five edges. Hence their edge symmetric difference contains at least 5+6−2·4=3 edges. This lower bound is attained: use bipartition {0,2} | {1,3,4}, delete C5 edge 34, and insert 03 and 24. One can first insert both edges while preserving diameter ≤2, then delete 34; the intermediate graphs cease to be edge-minimal.

Thus the certificate-state dynamics are trapped under one-edge swaps but admit a **three-edge-edit escape via noncritical intermediates**. This is an elementary obstruction to simplistic local normalization, not a refutation of the extremal conjecture.

## Independent verification

From the repository root:

    python -m pytest -q tests/test_murty_simon_witness.py

The standalone auditor compares the formula to recomputed shortest paths on all 456 diameter-≤2 non-isomorphic atlas graphs of order 3–7, for all 5,552 of their edges. It also matches every edge-minimality test and checks the C5 swap trap.

## Role in the general program

This module makes a *private obstruction set* explicit for an edge coordinate and demonstrates that a maximal progress target can lie in a different connected component of the restricted rewrite graph. Therefore coordinatewise descent on critical certificates alone is not complete. Temporarily abandoning criticality or allowing higher-arity edits is mathematically necessary even in the five-vertex case.

**Novelty boundary:** critical-edge certificates, the Murty–Simon conjecture, and the total-domination equivalence have extensive established literature. This note makes no literature-priority claim and gives no progress on the unrestricted n²/4 bound.
