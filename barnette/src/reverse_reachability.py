"""Connected-patch generation and bounded normalization checks."""
from __future__ import annotations
from collections import deque
from itertools import combinations
import networkx as nx
from .colouring_potential import phi


def connected_patches(graph: nx.Graph, max_size: int):
    nodes = list(graph.nodes())
    for size in range(1, max_size + 1):
        for patch in combinations(nodes, size):
            if nx.is_connected(graph.subgraph(patch)):
                yield sum(1 << v for v in patch)


def shortest_nonincreasing_path(graph: nx.Graph, start: int, max_patch_size: int):
    patches = tuple(connected_patches(graph, max_patch_size))
    parent = {start: None}; patch_used = {}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        current_phi = phi(graph, current)
        if current_phi == 0:
            path = []
            while current is not None:
                path.append((current, 0 if parent[current] is None else patch_used[current]))
                current = parent[current]
            return list(reversed(path))
        for patch in patches:
            nxt = current ^ patch
            try:
                nxt_phi = phi(graph, nxt)
            except ValueError:
                continue
            if nxt_phi <= current_phi and nxt not in parent:
                parent[nxt] = current; patch_used[nxt] = patch; queue.append(nxt)
    return None
