from itertools import combinations_with_replacement
import networkx as nx

from applications.berge_fulkerson.src.perfect_matchings import enumerate_perfect_matchings
from applications.berge_fulkerson.src.exhaustive_verification import verify_all_states_normalize
from applications.three_decomposition.src.verify_counterexample import verify


def test_petersen_complete_normalization():
    graph = nx.petersen_graph()
    matchings = enumerate_perfect_matchings(graph)
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
    result = verify_all_states_normalize(edges, matchings)
    assert result == {"perfect_matchings": 6, "states": 462, "targets": 1, "reached": 462, "unresolved": 0}


def test_fixed_cycle_counterexample_counts():
    result = verify()
    assert result["vertices"] == 16
    assert result["edges"] == 21
    assert result["leaves"] == [0, 1, 2]
    assert result["N0_connected_unicyclic"]
    assert result["size5_matchings"] == 1448
    assert result["size5_connected_unicyclic"] == 105
    assert result["size6_matchings"] == 615
    assert result["size6_tree_complements"] == 0
    assert all(all(side for side in sides) for sides in result["bridge_leaf_sides"])
