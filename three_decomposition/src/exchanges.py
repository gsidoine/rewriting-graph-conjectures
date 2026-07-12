"""Basis exchanges and exhaustive non-increasing neighbors."""
from __future__ import annotations
import networkx as nx
from .cotree_defect import bad_path_count


def basis_exchange_neighbors(graph: nx.Graph, tree_edges):
    tree_edges = {tuple(sorted(e)) for e in tree_edges}
    tree = nx.Graph()
    tree.add_nodes_from(graph.nodes())
    tree.add_edges_from(tree_edges)
    for added in graph.edges():
        added = tuple(sorted(added))
        if added in tree_edges:
            continue
        path = nx.shortest_path(tree, *added)
        cycle_edges = [tuple(sorted((path[i], path[i + 1]))) for i in range(len(path) - 1)]
        for removed in cycle_edges:
            yield frozenset((tree_edges | {added}) - {removed})


def nonincreasing_neighbors(graph: nx.Graph, tree_edges):
    current = bad_path_count(graph, tree_edges)
    for nxt in basis_exchange_neighbors(graph, tree_edges):
        if bad_path_count(graph, nxt) <= current:
            yield nxt
