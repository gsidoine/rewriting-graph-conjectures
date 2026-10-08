# Lean 4 / mathlib formalization plan — October 2026 research branch

**Status: not implemented, not compiled, not verified by Lean.** The current environment contains no `lean` / `lake` executable. The executable Python verifier provides independent finite-arithmetic checks but is not a replacement for a kernel-checked proof.

## Provenance and reference library

Mathlib 4 offers `SimpleGraph.Subgraph.IsPerfectMatching`, finite graph APIs and Hall's theorem. Documentation: <https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Matching.html> and <https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Hall.html>.

## Suggested formalization sequence

1. **Basic finite certificate encoding** (`Fin 18`, `Fin 27`): edge list `Fin 27 → Fin 18 × Fin 18`, one matching as a `Finset (Fin 27)`, six coordinates as `Fin 6 → Finset (Fin 27)`. Use `decide` to certify all degree-one matching constraints and the `Q` values 6, 6, 0.
2. **Weighted replacement identity:** for `m : E → ℤ`, a labelled coordinate `i`, and any replacement `N`, prove
   `Q(replace M i N) - Q(M) = Σ_{e∈N}w_i(e) - Σ_{e∈M_i}w_i(e)` with `w_i(e)=2(m(e)-2)+1-2·1_{e∈M_i}`. This is pure algebra over integers and finsets.
3. **Dual certificate lemma:** assume `a(u)+a(v) ≤ w(uv)` for all edges and equality on the current perfect matching. Sum across edges of any perfect matching and use unique matching at each vertex. Prove no lower-weight perfect matching exists. The six explicit 18-integer potentials are in `sharp_18_vertex_duals.json`; a Lean `decide` can check the finite inequalities without searching all perfect matchings.
4. **Balanced `K_(3,2)` expansion lemma:** encode the projection of any new perfect matching to an old one, construct six balanced lifts, establish `Q_new(replace) ≥ Q_old(replace)` due to internal nonnegative penalty. Formalize preservation of 3-edge-connectivity by case analysis on all gadget cut configurations.
5. **General frozen-factor completion:** use a formal bipartite multigraph degree-decomposition theorem (if available) or prove repeated Hall matching extraction from a regular bipartite multigraph. Prove the six-colour two-coordinate correction theorem at `Q=6`.
6. **Covering transfer:** later stage. Encode local graph covering and pull back the six integer vertex potential certificates.

Use `decide` or certificate-carrying proof terms for small finite propositions; avoid placing a large untrusted Python/C++ search in the Lean trusted base. Do not claim Lean verification unless the `.lean` files compile under pinned versions with no `sorry` or admitted axioms.
