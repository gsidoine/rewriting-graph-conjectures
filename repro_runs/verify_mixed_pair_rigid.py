"""Independent exhaustive global audit for K3,3/Petersen three-edge sums.

Run: python repro_runs/verify_mixed_pair_rigid.py
Needs NetworkX. Deliberately outside ordinary pytest CI: enumerates >20,000
labelled six-perfect-matching covers and all their neutral switches.
"""
from itertools import combinations, product
from collections import Counter
from math import prod
import networkx as nx

def graph_for(word):
    tiles = [(nx.complete_bipartite_graph(3, 3), (0, 1))
             if tag == 'K' else (nx.petersen_graph(), (0, 2))
             for tag in word]
    removed = {(j, ports[0]) for j, (_, ports) in enumerate(tiles) if j > 0}
    removed |= {(j, ports[1]) for j, (_, ports) in enumerate(tiles) if j+1 < len(word)}
    G = nx.Graph()
    for j, (T, _) in enumerate(tiles):
        G.add_nodes_from((j, u) for u in T)
        G.add_edges_from(((j, u), (j, v)) for u, v in T.edges())
    for j in range(len(tiles)-1):
        T, p = tiles[j]; U, q = tiles[j+1]
        G.add_edges_from(((j, u), (j+1, v)) for u, v in
                         zip(sorted(T.neighbors(p[1])), sorted(U.neighbors(q[0]))))
    G.remove_nodes_from(removed)
    assert all(d == 3 for _, d in G.degree())
    assert nx.edge_connectivity(G) == 3
    return G, tiles

def perfect_matchings(G, edges):
    adj = {u: [] for u in G}
    for i, (a, b) in enumerate(edges):
        adj[a].append((b, i)); adj[b].append((a, i))
    def search(unused, mask=0):
        if not unused:
            yield mask
        else:
            u = min(unused)
            for v, i in adj[u]:
                if v in unused:
                    yield from search(unused - {u, v}, mask | (1 << i))
    return sorted(set(search(frozenset(G))))

def cycle_masks(mask, edges):
    todo = {i for i in range(len(edges)) if mask >> i & 1}
    while todo:
        component = {todo.pop()}
        while True:
            vertices = {v for e in component for v in edges[e]}
            new = {e for e in todo if vertices.intersection(edges[e])}
            if not new: break
            todo |= set()  # no mutation except through explicit set operations
            component |= new
            todo -= new
        yield sum(1 << e for e in component)

def check(word):
    G, tiles = graph_for(word)
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    PM = perfect_matchings(G, edges)
    pmid = {m: i for i, m in enumerate(PM)}
    counts = [0]*len(edges)
    states = []
    edgeids = [tuple(i for i in range(len(edges)) if mask >> i & 1) for mask in PM]
    def enumerate_states(prefix):
        if len(prefix) == 6:
            if all(c == 2 for c in counts):
                states.append(tuple(prefix))
            return
        more = 5 - len(prefix)
        for i, chosen in enumerate(edgeids):
            if any(counts[e] == 2 for e in chosen): continue
            for e in chosen: counts[e] += 1
            if all(x+more >= 2 for x in counts):
                enumerate_states(prefix + [i])
            for e in chosen: counts[e] -= 1
    enumerate_states([])
    pool = set(states)
    Ktype_lookup = []
    for j, tag in enumerate(word):
        if tag != 'K': continue
        terminal_left = tiles[j][1][0] if j else None
        terminal_right = tiles[j][1][1] if j+1 < len(word) else None
        parity = []
        for pm in PM:
            local = []
            for e, (a, b) in enumerate(edges):
                if not (pm >> e & 1): continue
                if a[0] == j and b[0] == j:
                    local.append(tuple(sorted((a[1], b[1]))))
                elif a[0] == j or b[0] == j:
                    own = a if a[0] == j else b
                    cap = terminal_left if a[0] > j or b[0] < j else terminal_right
                    # Determine cap solely by the *other* endpoint's tile.
                    foreign = b if own == a else a
                    cap = terminal_left if foreign[0] < j else terminal_right
                    assert cap is not None
                    local.append(tuple(sorted((own[1], cap))))
            assert len(local) == 3, (word, pm, local)
            p = [next((v-3 if u == r else u-3)
                      for u,v in local if r in (u,v)) for r in range(3)]
            parity.append(sum(p[i] > p[k] for i in range(3) for k in range(i+1, 3)) % 2)
        Ktype_lookup.append(parity)
    typ = {s: tuple(sum(1-parity[i] for i in s)//3 for parity in Ktype_lookup)
           for s in states}
    adj = {}
    for s in states:
        opts = set()
        for a,b in combinations(range(6), 2):
            for c in cycle_masks(PM[s[a]] ^ PM[s[b]], edges):
                nxt = list(s)
                nxt[a] = pmid[PM[s[a]] ^ c]
                nxt[b] = pmid[PM[s[b]] ^ c]
                nxt = tuple(nxt)
                assert nxt in pool and typ[nxt] == typ[s]
                opts.add(nxt)
        adj[s] = opts
    def components(subset):
        unused = set(subset); result = []
        while unused:
            x = unused.pop()
            todo = [x]
            for y in todo:
                for z in adj[y]:
                    if z in unused:
                        unused.remove(z); todo.append(z)
            result.append((typ[x], len(todo)))
        return sorted(result)
    all_components = components(states)
    # Exposed left terminal of first tile remains a degree-three vertex.
    u = (0, tiles[0][1][0])
    star = [i for i,e in enumerate(edges) if u in e]
    assert len(star) == 3
    def signature(s):
        return tuple(tuple(k for k,j in enumerate(s) if PM[j]>>e&1)
                     for e in star)
    first = signature(states[0])
    fixed = [s for s in states if signature(s) == first]
    fixed_components = components(fixed)
    a = word.count('K')
    b = word.count('P')
    expected = sorted((t, 90*8**b*prod(8 if x==1 else 1 for x in t))
                      for t in product(range(3), repeat=a))
    expected_fixed = sorted((t, 8**b*prod(8 if x==1 else 1 for x in t))
                            for t in product(range(3), repeat=a))
    assert all_components == expected
    assert fixed_components == expected_fixed
    if a == 1:
        for old_type in (0, 1):
            left = [s for s in fixed if typ[s] == (old_type,)]
            right = [s for s in fixed if typ[s] == (old_type+1,)]
            distances = [sum(x != y for x, y in zip(s, t))
                         for s in left for t in right]
            assert min(distances) == 3, (word, old_type, min(distances))
        assert all(sum(x != y for x, y in zip(s, t)) >= 3
                   for s in states for t in states if typ[s] != typ[t])
    print(word, "vertices", len(G), "perfect matchings", len(PM),
          "covers", len(states), "directed neutral adjacency",
          sum(len(v) for v in adj.values()), "components", all_components,
          "fixed-signature components", fixed_components)

if __name__ == '__main__':
    for word in ('KP', 'PK', 'PP'):
        check(word)
    print('ALL MIXED PAIR-RIGID TESTS PASS')
