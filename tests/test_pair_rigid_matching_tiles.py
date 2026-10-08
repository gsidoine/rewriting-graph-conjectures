"""Local rigidity, multiplicity parity, and a sharp non-rigid obstruction.

Independent tests; NetworkX is already a repository requirement.
Run: python -m pytest -q tests/test_pair_rigid_matching_tiles.py
"""
from itertools import product
import networkx as nx


def all_perfect_matchings(G):
    def find(rest, selected):
        if not rest:
            yield frozenset(selected)
            return
        a = min(rest)
        for b in G[a]:
            if b in rest:
                e = frozenset((a, b))
                yield from find(rest - {a, b}, selected | {e})
    return list(find(frozenset(G), set()))


def diff_components(A, B):
    H = nx.Graph()
    for edge in (A ^ B):
        x, y = tuple(edge)
        H.add_edge(x, y)
    return list(nx.connected_components(H))


def test_pair_rigid_petersen_and_k33():
    for G, expected in ((nx.petersen_graph(), 6),
                        (nx.complete_bipartite_graph(3, 3), 6)):
        pm = all_perfect_matchings(G)
        assert len(pm) == expected
        for i in range(len(pm)):
            for j in range(i):
                assert len(diff_components(pm[i], pm[j])) == 1


def test_petersen_covering_multiplicity_requires_even_m():
    G = nx.petersen_graph()
    pm = all_perfect_matchings(G)
    E = {frozenset(e) for e in G.edges()}
    assert len(pm) == 6 and len(E) == 15
    assert all(sum(e in M for M in pm) == 2 for e in E)
    assert all(len(pm[i] & pm[j]) == 1
               for i in range(6) for j in range(i))
    for m in range(1, 6):
        vectors = [x for x in product(range(m+1), repeat=6)
                   if all(sum(x[i] for i, M in enumerate(pm) if e in M) == m
                          for e in E)]
        if m % 2:
            assert vectors == []
        else:
            assert vectors == [(m//2,) * 6]


def test_cube_two_component_pair_difference():
    G = nx.hypercube_graph(3)
    M = {}
    for j in range(3):
        M[j] = frozenset(frozenset((x, tuple(
            x[k] ^ int(k == j) for k in range(3))))
            for x in G if x[j] == 0)
    cycles = diff_components(M[0], M[1])
    assert sorted(map(len, cycles)) == [4, 4]
    first = {frozenset(e) for e in G.subgraph(cycles[0]).edges()}
    new_A = M[0] ^ first
    new_B = M[1] ^ first
    assert new_A not in (M[0], M[1])
    assert new_B not in (M[0], M[1])
    assert all(sum(e in M for M in (new_A, new_B))
               == sum(e in M for M in (M[0], M[1]))
               for e in map(frozenset, G.edges()))


if __name__ == "__main__":
    test_pair_rigid_petersen_and_k33()
    test_petersen_covering_multiplicity_requires_even_m()
    test_cube_two_component_pair_difference()
    print("PASS: Petersen/K3,3 pair rigidity, Petersen parity, cube obstruction")
