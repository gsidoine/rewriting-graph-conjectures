"""Exact finite checks for support-Cayley rigidity and Kempe counterexamples."""
from itertools import combinations
import networkx as nx
from applications.edge_coloring_rigidity import (
    rigid_family, proper_colorings, distance, components,
    budget_graph, color_orbits, kempe_graph, matching_partition_oracle)


def test_inflated_k4_phases_and_edge_repair():
    for k in range(7):
        G = rigid_family(k)
        n = len(G)
        E, S = proper_colorings(G)
        assert n == 4 + 2*k and len(E) == 3*n//2 and len(S) == 6
        assert all(d == 3 for _, d in G.degree())
        assert nx.check_planarity(G)[0] and nx.edge_connectivity(G) == 3
        assert all(distance(S[i], S[j]) in (n, 3*n//2)
                   for i, j in combinations(range(6), 2))
        assert sorted(map(len, components(budget_graph(S, n-1)))) == [1]*6
        assert sorted(map(len, components(budget_graph(S, n)))) == [6]
        assert sorted(map(len, components(kempe_graph(G,E,S)))) == [6]
        adj = budget_graph(S, n)
        assert sorted(map(len, adj)) == [3]*6
        assert nx.is_bipartite(nx.Graph([(i, j) for i in range(6) for j in adj[i]]))
        for s in S:
            for j in range(len(E)):
                for target in range(3):
                    cost = min(distance(s,t) for t in S if t[j] == target)
                    assert cost == (0 if s[j] == target else n)
        for a, b in combinations(range(3), 2):
            H = nx.Graph()
            H.add_edges_from(E[j] for j,c in enumerate(S[0]) if c in (a,b))
            assert len(H) == n and nx.is_connected(H)
            assert all(d == 2 for _, d in H.degree())


def test_independent_perfect_matching_partition_oracle():
    for k in range(5):
        G = rigid_family(k)
        assert (lambda a,b: a[0] == b[0] and set(a[1]) == b[1])(
            proper_colorings(G), matching_partition_oracle(G))
    for G in (nx.complete_bipartite_graph(3,3), nx.cubical_graph()):
        E,S = proper_colorings(G)
        F,T = matching_partition_oracle(G)
        assert E == F and set(S) == T


def test_k33_same_support_different_kempe_accessibility():
    G = nx.complete_bipartite_graph(3,3)
    E,S = proper_colorings(G)
    assert len(S) == 12
    orbits = color_orbits(S)
    kempe_components = components(kempe_graph(G,E,S))
    assert sorted(map(len, orbits)) == [6,6]
    assert {frozenset(o) for o in orbits} == {
        frozenset(c) for c in kempe_components}
    assert sorted(map(len, components(budget_graph(S,5)))) == [1]*12
    assert sorted(map(len, components(budget_graph(S,6)))) == [12]
    within = across = 0
    for i,j in combinations(range(12),2):
        if distance(S[i],S[j]) != 6: continue
        same = any(i in c and j in c for c in kempe_components)
        within += int(same); across += int(not same)
    assert (within, across) == (18, 36)


def test_cube_is_not_a_single_global_color_orbit():
    G = nx.cubical_graph()
    E,S = proper_colorings(G)
    assert len(S) == 24
    assert sorted(map(len, color_orbits(S))) == [6]*4
    assert sorted(map(len, components(kempe_graph(G,E,S)))) == [24]
    assert sorted(map(len, components(budget_graph(S,3)))) == [1]*24
    assert sorted(map(len, components(budget_graph(S,4)))) == [24]
