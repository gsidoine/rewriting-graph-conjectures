# A positive-defect immobility theorem for three-cut rewrites

**Status:** elementary argument and a complete ten-vertex audit; not a solution to Erdős #64; no originality claim.

## The theorem

Let G be a simple cubic graph in which every edge cut of size three separates a single vertex from the other vertices. Then no nontrivial reconnection of three **distinct boundary ports on both sides** exists: each possible three-cut is a star at one vertex, so one shore has only one vertex, not three distinct ports. Even if repeated ports were allowed, all permutations of edges incident to a single vertex give the same edge set.

Consequently, the three-cut reconnection operator of `cycle_transfer.py` cannot change G, regardless of which defect ranking or neutral routing rule is chosen. This is a structural limitation of the move set, not simply a poor choice of potential function.

## Explicit Petersen witness

The Petersen graph has ten vertices, is cubic and 3-edge-connected. Exhaustive inspection of all proper vertex bipartitions finds exactly ten unordered three-edge cuts, each separating a vertex. Independently enumerated unoriented simple cycles have length spectrum:

    length 5: 12
    length 6: 10
    length 8: 15
    length 9: 20

Hence Q(Petersen) = 15 > 0, yet the graph has no admissible three-cut rewrite, whether strict or neutral. The proof checks a finite 2^10-sized set of bipartitions and uses standard cycle enumeration; run:

    python -m pytest -q tests/test_erdos_gyarfas_three_cut_trap.py

## Consequence for general certificate coordination

The exact three-cut transfer identity is valid where applicable, but a **universal** descent/escape theorem needs moves that reach cyclically four-edge-connected cubic graphs. Enlarging the signature alone does not solve this: the obstacle is absence of an eligible separator. Possible additions are 4-/5-cut exchanges, vertex-level rewrites, or structure theorems for irreducible cores.

No assertion about the minimum order of Erdős–Gyárfás counterexamples, or existence of a counterexample, follows. Petersen is emphatically not a counterexample: it has 15 cycles of length eight.
