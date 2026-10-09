# An exact fibre and defect-transfer theorem for Fan–Raspaud reconfiguration

**Research note · 8 October 2026. Status: combinatorial proof with independently exhaustible local cases and two complete global counting checks; no claim of external novelty or resolution of Fan–Raspaud.**

## Definitions

Let `G` be any finite loopless cubic graph (for our computational checks, simple). Define `T(G)` by substituting a copy of the `K_{3,2}` three-pole for every vertex, with one terminal for each incident old edge; connect the corresponding two terminals by an external edge. We work with **ordered** triples of perfect matchings satisfying `M_0 ∩ M_1 ∩ M_2 = ∅`; allow replacement of **one whole matching coordinate** at a time, without imposing a defect monotonicity condition. The defect `u` is the number of uncovered edges. Let `R(G)` be this full (undirected) reconfiguration graph; distinct vertices of `R(G)` may differ in exactly one matching coordinate.

Every perfect matching of `T(G)` uses one external edge at every three-pole, hence projects to a perfect matching of `G`. The map `π:R(T(G))→R(G)` is surjective, by the local construction below.

## Theorem — exact fibre topology and partition-function transfer

For an FR-triple `M` on `G` with `n=|V(G)|` and `u=u_G(M)`:

1. The projection fibre `π^{-1}(M)` is **connected** in `R(T(G))`. More precisely its induced graph contains a spanning Cartesian product of local cubes `Q_3` at `n−2u` vertices and six-cycles `C_6` at `2u` vertices.
2. **Every edge of `R(G)` lifts from every vertex in its source fibre.** Consequently, projection induces a bijection on connected components, `π₀(R(T(G))) ≅ π₀(R(G))`. This is about unrestricted reachability; it says nothing about connectivity of sublevel graphs.
3. The defect enumerator of the entire fibre is exactly

   `F_M(z) = z^u (2+6z²)^(n−2u) (4z+2z²)^(2u)`.

   In particular, the minimum upstairs defect is `3u`, attained by exactly `2^(n−2u)4^(2u)` lifted FR-triples; the total fibre size is `8^(n−2u)6^(2u)`.
4. For the ordered-FR defect generating polynomial `Z_G(z)=∑_{M∈FR(G)} z^{u_G(M)}`, the **exact renormalization identity** is

   `Z_{T(G)}(z) = (2+6z²)^n Z_G( z³(2+z)²/(1+3z²)² )`.

   This rational substitution has no poles after the prefactor is distributed; the resulting expression is a polynomial. In particular

   `Z_{T(G)}(1)=8^n Z_G(9/16)` and `Z_{T(G)}(0)=2^n Z_G(0)`.

   When `FR(G)` is nonempty, `min_M u_{T(G)}(M) = 3 min_M u_G(M)`.

### Proof

Each matching locally chooses exactly one of the three ports as its external match; the remaining two ports are matched bijectively to the two core vertices. There are exactly two such completions for a prescribed port.

For three projected matchings at a base vertex, the port multiplicities sum to 3 and none is 3 by the FR condition. Thus, up to permutation, the ports are either `(0,1,2)` or `(0,0,1)`.

*For `(0,1,2)`*: all eight completion-bit triples are FR-legal, forming a 3-dimensional cube under single-coordinate bit flips. Exactly two completions leave no internal edge uncovered; the other six leave two edges uncovered. The local polynomial is `2+6z²`.

*For `(0,0,1)`*: exactly two of eight completion-bit triples violate FR, since their three internal matchings share an edge. The remaining six states form the cycle obtained from the cube by deleting two opposite vertices. Four legal completions have one uncovered internal edge; two have two uncovered internal edges, giving `4z+2z²`.

Every uncovered base edge is incident at both ends with a vertex of the second kind, and every second-kind vertex is incident with exactly one uncovered base edge. Hence precisely `2u` base vertices are of the second kind; the other `n−2u` are of the first kind. The external uncovered edges contribute a factor `z^u`. Independent local choices give the fibre product, its connectivity (single-coordinate internal bit flips remain permitted global matching replacements), and the polynomial formula.

For edge lifting, take any upstairs FR-triple above `M`, keep two matching coordinates fixed, and prescribe the new external port for the replaced coordinate according to a legal base move `M→M'`. At each gadget, at least one of the two choices for the replaced coordinate avoids a triple internal intersection: the two fixed matching completions either have no common internal edge, have one common internal edge, or (if their external ports coincide) have two common edges; in the last case the new external port must be distinct, and one of the two completions avoids both. Choices at distinct gadgets are independent, yielding an upstairs move. Since the projection of every upstairs move is either a base move or a stationary step, connected fibres and edge lifting imply the connected-component bijection.

Summing the fibre enumerator over all base FR-triples proves (4) upon factoring `(2+6z²)^n`. The minimum-defect and evaluations at `z=0,1` follow directly.

## Sharp additional fact — low-energy connectivity *within* a fibre

Let `L_min(M)` denote the set of lifts of `M` having minimum upstairs defect `3u`. Within that fibre, **any two such lifts** can be joined by a sequence of FR-preserving one-coordinate replacements whose defect never exceeds `3u+2`: connect one gadget at a time through its cube or six-cycle, keeping all other gadgets at minimum defect.

This `+2` allowance is sharp *within the fibre* whenever `n−2u>0` (some vertex has three distinct matching ports): changing between its two zero-defect local completions necessarily traverses a local state with two uncovered edges. When `n=2u>0`, `+1` is sharp, because the four minimum states of the local six-cycle form two components, joined using a two-uncovered-edge completion.

This **does not** assert such barriers are unavoidable if a path may change the projected base triple: the latter can sometimes leave and return to the fibre at lower maximum energy.

## Independent checks

`fibre_transfer.py` verifies all 1,296 valid local one-coordinate lifting situations exhaustively, verifies the two local polynomials and local connectedness, and performs complete matching-triple enumeration on expansions of both `K4` and `K3,3`. For expanded `K3,3`, the full ordered-FR count is `13,783,296` and matches the coefficient-wise formula. A separate direct state-graph enumeration on expanded `K4` found 47,904 ordered FR-triples forming one connected component.

## Relation to previous results and originality

This result **clarifies and strengthens** the earlier all-vertex balanced amplification used to construct uphill energy barriers: it proves unrestricted component preservation and provides exact counting. It does **not** prove preservation of barrier heights or shortest reconfiguration distances. The fibre's internal minimum-level sets are themselves disconnected, so inferring sublevel-graph equivalence would be a mistake.

Relevant prior research on cubic graph perfect-matching covers and multipoles includes Máčajová–Škoviera, *Cubic graphs that cannot be covered with four perfect matchings* (JCTB 2021), and Kardoš–Máčajová–Zerafa, *Disjoint odd circuits in a bridgeless cubic graph can be quelled by a single perfect matching* (JCTB 2023). The precise polynomial transformation and whole-coordinate reconfiguration statement require deeper novelty comparison; they have **not** been established as new relative to the literature.
