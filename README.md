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
