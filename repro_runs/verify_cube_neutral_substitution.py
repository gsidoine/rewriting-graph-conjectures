"""Exhaustive two-block six-matching neutral-substitution audit.

Run from repo root:
    python repro_runs/verify_cube_neutral_substitution.py

The local cover backtracker is shared with the independently tested finite
cube base lemma. All gluing, global matching formation, cycle switches,
component search and fixed-signature checks are implemented here.
"""
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import runpy

import networkx as nx

base = runpy.run_path(str(Path(__file__).resolve().parents[1]
                          / "tests" / "test_cube_neutral_transparency.py"))
enum_cover = base["covers"]


def perfect_matchings(graph):
    edges = tuple(sorted(tuple(sorted(e)) for e in graph.edges()))
    index = {e: j for j, e in enumerate(edges)}
    def rec(remaining, mask):
        if not remaining:
            yield mask
            return
        u = min(remaining)
        for v in graph[u]:
            if v in remaining:
                yield from rec(remaining - {u, v},
                               mask | (1 << index[tuple(sorted((u, v)))]))
    return edges, tuple(sorted(set(rec(frozenset(graph), 0))))


def cycles(bit, edges):
    remaining = {i for i in range(len(edges)) if bit >> i & 1}
    out = []
    while remaining:
        part = {remaining.pop()}
        while True:
            verts = {v for e in part for v in edges[e]}
            extra = {e for e in remaining if verts.intersection(edges[e])}
            if not extra:
                break
            remaining.difference_update(extra)
            part.update(extra)
        out.append(sum(1 << e for e in part))
    return out


def audit(host):
    cube = nx.cubical_graph()
    cap = 0
    a = sorted(cube.neighbors(cap))
    b = sorted(host.neighbors(cap))
    assert len(a) == len(b) == 3
    edges = []
    for block, tile in enumerate((cube, host)):
        edges += [tuple(sorted(((block, u), (block, v))))
                  for u, v in tile.edges() if u != cap and v != cap]
    cross = [tuple(sorted(((0, u), (1, v)))) for u, v in zip(a, b)]
    edges = tuple(sorted(edges + cross))
    edge_index = {e: i for i, e in enumerate(edges)}
    graph = nx.Graph()
    graph.add_edges_from(edges)
    assert all(d == 3 for _, d in graph.degree())
    assert nx.edge_connectivity(graph) == 3

    parts = []
    for block, tile, neighbors in ((0, cube, a), (1, host, b)):
        local_edges, matchings = perfect_matchings(tile)
        le = {e: i for i, e in enumerate(local_edges)}
        ports = []
        interior = []
        for pm in matchings:
            used = [i for i, v in enumerate(neighbors)
                    if pm >> le[tuple(sorted((cap, v)))] & 1]
            assert len(used) == 1
            ports.append(used[0])
            bit = 0
            for k, (u, v) in enumerate(local_edges):
                if pm >> k & 1 and cap not in (u, v):
                    bit |= 1 << edge_index[tuple(sorted(((block, u),
                                                          (block, v))))]
            interior.append(bit)
        groups = defaultdict(list)
        for state in enum_cover(matchings, 6, 2):
            signature = tuple(tuple(k for k, j in enumerate(state)
                                    if ports[j] == p) for p in range(3))
            groups[signature].append(state)
        assert len(groups) == 90
        parts.append((ports, interior, groups))
    (ports0, inside0, left), (ports1, inside1, right) = parts
    assert left.keys() == right.keys()
    cross_bits = [1 << edge_index[e] for e in cross]

    full_pm = []
    pair_to_index = {}
    for i, j in product(range(len(ports0)), range(len(ports1))):
        if ports0[i] != ports1[j]:
            continue
        bit = inside0[i] | inside1[j] | cross_bits[ports0[i]]
        assert bit.bit_count() == graph.number_of_nodes() // 2
        pair_to_index[i, j] = len(full_pm)
        full_pm.append(bit)
    assert len(full_pm) == len(set(full_pm)) == 18
    pm_index = {bit: k for k, bit in enumerate(full_pm)}

    states = set()
    for signature in left:
        for x, y in product(left[signature], right[signature]):
            st = tuple(pair_to_index[i, j] for i, j in zip(x, y))
            assert st not in states
            states.add(st)
    for st in states:
        assert all(sum(bool(full_pm[j] >> e & 1) for j in st) == 2
                   for e in range(len(edges)))

    switching = {}
    for a, b in combinations(range(len(full_pm)), 2):
        switching[a, b] = [
            (pm_index[full_pm[a] ^ cyc], pm_index[full_pm[b] ^ cyc])
            for cyc in cycles(full_pm[a] ^ full_pm[b], edges)
        ]

    def neighbors(st):
        for i, j in combinations(range(6), 2):
            if st[i] == st[j]:
                continue
            a, b = sorted((st[i], st[j]))
            for x, y in switching[a, b]:
                new = list(st)
                new[i] = x if st[i] == a else y
                new[j] = y if st[j] == b else x
                yield tuple(new)

    def component_sizes(seed_states):
        unseen = set(seed_states)
        result = []
        transitions = 0
        while unseen:
            frontier = [unseen.pop()]
            for state in frontier:
                for other in neighbors(state):
                    transitions += 1
                    assert other in states
                    if other in unseen:
                        unseen.remove(other)
                        frontier.append(other)
            result.append(len(frontier))
        return sorted(result), transitions

    star = tuple(i for i, e in enumerate(edges) if (0, 7) in e)
    assert len(star) == 3
    def signature(st):
        return tuple(tuple(j for j, k in enumerate(st)
                           if full_pm[k] >> e & 1) for e in star)
    representative = next(iter(states))
    fixed = {st for st in states if signature(st) == signature(representative)}

    sizes, transitions = component_sizes(states)
    fixed_sizes, fixed_transitions = component_sizes(fixed)
    if host.number_of_nodes() == 6:
        assert (sizes, fixed_sizes, len(states)) == (
            [4320, 4320, 34560], [48, 48, 384], 43200)
    else:
        assert (sizes, fixed_sizes, len(states)) == (
            [34560], [384], 34560)
    print(f"PASS: n={graph.number_of_nodes()}, PM={len(full_pm)}, "
          f"covers={len(states)}, global_components={sizes}, "
          f"global_directed_switches={transitions}, "
          f"fixed_components={fixed_sizes}, "
          f"fixed_directed_switches={fixed_transitions}")
    return transitions


if __name__ == "__main__":
    t = audit(nx.complete_bipartite_graph(3, 3))
    t += audit(nx.petersen_graph())
    assert t == 1645920
    print("PASS: all 1,645,920 directed switches checked")
