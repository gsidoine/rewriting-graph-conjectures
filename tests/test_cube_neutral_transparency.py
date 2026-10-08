"""Computer-assisted finite base of the transparent-cube substitution theorem.

Pytest checks complete labelled state enumeration and all fixed-star neutral
fiber diameters, not random samples. Requires networkx only.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import comb

import networkx as nx


G = nx.cubical_graph()
E = tuple(sorted(tuple(sorted(e)) for e in G.edges()))
PORT = 0
STAR = tuple(i for i, (u, v) in enumerate(E) if PORT in (u, v))
EVEN = tuple(
    mask for mask in range(1 << len(E))
    if all(
        sum((mask >> i) & 1 for i, (u, w) in enumerate(E) if v in (u, w)) % 2 == 0
        for v in G
    )
)
assert len(E) == 12 and len(EVEN) == 32
EVEN_INDEX = {mask: j for j, mask in enumerate(EVEN)}


def matchings():
    adj = {v: [] for v in G}
    for i, (u, v) in enumerate(E):
        adj[u].append((v, i))
        adj[v].append((u, i))

    def search(unused, mask):
        if not unused:
            yield mask
            return
        u = min(unused)
        for v, e in adj[u]:
            if v in unused:
                yield from search(unused - {u, v}, mask | (1 << e))

    return tuple(sorted(set(search(frozenset(G), 0))))


PM = matchings()
assert len(PM) == 9


def covers(masks, count, multiplicity):
    membership = [
        tuple(i for i in range(len(E)) if (mask >> i) & 1)
        for mask in masks
    ]
    tally = [0] * len(E)

    def backtrack(partial):
        depth = len(partial)
        if depth == count:
            if all(x == multiplicity for x in tally):
                yield tuple(partial)
            return
        remaining = count - depth - 1
        for k, support in enumerate(membership):
            if any(tally[e] == multiplicity for e in support):
                continue
            for e in support:
                tally[e] += 1
            if all(x + remaining >= multiplicity for x in tally):
                yield from backtrack(partial + [k])
            for e in support:
                tally[e] -= 1

    yield from backtrack([])


def edge_components(bit):
    remaining = {i for i in range(len(E)) if (bit >> i) & 1}
    result = []
    while remaining:
        todo = {remaining.pop()}
        while True:
            vertices = {v for e in todo for v in E[e]}
            new = {i for i in remaining if vertices.intersection(E[i])}
            if not new:
                break
            todo.update(new)
            remaining.difference_update(new)
        result.append(sum(1 << i for i in todo))
    return result


def signatures(states, masks):
    groups = defaultdict(set)
    for state in states:
        signature = tuple(
            tuple(j for j, k in enumerate(state) if (masks[k] >> e) & 1)
            for e in STAR
        )
        groups[signature].add(state)
    return groups


def fiber_diameter(group, masks):
    inverse = {mask: k for k, mask in enumerate(masks)}
    group = set(group)
    n = len(next(iter(group)))
    adjacency = {}
    for state in group:
        moves = set()
        for i, j in combinations(range(n), 2):
            for cyc in edge_components(masks[state[i]] ^ masks[state[j]]):
                other = list(state)
                other[i] = inverse[masks[state[i]] ^ cyc]
                other[j] = inverse[masks[state[j]] ^ cyc]
                other = tuple(other)
                assert other in group
                moves.add(other)
        adjacency[state] = moves

    maximum = 0
    for start in group:
        lengths = {start: 0}
        queue = deque([start])
        while queue:
            a = queue.popleft()
            for b in adjacency[a]:
                if b not in lengths:
                    lengths[b] = lengths[a] + 1
                    queue.append(b)
        assert len(lengths) == len(group), "Disconnected neutral fiber"
        maximum = max(maximum, max(lengths.values()))
    return maximum


def test_cube_pm6_fiber_is_transparent():
    states = list(covers(PM, 6, 2))
    assert len(states) == len(set(states)) == 4320
    grouped = signatures(states, PM)
    assert len(grouped) == 90
    assert set(map(len, grouped.values())) == {48}
    assert fiber_diameter(next(iter(grouped.values())), PM) == 4


def test_cube_cdc_q3_through_q6_fibers():
    expected = {
        3: (24, 6, 4, 2),
        4: (768, 24, 32, 6),
        5: (3960, 60, 66, 6),
        6: (13440, 120, 112, 7),
    }
    for q, (total, sigs, width, diameter) in expected.items():
        states = list(covers(EVEN, q, 2))
        assert len(states) == len(set(states)) == total
        grouped = signatures(states, EVEN)
        assert len(grouped) == sigs == 6 * comb(q, 3)
        assert set(map(len, grouped.values())) == {width}
        assert fiber_diameter(next(iter(grouped.values())), EVEN) == diameter


def test_cube_cdc_q6_inactive_support_coefficients():
    states = list(covers(EVEN, 6, 2))
    group = next(iter(signatures(states, EVEN).items()))
    signature, fiber = group
    active = set(j for labels in signature for j in labels)
    assert len(active) == 3
    support = Counter(
        sum(EVEN[k] != 0 for j, k in enumerate(state) if j not in active)
        for state in fiber
    )
    assert support == {0: 4, 1: 84, 2: 18, 3: 6}
    for q, expected in [(3, 4), (4, 32), (5, 66), (6, 112),
                        (7, 176), (8, 264)]:
        r = q - 3
        assert 4 + 28*r + 6*comb(r, 2) + 6*comb(r, 3) == expected
