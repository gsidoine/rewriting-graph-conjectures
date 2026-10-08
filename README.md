# Rewriting Graph Conjectures

**A computational research programme for turning graph-existence conjectures into local normalization problems.**

This project asks a recurring question:

> Can a feasible graph certificate be improved by local rewrites until an exact defect vanishes - and, when normalization fails, what mathematical obstruction does the failed dynamics reveal?

The programme was inspired by Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule's [rewriting-Collatz repository](https://github.com/emreyolcu/rewriting-collatz) and their paper *An Automated Approach to the Collatz Conjecture*. Their work translates arithmetic dynamics into formal string-rewriting termination problems and searches for automated proofs. Here the connection is methodological rather than literal: the graph systems have different state spaces and are not term-rewriting systems, but they follow the same cycle of encoding, defect design, automated search, termination analysis, and obstruction extraction.

## Two-track research program

**[Track A — General coordination theory](theory/README.md)** develops repair width, obstruction hypergraphs, strict and neutral reconfiguration, separator composition, and complexity results. Code and certificates live in [`certificate_coordination/`](certificate_coordination) and in the six-matching [`plateau`](applications/berge_fulkerson/plateau) work.

**[Track B — Applications to graph problems](applications/README.md)** develops problem-specific certificate dynamics for Berge–Fulkerson, 3-Decomposition, Barnette, edge-connectivity partitions and related questions. Applications both test the theory and expose its limitations.

### From experiment to theorem

```text
open graph question or general certificate system
   -> exact state/defect/obstruction certificate
   -> strict + neutral rewrites; separator interfaces
   -> independent finite counterexample or structural theorem
   -> adversarial proof + literature audit + reproducible files
```

## Start here

- [General theory](theory/README.md) and [applications](applications/README.md)
- [October claim register](docs/claim_register_oct2026.md) — provisional theorem drafts vs computation vs open gaps
- [July mathematical status](docs/mathematical_status.md) — historical audited baseline
- [Architecture and versioning](docs/repository_architecture.md)
- [Reproducibility instructions](docs/reproducibility.md)
- [Research directions](docs/research_directions.md)

> **Research status (8 October 2026).** These materials include unpublished theorem drafts, independently checkable finite data, and conjectural extrapolations. We do **not** claim to have solved Berge–Fulkerson, Fan–Raspaud, Barnette or edge-connectivity partitioning; no October claim is Lean-certified or externally peer-reviewed. External preprints concerning 3-Decomposition require separate assessment.

**New October result:** a [sharp 14-vertex FR-triple nonextension certificate](applications/berge_fulkerson/plateau/FR_EXTENSION_OBSTRUCTIONS_20261008.md), with a Petersen residual kernel and all-even-order triangle lifts, illustrates the distinction between direct extension and a one-coordinate strict escape. See the [exact cut-signature theory](theory/cut_signature_factorization_2026-10-08.md). These are *research results requiring an external novelty review*, not counterexamples to Berge–Fulkerson.


**Theorem-first pivot (8 October 2026):** [Cycle double-cover rewriting application](applications/cycle_double_cover/README.md) and [cross-certificate three-cut reconfiguration theory](theory/three_cut_synchronized_reconfiguration_2026-10-08.md), including exact [K3,3 neutral-fiber obstructions](theory/k33_neutral_fiber_obstructions_2026-10-08.md). These are research drafts and independently testable small cases, **not** a solution to 5-CDC. See the [theorem-first research programme](docs/theorem_first_reconfiguration_program_2026-10-08.md).


**New theorem-first milestone (8 October 2026):** [exact exponential neutral components of matching multicovers](theory/exponential_neutral_components_multicovers_2026-10-08.md) on a chain of K3,3 blocks, including `3^n` distinct reconfiguration classes for six-perfect-matching double covers on connected, 3-edge-connected bipartite cubic graphs. The same exponential bound holds after fixing the boundary signature. **Proof draft and independent finite checks; no specialist novelty claim.**


**Extended theorem-first milestone (8 October 2026):** [pair-rigid tile algebra](theory/pair_rigid_tile_multicover_algebra_2026-10-08.md) now gives an exact neutral-component factorization for chains of rigid cubic tiles and non-3-edge-colorable K3,3/Petersen mixtures. The cube Q3 shows the rigidity assumption is necessary for this matching-multiset invariant. **Human proof draft; independently checked finite cases; literature novelty unverified.**


**New theorem-first continuation:** [Pair-rigid tile neutral algebra](theory/pair_rigid_tile_multicover_algebra_2026-10-08.md) extends exact component-count and reachability formulas from K3,3 to chains with Petersen blocks, including non-3-edge-colorable graphs, and identifies an arity-three escape from binary-neutral components. The result is a research proof draft with independent computational checks and an explicit novelty warning.


**New generalization beyond pair rigidity (8 October):** [neutral-transparent cube substitution](theory/neutral_transparent_cube_substitution_2026-10-08.md) preserves neutral-reconfiguration component sets when inserting a cube, both for six-perfect-matching double covers and for padded q-sheet cycle double covers with arbitrary q>=3. The exact cycle-cover state multiplier includes q=5 and q=8. The local transparency claims use exhaustive finite cube checks; no major open conjecture is resolved and novelty remains under review.



**Theorem-first structural milestone:** [complete component-enriched typed three-cut relation algebra](theory/component_enriched_three_cut_relation_2026-10-08.md) now computes neutral reconfiguration exactly across arbitrary three-edge sums for both six-matching double covers and padded cycle double covers, including disconnected internal boundary fibers. This subsumes the pair-rigid product and cube-transparent insertion as special cases. It is an exact structural **research proof**, not a polynomial-time result or independently vetted novelty claim.


## Quick start

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

make test
make reproduce-small
make reproduce-cpp
```

Python 3.10+, NetworkX, and a C++17 compiler are required. The large exhaustive runs are separated from the smoke tests and documented with their expected outputs.

## Research status

The repository contains substantial partial results, finite verification, and falsified intermediate ideas, but **does not claim a proof of Berge-Fulkerson, 3-Decomposition, Barnette, or Tutte 5-Flow**. A historical 48-vertex Barnette trap certificate was found inconsistent with its supplied graph and is preserved only as a documented failed certificate. This is intentional: failed rewrite systems are part of the research record.

## Manuscripts and publications

The private research repository includes source manuscripts and convenience PDF snapshots. Proof status is tracked in the dated claim register; manuscript drafts have not been independently peer reviewed. Their eventual preprints, journal versions, and archival DOIs should be listed in [`publications/README.md`](publications/README.md).

## Author

**Guillaume Sidoine**  
Independent Researcher  
ORCID: [0009-0005-4525-1182](https://orcid.org/0009-0005-4525-1182)

## Citation and licensing

Citation metadata are in [`CITATION.cff`](CITATION.cff). Code is released under the MIT License; original research documentation is released under CC BY 4.0 where indicated.

### New (October 8, 2026): resistance--kernel universality

See [the mathematical status and proof](theory/resistance_kernel_realization_2026-10-08.md) and [the paper](applications/berge_fulkerson/plateau/resistance_paper/README.md). This is an unrefereed, novelty-unverified general theorem candidate linking edge-colouring resistance to the minimum defect/order of an FR-triple residual-kernel realization.

### New (October 8, 2026): unbounded uphill FR-triple barriers

A [five-page proof draft](applications/berge_fulkerson/plateau/energy_barriers/paper/main.tex) and [independent exact certificates](applications/berge_fulkerson/plateau/energy_barriers/README.md) establish a family of simple 3-edge-connected, 3-edge-colourable cubic graphs in which every FR-preserving one-matching normalization path must temporarily *increase* the uncovered-edge defect by an unbounded amount. The 10-vertex seed has the exact path `3 -> 4 -> 3 -> 0`; balanced `K_{3,2}` replacement amplifies its barrier. See the [theorem status](theory/fr_uphill_barriers_2026-10-08.md). Novelty remains to be independently audited.

## New theory: exact FR three-pole renormalization (October 8, 2026)

The balanced `K_{3,2}` expansion preserves **full** one-coordinate Fan–Raspaud reconfiguration connected components while transforming the ordered-FR-triple defect polynomial by an explicit algebraic substitution. The exact local fibres are `Q3` and `C6`; iterating the operator gives closed minimizer counts and a universal weighted-defect entropy. [Proof/status](theory/fr_three_pole_renormalization_2026-10-08.md) · [LaTeX/PDF](applications/berge_fulkerson/plateau/energy_barriers/transfer_paper/) · [executable verifier](applications/berge_fulkerson/plateau/energy_barriers/transfer_operator.py). This is an unrefereed research theorem draft; novelty is not established.
