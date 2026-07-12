# Computational Claims and Certificates

## Reproducible now

### Python checks

Run `make reproduce-small`.  The extracted scripts are literal notebook-code reconstructions with deterministic seeds where randomness occurs.

- `bf_quadratic_checks.py`: symbolic/finite verification of the replacement and aggregate identities.
- `blossom_certificate.py`: exact 16-vertex obstruction and all matching counts.
- `three_decomposition_exhaustive.py`: all 27 connected simple cubic graph classes through ten vertices and all 30,619 spanning trees.
- `combined_checks.py`: Barnette cube identity, explicit 36-vertex escape, expectation formulas, Petersen normalization.
- `other_conjectures_checks.py`: smaller generated Barnette sample.

### C++ checks

Run `make reproduce-cpp`.

- `j5_rewrite.cpp` performs exact reverse reachability on all 2,324,784 multisets of six perfect matchings of the supplied standard Flower snark `J5` instance.
- `test_barnette_k.cpp` reruns the selected 30-instance `steps8` batch.

## Historical only

- `barnette_big.txt` / `barnette_results_historical.txt`: large complete-colouring runs.  Preserved but not fully repeated in this audit.
- `bfr_results_all_historical.txt` and `bip_results_historical.txt`: large perfect-matching state-space logs.  Preserved; generator reconstruction is incomplete.
- `step10_unresolved_historical.txt`: inconsistent with the supplied `step10.txt` instance under the archived verifier's potential.  Never use as a verified certificate.

## Certificate policy

A future full run should emit:

1. canonical graph encoding or exact edge list;
2. state encoding specification;
3. result JSON;
4. source and binary SHA-256;
5. compiler/interpreter versions;
6. wall time and peak memory;
7. a separate checker that validates the result without repeating the search when possible.
