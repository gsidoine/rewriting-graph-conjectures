# Berge-Fulkerson: Quadratic Coordinate Descent

This case study asks whether six perfect matchings can be normalized to a Fulkerson cover by replacing one matching at a time. The defect is

```text
Q = sum_e (multiplicity(e) - 2)^2.
```

The proved descent theorem guarantees a strict coordinate replacement whenever `Q > 2n`. The computational layer tests the residual low-defect region and provides exact Petersen and Flower-snark checks.

- Mathematical status: [`../docs/mathematical_status.md`](../docs/mathematical_status.md)
- Conceptual notes: [`theory/`](theory/)
- Reusable implementation: [`src/`](src/)
- Exact C++ check: [`cpp/j5_rewrite.cpp`](cpp/j5_rewrite.cpp)
- Certificates and logs: [`certificates/`](certificates/) and [`logs/`](logs/)
- Publication status: [`../publications/README.md`](../publications/README.md)
