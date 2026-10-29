"""Check the shared gluing theorem on three-sheet CDCs of K3,3 + cube.

The omitted matching in each of the three even CDC sheets gives an ordered
3-edge-coloring; switching two even sheets is a two-color Kempe cycle move.
"""
from itertools import permutations, combinations
from collections import defaultdict
from repro_runs.verify_mixed_pair_rigid import graph_for, perfect_matchings, cycle_masks


def sizes(subset, adj):
    todo = set(subset)
    result = []
    while todo:
        start = todo.pop()
        queue = [start]
        for x in queue:
            for y in adj[x]:
                if y in todo:
                    todo.remove(y)
                    queue.append(y)
        result.append(len(queue))
    return sorted(result)


def test_cdc_k33_cube_exact_gluing():
    G, tiles = graph_for("KC")
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    PM = perfect_matchings(G, edges)
    by_mask = {mask: i for i, mask in enumerate(PM)}
    all_edges = (1 << len(edges)) - 1
    states = [
        state
        for state in permutations(range(len(PM)), 3)
        if (PM[state[0]] | PM[state[1]] | PM[state[2]]) == all_edges
        and all(PM[state[a]] & PM[state[b]] == 0
                for a, b in combinations(range(3), 2))
    ]
    assert len(states) == 48
    S = set(states)
    adj = {}
    for s in states:
        opts = set()
        for a, b in combinations(range(3), 2):
            for C in cycle_masks(PM[s[a]] ^ PM[s[b]], edges):
                z = list(s)
                z[a] = by_mask[PM[s[a]] ^ C]
                z[b] = by_mask[PM[s[b]] ^ C]
                z = tuple(z)
                assert z in S
                opts.add(z)
        adj[s] = opts
    assert sizes(states, adj) == [24,24]
    # The first K3,3 tile's right terminal (0,1) is removed by graph_for('KC').
    # Its exposed left terminal remains cubic and supplies the fixed star.
    root = (0, tiles[0][1][0])
    star = [e for e, edge in enumerate(edges) if root in edge]
    assert len(star) == 3
    grouped = defaultdict(list)
    for s in states:
        sig = tuple(next(i for i, pm in enumerate(s) if PM[pm] >> e & 1)
                    for e in star)
        grouped[sig].append(s)
    assert len(grouped) == 6
    assert all(len(g) == 8 and sizes(g, adj) == [4,4] for g in grouped.values())
