# Erdős–Gyárfás #64 — exact 3-cut cycle-transfer and rewrite calculus

**Research status (2026-10-28):** complete elementary counting proof; independently tested finite instances; no Lean kernel verification, no new conjecture bound, no externally audited novelty, and **no proof or disproof of Erdős #64**.

[Erdős #64](https://www.erdosproblems.com/64) ($1,000) asks whether every finite simple graph with minimum degree at least three has a simple cycle whose length is a power of two, starting with 4.

## Exact boundary response

Let L and R have disjoint vertex sets and three **distinct ordered ports** each, say l₀,l₁,l₂ and r₀,r₁,r₂. Form G by adding just three edges lᵢrᵢ. Let c_H(t) count unoriented simple cycles of length t in H, and p^H_ij(s) count simple paths of length s between ports i and j.

Introduce the finite generating polynomials

    C_H(z) = Σ_{t≥3} c_H(t) z^t
    P^H_ij(z) = Σ_{s≥1} p^H_ij(s) z^s.

**Exact cycle-spectrum factorization:**

    C_G(z) = C_L(z) + C_R(z)
             + z² Σ_{0≤i<j≤2} P^L_ij(z) P^R_ij(z).

**Proof:** Every simple cycle crosses the three-edge cut an even number of times, hence zero or two. A zero-crossing cycle is contained in a shore. The two crossing edges of any other cycle pick a unique unordered port pair {i,j}. Removing the crossing edges leaves one simple lᵢ–lⱼ path and one simple rᵢ–rⱼ path. Conversely two such paths together with those edges make a unique simple cycle. The length is the sum of the path lengths plus two. Counting gives the formula. QED.

No regularity hypothesis is required for this identity. If each port has degree two inside its shore and every other vertex has degree three, **each reconnection is a simple cubic graph**.

## Exact defect and local rewriting

Define

    Q(G) = Σ_{k≥2} c_G(2^k),

the number of power-of-two cycles. Then Q(G)=0 iff G is power-of-two-cycle-free. **For a counterexample search, zero is the target**, and strict defect descent is a search heuristic, not evidence for the truth of the conjecture.

The three-cut cross term is exactly

    Q_cross(L,R)
      = Σ_{i<j} Σ_{a,b} p^L_ij(a) p^R_ij(b)
                   [a+b+2 is a power of two ≥4].

For a shore replacement L→L' in a fixed right context R, the exact variation is

    Q(L'⊕R) - Q(L⊕R)
      = Q(L')-Q(L)
        + Σ_{i<j} Σ_{a,b}
             (p^L'_ij(a)-p^L_ij(a)) p^R_ij(b)
             [a+b+2 is a power of two ≥4].

Thus the appropriate local certificate is **the internal cycle count plus three length-resolved path distributions**, not an isolated local defect or a Boolean signature. The variation is linear in the changed path-count profile.

A sufficient universal safety condition is Q(L')≤Q(L) and coefficientwise p^L'_ij(s)≤p^L_ij(s) for every port pair and length. This is sufficient, not necessary.

For fixed shores there are six port reconnections. Testing all six using the formula yields an exact local rewrite operator. Every *strictly defect-decreasing* reconnection preserves cubicity and decreases the nonnegative integer Q by at least one, so any sequence of strict reconnections, even using different cuts, terminates in at most Q(G_start) steps. **Terminal states may have Q>0; neutral moves need not terminate.**

## Adversarial certificate: context can reverse a local preference

Let A be the triangle K₃ with all vertices serving as ports (equivalently K₄ minus one vertex). Let B be a triangular prism minus one vertex, with the three former neighbors as ports. The two right contexts are R⁻=A and R⁺, a seven-vertex cubic three-pole formed from the following edges, with ports 1,6,7:

    (1,7), (1,3), (2,4), (2,7), (2,5),
    (3,4), (3,6), (4,5), (5,6).

All four glued graphs are simple cubic.

| Gluing | Number C4 | Number C8 | Q |
|---|---:|---:|---:|
| A ⊕ R⁻ | 3 | 0 | 3 |
| B ⊕ R⁻ | 2 | 3 | 5 |
| A ⊕ R⁺ | 2 | 12 | 14 |
| B ⊕ R⁺ | 2 | 11 | 13 |

The preference reverses: A has lower Q in the first context, B in the second. This disproves **context-independent global-defect ranking of these two local fragments**, not Erdős–Gyárfás. Every example here has Q>0.

For B⊕R⁺, the six port permutations have exact defects

    [13, 14, 13, 10, 14, 10]

in lexicographic permutation order; a strict cubic-preserving rewrite reduces Q from 13 to 10.

## Reproduce and limitations

Run from the repository root:

    python -m pytest -q tests/test_erdos_gyarfas_cycle_transfer.py
    python -m applications.erdos_gyarfas.cycle_transfer

The independent auditor uses NetworkX's simple-cycle iterator (not the transfer counting algorithm) and checks the four cubic witnesses, all six port permutations, and 120 random general shore pairs.

The cut-parity argument and convolution style are classical. [Garcia (2026)](https://arxiv.org/abs/2609.04686) already develops an exact *window calculus* for vertex-replacement constructions; [Ducoffe–Dumitru (2026)](https://arxiv.org/abs/2609.28594) prove strong counterexample restrictions and computational bounds. No claim of literature novelty is made for this exact separator identity.

**What remains open:** To solve #64 through rewriting one would need a theorem showing that a suitable repertoire of safe local moves eliminates Q, or else a genuine global obstruction/classification of positive-defect terminal components. The present identity proves neither; graphs with no usable three-edge cut lie outside this operator.
