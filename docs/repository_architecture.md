# Repository architecture and versioning policy

## Two research tracks

The central navigation uses [`theory/`](../theory/) and [`applications/`](../applications/). Existing importable code remains at stable locations such as `certificate_coordination/` and `berge_fulkerson/plateau/`. We intentionally did not relocate import paths or duplicate modules just to make the directory tree aesthetically symmetric.

* `theory/`: general mechanisms — certificate coordination, multiplicity, obstruction hypergraphs, exact repair, strict and neutral rewriting, dynamic programming, separator interfaces.
* `applications/`: problem-facing experiments — Berge–Fulkerson, 3-Decomposition, Barnette, Tutte 5-flow, edge-connectivity partitioning.
* `docs/`: theorem/claim ledger, audit summaries, methodological notes, reproducibility and literature.
* `archive/`: older historical or inconsistent logs, preserved to avoid hiding negative evidence.
* `tests/`, `repro_runs/`: checks and independent reproduction scripts.
* `publications/` and per-project `paper/`: LaTeX research drafts and pre-existing compiled PDF snapshots. None of the October drafts is described as journal-accepted.

## Versions, snapshots and permanence

- Preserve historical commits; use new commits and branches rather than rewriting history.
- The July `RELEASE_NOTES.md` and `docs/mathematical_status.md` retain their historical audit date.
- Put later results in separate dated documents and dedicated research directories, with distinct claim statuses.
- Commit self-contained finite input datasets, scripts and compact verifiers. Keep large intermediate datasets out of routine CI.
- Store compiled PDFs alongside sources as reproducible convenience snapshots, but use `.tex` as the editable authority.
- Never silently promote a computational claim to an infinite theorem or a proof draft to independently established novel work.

## Fast verification

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

For additional exact exhaustions follow each research directory README; many are intentionally excluded from normal CI.
