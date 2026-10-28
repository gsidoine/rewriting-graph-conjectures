"""Independent structural and exhaustive checks of minimum-repair theorem."""
from itertools import combinations
import networkx as nx

from applications.murty_simon.moore_repair import (
    hypotheses, broken_witness_triple, restoring_uv_candidates,
    minimum_repair_count, optimal_repair
)


def deleted_broken_pairs(G, u, v):
    H = G.copy()
    H.remove_edge(u, v)
    return {frozenset((a, b)) for a, b in combinations(G.nodes, 2)
            if not nx.has_path(H, a, b)
            or nx.shortest_path_length(H, a, b) > 2}


def test_three_moore_graphs_all_195_edges():
    examples = [(nx.cycle_graph(5), 2), (nx.petersen_graph(), 3),
                (nx.hoffman_singleton_graph(), 7)]
    total = 0
    for G, degree in examples:
        assert hypotheses(G)
        assert all(d == degree for _, d in G.degree())
        for u, v in G.edges():
            x, y, forced = broken_witness_triple(G, u, v)
            B = deleted_broken_pairs(G, u, v)
            assert forced <= B and len(B) == 2 * degree - 1
            assert len(restoring_uv_candidates(G, u, v)) == 2 * (degree - 1)
            assert minimum_repair_count(G, u, v) == degree
            additions, H = optimal_repair(G, u, v)
            assert len(additions) == degree and not H.has_edge(u, v)
            assert nx.diameter(H) <= 2
            total += 1
    assert total == 195


def test_exhaustive_small_minimality():
    # This check is an independent optimization audit, not the general proof.
    for G, optimum in [(nx.cycle_graph(5), 2), (nx.petersen_graph(), 3)]:
        for u, v in G.edges():
            H = G.copy()
            H.remove_edge(u, v)
            available = list(nx.non_edges(G))  # excludes the deleted uv
            for k in range(optimum):
                for F in combinations(available, k):
                    J = H.copy()
                    J.add_edges_from(F)
                    assert not nx.is_connected(J) or nx.diameter(J) > 2


def test_all_atlas_graphs_satisfying_hypotheses():
    examples = [G for G in nx.graph_atlas_g()
                if len(G) >= 5 and hypotheses(G)]
    assert len(examples) >= 1
    for G in examples:
        for u, v in G.edges():
            additions, repaired = optimal_repair(G, u, v)
            assert len(additions) == minimum_repair_count(G, u, v)
            assert nx.diameter(repaired) <= 2


def test_endpoint_local_girth_only_unequal_degrees():
    import itertools
    from applications.murty_simon.moore_repair import (
        edge_hypotheses, girth_at_least_five)
    G = nx.Graph()
    u, v = "u", "v"
    X = [f"x{i}" for i in range(2)]
    Y = [f"y{j}" for j in range(3)]
    Z = [f"z{i}{j}" for i in range(2) for j in range(3)]
    G.add_edge(u, v)
    for x in X:
        G.add_edge(v, x)
    for y in Y:
        G.add_edge(u, y)
    for i in range(2):
        for j in range(3):
            z = f"z{i}{j}"
            G.add_edge(X[i], z)
            G.add_edge(Y[j], z)
    G.add_edges_from(itertools.combinations(Z, 2))
    assert (len(G), G.number_of_edges(), nx.diameter(G)) == (13, 33, 2)
    assert (G.degree(u), G.degree(v)) == (4, 3)
    assert edge_hypotheses(G, u, v)
    assert not girth_at_least_five(G)  # contains triangles elsewhere
    assert minimum_repair_count(G, u, v) == 3
    additions, H = optimal_repair(G, u, v)
    assert len(additions) == 3 and nx.diameter(H) == 2
    H0 = G.copy()
    H0.remove_edge(u, v)
    available = list(nx.non_edges(G))
    for k in (0, 1, 2):
        for F in combinations(available, k):
            J = H0.copy()
            J.add_edges_from(F)
            assert not nx.is_connected(J) or nx.diameter(J) > 2
