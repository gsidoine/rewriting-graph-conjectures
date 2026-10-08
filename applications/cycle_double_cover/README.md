# Cycle double-cover certificate rewriting (October 2026)

This application studies **reconfiguration of labelled cycle-double-cover certificates**. It is part of the repository's general certificate-coordination programme. It is **not** a proof of the five-cycle double cover conjecture (5-CDC).

## Core questions

A certificate is a tuple of even edge sets, each original edge occurring exactly twice. A strict move reduces the number of nonempty sheets while preserving exact edge multiplicities. A neutral move swaps two labelled sheets along a component of their symmetric difference. When does a sequence of neutral moves enable a strict move? How does this depend on a graph's three-edge-cut structure?

## Results and provenance

* **Exact trade criterion (proof draft).** Four selected sheets can be replaced by at most three even sheets precisely when a suppressed auxiliary cubic multigraph is properly three-edge-colorable. More generally the criterion applies to any selection of at least three sheets.
* **Direct-descent obstruction (proof draft).** A covering-design / Petersen-block three-edge-sum construction gives, for every q>=6, a connected 3-edge-connected non-3-edge-colorable cubic graph with a q-sheet certificate that is blocked against every direct trade involving at most four sheets, although the graph admits a five-sheet CDC. Such graphs have nontrivial cyclic three-edge cuts.
* **Neutral escape (finite certificate).** One 162-vertex q=8 example has a verified six-move route 8 -> 8 -> 7 -> 6 -> 6 -> 6 -> 5, with three neutral switches and three four-to-three trades. At the six-sheet intermediate state, 16,137 possible nontrivial single-pair neutral trades fail to unlock a strict reduction, while a two-switch sequence succeeds.
* **Small-order compression (proof draft).** An averaging argument and extra integral parity exclude globally quartet-obstructed q-sheet covers for q=6,7,8,9,10 in specific small-order ranges, including all eight-sheet covers on at most 20 vertices.
* **Independent finite experiments.** Nine sampled 30-vertex cyclically four-edge-connected snarks show 69 or 70 compressible quartets in their selected eight-sheet covers; these are not exhaustive over covers.

Read [claim status](CLAIM_STATUS.md), [compression mathematics](compression_theorems.md), and [negative and neutral-dynamics results](obstructions_and_neutral_escape.md).

## Reproducibility

The canonical **original research archives** were produced on 2026-10-08, but are not yet attached to this GitHub branch as machine-readable data. Thus the finite figures above are clearly recorded as *prior finite certificates, awaiting in-repository independent replay*, not CI-certified claims. Do not infer that the repository currently includes the 162-vertex JSON or all eight-to-five move witnesses. Those must be imported from the original archived package before marking the branch fully reproducible.

The new cross-certificate theorem and its own independent small-case test are in [three-cut synchronized reconfiguration](../../theory/three_cut_synchronized_reconfiguration_2026-10-08.md).

## Novelty boundary

Local parity, T-joins, Petersen snark obstruction, 3-edge-coloring, three-cut splicing, and much of the reconfiguration literature are classical. These notes are internal research records, **not** submitted peer-reviewed papers or certified novel results. Earlier finite test cases with small oddness do not establish advances on the existence of five-sheet covers: 5-CDC is known for cubic graphs of oddness at most four.

## Stop/pivot criterion

Archive further isolated finite-order bounds unless they yield an infinite-family result, a new invariant with nontrivial cross-problem implications, or an independently falsifiable structural obstruction. The principal research direction is theorem-first certificate reconfiguration, not endless weakening of eight-to-five descent.
