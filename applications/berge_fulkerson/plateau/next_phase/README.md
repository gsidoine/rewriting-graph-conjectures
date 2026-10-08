# October 2026: sharp unrestricted exact-coordinate repair thresholds

**Research-only branch.** These theorems have undergone algebraic, enumerative, and independent certificate verification, but have not been formally checked by Lean or evaluated by an external referee. The repository's July 2026 status ledger and prior research artifacts are preserved.

## Main theorem

Let `G` be a simple cubic bipartite graph, and `M_0,...,M_5` be perfect matchings, with repetition allowed. Define multiplicity `m(e)`, potential `Q=sum_e (m(e)-2)^2`, and `kappa` as the smallest number of whole matchings to replace *in one simultaneous step* in order to get `Q=0`. Then:

* For every sextuple with `Q<=10`, `kappa<=2`. Sharp at `Q=12` by the 18-vertex certificate already in the v3 branch.
* For every sextuple with `Q<=32`, `kappa<=3`. **Sharp at `Q=34`** by `q34_witness_32.json`, a 32-vertex 3-edge-connected cubic bipartite graph.
* The exact extremal positive-defect thresholds for `kappa>=2,>=3,>=4` are `6,12,34` (including for 3-edge-connected cubic bipartite graphs). The previously reported `6,12,40` remains the sharp hierarchy restricted to all edge multiplicities in `{1,2,3}`.
* Four coordinates always suffice by regular bipartite multigraph decomposition.

The proof is in `paper/main.tex` and rendered `paper/main.pdf`. It uses a finite covering argument on the 20 three-element subsets of the six matching coordinates; a separate exhaustive C++ verifier is included as independent corroboration. The new `Q=34` witness has exactly 3 edges with multiplicity 4, 8 with 3, 23 with 2, and 14 with 1.

## Reproduce

From the repository root:

```bash
python applications/berge_fulkerson/plateau/next_phase/q34_standalone_checker.py
python applications/berge_fulkerson/plateau/next_phase/independent_checker.py
g++ -std=c++17 -O3 berge_fulkerson/plateau/next_phase/type_cover_bound.cpp -o /tmp/type_cover_bound
/tmp/type_cover_bound
python -m pytest -q
```

The graph certificate checker uses only the Python standard library. It verifies all 1,177 edge-deletion sets up to size two. The C++ program derives all 122 vertex-label partition types from first principles and computes a shortest-path DP over `2^20` blocking masks. It verifies the minimum local energy `34` for complete triple blocking with no multiplicity-six edge, independently of the human case analysis.

## What is and isn't achieved

**Achieved:** a complete conditional mathematical proof of the sharp direct-repair hierarchy, explicit finite extremal graphs, a dependency-free verifier and a separate finite covering oracle, under the specified graph and multiplicity assumptions.

**Not achieved:** a proof/disproof of two-coordinate *strict descent* for arbitrary positive defect, a Berge–Fulkerson/Fan–Raspaud solution, Lean formalization, or established literature novelty. On the new 32-vertex instance, an exact two-coordinate optimizer finds a strict improvement `Q:34 -> 8`; the fact that four coordinates are required for direct repair must not be confused with a two-coordinate local trap.

## New external literature warning

Jicheng Ma, *Matching complements in subcubic graphs and a proof of the 3-Decomposition Conjecture*, arXiv:2608.25385 (posted 26 August 2026), claims a proof of the original 3-Decomposition Conjecture. Until independently assessed, the original conjecture cannot be treated as safely open in the project's papers or problem inventory. This source should be checked against any manuscript claiming open status.
