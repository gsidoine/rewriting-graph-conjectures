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

## Research manuscript (unrefereed)

[A Sharp Petersen-Kernel Obstruction to Extending Fan--Raspaud Triples](plateau/fr_extension_paper/main.pdf) ([LaTeX source](plateau/fr_extension_paper/main.tex)); 4 pages. The finite graph and checks are maintained separately. This is a **research draft** without an externally established novelty claim.

## October 2026: prescribed FR-triple extension and residual kernels

The [order-14 nonextension theorem candidate](plateau/FR_EXTENSION_OBSTRUCTIONS_20261008.md) exhibits a 3-edge-connected, 3-edge-colourable cubic host and a Fan–Raspaud triple with a bridgeless but non-3-edge-colourable residual. The residual suppresses to Petersen; nevertheless one coordinate change repairs the original triple. The [explicit JSON certificate](plateau/fr_n14_petersen_kernel.json), [standard-library verifier](plateau/fr_extension_core.py), and [regression test](../../tests/test_fr_extension_core.py) are maintained here. This concerns extension of a *prescribed* triple, not Berge–Fulkerson itself.

## October 8: resistance--kernel realization

The new [resistance universality theorem and reproducible manuscript](plateau/resistance_paper/README.md) shows that colouring resistance of any simple 3-edge-connected cubic graph is exactly the minimum number of uncovered edges needed to realize it as a frozen Fan--Raspaud residual kernel. Independent Petersen and flower snark certificates are included. External novelty is unverified.

## Uphill Fan–Raspaud reconfiguration barriers

The [unbounded energy-barrier project](plateau/energy_barriers/README.md) supplies a 10-vertex class-one cubic seed, dependency-free exact enumeration and a `K_{3,2}` amplification theorem. It demonstrates that neutral moves alone are not universally sufficient for normalization. [Paper source](plateau/energy_barriers/paper/main.tex). This does not settle Berge–Fulkerson or Fan–Raspaud.

## Exact FR three-pole polynomial and reconfiguration components

A new [theory note](../../theory/fr_three_pole_renormalization_2026-10-08.md) and [five-page manuscript](plateau/energy_barriers/transfer_paper/) prove that the `K_{3,2}` replacement preserves the **full** FR reconfiguration connected components and gives an exact uncovered-edge polynomial renormalization, with universal iterated entropy. Unlike the existing uphill-barrier paper, this identifies the entire fibre structure and distribution. Research draft; independent novelty audit pending.
