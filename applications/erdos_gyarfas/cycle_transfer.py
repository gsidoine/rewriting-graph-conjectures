"""Exact simple-cycle counting across a three-edge cut.

The two shores have disjoint vertex sets and three distinct ports each.
For cubic graphs, each port has internal degree 2 and all non-ports 3.
"""
from collections import Counter
from itertools import combinations, permutations


def adjacency(vertices, edges):
    adj = {v: set() for v in vertices}
    for u, v in edges:
        assert u in adj and v in adj and u != v
        adj[u].add(v)
        adj[v].add(u)
    return adj


def path_counts(vertices, edges, source, target):
    """Simple source-to-target paths by their number of edges."""
    assert source != target
    adj = adjacency(vertices, edges)
    ans = Counter()

    def dfs(u, seen, depth):
        if u == target:
            ans[depth] += 1
            return
        for v in adj[u] - seen:
            dfs(v, seen | {v}, depth + 1)

    dfs(source, {source}, 0)
    return ans


def cycle_counts(vertices, edges):
    """Unoriented simple cycles by length, counted once each."""
    adj = adjacency(vertices, edges)
    rank = {v: k for k, v in enumerate(sorted(adj, key=str))}
    out = Counter()

    def dfs(root, u, seen, k):
        for v in adj[u]:
            if v == root and k >= 3:
                out[k] += 1
            elif v not in seen and rank[v] > rank[root]:
                dfs(root, v, seen | {v}, k + 1)

    for root in rank:
        dfs(root, root, {root}, 1)
    return Counter({k: v // 2 for k, v in out.items()})


def profile(vertices, edges, ports):
    assert len(ports) == len(set(ports)) == 3
    assert set(ports) <= set(vertices)
    return {
        "cycles": cycle_counts(vertices, edges),
        "paths": {
            ij: path_counts(vertices, edges, ports[ij[0]], ports[ij[1]])
            for ij in combinations(range(3), 2)
        },
    }


def cross_counts(left, right):
    """Cycles using exactly two of the three cut edges."""
    ans = Counter()
    for ij in combinations(range(3), 2):
        for a, ca in left["paths"][ij].items():
            for b, cb in right["paths"][ij].items():
                ans[a + b + 2] += ca * cb
    return +ans


def transfer_counts(left, right):
    return +(left["cycles"] + right["cycles"] + cross_counts(left, right))


def is_power_two_cycle(k):
    return k >= 4 and k & (k - 1) == 0


def defect(counts):
    """Number of all power-of-two cycles (not just forbidden lengths)."""
    return sum(v for k, v in counts.items() if is_power_two_cycle(k))


def context_cost(left, right):
    return defect(cross_counts(left, right))


def rewrite_delta(before, after, context):
    """Exact change Q(after ⊕ context) - Q(before ⊕ context)."""
    return (
        defect(after["cycles"]) - defect(before["cycles"])
        + context_cost(after, context) - context_cost(before, context)
    )


def glue(lv, le, lp, rv, re, rp):
    assert not (set(lv) & set(rv)), "Shores must be disjoint"
    assert len(lp) == len(set(lp)) == len(rp) == len(set(rp)) == 3
    return list(lv) + list(rv), list(le) + list(re) + list(zip(lp, rp))


def permutation_defects(left_profile, right_vertices, right_edges, right_ports):
    """Exact defect for each of the six 3-cut reconnections."""
    assert len(right_ports) == len(set(right_ports)) == 3
    return {
        perm: defect(transfer_counts(
            left_profile,
            profile(right_vertices, right_edges, [right_ports[i] for i in perm]),
        ))
        for perm in permutations(range(3))
    }


if __name__ == "__main__":
    a = ["a", "b", "c"]
    b = ["x", "y", "z"]
    t = lambda x: [(x[0], x[1]), (x[1], x[2]), (x[2], x[0])]
    c = transfer_counts(profile(a, t(a), a), profile(b, t(b), b))
    assert c == Counter({3: 2, 4: 3, 5: 6, 6: 3})
    print("triangular prism cycle spectrum:", dict(c))
