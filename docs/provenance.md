# Provenance

The repository was reconstructed from two upload batches on 12 July 2026.  The original files are immutable under `archive/original_files/`; `archive/SHA256SUMS_supplied.txt` is the chain-of-custody manifest.

Audited `main.tex` files are derived from the corresponding `main_original.tex` files and contain explicit proof/status corrections.  Extracted Python scripts under `repro_runs/scripts/` were generated from notebook code cells to remove hidden execution state.  Fresh output files use the suffix `_reproduced` or live under `repro_runs/`; files marked `_historical` are never treated as independently rerun.

The graph-theory research was methodologically inspired by a rewriting approach to Collatz, as described in `relation_to_rewriting_collatz.md`.  No external code-reuse claim is made.
