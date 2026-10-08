# Stale-file and provenance audit — 2026-10-08

This audit distinguishes **superseded**, **historical evidence**, and **live executable work**. Removing old records from the active root is not a repudiation of results, and original commits remain accessible.

## Excluded from the active research tree

1. `OCT2026_*_README.md` at repository root: historical handover snapshots, moved to `archive/`. The current navigation is `README.md`, `theory/README.md`, and `applications/README.md`.
2. Root-level `SHA256SUMS*.txt`: checksum snapshots from previous directory layouts, moved to `archive/historical_manifests/`. These checksums cannot validate the reorganized source tree. A current manifest is at `docs/sha256_current_tree_2026-10-08.txt`.
3. Zero-byte `repro_runs/cpp/barnette_big_reproduced.{stdout,stderr}`: uninformative outputs, moved to `archive/reproduction_attempts/`, clearly labelled as **not evidence of successful reproduction**.
4. Previously tracked `__pycache__` bytecode and transient test caches: removed from current tree (historical commits retained), excluded via `.gitignore`.

## Intentionally retained (do not silently delete)

- The historical 48-vertex Barnette mask files and inconsistency audit: they document a falsified computational claim, not a valid trap. Their current path is under `applications/barnette/` and their status remains flagged.
- Contaminated or mixed historical notebooks: keep as evidence, label provenance, and do not cite outputs without rerunning independent scripts.
- Previous October LaTeX source and PDF snapshots: multiple versions describe **different stages of mathematical claims**, and superseding them without a proof audit risks destroying the intellectual provenance. The claim ledger distinguishes them.
- July `docs/mathematical_status.md` and dated research logs: immutable historical status; new claims belong in dated registers.

## Application relocation

The entire source/data subtrees for `barnette`, `berge_fulkerson`, `three_decomposition`, `tutte_5flow`, `edge_partitioning`, and `open_problem_garden` moved into `applications/`. The general `certificate_coordination/` and `shared/` packages remain at root. Historical internal text may still reference the old layout; run current commands from `README.md`, `Makefile`, and project READMEs.

## Acceptance checks

Run `python -m pytest -q`, `make reproduce-small`, `make reproduce-cpp`, and `python -m pip install --no-deps --no-build-isolation -e . (when offline and build dependencies are installed)` on a fresh checkout. The checksum manifest may be regenerated after modifying inputs and outputs.
