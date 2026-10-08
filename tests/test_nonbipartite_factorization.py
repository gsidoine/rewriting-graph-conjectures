"""Exact two-coordinate factorization obstruction on the triangular prism."""
from itertools import combinations
from certificate_coordination.collision_hypergraph import collision_edges, minimum_repair


def all_pm(n, edges):
    result=[]
    for I in combinations(range(len(edges)),n//2):
        v=[x for j in I for x in edges[j]]
        if len(set(v))==n:
            result.append(frozenset(I))
    return result


def test_triangular_prism_collision_vs_factorization():
    n=6
    E=[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
    vertical=frozenset([6,7,8])
    matchings=all_pm(n,E)
    assert vertical in matchings and len(matchings)==4
    # Start with three identical copies of the vertical perfect matching.
    original=[vertical]*3
    S=[tuple(i for i,M in enumerate(original) if e in M) for e in range(len(E))]
    width,chosen=minimum_repair(S,1,3)
    assert width==2 and len(collision_edges(S,1))==3
    # All size-two coordinate replacements freeze one vertical matching.
    # The horizontal edges form two triangles and cannot split into 2 PMs.
    assert not any(A.isdisjoint(vertical) and B.isdisjoint(vertical) and A.isdisjoint(B)
                   for A in matchings for B in matchings)
    # However the graph is class I: it has a 1-fold 3-perfect-matching cover.
    exact=[C for C in combinations(matchings,3)
           if len(set().union(*C))==len(E) and sum(len(M) for M in C)==len(E)]
    assert exact
    assert sum(len(M) for M in exact[0])==9
