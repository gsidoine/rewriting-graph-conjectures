# A five-round routing theorem for Fan–Raspaud three-pole fibres

**Research addendum, 8 October 2026.** Independently checked local finite-state proof; external originality not established. This strengthens the previously proved component-preserving substitution theorem. No open conjecture is claimed solved.

## Theorem (uniform additive distortion)

Let `G` be a finite simple cubic graph with at least one ordered Fan–Raspaud triple and let `T(G)` replace every vertex by the `K_{3,2}` three-pole. Write `R(G)` for the graph of ordered FR-triples, with one entire perfect matching changed per move, and `pi : R(T(G)) -> R(G)` for projection to external matching edges. For any two lifted FR-triples `X,Y` whose projections are in the same connected component,

\[
 d_{R(G)}(\pi X,\pi Y)\ \le\ d_{R(T(G))}(X,Y)\ \le\ d_{R(G)}(\pi X,\pi Y)+5.
\]

In particular every fibre has **diameter at most five**, **independent of the order of `G`**. The connected-component correspondence previously established for `pi` follows at once. The number five is a proved upper bound, not asserted to be the sharp distance constant over all cubic host graphs.

## Proof

Fix a projected FR-triple `A`. At each original vertex, label the three terminals by `0,1,2`, and let `(p_0,p_1,p_2)` be the external terminal occupied by the three projected matchings. Since `A` is FR, at least two distinct terminals occur. For each coordinate `i`, the two unmatched terminals may be paired to the two internal vertices in exactly two ways; represent this choice by a bit `b_i`. Thus a local completion is a three-bit word `b=(b_0,b_1,b_2)`.

If all `p_i` differ, **every** bit word is valid and the one-bit-flip graph is `Q_3`. If exactly two `p_i` agree, the two forbidden bit words are antipodal: either choice makes an internal edge belong to all three matchings. The allowed local graph is therefore `Q_3` with two opposite vertices removed, hence `C_6`. All gadget choices are independent, so the full fibre is a Cartesian product of these graphs. A one-bit flip in one factor is a legal one-coordinate global matching replacement.

More strongly, the **fixed coordinate schedule**

\[
             (0,1,0,2,0)\tag{*}
\]

has the following universal routing property: for *every* local profile, every valid starting bit word and every valid target bit word, there is a subsequence of (*) whose corresponding single-bit flips join the endpoints while remaining valid. This is an exact finite claim over five possible legality masks on the eight words; `tests/test_fr_uniform_fibre_routing.py` enumerates all of them, exhaustively checks (*), and checks that no single fixed word of length at most four works uniformly for *all* local profiles. The claim can alternatively be verified by listing the cube and the four possible deleted-antipode hexagons.

To join any two lifts in a common fibre, carry out the five rounds of (*) globally. At round `j`, modify only those local gadget completions whose selected subsequence uses that round. Each coordinate replacement remains a perfect matching and the FR condition holds inside every gadget. After the final round, every local completion equals the prescribed target. Omit rounds in which no change is needed. Thus every fibre diameter is at most five.

Each lifted one-coordinate move projects to either the same triple or a legal one-coordinate move, so `d_G <= d_T`. Conversely, the established *local edge-lifting property* says that any base FR move can be lifted from **every** upstairs preimage by independently selecting the new coordinate's internal completion in each gadget. Hence a shortest `pi X -> pi Y` base path lifts from `X` with the same number of moves to some point `Y'` above `pi Y`. The five-round fibre route joins `Y'` to `Y`. This proves the claimed upper bound.

## Corollary (iterated substitution and barrier–distance separation)

For `t >= 0` and lifts `X_t,Y_t` on `T^t(G)` whose iterated projections are `X_0,Y_0` in a common base FR reconfiguration component, repeated application gives

\[
 d_G(X_0,Y_0)\le d_{T^t(G)}(X_t,Y_t)\le d_G(X_0,Y_0)+5t.
\]

Hence full reconfiguration distance increases by at most `5 log_5(|V(T^t(G))|/|V(G)|)`, although the vertex count grows as `5^t`. Applied to the **ten-vertex uphill seed**, choose an equality-attaining FR lift `X_t` of the obstructed triple and *any proper three-edge-colouring lift* `Y_t` of its known 3-step normalization endpoint. Then

\[
    d(X_t,Y_t)\le 3+5t,
    \qquad
    B(X_t)\ge 3^t.
\]

Thus this family has increasingly high energy barriers even though a full normalization path of length at most `3+5t` exists. **Large barriers do not imply long unrestricted rewrite distance.** This is an exact rigorous consequence of the lift-and-routing lemmas, not an experimental scaling extrapolation.

## Companion enumerative theorem

For `n=|V(G)|`, the exact polynomial identity already established in `theory/fr_three_pole_renormalization_2026-10-08.md` is

\[
Z_{T(G)}(z)=\sum_{A\in\mathrm{FR}(G)}
 z^{u(A)} (2+6z^2)^{n-2u(A)}(4z+2z^2)^{2u(A)}.
\]

The term for a fixed ordered triple counts **all** lifts of that triple, including their extra internal defects. The same transformation holds component by component, since the present theorem ensures that the full inverse image of a base component is a single upstairs component. This does **not** imply a corresponding identity for *components of energy sublevel sets*: the cube/hexagon fibres may split when high-defect states are discarded.

For illustration, the ten-vertex uphill seed with `u=3` has `8^4 * 6^6 = 191,102,976` ordered lifted FR states in its fibre; exactly `2^4 * 4^6 = 65,536` attain the minimum possible upstairs defect `u'=9`.

## Independent exact checks

- Every local port pattern with at least two distinct ports, every locally valid three-bit phase word, and every allowed one-coordinate replacement were checked directly.
- For `K_4`, direct matching enumeration returns `Z_{K4}(z)=6+18z^2`; on the 20-vertex expansion it returns 48 perfect matchings and 47,904 ordered FR-triples, matching every coefficient of the predicted polynomial.
- Full unordered FR reconfiguration graph on `T(K4)` has 8,032 states and is connected.
- Exhaustive length-four universal routing enumeration rejects every candidate; the five-round schedule passes all masks/start/target pairs.

**Source / verifier:** `applications/berge_fulkerson/plateau/energy_barriers/independent_fibre_routing.py` and `tests/test_fr_uniform_fibre_routing.py`. Previous main manuscript remains a research draft; this note strengthens its distance bound without changing its previously proved statements.

## Research interpretation

The substitution `G -> T(G)` acts as a **component-preserving, additive-5 quasi-isometry** of ordered FR reconfiguration graphs and simultaneously as an exactly solvable defect-polynomial substitution. Large energy barriers and drastically increasing numbers of certificates can therefore arise without disconnecting the full reconfiguration space or substantially increasing the *shortest unrestricted* route between projected certificates. Such a separation between geometric distance and energy-filtered reachability deserves further study in other graph certificate systems.