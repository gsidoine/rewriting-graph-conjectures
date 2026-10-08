# Berge-Fulkerson: Quadratic Coordinate Descent

This case study asks whether six perfect matchings can be normalized to a Fulkerson cover by replacing one matching at a time. The defect is

```text
Q = sum_e (multiplicity(e) - 2)^2.
```

The proved descent theorem guarantees a strict coordinate replacement whenever `Q > 2n`. The computational layer tests the residual low-defect region and provides exact Petersen and Flower-snark checks.

- Mathematical status: [`../docs/mathematical_status.md`](../../docs/mathematical_status.md)
- Conceptual notes: [`theory/`](theory)
- Reusable implementation: [`src/`](src)
- Exact C++ check: [`cpp/j5_rewrite.cpp`](cpp/j5_rewrite.cpp)
- Certificates and logs: [`certificates/`](certificates) and [`logs/`](logs)
- Publication status: [`../publications/README.md`](../../publications/README.md)

## October 2026: prescribed FR-triple extension and residual kernels

The [order-14 nonextension theorem candidate](plateau/FR_EXTENSION_OBSTRUCTIONS_20261008.md) exhibits a 3-edge-connected, 3-edge-colourable cubic host and a Fan–Raspaud triple with a bridgeless but non-3-edge-colourable residual. The residual suppresses to Petersen; nevertheless one coordinate change repairs the original triple. The [explicit JSON certificate](plateau/fr_n14_petersen_kernel.json), [standard-library verifier](plateau/fr_extension_core.py), and [regression test](../../tests/test_fr_extension_core.py) are maintained here. This concerns extension of a *prescribed* triple, not Berge–Fulkerson itself.
