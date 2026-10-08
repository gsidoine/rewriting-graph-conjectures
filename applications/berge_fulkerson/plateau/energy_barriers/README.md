# Fan–Raspaud reconfiguration: unbounded uphill barriers

**Status (8 October 2026): mathematical research draft with a complete combinatorial proof and an exact finite certificate; external originality unverified.** This does not solve Berge–Fulkerson or Fan–Raspaud.

## Main result

For every integer `t >= 0` there is a **simple, 3-edge-connected, 3-edge-colourable cubic graph** `G_t` and an FR-triple with

- `|V(G_t)| = 10*5**t`,
- initial uncovered-edge count `u_t = 3**(t+1)`,
- every FR-preserving sequence of one-coordinate perfect-matching replacements reaching `u=0` must visit a state with `u >= 4*3**t`,
- some normalization path exists.

Therefore the unavoidable uphill barrier `max(u)-u_start` is at least `3**t`. The statement also applies to quadratic coverage defect `Q=2u`.

## Proof and certificates

- [`paper/main.tex`](paper/main.tex) and [`paper/main.pdf`](paper/main.pdf): five-page complete proof draft.
- [`ten_vertex_witness.json`](ten_vertex_witness.json): the minimal seed used in the proof, with its explicit `3 -> 4 -> 3 -> 0` escape.
- [`flower_host24_witness.json`](flower_host24_witness.json): independent 24-vertex barrier, with an exact 36-state isolated sublevel-3 component and path `3 -> 4 -> 3 -> 2 -> 0`.
- [`standalone_audit.py`](standalone_audit.py): **dependency-free** enumeration of every perfect matching and every FR-triple, full sublevel graph connectivity, exact paths, and connectivity after every deletion of up to two edges.
- [`balanced_lift.py`](balanced_lift.py): constructive balanced `K_{3,2}` vertex substitutions and equality-attaining FR lifts; internal gadget constraints are separately exhaustively tested.
- [`tests/test_fr_energy_barriers.py`](../../../../tests/test_fr_energy_barriers.py): four repeatable tests. (Root-level `tests` is used.)

From repository root:

```bash
python applications/berge_fulkerson/plateau/energy_barriers/standalone_audit.py
python -m pytest -q tests/test_fr_energy_barriers.py
```

A nontrivial point: *triangle expansion is not an exact perfect-matching projection*. A triangle can match all three exterior edges, so naive claims of reconfiguration-graph isomorphism are false. The balanced `K_{3,2}` three-pole fixes projection, and yields **an inequality** `u_new >= 3*u_projected` for every FR-triple, plus a lift attaining equality. The proof does not incorrectly assert an isomorphism of state graphs.

### Novelty boundary

Colouring defect and triples of perfect matchings are established subjects (Karabáš, Máčajová, Nedela and Škoviera, E-JC 2024; Allie, Discrete Mathematics 2026). Perfect-matching *alternating-square flip* reconfiguration is also well developed (Bonamy et al., 2019). Our moves replace whole perfect-matching coordinates. The exact uphill-barrier theorem should be subjected to specialist literature review before submission.
