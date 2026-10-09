"""Small independent pair-rigid tile checks, using networkx.
Run: pytest -q tests/test_pair_rigid_tile_algebra.py
"""
import itertools
import networkx as nx


def matchings(g):
    matches=[]
    def rec(U,chosen):
        if not U:
            matches.append(frozenset(chosen))
            return
        v=min(U)
        for w in g[v]:
            if w in U:
                rec(U-{v,w},chosen+[tuple(sorted((v,w)))])
    rec(set(g),[])
    return matches


def xor_components(A,B):
    graph=nx.Graph()
    graph.add_edges_from(A^B)
    return list(nx.connected_components(graph))


def test_k33_and_petersen_are_pair_rigid():
    for g,expected in ((nx.complete_bipartite_graph(3,3),6),(nx.petersen_graph(),6)):
        P=matchings(g)
        assert len(P)==expected
        assert all(len(xor_components(a,b))==1 for a,b in itertools.combinations(P,2))
        assert nx.edge_connectivity(g)==3


def test_petersen_incidence_forces_even_multiplicity():
    g=nx.petersen_graph()
    P=matchings(g)
    assert len(P)==6
    edge_owners={tuple(sorted(e)):frozenset(i for i,M in enumerate(P) if tuple(sorted(e)) in M) for e in g.edges()}
    assert all(len(owners)==2 for owners in edge_owners.values())
    assert set(edge_owners.values())=={frozenset(x) for x in itertools.combinations(range(6),2)}
    for m in range(1,6):
        solutions=[v for v in itertools.product(range(m+1),repeat=6)
                   if all(v[i]+v[j]==m for i,j in itertools.combinations(range(6),2))]
        assert solutions==([(m//2,)*6] if m%2==0 else [])


def test_cube_pair_rigidity_fails_by_valid_partial_switch():
    g=nx.cubical_graph()
    P=matchings(g)
    assert len(P)==9
    a,b=next((a,b) for a,b in itertools.combinations(P,2) if len(xor_components(a,b))==2)
    component=next(iter(xor_components(a,b)))
    C=frozenset(tuple(sorted(e)) for e in g.edges() if e[0] in component and e[1] in component and tuple(sorted(e)) in (a^b))
    aa=a^C
    bb=b^C
    assert aa in P and bb in P
    assert {aa,bb}!={a,b}
    assert (a&b)==(aa&bb) and (a|b)==(aa|bb)
