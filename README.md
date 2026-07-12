# Rewriting Graph Conjectures

**A computational research programme for turning graph-existence conjectures into local normalization problems.**

This project asks a recurring question:

> Can a feasible graph certificate be improved by local rewrites until an exact defect vanishes - and, when normalization fails, what mathematical obstruction does the failed dynamics reveal?

The programme was inspired by Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule's [rewriting-Collatz repository](https://github.com/emreyolcu/rewriting-collatz) and their paper *An Automated Approach to the Collatz Conjecture*. Their work translates arithmetic dynamics into formal string-rewriting termination problems and searches for automated proofs. Here the connection is methodological rather than literal: the graph systems have different state spaces and are not term-rewriting systems, but they follow the same cycle of encoding, defect design, automated search, termination analysis, and obstruction extraction.

## The research loop

```text
existence conjecture
        |
        v
certificate state + exact defect
        |
        v
feasible local rewrites
        |
        +--> strict moves lower the defect
        +--> neutral moves explore a plateau
        |
        v
reverse reachability / terminal-SCC search
        |
        +--> normalization theorem or algorithm
        +--> counterexample to the chosen rule system
        +--> structural obstruction or complexity theorem
        +--> redesigned state space and new rules
```

The repository is therefore not a claim that the major conjectures are solved. It is a reusable laboratory for discovering what a successful normalization proof would need to do.

## Three case studies

### 1. Berge-Fulkerson

A state is a sextuple of perfect matchings. Its defect is the quadratic discrepancy

```text
Q = sum_e (multiplicity(e) - 2)^2.
```

The main proved result gives a polynomially computable strict coordinate descent whenever `Q > 2n`, confining any one-coordinate obstruction to a low-defect region. Exact state-space checks are included for the Petersen graph and the Flower snark `J5`.

### 2. 3-Decomposition

A state is a spanning tree. The defect `b(T)` counts long path components in the cotree. The target `b(T)=0` is exactly a 3-decomposition. The programme studies safe basis exchanges, neutral plateaux, and the **Monotone Exchange Conjecture**. It also records an explicit fixed-cycle obstruction and a constrained NP-completeness result showing why the cycle component must be allowed to change.

### 3. Barnette

A state is a binary colouring of the dual Eulerian triangulation. An exact topological potential measures distance from a two-tree partition. Connected face-patch flips define the rewrite dynamics. Small-radius failure produces explicit traps; allowing three-face patches resolves the verified examples and motivates a stronger normalization conjecture.

## What is in this repository

- reusable Python and C++ implementations of the state spaces, defects, and rewrite graphs;
- exact instances, logs, and machine-checkable certificates;
- independent reproduction scripts and tests;
- a claim-by-claim status ledger separating proofs, finite computations, conjectures, failures, and open gaps;
- research notes explaining how the three programmes fit the common method.

Start with:

- [`docs/research_program.md`](docs/research_program.md) for the conceptual programme;
- [`docs/mathematical_status.md`](docs/mathematical_status.md) for the authoritative claim ledger;
- [`docs/reproducibility.md`](docs/reproducibility.md) for exact commands;
- [`docs/relation_to_rewriting_collatz.md`](docs/relation_to_rewriting_collatz.md) for the intellectual relationship to the original inspiration.

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

The public research repository is best kept focused on the method, software, exact data, and certificates. Manuscripts are maintained separately while being prepared or reviewed. Their eventual preprints, journal versions, and archival DOIs should be listed in [`publications/README.md`](publications/README.md).

## Author

**Guillaume Sidoine**  
Independent Researcher  
ORCID: [0009-0005-4525-1182](https://orcid.org/0009-0005-4525-1182)

## Citation and licensing

Citation metadata are in [`CITATION.cff`](CITATION.cff). Code is released under the MIT License; original research documentation is released under CC BY 4.0 where indicated.
