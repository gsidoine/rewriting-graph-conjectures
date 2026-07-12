# 3-Decomposition: Basis-Exchange Normalization

A state is a spanning tree `T`. The defect `b(T)` counts cotree path components containing at least two edges; `b(T)=0` is exactly a 3-decomposition. The rewrite graph is the spanning-tree basis-exchange graph restricted to non-increasing moves.

This directory contains universal safe exchanges, exhaustive plateau checks through ten vertices, an explicit fixed-cycle obstruction, and an audited constrained NP-completeness reduction.

- Mathematical status: [`../docs/mathematical_status.md`](../docs/mathematical_status.md)
- Rewrite rules and conjectures: [`theory/`](theory/)
- Exact counterexample verifier: [`src/verify_counterexample.py`](src/verify_counterexample.py)
- Canonical notebooks: [`notebooks/`](notebooks/)
- Certificates: [`certificates/`](certificates/)
- Publication status: [`../publications/README.md`](../publications/README.md)
