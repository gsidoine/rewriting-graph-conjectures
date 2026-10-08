# Research Log

## Target A: 3-Edge-Coloring Conjecture

**Question.** Does every connected 3-edge-colourable cubic graph with more than two vertices contain an edge whose deletion and suppression of the two degree-two vertices is again 3-edge-colourable?

**Reformulation.** In flow language, does every cubic graph with a nowhere-zero 4-flow have a 4-removable edge?

**Current frontier.** Recent work proves the conjecture for bipartite cubic graphs and proves that every cubic graph with a nowhere-zero 4-flow has a nonempty 4-removable set of size at most `|E|/6`.  The local-rewrite gap is therefore: compress a bounded removable set to one edge while preserving a 4-flow.

**Finite experiment.** `candidate_1/removable_edge_finite_check.py` checks every connected simple cubic class through ten vertices in the supplied 27-graph catalogue.  Of these, 25 are 3-edge-colourable, and every one has a removable edge.  The minimum number of removable edges over these classes is six.

**Structural attempt.** Fix a 3-edge-colouring and delete one edge of colour 0.  Suppression creates two replacement edges whose colour constraints are determined by the two missing-colour pairs at the endpoints.  A Kempe-cycle exchange can alter these constraints only along alternating two-colour cycles.  The obstruction can therefore be encoded as a parity/compatibility condition on the two alternating-cycle systems through an edge.  The pass did not prove that some edge always has compatible systems; this is the precise remaining local lemma.

**Verdict.** No proof or disproof.  The finite verifier and compatibility formulation are retained as a starting point.

## Target B: Matching Cut and Girth

The natural defect of a bipartition is the number of vertices incident with at least two crossing edges.  Flipping a vertex changes this defect locally, but a zero-defect state may be trivial (one side empty) and expansion constraints at high girth are global.  Averaging gives useful sparse-cut candidates when average degree is below three, consistent with known extremal results, but the attempted local potential did not yield a bound for arbitrary fixed `d`.

**Verdict.** The approach reached a genuine blocker: local flips alone do not control nontriviality of both sides or the global matching-cut condition.  No new theorem is claimed.

## Final target: 3-Decomposition

The programme's strongest substantial result facing a listed open problem is not a solution but a restriction theorem on proof strategy:

- fixed-cycle one-defect repair is false on an explicit 16-vertex graph;
- the corresponding promised completion problem is NP-complete;
- therefore a successful normalization proof must permit the cycle part to change.

This is the final target because it combines a universal defect identity, safe local moves, complete small-state evidence, a concrete obstruction, and a theorem that explains why the failed route is intrinsically difficult.
