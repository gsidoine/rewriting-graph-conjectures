# Prescribed Fan--Raspaud triple extension — 14-vertex minimal witness

**Status:** unrefereed research draft; exact finite certificate checked and written mathematical proof supplied. Several reduction ingredients are known (Fouquet--Vanherpe 2009; Lin--Wang 2018). The particular sharp order and construction have not undergone specialist novelty review. This is **not** a solution of Berge--Fulkerson.

- [`main.tex`](main.tex): editable four-page LaTeX manuscript.
- [`main.pdf`](main.pdf): compiled convenience snapshot.
- [`../fr_n14_petersen_kernel.json`](../fr_n14_petersen_kernel.json): complete host graph, prescribed matchings, independent 3-edge-colouring and Petersen residual-kernel isomorphism.
- [`../fr_extension_core.py`](../fr_extension_core.py): dependency-free verification and triangle-expansion generator.
- [`../FR_EXTENSION_OBSTRUCTIONS_20261008.md`](../FR_EXTENSION_OBSTRUCTIONS_20261008.md): full derivations, experiment counts and caveats.

Verify from the repository root:

```bash
python -m applications.berge_fulkerson.plateau.fr_extension_core
python -m pytest -q tests/test_fr_extension_core.py
```

Rebuild the paper with `latexmk -pdf main.tex`; only `main.tex` and `main.pdf` are versioned.
