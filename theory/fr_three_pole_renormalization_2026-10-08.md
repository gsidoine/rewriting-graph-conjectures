# Exact FR renormalization and component-preserving three-pole substitution

**8 October 2026 — original research draft.** Proofs and tests completed within this research pass. Independent specialist novelty/referee audit outstanding. Neither Fan–Raspaud nor Berge–Fulkerson is solved.

## Mathematical model

- State: an **ordered** triple `(M0,M1,M2)` of perfect matchings on a finite simple cubic graph `G`, with `M0 ∩ M1 ∩ M2 = ∅`. Repeated coordinates are allowed.
- One-coordinate move: replace one matching by any other perfect matching while retaining the intersection constraint; energy `u` is the number of uncovered edges.
- `T(G)` substitutes at each vertex the `K_{3,2}` three-terminal, two-internal-vertex gadget and reconnects terminals according to the original edges.

## Proven in the manuscript

1. **Local signature.** For three distinct projected external ports, all 8 phase assignments are allowed (local phase graph the cube `Q3`) and the internal defect polynomial is `A(z)=2+6z^2`. For two identical ports and one different, 6 phases are allowed (phase graph `C6`) and the internal defect polynomial is `B(z)=4z+2z^2`.
2. **Full graph of states.** The matching projection `R(T(G)) -> R(G)` is surjective, every downstairs edge lifts from every upstairs preimage, and each fibre is connected by single-coordinate moves. Hence it induces **a bijection on reconfiguration connected components**. Within a component, `d_G(πx,πy) <= d_T(x,y) <= d_G(πx,πy)+5`.
3. **Exact generating polynomial.** If `Z_G(z)=Σ_{ordered FR triples} z^{u}`, then

   `Z_{T(G)}(z) = (2+6z^2)^n Z_G( z^3 ((2+z)/(1+3z^2))^2 )`.

   The same applies separately to any reconfiguration component.
4. **Minimizers.** If the minimal defect of `G` is `m` and the number of minimizing ordered states is `a`, then for `G_t=T^t(G)`, `m_t=3^t m` and `a_t=a 2^{n(5^t-1)/4+m(3^t-1)}`.
5. **Universal thermodynamic limit.** Provided `G` possesses at least one FR-triple, `lim_t log Z_{G_t}(z)/(n5^t)` exists for all real `z>0`, is independent of the seed and equals `Σ_{j>=0}5^{-j-1} log(2+6 R^j(z)^2)`. The limiting uniform `z=1` logarithmic count per vertex is approximately `0.4792835312641252`, and the mean uncovered-edge count per vertex is `0.3296843222147383`. Numerical decimals are computed values, not certified intervals.

See also [uniform five-round fibre routing](uniform_fibre_routing_2026-10-08.md), which strengthens the former `+3n` distance bound to an absolute `+5`, proves the routing schedule `(0,1,0,2,0)`, and gives the iteration bound `d(T^t) <= d(G)+5t`.

## Exact validations

- A stand-alone local enumeration obtains `Q3` and `C6`, checks all 156 local FR phase states and 828 eligible one-port changes; every projected move lifts.
- On `K4`, a separate brute-force enumerator finds 3 perfect matchings and `Z_{K4}(z)=6+18z^2`. On `T(K4)` it independently finds 48 perfect matchings, 47,904 ordered FR-triples, and verifies **every coefficient** of the transfer identity.
- Exhaustive BFS on all 47,904 FR states of `T(K4)` confirms a single component, consistent with the theorem.
- Eight new tests pass independently in this branch; integrating them into the main repository's full regression suite requires the remote CI run.

## Novelty boundary

The correspondence of three-matchings with regular colouring defect, and multipole substitution, are established subjects. For adjacent literature see Karabáš–Máčajová–Nedela–Škoviera, *Colouring defect of a cubic graph and the conjectures of Fan–Raspaud and Fulkerson*, Ars Mathematica Contemporanea (2025), arXiv:2312.13638, and Allie, *Resistance, oddness and colouring defect of snarks*, Discrete Mathematics (2026). The general principle of polynomial substitution for finite-state vertex gadgets also has analogues in Tutte/Holant/matchgate methods. Do **not** claim that a general graph-polynomial substitution mechanism itself is new. The particular FR defect signature, reconfiguration-component lifting, component-wise renormalization and pressure limit require a dedicated specialist novelty audit.

## Next research directions

- Characterize which cubic three-poles admit surjective matching projection, connected state fibres and uniformly bounded local phase graphs; give a classification under a small-vertex constraint.
- Extend the component-wise transfer to edge separators, avoiding the false assertion that coarse boundary signatures automatically capture reconfiguration connectivity (the repository has independent `K3,3` counterexamples).
- Track energy **sublevel** components via refined boundary phases; these need not be preserved even when entire reconfiguration components are preserved.
- Determine how optimal reconfiguration barriers behave under substitution beyond the proven multiplicative lower bound and whether the degree-three amplification ratio `3/5` is optimal among local matching-projection gadgets.

**Code:** `applications/berge_fulkerson/plateau/energy_barriers/transfer_operator.py`, `tests/test_fr_transfer_operator.py`. **Paper:** `applications/berge_fulkerson/plateau/energy_barriers/transfer_paper/main.tex`.
