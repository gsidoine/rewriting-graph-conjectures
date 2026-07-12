"""Exact perfect-matching enumeration for small verification instances."""
from __future__ import annotations
import networkx as nx

Edge = tuple[int, int]
Matching = frozenset[Edge]


def enumerate_perfect_matchings(graph: nx.Graph) -> list[Matching]:
    """Enumerate every perfect matching of a small loopless simple graph."""
    if graph.number_of_nodes() % 2:
        return []
    found: set[Matching] = set()

    def recurse(remaining: frozenset[int], chosen: tuple[Edge, ...]) -> None:
        if not remaining:
            found.add(frozenset(chosen))
            return
        u = min(remaining)
        for v in graph.neighbors(u):
            if v in remaining:
                recurse(remaining - {u, v}, chosen + ((min(u, v), max(u, v)),))

    recurse(frozenset(graph.nodes()), ())
    return sorted(found, key=lambda matching: sorted(matching))
