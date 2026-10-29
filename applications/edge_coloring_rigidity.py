"""Exact edge-coloring support and Kempe graphs (finite exhaustive oracle).

These are classical Y-to-triangle uniquely-colorable cubic graph families.
The purpose is to distinguish support-budget moves from Kempe moves.
"""
from itertools import combinations, permutations
import networkx as nx


def normedge(u, v):
    return tuple(sorted((u, v)))


def triangle_expand(G, v):
    assert G.degree(v) == 3
    H = G.copy()
    neighbors = sorted(G.neighbors(v))
    H.remove_node(v)
    start = max(H.nodes()) + 1
    t = list(range(start, start + 3))
    H.add_edges_from((neighbors[i], t[i]) for i in range(3))
    H.add_edges_from([(t[0], t[1]), (t[1], t[2]), (t[2], t[0])])
    assert all(d == 3 for _, d in H.degree())
    return H


def rigid_family(k):
    assert k >= 0
    G = nx.complete_graph(4)
    for _ in range(k):
        G = triangle_expand(G, min(G.nodes()))
    return G


def proper_colorings(G):
    """Enumerate all labeled proper cubic 3-edge-colorings."""
    assert all(d == 3 for _, d in G.degree())
    E = sorted(normedge(*e) for e in G.edges())
    colors = [-1] * len(E)
    used = {v: set() for v in G}
    result = []

    def search(remaining):
        if not remaining:
            result.append(tuple(colors))
            return
        i = max(remaining, key=lambda j: len(used[E[j][0]] | used[E[j][1]]))
        u, v = E[i]
        for a in range(3):
            if a not in used[u] and a not in used[v]:
                used[u].add(a); used[v].add(a)
                colors[i] = a
                search(remaining - {i})
                colors[i] = -1
                used[u].remove(a); used[v].remove(a)

    search(set(range(len(E))))
    return E, result


def distance(x, y):
    return sum(a != b for a, b in zip(x, y))


def components(adj):
    remaining = set(range(len(adj)))
    result = []
    while remaining:
        root = remaining.pop()
        cc, todo = {root}, [root]
        while todo:
            for v in adj[todo.pop()]:
                if v in remaining:
                    remaining.remove(v); cc.add(v); todo.append(v)
        result.append(cc)
    return result


def budget_graph(states, r):
    adj = [set() for _ in states]
    for i, j in combinations(range(len(states)), 2):
        if distance(states[i], states[j]) <= r:
            adj[i].add(j); adj[j].add(i)
    return adj


def color_orbits(states):
    remaining = set(range(len(states)))
    result = []
    while remaining:
        i = next(iter(remaining))
        orbit_states = {tuple(p[a] for a in states[i])
                        for p in permutations(range(3))}
        orbit = {j for j in remaining if states[j] in orbit_states}
        remaining -= orbit
        result.append(orbit)
    return result


def kempe_graph(G, E, states):
    """Flip exactly ONE connected two-colored cycle per move."""
    index = {s: i for i, s in enumerate(states)}
    adj = [set() for _ in states]
    for i, state in enumerate(states):
        for a, b in combinations(range(3), 2):
            H = nx.Graph()
            H.add_edges_from(E[j] for j, col in enumerate(state) if col in (a, b))
            for cc in nx.connected_components(H):
                new = list(state)
                for j, (u, v) in enumerate(E):
                    if u in cc and v in cc and state[j] in (a, b):
                        new[j] = a + b - state[j]
                j = index[tuple(new)]
                assert j != i
                adj[i].add(j)
    return adj


def matching_partition_oracle(G):
    """Independent enumeration through ordered perfect-matching triples."""
    E = sorted(normedge(*e) for e in G.edges())
    incident = {v: [] for v in G}
    for j, (u, v) in enumerate(E):
        incident[u].append((v, j)); incident[v].append((u, j))

    def enumerate_matchings(free, mask):
        if not free:
            yield mask
        else:
            v = min(free)
            for u, j in incident[v]:
                if u in free:
                    yield from enumerate_matchings(free - {u, v}, mask | (1 << j))

    matchings = set(enumerate_matchings(frozenset(G), 0))
    full = (1 << len(E)) - 1
    result = set()
    for m0 in matchings:
        for m1 in matchings:
            if m0 & m1: continue
            m2 = full ^ (m0 | m1)
            if m2 not in matchings: continue
            result.add(tuple(next(c for c, m in enumerate((m0, m1, m2))
                                  if (m >> j) & 1) for j in range(len(E))))
    return E, result
