# Resistance–kernel universality (2026-10-08)

**Status:** complete mathematical proof draft and checked finite examples; unrefereed; novelty relative to all prior literature **not established**.

The main theorem shows that every simple 3-edge-connected cubic graph `K` occurs as the suppressed residual kernel of a prescribed Fan–Raspaud triple on a simple 3-edge-connected cubic graph `G`, using exactly `r(K)` uncovered edges and adding exactly `2 r(K)` vertices, where `r(K)` is edge-colouring resistance. No realization with fewer uncovered edges exists. If `r(K)=2`, the host `G` can be chosen 3-edge-colourable.

This is a *fixed-triple extension* theorem, not a solution or disproof of Berge–Fulkerson or Fan–Raspaud.

* Manuscript source: [`main.tex`](main.tex); compiled copy: [`main.pdf`](main.pdf).
* Constructive solver: [`../resistance_kernel_lift.py`](../resistance_kernel_lift.py).
* Independently checkable Petersen and flower-snark certificates: [`../resistance_certificates/`](../resistance_certificates/).
* Reproduction: from root `python -m pytest -q tests/test_resistance_kernel_lift.py` or full `python -m pytest -q`.

Both certificates encode the deletion set, proper partial edge-colouring, port colours, resulting host and the three perfect matchings. Connectivity and the exact kernel are checked in tests using an independent graph library.

A related 14-vertex Petersen certificate based on a different construction was already archived in `../fr_extension_paper/`. The current theorem subsumes its order lower bound and extends it to every simple 3-edge-connected cubic graph.

Relevant literature to audit before submission: Fouquet–Vanherpe (2009); Lin–Wang (2018); Karabáš–Máčajová–Nedela–Škoviera (2024); Allie (2022, 2026), and broader snark-resistance/superposition literature.
