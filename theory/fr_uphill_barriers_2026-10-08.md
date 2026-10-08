# Fan–Raspaud states: non-monotone reconfiguration and amplified uphill barriers

**8 October 2026 · proved research draft with an exhaustive finite base certificate; novelty unverified.**

## Structural result

The potential `u` is the number of edges uncovered by a triple of perfect matchings with empty total intersection. We study moves replacing one coordinate while maintaining the empty intersection. At every FR-state, `Q=sum_e(m(e)-1)^2=2u`.

There is a ten-vertex **3-edge-connected, 3-edge-colourable** cubic graph with an FR-triple at `u=3` whose six distinct legal single-coordinate neighbours **all** have `u=4`; nevertheless `3 -> 4 -> 3 -> 0` is a valid path. The complete graph, all six perfect matchings, and path are verified in `applications/berge_fulkerson/plateau/energy_barriers/`.

Using balanced all-vertex replacement by the `K_{3,2}` three-pole, for every `t>=0` one obtains a simple 3-edge-connected class-one cubic graph on `10*5^t` vertices with an FR-triple at `u=3**(t+1)` such that **every** normalization path must pass through `u>=4*3**t`. Such a path always exists. Hence the required *absolute* temporary increase is at least `3**t`, unbounded as graph order grows. No linear-in-order lower bound is claimed (`3**t = Theta(|V|^{log_5 3})`).

## Why the lift works

Each pair of internal vertices in a `K_{3,2}` gadget must be matched to two of the three ports. Thus **exactly one external edge per gadget** occurs in every perfect matching; projection back to the host is well-defined. A local FR incidence pattern is either `(1,1,1)` or `(2,1,0)`. For each uncovered external edge, both endpoints have pattern `(2,1,0)` and each forces at least one further uncovered internal edge. Hence `u_expanded >= 3*u_projected`. Independent choices of the two completions of each gadget realize equality for a prescribed FR triple, and any base FR move admits a lift from any FR preimage. The corresponding vertex splice with `K_{3,3}` preserves 3-edge-connectivity; proper 3-edge-colourings lift.

Ordinary vertex-to-triangle expansion is **not suitable**: a perfect matching may use all three exterior edges at the triangle, so there is no bijection of perfect matchings or a correct projection to a single old matching.

## Research impact and next targets

The theorem **falsifies monotone normalization for FR triples even on class-one, 3-edge-connected cubic graphs**. It offers one exact, nontrivial application of obstruction-guided graph rewriting and supplies scalable quantitative barriers. It does *not* imply a counterexample to either major cubic conjecture (the hosts are themselves class one).

Possible next targets are characterizing sublevel-set components under small separators, deciding whether minimal barrier is fixed-parameter tractable in defect, and strengthening lower bounds to linear in graph order under stronger girth/cyclic-connectivity constraints.

See the complete paper at [`applications/berge_fulkerson/plateau/energy_barriers/paper/main.tex`](../applications/berge_fulkerson/plateau/energy_barriers/paper/main.tex), plus the dependency-free checker and machine-readable certificates.
