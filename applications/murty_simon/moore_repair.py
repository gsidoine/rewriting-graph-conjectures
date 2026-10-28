"""Exact high-girth diameter-two edge-repair constructions.

For diam<=2, girth>=5, min degree>=2 and edge uv, the proven minimum
number of DIFFERENT edges added to G-uv (excluding uv) to recover
diameter<=2 is max(p,q) if p != q, and p+1 if p=q, where
p=deg(v)-1, q=deg(u)-1. See MOORE_REPAIR_THEOREM.md for the proof.
"""
from itertools import combinations


def girth_at_least_five(G):
    """Exclude triangles and four-cycles, including in nonregular graphs."""
    for u in G:
        for v, w in combinations(G.neighbors(u), 2):
            if G.has_edge(v, w):
                return False
    for u, v in combinations(G.nodes(), 2):
        if len(set(G.neighbors(u)) & set(G.neighbors(v))) >= 2:
            return False
    return True


def hypotheses(G):
    import networkx as nx
    return (len(G) >= 5 and min(dict(G.degree()).values()) >= 2
            and nx.is_connected(G) and nx.diameter(G) <= 2
            and girth_at_least_five(G))


def broken_witness_triple(G, u, v):
    """Three pairs that must break after uv deletion, with endpoints x,y."""
    assert hypotheses(G) and G.has_edge(u, v)
    x = next(w for w in G.neighbors(v) if w != u)
    y = next(w for w in G.neighbors(u) if w != v)
    return x, y, {frozenset((u, v)),
                  frozenset((u, x)), frozenset((v, y))}


def restoring_uv_candidates(G, u, v):
    """Only single new edges other than uv that might restore d(u,v)<=2."""
    assert G.has_edge(u, v)
    return ([frozenset((u, x)) for x in G.neighbors(v) if x != u]
            + [frozenset((v, y)) for y in G.neighbors(u) if y != v])


def minimum_repair_count(G, u, v):
    assert hypotheses(G) and G.has_edge(u, v)
    p, q = G.degree(v) - 1, G.degree(u) - 1
    return p + 1 if p == q else max(p, q)


def optimal_repair(G, u, v):
    """Construct a minimum-size replacement edge family, without using uv."""
    import networkx as nx
    assert hypotheses(G) and G.has_edge(u, v)
    X = [x for x in G.neighbors(v) if x != u]
    Y = [y for y in G.neighbors(u) if y != v]
    k = min(len(X), len(Y))
    additions = [(X[i], Y[i]) for i in range(k)]
    additions += [(u, x) for x in X[k:]]
    additions += [(v, y) for y in Y[k:]]
    if len(X) == len(Y):
        additions.append((u, X[0]))
    assert len(additions) == minimum_repair_count(G, u, v)
    assert len(set(map(frozenset, additions))) == len(additions)
    assert all(not G.has_edge(*e) for e in additions)
    H = G.copy()
    H.remove_edge(u, v)
    H.add_edges_from(additions)
    assert not H.has_edge(u, v) and nx.is_connected(H) and nx.diameter(H) <= 2
    return additions, H
