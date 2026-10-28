"""Exact private-distance witness calculus for diameter-two graphs."""
from itertools import combinations


def broken_pairs_formula(G, u, v):
    """Pairs whose distance becomes >2 on deleting uv, if diam(G)<=2."""
    assert u != v and G.has_edge(u, v)
    nu, nv = set(G.neighbors(u)), set(G.neighbors(v))
    broken = set()
    if not (nu & nv):
        broken.add(frozenset((u, v)))
    for x in nv - {u}:
        if not G.has_edge(u, x) and (nu & set(G.neighbors(x))) == {v}:
            broken.add(frozenset((u, x)))
    for x in nu - {v}:
        if not G.has_edge(v, x) and (nv & set(G.neighbors(x))) == {u}:
            broken.add(frozenset((v, x)))
    return broken


def broken_pairs_oracle(G, u, v):
    """Independent shortest-path oracle; test code only."""
    import networkx as nx
    H = G.copy()
    H.remove_edge(u, v)
    return {frozenset((a, b)) for a, b in combinations(G.nodes, 2)
            if not nx.has_path(H, a, b)
            or nx.shortest_path_length(H, a, b) > 2}


def is_diameter2(G):
    import networkx as nx
    return len(G) > 2 and nx.is_connected(G) and nx.diameter(G) <= 2


def is_diameter2_critical(G):
    return is_diameter2(G) and all(
        broken_pairs_formula(G, u, v) for u, v in G.edges())


def one_edge_swaps_preserving_diameter2(G):
    """All delete-one/add-a-different-edge moves retaining diameter <=2."""
    for u, v in list(G.edges()):
        H = G.copy()
        H.remove_edge(u, v)
        for x, y in combinations(G.nodes, 2):
            if not G.has_edge(x, y):
                J = H.copy()
                J.add_edge(x, y)
                if is_diameter2(J):
                    yield (u, v), (x, y)
