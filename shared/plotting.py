"""Optional plotting helpers; no plotting is required for verification."""
from __future__ import annotations
import networkx as nx


def spring_positions(graph: nx.Graph, seed: int = 0):
    return nx.spring_layout(graph, seed=seed)
