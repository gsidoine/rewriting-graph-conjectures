# Methodology: Local Rewriting and Relative Termination

The common research object is not merely a graph but a **certificate state**:

- a sextuple of perfect matchings for Berge–Fulkerson;
- a spanning tree for 3-Decomposition;
- a binary colouring of the dual triangulation for Barnette.

Each state receives an exact nonnegative defect.  A target has defect zero.  Local rewrites preserve feasibility and are classified as:

- **strict:** defect decreases;
- **neutral:** defect is unchanged;
- **forbidden:** defect increases.

The central dynamical question is relative termination: does every state reach a target using only strict and neutral rewrites?  On a finite state space this is equivalent to the absence of a closed terminal strongly connected component at positive defect.

The research cycle is:

1. derive exact local change identities;
2. prove universally safe rewrites;
3. enumerate small state spaces and reverse-reachable targets;
4. extract terminal components when a rule fails;
5. turn the failure into a counterexample, structural lemma, complexity theorem, or enlarged rule set;
6. repeat at the first unresolved defect layer.

Computations are discovery and finite verification tools, not substitutes for universal proofs.  Every exact computational statement in the repository has a status, input, source, output, and—where feasible—an independent checker.
