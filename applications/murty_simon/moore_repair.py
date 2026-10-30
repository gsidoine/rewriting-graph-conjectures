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



def endpoint_locally_short_cycle_free(G, u, v):
    """Neither endpoint is on a triangle or a four-cycle."""
    if not G.has_edge(u, v) or G.degree(u) < 2 or G.degree(v) < 2:
        return False
    for w in (u, v):
        for a, b in combinations(G.neighbors(w), 2):
            if G.has_edge(a, b):
                return False
            if (set(G.neighbors(a)) & set(G.neighbors(b))) - {w}:
                return False
    return True


def edge_hypotheses(G, u, v):
    """Local hypotheses: global diameter <=2, no short cycles AT u/v."""
    import networkx as nx
    return (nx.is_connected(G) and nx.diameter(G) <= 2
            and endpoint_locally_short_cycle_free(G, u, v))


def hypotheses(G):
    import networkx as nx
    return (len(G) >= 5 and min(dict(G.degree()).values()) >= 2
            and nx.is_connected(G) and nx.diameter(G) <= 2
            and girth_at_least_five(G))


def broken_witness_triple(G, u, v):
    """Three pairs that must break after uv deletion, with endpoints x,y."""
    assert edge_hypotheses(G, u, v)
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


def grid_clique_example(p, q):
    """Explicit n=(p+1)(q+1)+1 diameter-two family with exact repair width."""
    import networkx as nx
    assert p >= 1 and q >= 1
    G = nx.Graph()
    u, v = ("u",), ("v",)
    X = [("x", i) for i in range(p)]
    Y = [("y", j) for j in range(q)]
    Z = [("z", i, j) for i in range(p) for j in range(q)]
    G.add_edge(u, v)
    G.add_edges_from((v, x) for x in X)
    G.add_edges_from((u, y) for y in Y)
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            z = ("z", i, j)
            G.add_edge(x, z)
            G.add_edge(y, z)
    G.add_edges_from(combinations(Z, 2))
    assert len(G) == (p + 1) * (q + 1) + 1
    assert edge_hypotheses(G, u, v)
    assert minimum_repair_count(G, u, v) == (p + 1 if p == q else max(p, q))
    return G, u, v
