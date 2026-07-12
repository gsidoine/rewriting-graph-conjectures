"""Small, explicit graph I/O helpers used by certificate checkers."""
from __future__ import annotations
from pathlib import Path
from typing import Iterable
import networkx as nx


def canonical_edges(graph: nx.Graph) -> tuple[tuple[int, int], ...]:
    """Return a sorted, orientation-free edge tuple for a simple graph."""
    return tuple(sorted((min(u, v), max(u, v)) for u, v in graph.edges()))


def read_graph6(text_or_path: str | Path) -> nx.Graph:
    path = Path(text_or_path)
    text = path.read_text().strip() if path.exists() else str(text_or_path).strip()
    return nx.from_graph6_bytes(text.encode("ascii"))


def write_edge_list(path: str | Path, edges: Iterable[tuple[int, int]]) -> None:
    Path(path).write_text("\n".join(f"{u} {v}" for u, v in sorted(edges)) + "\n")
