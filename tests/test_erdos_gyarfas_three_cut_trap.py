"""Petersen: positive-defect, three-cut-immobile cubic graph."""
from collections import Counter
from itertools import combinations

import networkx as nx


def three_edge_cuts(G):
    vertices = tuple(G.nodes())
    root = vertices[0]
    for r in range(1, len(vertices)):
        for others in combinations(vertices[1:], r-1):
            shore = frozenset((root, *others))
            cut = tuple((u, v) for u, v in G.edges()
                        if (u in shore) != (v in shore))
            if len(cut) == 3:
                yield shore, cut


def test_petersen_three_cut_immobility():
    G = nx.petersen_graph()
    assert len(G) == 10 and all(d == 3 for _, d in G.degree())
    cuts = list(three_edge_cuts(G))
    assert len(cuts) == 10
    assert all(min(len(S), 10 - len(S)) == 1 for S, _ in cuts)
    counts = Counter(map(len, nx.simple_cycles(G)))
    assert counts == Counter({5: 12, 6: 10, 8: 15, 9: 20})
    assert sum(c for k, c in counts.items()
               if k >= 4 and k & (k - 1) == 0) == 15
    assert nx.edge_connectivity(G) == 3
