"""Independent seven-vertex atlas and C5 obstruction tests."""
from collections import Counter
import networkx as nx
from applications.murty_simon.private_witness import (
    broken_pairs_formula, broken_pairs_oracle, is_diameter2,
    is_diameter2_critical, one_edge_swaps_preserving_diameter2)


def test_all_atlas_diameter_two_graphs_to_seven():
    edges_checked = 0
    graphs_checked = 0
    for graph in nx.graph_atlas_g():
        if not (3 <= len(graph) <= 7 and is_diameter2(graph)):
            continue
        graphs_checked += 1
        for u, v in graph.edges():
            assert broken_pairs_formula(graph, u, v) == broken_pairs_oracle(graph, u, v)
            edges_checked += 1
    assert (graphs_checked, edges_checked) == (456, 5552)


def test_criticality_matches_independent_deletion_oracle():
    counts = Counter()
    for G in nx.graph_atlas_g():
        if not (3 <= len(G) <= 7 and is_diameter2(G)):
            continue
        predicted = is_diameter2_critical(G)
        independently = True
        for e in G.edges():
            H = G.copy()
            H.remove_edge(*e)
            if is_diameter2(H):
                independently = False
                break
        assert predicted == independently
        if predicted:
            counts[len(G)] += 1
    assert dict(counts) == {3: 1, 4: 2, 5: 3, 6: 5, 7: 10}


def test_c5_single_swap_trap_and_denser_target():
    G = nx.cycle_graph(5)
    assert is_diameter2_critical(G)
    assert list(one_edge_swaps_preserving_diameter2(G)) == []
    assert broken_pairs_formula(G, 0, 1) == {
        frozenset((0, 1)), frozenset((0, 2)), frozenset((1, 4))}
    K = nx.complete_bipartite_graph(2, 3)
    assert is_diameter2_critical(K) and K.number_of_edges() == 6
