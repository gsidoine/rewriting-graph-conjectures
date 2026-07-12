"""Cotree components and the exact 3-decomposition defect statistic."""
from __future__ import annotations
import networkx as nx


def cotree(graph: nx.Graph, tree_edges) -> nx.Graph:
    normalized = {tuple(sorted(edge)) for edge in tree_edges}
    result = nx.Graph()
    result.add_nodes_from(graph.nodes())
    result.add_edges_from(edge for edge in graph.edges() if tuple(sorted(edge)) not in normalized)
    return result


def bad_path_count(graph: nx.Graph, tree_edges) -> int:
    complement = cotree(graph, tree_edges)
    count = 0
    for vertices in nx.connected_components(complement):
        component = complement.subgraph(vertices)
        if component.number_of_edges() >= 2 and max(dict(component.degree()).values(), default=0) <= 2:
            if sum(d == 1 for _, d in component.degree()) == 2:
                count += 1
    return count


def defect_edges(graph: nx.Graph, tree_edges) -> set[tuple[int, int]]:
    tree = nx.Graph()
    tree.add_nodes_from(graph.nodes())
    tree.add_edges_from(tree_edges)
    complement = cotree(graph, tree_edges)
    return {
        tuple(sorted((u, v)))
        for u, v in complement.edges()
        if {tree.degree(u), tree.degree(v)} == {1, 2}
    }
