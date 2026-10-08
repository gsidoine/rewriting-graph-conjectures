# October 8, 2026: two-coordinate descent, localization and plateau amplification

**Status: private research branch; independent publication/novelty review not yet complete.**

This document is an additive continuation of the July 2026 audited graph-rewriting program and the October v4 sharp direct-repair threshold package. The historical `docs/mathematical_status.md` has not been overwritten. The proofs appear in `berge_fulkerson/plateau/next_phase/continuation_20261008/paper/main.tex` and the PDF in the same directory.

## New general mathematical claims

1. **Exact 45-move pair-coordinate drift.** On any 3-edge-colourable cubic graph G with n vertices and a given 3-edge-colouring into factors F1,F2,F3, the defects resulting from the 15 choices of original coordinate pair and 3 choices of distinct colour-factor pairs sum to `18 Q + 39 n`. Consequently a strictly improving two-matching replacement exists whenever `Q > 13n/9`. Choosing the best of these 45 candidate moves decreases excess over the threshold geometrically, requiring O(log n) moves to enter the low-defect region. This is an elementary averaging identity, not a resolution of Berge–Fulkerson.
2. **Exact 20-move triple-coordinate drift.** Across choices of three original positions replaced by F1,F2,F3, the defects sum to `4 Q + 12 n`; strict three-coordinate descent holds if `Q > 3n/4`.
3. **Boundary-stiff 3-edge-cut gluing.** There is a certificate-defined 18-vertex 3-edge-connected cubic bipartite gadget whose Q=6 state cannot strictly improve using one matching. Its port mismatch costs at least 2 units in the quadratic defect. Splicing k gadgets along 3-edge cuts produces a simple 3-edge-connected bipartite cubic graph with `16k+2` vertices and `Q=6k` at a one-coordinate non-improving state, while an explicit `2k`-move path uses alternating neutral and improving single-coordinate replacements to reach Q=0. This proof includes an exact double-count correction at each cut.
4. **Independent defect-component repair.** On a cubic bipartite graph, a connected component C of the edges with m!=2 can be corrected *alone*, leaving all other edge multiplicities unchanged, by replacing r>=2 selected coordinates I **iff** `s_I(e)>=m_e-2` at each surplus edge in C. The construction is a decomposition of a regular bipartite multigraph into r perfect matchings. This is a specific application of a classical factorization theorem, not a new edge-colouring theorem.
5. **Unlimited-size small-cycle normalization.** For any cubic bipartite sextuple with only multiplicities 1,2,3 and all defect components alternating cycles of length at most 10, sequential two-coordinate strict replacements lead to Q=0, correcting one cycle at a time. Length at most 38 guarantees the analogous three-coordinate procedure. **Total Q and graph size may be arbitrarily large.** The pair hitting argument uses the nonexistence of a triangle decomposition of K6; the triple hitting argument uses the 20 complements of 3-subsets of six labels.

## New finite computer-assisted claims

- On the 18-vertex gadget there are 47 perfect matchings. A dependency-free exhaustive test checks its six one-coordinate boundary-stiffness inequalities for each possible alternative. The concrete Q=6→6→0 path and both ports are also verified.
- Four explicit spliced examples k=1,2,3,4 are checked for valid graph/matching data, their full move trace, and edge connectivity at least three (by checking all 0/1/2 edge deletions).
- All nine nonisomorphic simple connected cubic bipartite graphs through 12 vertices have been enumerated by a canonical row/column method. An exact optimizer checked **665,112** six-perfect-matching multisets, finding no positive-defect strict two-coordinate local minima.
- On the flower snark J5 an independent C++17 exhaustive optimizer checked **2,324,784** six-perfect-matching multiset states, again finding no positive-defect strict two-coordinate local minima.
- The previous 32-vertex Q=34 direct-repair obstruction (requiring four coordinates for one-step Q=0) has a certified three-step exact correction, replacing **two** matchings on each step, with trace **34→24→12→0**. Each step fixes one defect component and exactly preserves the multiplicities of every edge outside it. A standalone stdlib Python checker verifies all replacement perfect matchings.

## Important novelty correction

**Linearly growing one-coordinate traps were already present in this very repository.** The earlier `berge_fulkerson/plateau/cover_lifting.py` constructs connected graph covers inheriting one-coordinate local optimality and Q growing proportionally to vertex count, with base density 1/3. The current 3-edge-cut construction is therefore **not a qualitative discovery of unbounded trap defect**. What differs is the 3-edge-cut boundary-stiffness mechanism, a direct local composition inequality, and a higher limiting Q/n density of 3/8. Before submission, compare these carefully with established matching-covered graph theory and exact-potential local search.

## Research boundary

**Not proved:** global strict two-coordinate descent for every cubic bipartite sextuple; any universal normalized two-coordinate path on snarks; Fan–Raspaud; Berge–Fulkerson. The finite results must not be stated as a universal proof. No Lean kernel verification is included. The draft has not passed external novelty assessment.

An August 26 / September 3 2026 preprint by Jicheng Ma (arXiv:2608.25385v2) **claims** a full 3-Decomposition Conjecture proof. This has not been independently validated in our audit, but the original 3-decomposition conjecture should not be promoted as definitely open pending expert review of that preprint.

## Reproduce

From the repository root:

```bash
PYTHONPATH=. pytest -q
PYTHONPATH=. python -m applications.berge_fulkerson.plateau.next_phase.continuation_20261008.verify_stiff_base
PYTHONPATH=. python -m applications.berge_fulkerson.plateau.next_phase.continuation_20261008.check_certificates
PYTHONPATH=. python -m applications.berge_fulkerson.plateau.next_phase.continuation_20261008.verify_component_certificate
PYTHONPATH=. python -m applications.berge_fulkerson.plateau.next_phase.continuation_20261008.verify_drift
PYTHONPATH=. python -m applications.berge_fulkerson.plateau.next_phase.continuation_20261008.all_small_pair_audit

g++ -O3 -std=c++17 berge_fulkerson/plateau/next_phase/continuation_20261008/j5_exhaustive_pair.cpp -o /tmp/j5_audit
/tmp/j5_audit berge_fulkerson/instances/j5/j5_input.txt
```

The new `componentwise_repair.py` and `verify_component_certificate.py` require no third-party libraries, although the full repository test suite has pre-existing third-party dependencies.

## Next meaningful theorem milestone

The precise open problem is: *Does every six-perfect-matching sextuple on a cubic bipartite graph with Q>0 admit a strictly improving replacement of at most two of the six matchings?* A proof would upgrade the componentwise restriction to a universal theorem; a concrete example with an exact min-cost-flow or exhaustive certificate would disprove it. Other promising targets are cyclically 4-edge-connected plateau constructions (avoid trivial 3-edge-cut amplification), and a nonbipartite parity-aware residual factorization theorem enabling coordinated repair on snarks.
