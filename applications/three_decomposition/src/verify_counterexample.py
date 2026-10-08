"""Independent verifier for the 16-vertex fixed-cycle obstruction."""
from __future__ import annotations
from itertools import combinations
import networkx as nx

GRAPH6 = "O??DQ?[C?AaAA?@O??wGS"
N0 = frozenset({(3, 8), (4, 12), (5, 13), (7, 10), (9, 11)})


def enumerate_matchings(graph: nx.Graph, size: int):
    edges = [tuple(sorted(e)) for e in graph.edges()]
    for chosen in combinations(edges, size):
        vertices = [v for edge in chosen for v in edge]
        if len(vertices) == len(set(vertices)):
            yield frozenset(chosen)


def verify():
    graph = nx.from_graph6_bytes(GRAPH6.encode())
    leaves = sorted(v for v, d in graph.degree() if d == 1)
    bridges = [tuple(sorted(e)) for e in nx.bridges(graph)]
    bridge_leaf_sides = []
    for edge in bridges:
        cut = graph.copy(); cut.remove_edge(*edge)
        sides = list(nx.connected_components(cut))
        bridge_leaf_sides.append([sorted(set(leaves) & side) for side in sides])
    complement = graph.copy(); complement.remove_edges_from(N0)
    five = list(enumerate_matchings(graph, 5))
    six = list(enumerate_matchings(graph, 6))
    five_good = 0
    for matching in five:
        remainder = graph.copy(); remainder.remove_edges_from(matching)
        if nx.is_connected(remainder) and remainder.number_of_edges() == remainder.number_of_nodes():
            five_good += 1
    six_good = 0
    for matching in six:
        remainder = graph.copy(); remainder.remove_edges_from(matching)
        if nx.is_tree(remainder):
            six_good += 1
    return {
        "vertices": graph.number_of_nodes(), "edges": graph.number_of_edges(),
        "leaves": leaves, "bridges": bridges, "bridge_leaf_sides": bridge_leaf_sides,
        "N0_connected_unicyclic": nx.is_connected(complement) and complement.number_of_edges() == complement.number_of_nodes(),
        "size5_matchings": len(five), "size5_connected_unicyclic": five_good,
        "size6_matchings": len(six), "size6_tree_complements": six_good,
    }
