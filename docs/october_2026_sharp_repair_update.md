# October 8, 2026 — research branch update (not yet canonical)

**Research owner:** Guillaume Sidoine, independent researcher.  
**Trust boundary:** This is an **additive research branch**, not an update to the authoritative July `docs/mathematical_status.md` until an independent specialist literature audit and external proof check have been completed. No Lean verification has been performed.

## New theorem: unrestricted direct repair hierarchy

For any six perfect matchings (repetitions allowed) of a finite simple cubic bipartite graph, let

`Q = sum_e (m(e)-2)^2` and `kappa = min number of matching coordinates that must be replaced simultaneously to attain Q=0`.

The sharp minima of `Q` for `kappa>=2`, `kappa>=3`, `kappa>=4` are **6, 12, 34**, even among 3-edge-connected cubic bipartite graphs.

- Universal `Q<=10 -> kappa<=2` (improves previous *unit-defect* exact-repair and strict-descent bounds to all multiplicity configurations).
- Universal `Q<=32 -> kappa<=3` (new sharp all-multiplicity theorem; previous unit-defect boundary was 38/40).
- New **32-vertex simple 3-edge-connected cubic bipartite graph** with `Q=34, kappa=4`. Certificate has 48 edges with multiplicity histogram `{1:14, 2:23, 3:8, 4:3}`. It is explicitly included as a 16-row adjacency/label table in the new LaTeX manuscript and as JSON. A pure-standard-library verifier checks every deletion of at most two edges (1,177 subsets).
- The example has strict two-coordinate descent `Q:34 -> 8`; thus it **does not refute** the broader strict two-coordinate descent conjecture.
- Universal exact direct-repair criterion: a coordinate subset `I` can be replaced iff its intersection with each edge label set `S_e` has cardinality at least `m_e-2` whenever `m_e>2`.
- Key energy identity: `Q/2 = n_0+n_3+3*n_4+6*n_5+10*n_6`.
- All positive `Q<=32` restrictions follow from an elementary case argument for the seven possible multiplicity partitions at a cubic vertex. The accompanying C++ program independently performs finite subset DP on all 20 triple choices, discovering minimum local energy 34 without sixfold edges.

## Validity and remaining uncertainties

- **Proof**: Complete self-contained five-page new theorem draft under `berge_fulkerson/plateau/next_phase/paper/main.tex`, with zero-external-dependency finite certificate checker. This has **not** been externally refereed or kernel checked in Lean.
- **Novelty**: The partial-order/direct-repair characterization is a direct consequence of König bipartite factorization and is not claimed new. The proposed new contribution is the **sharp cubic-graph realizability threshold 34**, plus full all-multiplicity hierarchy. A web search found no immediate exact duplicate but this is not a literature clearance.
- **Related literature**: Bonamy et al., *The Perfect Matching Reconfiguration Problem* (2019), https://doi.org/10.4230/LIPIcs.MFCS.2019.80; Mori, Motomura, Ohsugi and Tsuchiya, *Toric ideals of matching polytopes and edge colorings* (Mathematika 2026), https://doi.org/10.1112/mtk.70099. The latter result concerns transformations preserving aggregate edge multiplicities, which should not be conflated with our defect-changing direct replacements.
- **Distinct problem**: Whether *every* `Q>0` state in cubic bipartite graphs admits **strict descent** replacing at most two matching coordinates remains open in this programme. The new `Q=34` example has exact two-coordinate best `Q=8`, hence is not a counterexample. A standalone finite audit examined 199,129 multisets on four selected cyclic cubic bipartite graphs of orders 6, 8, 10, 12; no positive-Q pairwise local minima occurred. This is evidence only, not an exhaustive classification of all graphs of those sizes.

## Literature alert changing the larger project

Jicheng Ma, *Matching complements in subcubic graphs and a proof of the 3-Decomposition Conjecture*, arXiv:2608.25385 (posted August 26, 2026), claims a proof of the previously open 3-Decomposition Conjecture. Original source: https://arxiv.org/abs/2608.25385 . Independently audit before declaring the conjecture resolved, but **do not describe it as unconditionally still open in future project submissions**. Audit the impact on the previous 3-decomposition manuscript and its novelty positioning.

## Reproduce

```bash
python berge_fulkerson/plateau/next_phase/q34_standalone_checker.py
python berge_fulkerson/plateau/next_phase/independent_checker.py
g++ -O3 -std=c++17 berge_fulkerson/plateau/next_phase/type_cover_bound.cpp -o /tmp/type_cover_bound
/tmp/type_cover_bound
python -m berge_fulkerson.plateau.next_phase.exhaustive_pair_small
python -m pytest -q
cd berge_fulkerson/plateau/next_phase/paper && latexmk -pdf main.tex
```

## Suggested research continuation

1. Novelty audit against covering-design and matching reconfiguration literature, with specialist referees and primary papers.
2. Formalize the seven local multiplicity partition cases and the 32-vertex certificate checker in Lean 4; avoid importing the finite DP as an opaque trust assumption.
3. Investigate arbitrary-Q strict two-coordinate descent; use optimal two-coordinate minimum-cost flow for adversarial construction and use the toric/edge-colouring literature to understand irreducible neutral plateaux.
4. Explore nonbipartite low-defect cases where freezing four matchings leaves a 2-regular multigraph; exact pair repair requires all cycles of that multigraph to be even.
5. Separate empirical results, theoretical results, counterexamples, and literature-complete novelty claims. Do not make the repo public or submit the manuscript until the canonical ledger is updated and the central claims receive external audit.
