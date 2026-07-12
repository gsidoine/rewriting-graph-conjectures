"""Exact spanning-tree enumeration used on small cubic graphs."""
from __future__ import annotations
from itertools import combinations
import networkx as nx


def enumerate_spanning_trees(graph: nx.Graph):
    n = graph.number_of_nodes()
    edges = [tuple(sorted(e)) for e in graph.edges()]
    for chosen in combinations(edges, n - 1):
        tree = nx.Graph()
        tree.add_nodes_from(graph.nodes())
        tree.add_edges_from(chosen)
        if nx.is_tree(tree):
            yield frozenset(chosen)
