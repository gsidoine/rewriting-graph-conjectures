# Cycle-cover rewriting: direct obstructions and neutral escape

**Status:** 2026-10-08 historical research summary. Universal argument is a **proof draft**; 162-vertex and plateau claims come from previously independently checked finite witness files. Original large JSON witnesses are not yet in this GitHub branch. No new graph-existence conjecture is resolved.

## Failure of direct low-arity descent

The natural conjecture that every eight-sheet CDC contains a directly reducible quartet is false when cyclic three-edge cuts are allowed.

**Draft theorem.** For each integer q>=6 there is a connected, simple, 3-edge-connected, cubic, non-3-edge-colorable graph of girth at least five and a q-sheet double cover in which no direct four-to-three trade is possible; nevertheless the graph admits a five-sheet CDC.

**Construction sketch.** Cover all 4-subsets of q global sheet labels with a walk through 5-subsets in the Johnson graph J(q,5), consecutive sets differing by one label. Put a relabelled Petersen five-sheet CDC at each position. Glue adjacent copies along labelled three-edge ports, choosing nonadjacent port vertices in internal copies. A quartet of labels lies inside at least one Petersen block's five-set; if its four sheets compressed to three, the output-edge coloring (color multiplicity-one edges by the unique owner and multiplicity-two edges by the unique omission) would induce a proper 3-edge-coloring of that Petersen block, contradicting the Petersen graph's noncolorability. By propagating just five global labels coherently along the three-edge interfaces, a five-sheet CDC can nevertheless be constructed on the same graph.

**Explicit witness previously verified.** The q=8 instance has 20 Petersen blocks, 19 splices, 162 vertices and 243 edges. All 70 quartets are obstructed in the initial labelled cover. A separate five-sheet cover exists.

The local graph may have small edge cuts and is *not* an obstruction to an analogous statement restricted to cyclically 4-edge-connected snarks.

## Neutral trajectory and depth-two plateau

In the original independently replayed finite certificate, the 162-vertex initial cover follows the sequence

`8 --neutral(51-edge cycle)--> 8 --4:3--> 7 --4:3--> 6 --neutral(15 edges)--> 6 --neutral(34 edges)--> 6 --4:3--> 5`.

At the six-sheet checkpoint every immediate four-to-three compression was blocked. Exhaustively enumerating 16,137 nontrivial single-pair neutral switches (arbitrary unions of symmetric-difference cycles) still found no direct compression, while the exhibited *two* subsequent switches unlocked one. This is an example of a depth-two plateau under the specified move system, not a universal lower bound.

The original full package includes the edge-indexed graph, every sheet, and each move. **It must be imported and rerun before the repository marks this computational claim as fully reproduced.** A narrative statement without the corresponding archive is not a substitute for the witness.

## General lesson

Separator signatures and component-level dynamics matter more than another increment in finite graph order. A system that is terminal under all immediate strict moves may admit neutral trajectories enabling descent. The next theorem-first work must characterize the reachability barriers, rather than keep proving increasingly narrow small-order estimates.

See also [exact three-cut synchronization](../../theory/three_cut_synchronized_reconfiguration_2026-10-08.md) and the [K3,3 fiber classification](../../theory/k33_neutral_fiber_obstructions_2026-10-08.md).

**Novelty warning:** Petersen parity, three-edge sums, Latin-square/Kempe switches and much of the obstruction vocabulary are classical; no paper-level originality has been established.
