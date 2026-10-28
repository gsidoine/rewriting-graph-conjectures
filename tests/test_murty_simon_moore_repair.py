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
