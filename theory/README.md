# Track A — General certificate-coordination theory

**Purpose.** Study exact repair width, strict/neutral reconfiguration, obstruction hypergraphs, and finite separator interfaces independently of particular open graph conjectures.

The implementations stay at their original import-compatible package paths. This directory is a stable navigational layer; the research modules are linked below, not silently renamed or duplicated.

| Workstream | Code and certificates | Paper and status |
|---|---|---|
| Multiplicity-2 six-matching repair/plateaux | [`berge_fulkerson/plateau/`](../berge_fulkerson/plateau/) | [paper source](../berge_fulkerson/plateau/paper/main.tex), [readme](../berge_fulkerson/plateau/README.md) |
| Sharp direct-repair thresholds / local drift | [`berge_fulkerson/plateau/next_phase/`](../berge_fulkerson/plateau/next_phase/) | [notes](../berge_fulkerson/plateau/next_phase/README.md) |
| Three-cut gluing, componentwise corrections | [`berge_fulkerson/plateau/next_phase/continuation_20261008/`](../berge_fulkerson/plateau/next_phase/continuation_20261008/) | [claim status](../berge_fulkerson/plateau/next_phase/continuation_20261008/CLAIM_STATUS.md) |
| Obstruction conflicts, variable-degree systems | [`certificate_coordination/`](../certificate_coordination/) | [v7 proof](../certificate_coordination/paper/main.tex), [status](../certificate_coordination/RESEARCH_STATUS.md) |
| Complete-bipartite hypergraph universality, multiplicity `k`, width-DP | [`certificate_coordination/v8/`](../certificate_coordination/v8/) | [v8 proof](../certificate_coordination/v8/paper/main.tex), [status](../certificate_coordination/v8/README.md) |

## Primary definitions

For a tuple of `kd` perfect matchings in a `d`-regular bipartite graph, the target is multiplicity `k` on every edge, with defect `Q_k = sum_e (m(e)-k)^2`. **Direct-repair width** is the fewest labelled coordinates replaced at once to reach zero. **Strict reconfiguration distance** is the shortest sequence of one-coordinate changes strictly decreasing `Q_k` at every move; infinity is allowed. These parameters are not interchangeable.

## Research integrity

- Proofs in October 2026 manuscripts are **research drafts**, with independently executable finite checks but no formal Lean kernel checking, journal refereeing, or comprehensive specialist novelty audit.
- Statements proved by finite code are **finite computational results**, not infinite theorems.
- Results for variable degree (and `kd` coordinates) must **not** be projected to the fixed cubic six-matching conjectures.
- To reproduce: run `python -m pytest -q`; then follow the `README.md` in each workstream for independent certificate programs.

See [current claim register](../docs/claim_register_oct2026.md) for a cross-project classification.
