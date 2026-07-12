# The Research Programme

## Central idea

Many graph conjectures ask whether every graph in a class possesses a global certificate: a family of perfect matchings, a constrained spanning tree, a Hamiltonian cycle, or an equivalent colouring. A direct search for the target certificate often hides the geometry of the obstruction.

This programme replaces the bare existence question with a dynamical one.

1. **Choose a certificate state.** The state should remain feasible under elementary local changes.
2. **Define an exact nonnegative defect.** Defect zero must coincide with the desired certificate.
3. **Derive local change formulae.** A rewrite should have a computable effect on the defect.
4. **Separate descent from plateau motion.** Strict moves lower the defect; neutral moves reveal the geometry of local minima.
5. **Analyze relative termination.** On finite state spaces, reverse reachability and terminal strongly connected components test whether every state can normalize without increasing the defect.
6. **Treat failure as data.** A terminal component may expose a false lemma, a missing move, a rigid low-defect configuration, or a computationally hard subproblem.
7. **Return to proof.** Computation suggests the right theorem, but universal claims require mathematical proof or independently checkable certificates.

## Why this is related to rewriting-Collatz

The rewriting-Collatz project turns Collatz-like maps into formal string-rewriting systems and applies automated termination techniques. This graph programme does not reuse those rewrite rules or claim that graph basis exchanges are string rewrites. The shared research pattern is:

- encode the conjecture as normalization;
- search for ranking functions or defects;
- automate the search for local proof steps;
- investigate relative termination rather than only greedy descent;
- extract mathematical information from failed termination attempts.

The graph setting adds a distinct feature: the states often form classical reconfiguration spaces, such as basis-exchange graphs or products of perfect-matching polytopes. This allows graph structure, polyhedral arguments, and exact state-space computation to interact.

## What counts as progress

The programme recognizes several legitimate outputs:

- a full normalization theorem;
- a quantitative descent barrier;
- a low-defect classification;
- a stronger conjecture that explains the dynamics;
- an exact counterexample to an appealing but false local principle;
- a complexity theorem showing that a restricted repair model is intrinsically hard;
- a finite verification accompanied by reproducible certificates.

A failed attempt is not presented as a theorem. It is retained when it narrows the design space of possible proofs.

## Current programme map

| Programme | State | Defect-zero target | Rewrite mechanism | Present frontier |
|---|---|---|---|---|
| Berge-Fulkerson | Six perfect matchings | Every edge has multiplicity two | Replace one perfect matching | Classify or eliminate low-`Q` local minima |
| 3-Decomposition | A spanning tree | Cotree is cycles plus a matching | Basis exchange | Prove plateau exit or understand minimal terminal plateaux |
| Barnette | Binary dual colouring | Two induced trees / Hamiltonian primal cycle | Connected patch flip | Prove three-face normalization, beginning at potential two |
| Tutte 5-Flow | Residual flow state | Feasible nowhere-zero flow | Residual/cycle adjustment | Exploratory only |

## Standards used in this repository

Every substantial statement is marked as a theorem, reproducible computation, historical log, conjecture, disproof, heuristic, or open gap. Exact inputs and outputs are versioned. The repository does not silently upgrade experiments into universal mathematics.
