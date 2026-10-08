# Exact disconnected neutral fibers on K_{3,3}: two certificate systems

**Date:** 2026-10-08. **Status:** elementary full proofs and independent exhaustive finite enumeration. Novelty relative to Kempe equivalence / Latin-square reconfiguration **not yet checked**.

## The question

Fix the three cut edges incident with a vertex `v` of the cubic graph `K_{3,3}`; equivalently take `K_{3,3}` as a capped shore of a three-edge-cut decomposition. A *boundary signature* specifies exactly which labelled certificate coordinates contain each of the three edges at `v`. Within a fixed signature, allow neutral switches of two coordinates along any single connected component of their symmetric difference, as in [three-cut synchronization](three_cut_synchronized_reconfiguration_2026-10-08.md).

Do these local signature fibers have to be neutral-connected? **No, even in the two simplest natural systems.**

## Theorem 1 — three labelled CDC sheets

On `K_{3,3}`, there are exactly 12 labelled three-sheet CDCs and six possible boundary signatures at `v`. Each signature fiber consists of **two isolated vertices** under signature-preserving neutral two-sheet switches.

**Proof.** Given a three-sheet CDC, every edge is present in two sheets, so color an edge by the unique sheet *missing* it. At every cubic vertex the three edge colors are pairwise distinct, as each sheet has degree exactly two. Conversely a proper three-edge-coloring gives a CDC by taking complements of its color classes. A proper three-edge-coloring of `K_{3,3}` is a `3 x 3` Latin square, with its three color symbols labelled.

There are 12 Latin squares of order three. Fixing the three colors on the star at `v` fixes one complete row; exactly two Latin squares complete that row (the second row may be one of two derangements, and the last is then determined). Any union of two color classes in a three-edge-coloring of `K_{3,3}` is a spanning six-cycle. Every pair-coordinate neutral switch consequently swaps these two colors **globally**, including two edges at `v`. No nontrivial switch preserves its boundary signature. Both completions are therefore isolated in their fiber. QED.

## Theorem 2 — six labelled perfect matchings of multiplicity two

On `K_{3,3}`, there are exactly **900** labelled six-perfect-matching double covers, and **90** possible boundary signatures at `v`. Each signature fiber has ten elements split into exactly **three** neutral connected components of sizes

`1, 8, 1`.

The nontrivial component is a three-dimensional Boolean cube: three independent signature-preserving alternating four-cycle switches flip its three bits.

**Proof.** Identify perfect matchings with permutations `pi in S_3`: the matching uses edge `(i, pi(i))` in a fixed bipartition. Every six-matching double cover uses each edge twice. At `v`, each of the three edges is owned by exactly two of the six matching labels; fixing the boundary signature therefore partitions six labels into three labelled pairs. There are `6!/(2!)^3=90` such signatures.

Within each two-label group belonging to a boundary edge `(0,j)`, there are exactly two possible permutations, one even and one odd. Let `t_j in {0,1,2}` count how many of its two matchings use the even permutation. For an edge `(1,c)`, exactly two boundary groups can cover it; in one group it is selected by the even permutation, and in the other by the odd permutation. Exact multiplicity two forces `t_j+(2-t_k)=2`, hence `t_j=t_k`. Since every pair of boundary groups arises this way, all counts equal a common `t in {0,1,2}`.

For `t=0` or `t=2`, the two matching labels in each boundary group are identical, yielding exactly one state of each kind. For `t=1`, in each group one label uses the even permutation and the other uses the odd one. This gives `2^3=8` states.

A signature-preserving two-coordinate alternating-cycle switch must involve matching labels using **the same edge at `v`**: if their incident edges at `v` differ, their symmetric-difference cycle includes `v` and switching it changes the signature. Within one group, distinct permutations differ exactly along an alternating four-cycle disjoint from `v`; switching that cycle exchanges the two labels' permutations. This exists precisely in the `t=1` family and flips one of the three independent bits. Thus the eight states form a cube, and both `t=0,2` states are isolated. QED.

## Consequence for separator-response theory

The bare boundary signature is **not** a complete neutral-reachability state. The connected-fiber hypothesis in the synchronized fiber-product theorem fails for both certificate systems on a capped shore as small as `K_{3,3}`.

The correct repair is to augment a signature by its internal neutral-component index. For these examples:

* three-sheet CDC: two component types per signature (the two Latin completions);
* six-matching multicover: three component types per signature (even-only, mixed, odd-only).

A global separator automaton based on signatures alone can therefore predict **spurious reachability** even though all local certificate-feasibility conditions are satisfied.

This provides a concrete research target: characterize *when* the number of fiber components, and their typed boundary transitions, can be bounded by a function of the cut size and certificate multiplicity, rather than graph order. The K_{3,3} example rules out taking this bound to be 1.

## Independent reproduction

The stand-alone enumerator `tests/test_k33_neutral_fibers.py` checks all 12 labelled three-sheet CDC states and all 900 labelled six-matching double-cover states and builds their exact neutral fiber components. It found precisely the component types claimed above.

## Context and novelty

The classification uses standard Latin-square facts and Kempe-switch arguments. Its value is as a **shared, minimal adversarial example and corrected boundary-state design**, not as a currently established novel theorem. Prior work on edge-coloring Kempe equivalence must be reviewed before any publication claim. Relevant comparison: Chakraborty–Feghali–Mahmoud, *Kempe equivalent list colorings revisited* (JGT 2024), DOI:10.1002/jgt.23142.


## Literature audit correction (added 2026-10-08)

**The three-sheet CDC part is not a novel edge-Kempe result.** Belcastro and Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, Discrete Mathematics 325 (2014), 77–84, DOI [10.1016/j.disc.2014.02.014](https://doi.org/10.1016/j.disc.2014.02.014), explicitly establish the two edge-Kempe classes of K3,3 and a product formula under nontrivial 2-/3-edge-cut decompositions. The correspondence from 3-CDC sheets to a 3-edge-coloring makes their result directly applicable. Goedgebeur and Östergård, *Switching 3-edge-colorings of cubic graphs*, Discrete Mathematics 345 (2022), article 112963, DOI [10.1016/j.disc.2022.112963](https://doi.org/10.1016/j.disc.2022.112963), also discuss families with exponentially many edge-Kempe classes. Therefore exponential amplification by 3-edge-summing K3,3 blocks is **not a new theorem** in the 3-CDC setting.

Our additional classification of the **six-perfect-matching multicover** fiber (component sizes 1,8,1) remains a rigorous elementary companion observation, but **its originality has not been established**. The theorem-first next target should NOT simply restate the known 2014 product formula. It should characterize the richer matching-multicover signature-component dynamics or strict-escape behavior under hypotheses that yield consequences beyond existing Kempe theory.
