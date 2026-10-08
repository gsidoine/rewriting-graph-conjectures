"""Exact direct-repair width via (k+1)-coordinate collision hypergraphs.

Given t=kd perfect-matching coordinates of a d-regular bipartite graph,
`signatures` lists the sets of indices currently using each graph edge.
This module is independent of graph libraries and numerical optimization.

For a non-bipartite host, `minimum_repair` is only a lower bound unless
residual edge-colourability is separately certified.
"""
from __future__ import annotations
from itertools import combinations


def collision_edges(signatures, k: int):
    """Generate the (k+1)-subsets contained in any edge signature.

    May take time polynomial of degree k+1 for fixed k; prefer
    `repair_with_budget` for large signatures since it branches implicitly.
    """
    assert k >= 1
    return tuple(sorted({tuple(H) for S in signatures
                         for H in combinations(sorted(set(S)), k + 1)}))


def repair_with_budget(signatures, k: int, t: int, budget: int):
    """Find <= budget changed coordinates satisfying frozen multiplicity<=k.

    Deterministic bounded-depth branching. A violating signature supplies a
    (k+1)-subset, at least one of whose indices MUST be selected.
    Returns a sorted tuple of selected coordinate indices, or None.
    """
    assert k >= 1 and t >= 1 and 0 <= budget <= t
    sets = tuple(frozenset(S) for S in signatures)
    assert all(all(isinstance(x,int) and 0 <= x < t for x in S) for S in sets)

    def branch(selected: frozenset[int], remaining: int):
        violating = next((S - selected for S in sets if len(S - selected) > k), None)
        if violating is None:
            return tuple(sorted(selected))
        if remaining == 0:
            return None
        # Every feasible repair must hit this (k+1)-subset.
        witness = sorted(violating)[:k + 1]
        for index in witness:
            solution = branch(selected | {index}, remaining - 1)
            if solution is not None:
                return solution
        return None
    return branch(frozenset(), budget)


def minimum_repair(signatures, k: int, t: int):
    """Exact minimum direct-repair width for a bipartite multicover.

    Return (width, indices). Complexity O((k+1)^width poly(input size))
    when k is fixed. Valid for arbitrary surplus multiplicities.
    """
    S = tuple(tuple(s) for s in signatures)
    for r in range(t + 1):
        indices = repair_with_budget(S,k,t,r)
        if indices is not None:
            return r,indices
    raise AssertionError('All coordinates can always be unfrozen')


def verify_repair(signatures, k: int, t: int, indices):
    """Check frozen-multiplicity criterion, independently of the search."""
    J = set(range(t)) - set(indices)
    return all(len(set(S) & J) <= k for S in signatures)


def signatures_from_permutations(permutations):
    """Edge signatures of matchings in K_(d,d), each encoded by a permutation."""
    perms = [tuple(p) for p in permutations]
    assert perms
    d=len(perms[0]);out={}
    for i,p in enumerate(perms):
        assert sorted(p)==list(range(d))
        for a,b in enumerate(p):out.setdefault((a,b),set()).add(i)
    return tuple(out.values())
