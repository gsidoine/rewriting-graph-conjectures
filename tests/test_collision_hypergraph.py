"""Independent brute-force cross-checks for the collision-hypergraph theorem."""
from itertools import combinations
from random import Random
from certificate_coordination.collision_hypergraph import (
    collision_edges,repair_with_budget,minimum_repair,verify_repair,
    signatures_from_permutations,
)


def brute(signatures,k,t):
    for r in range(t+1):
        for I in combinations(range(t),r):
            if verify_repair(signatures,k,t,I):return r,I
    raise AssertionError


def test_all_small_arbitrary_incidence():
    rng=Random(8112026)
    for k in (1,2,3):
        for t in range(k+1,9):
            for _ in range(35):
                S=[tuple(i for i in range(t) if rng.random()<0.5)
                   for j in range(rng.randrange(2,11))]
                b,w=brute(S,k,t)
                got,I=minimum_repair(S,k,t)
                assert got==b and verify_repair(S,k,t,I)
                assert repair_with_budget(S,k,t,b-1) is None if b else True
                C=collision_edges(S,k)
                assert all(set(I)&set(H) for H in C)


def test_actual_random_perfect_matching_tuples():
    rng=Random(8082026)
    for k in (1,2):
        for d in (3,4):
            for _ in range(30):
                perms=[]
                for i in range(k*d):
                    a=list(range(d));rng.shuffle(a);perms.append(a)
                S=signatures_from_permutations(perms)
                b,_=brute(S,k,k*d)
                opt,I=minimum_repair(S,k,k*d)
                assert opt==b
                assert verify_repair(S,k,k*d,I)


def test_complete_bipartite_universality_instances():
    from certificate_coordination.v8.complete_bipartite_realization import construct_complete
    from certificate_coordination.v8.hypergraph_realization import hypergraph_from_graph_edges, min_transversal
    for k in (1,2,3):
        h,F=hypergraph_from_graph_edges(4,[(0,1),(1,2),(2,3)],k)
        data=construct_complete(h,F,k)
        S=signatures_from_permutations(data['permutations'])
        width,I=minimum_repair(S,k,data['t'])
        assert width==len(min_transversal(h,F))==2
        assert verify_repair(S,k,data['t'],I)


def test_collision_uniformity_at_high_multiplicity():
    # A 5-covered edge with k=2 requires 3 deletions: all triples must be hit.
    S=[(0,1,2,3,4)]
    assert len(collision_edges(S,2))==10
    assert minimum_repair(S,2,6)[0]==3
