# Theorem-first research programme: local and neutral reconfiguration

**Decision date:** 2026-10-08. This programme replaces the previous open-conjecture-first iteration of progressively narrower finite bounds.

## Research objective

Develop transferable structure theorems for a pair `(S,D)` consisting of a finite graph-certificate state space `S` and an exact integer-valued defect `D`, together with strict moves (`D` decreases) and neutral moves (`D` is preserved). Study the neutral connected components inside defect levels, effective boundary summaries, strict-escape distances, and the obstructions that arise when the intended quotient forgets relevant information.

**Two anchor applications:**

1. Labelled cycle-double-cover sheets, neutral symmetric-difference cycle switches, strict four-to-three compression.
2. Multiplicity-two perfect-matching multicovers, neutral alternating-cycle switches, and multi-coordinate direct repair.

The first shared structure theorem is [three-edge-cut synchronization](../theory/three_cut_synchronized_reconfiguration_2026-10-08.md). Its strongest assumption, connected signature fibers, is explicitly *false*: [K3,3 has disconnected fibers in both applications](../theory/k33_neutral_fiber_obstructions_2026-10-08.md).

## Revised proof target (nontrivial)

For cubic graphs assembled by three-edge sums, develop **component-enriched typed boundary automata**. State a corrected theorem of the form:

> For a graph family with bounded separator size and a bounded number of certificate coordinates, neutral-reachability components and the minimum boundary-change cost to strict escape are completely determined by a finite algebra of *boundary-signature plus local neutral-component* responses.

One must prove a uniform bound on the number of local components (or impose and verify a genuinely meaningful structural hypothesis); this **does not follow** from bounded cut size alone.

Theorem-first stopping criterion: no claim of substantial progress until we have either (i) a new infinite-family classification, (ii) a transfer theorem whose hypotheses are verified in two independent certificate systems beyond trivial examples, or (iii) a sharp certified obstruction to a published/explicit general hypothesis.

## Falsification programme

* Enumerate local signature fibers in small capped cubic shores. The full K3,3 classifications (2 disconnected CDC states; 1+8+1 matching-cover states) are permanent regression tests.
* Enumerate *typed* boundary transitions: which pairs of labels and which pair of ports are switched? Untyped graph intersections can hallucinate moves.
* Construct three-edge sums with a prescribed mismatch of component indices, to test whether a component-enriched state is sufficient.
* Determine whether the response set or number of components can grow unboundedly even for a fixed q and fixed cut size. A single unbounded family rules out naive constant-state dynamic programming.
* Derive composition rules for terminal strongly connected components and strict-escape radius; benchmark against existing matching-reconfiguration and Kempe-equivalence literature.
* Check relevance to general graphs of high cyclic edge-connectivity; do not infer major-conjecture progress from oddness<=4 examples where 5-CDC existence is already known.

## Proof audit and novelty policy

Every statement must be tagged as proof draft, independently checked finite claim, falsified conjecture, or open. A correct low-dimensional counting argument alone is not necessarily new or publication worthy.

Required comparison: Marcin Wrochna (2018), reconfiguration hardness even at bounded bandwidth; recent Kempe-equivalence literature including Chakraborty–Feghali–Mahmoud (2024); Catlin decomposition / snark reduction; Liu et al. (2023) on 5-CDC and 4-flows. Do not promise a polynomial algorithm merely because the cut alphabet has 336 or 90 elements: the number of *fiber components* can be greater than one and may be large.

## Success metric

A journal-worthy candidate should imply a nontrivial result for an unbounded graph family or unify two genuinely different certificate systems with strong, verified hypotheses. Small graph enumerations supply adversarial tests, not the central theorem.


## First full theorem candidate — exact exponential neutral classes (8 October)

[Uniform-multiplicity K3,3 amplification](../theory/exponential_neutral_components_multicovers_2026-10-08.md) gives an *exact* two-parameter result: for `m>=1`, `n>=1`, the six-matching system at `m=2` and all `3m`-matching `m`-fold systems have `(m+1)^n` neutral components on a simple 3-edge-connected bipartite cubic `4n+2`-vertex graph. Even fixing the entire boundary signature does not reduce the count. Component sizes are explicit binomial products, with totals involving Franel numbers.

**Research pivot update:** no uniform *constant* bound on neutral-component refinements from fixed boundary size and coordinate count is possible. Seek factorized/semigroup state representations with bounded local generating sets instead. Independent novelty checking remains required; m=1 is the known Belcastro--Haas edge-Kempe result.
