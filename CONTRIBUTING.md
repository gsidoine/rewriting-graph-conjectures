# Contributing

Contributions should preserve the distinction between proof, finite computation, conjecture, heuristic, and historical evidence.

1. Add or update a row in `docs/mathematical_status.md` for every nontrivial claim.
2. Supply a deterministic verifier and a machine-readable certificate for computational claims.
3. Add a regression test for every bug or corrected counterexample.
4. Do not strengthen novelty language without a documented literature search.
5. Build all papers with `latexmk`, not a single `pdflatex` pass.

For large enumerations, include a small smoke-test instance in CI and archive the full command, compiler version, runtime, peak memory, and SHA-256 checksums.
