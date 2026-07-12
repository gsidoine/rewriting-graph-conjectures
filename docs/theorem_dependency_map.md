# Theorem Dependency Map

## Berge–Fulkerson

```text
Perfect-matching polytope fact
        + replacement identity
        -> coordinate inequality S_i <= n/3
        + sum_i S_i = Q
        -> universal barrier Q <= 2n at local minima
        + Q <= 12n and parity
        -> at most 5n strict descent steps

relative interior at x=1/3
        + affine-hull/adjacency argument
        -> S_i < n/3 in the nonbipartite cyclically-4-edge-connected case
        -> residue-dependent strict barrier

local multiplicity classification
        -> alternating defect cycles
        + 4-cycle repair
        -> lower local-minimum barrier Q >= 6
```

## 3-Decomposition

```text
cubic degree accounting
        -> cotree has maximum degree 2
        -> b(T)=0 iff 3-decomposition
        -> |D(T)|=2b(T)

fundamental-cycle basis exchanges
        -> endpoint leaf-slide / tail-peel are safe
        -> Monotone Exchange Conjecture
        -> would imply 3-Decomposition

fixed-cycle repair proposal
        -> explicit 16-vertex disproof
        + Hamiltonian fairly cubic source problem
        -> Near-Unicyclic Matching Decycling NP-complete
        -> fixed-cycle repair NP-complete
        -> cycle-flexible normalization required
```

## Barnette

```text
classical dual two-tree equivalence
        + bichromatic-edge primal subgraph
        + Euler formula and Jordan separation
        -> Phi = z + 2(t-1)
        -> Phi=0 iff Hamiltonian

connected patch flips
        + finite reverse reachability
        -> radius-two obstruction evidence
        -> three-face normalization conjecture
        -> Phi=2 escape frontier
```
