"""The dual colouring potential Phi."""
from __future__ import annotations
import networkx as nx


def psi(graph: nx.Graph) -> int:
    if graph.number_of_nodes() == 0:
        raise ValueError("psi is defined here only for nonempty graphs")
    components = nx.number_connected_components(graph)
    beta = graph.number_of_edges() - graph.number_of_nodes() + components
    return components - 1 + beta


def phi(graph: nx.Graph, colour_mask: int) -> int:
    vertices = list(graph.nodes())
    a = {v for v in vertices if (colour_mask >> v) & 1}
    b = set(vertices) - a
    if not a or not b:
        raise ValueError("the exact identity is stated for nontrivial colourings")
    return psi(graph.subgraph(a)) + psi(graph.subgraph(b))
