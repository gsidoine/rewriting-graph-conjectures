"""Computer-certified local port coherence of the non-rigid cube in two systems.

The 3-sheet CDC is encoded by *complementary* 3-edge-color classes, so its
neutral moves correspond exactly to two-color alternating cycle swaps.
The 6-matching double cover uses exact edge multiplicity 2.
Run: python -m pytest -q tests/test_cube_port_coherence.py
"""
import itertools
from collections import defaultdict
import networkx as nx


def cube_data():
    G = nx.hypercube_graph(3)
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    adj = {u: [] for u in G}
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    def pm(unmatched, mask=0):
        if not unmatched:
            yield mask
            return
        u = min(unmatched)
        for v, i in adj[u]:
            if v in unmatched:
                yield from pm(unmatched - {u, v}, mask | (1 << i))
    PM = sorted(set(pm(frozenset(G))))
    assert len(PM) == 9
    star = [i for i, e in enumerate(edges) if (0,0,0) in e]
    assert len(star) == 3
    return edges, PM, star


def cycles_of(mask, edges):
    remaining = {i for i in range(len(edges)) if mask >> i & 1}
    while remaining:
        part = {remaining.pop()}
        while True:
            vertices = {u for e in part for u in edges[e]}
            new = {i for i in remaining if vertices.intersection(edges[i])}
            if not new:
                break
            part |= new
            remaining -= new
        yield sum(1 << i for i in part)


def neutral_neighbors(states, PM, edges):
    mask_to_idx = {p: i for i, p in enumerate(PM)}
    S = set(states)
    result = {}
    for st in states:
        choices = set()
        for a, b in itertools.combinations(range(len(st)), 2):
            for cycle in cycles_of(PM[st[a]] ^ PM[st[b]], edges):
                out = list(st)
                out[a] = mask_to_idx[PM[st[a]] ^ cycle]
                out[b] = mask_to_idx[PM[st[b]] ^ cycle]
                out = tuple(out)
                assert out in S
                choices.add(out)
        result[st] = choices
    return result


def component_sizes(states, neighbors):
    remaining = set(states)
    sizes = []
    while remaining:
        start = remaining.pop()
        queue = [start]
        for x in queue:
            for y in neighbors[x]:
                if y in remaining:
                    remaining.remove(y)
                    queue.append(y)
        sizes.append(len(queue))
    return tuple(sorted(sizes))


def group_by_signature(states, PM, star):
    by = defaultdict(list)
    for st in states:
        key = tuple(tuple(j for j, i in enumerate(st) if PM[i] >> e & 1)
                    for e in star)
        by[key].append(st)
    return by


def test_cube_three_sheet_cdc_port_coherence():
    edges, PM, star = cube_data()
    allmask = (1 << len(edges)) - 1
    states = [st for st in itertools.permutations(range(len(PM)), 3)
              if (PM[st[0]] | PM[st[1]] | PM[st[2]]) == allmask
              and all(PM[st[a]] & PM[st[b]] == 0
                      for a, b in itertools.combinations(range(3), 2))]
    assert len(states) == 24
    adj = neutral_neighbors(states, PM, edges)
    assert component_sizes(states, adj) == (24,)
    fibers = group_by_signature(states, PM, star)
    assert len(fibers) == 6
    assert all(len(f) == 4 and component_sizes(f, adj) == (4,)
               for f in fibers.values())


def test_cube_six_matching_double_cover_port_coherence():
    edges, PM, star = cube_data()
    state = []
    counter = [0] * len(edges)
    incident = [[e for e in range(len(edges)) if p >> e & 1] for p in PM]
    def gen(prefix):
        if len(prefix) == 6:
            if all(x == 2 for x in counter):
                state.append(tuple(prefix))
            return
        slots_left = 5 - len(prefix)
        for i, present in enumerate(incident):
            if any(counter[e] == 2 for e in present):
                continue
            for e in present:
                counter[e] += 1
            if all(x + slots_left >= 2 for x in counter):
                gen(prefix + [i])
            for e in present:
                counter[e] -= 1
    gen([])
    assert len(state) == 4320
    adj = neutral_neighbors(state, PM, edges)
    assert component_sizes(state, adj) == (4320,)
    fibers = group_by_signature(state, PM, star)
    assert len(fibers) == 90
    assert all(len(f) == 48 and component_sizes(f, adj) == (48,)
               for f in fibers.values())


if __name__ == '__main__':
    test_cube_three_sheet_cdc_port_coherence()
    test_cube_six_matching_double_cover_port_coherence()
    print('PASS: cube port coherence 24 CDC states / 4320 matching covers')
