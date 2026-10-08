"""Exact component-enriched typed 3-edge-cut quotient verification.

Run: python repro_runs/verify_typed_cut_quotient.py
Independently enumerates local PM6 covers, signature-preserving neutral
components and crossing moves, then forms exact weighted quotient products.
No enumeration of the joined/global graphs is used in this script.
Requires networkx.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
import networkx as nx


def perfect_matchings(graph):
    edges = tuple(sorted(tuple(sorted(e)) for e in graph.edges()))
    index = {e: i for i, e in enumerate(edges)}
    def rec(unused, bits):
        if not unused:
            yield bits
            return
        u = min(unused)
        for v in graph[u]:
            if v in unused:
                yield from rec(unused - {u, v},
                               bits | (1 << index[tuple(sorted((u, v)))]))
    masks = tuple(sorted(set(rec(frozenset(graph), 0))))
    return edges, masks


def double_covers(matchings, nedges):
    supports = [tuple(e for e in range(nedges) if pm >> e & 1)
                for pm in matchings]
    counts = [0] * nedges
    def rec(used):
        if len(used) == 6:
            if all(c == 2 for c in counts):
                yield tuple(used)
            return
        remaining = 5 - len(used)
        for i, support in enumerate(supports):
            if any(counts[e] == 2 for e in support):
                continue
            for e in support:
                counts[e] += 1
            if all(c + remaining >= 2 for c in counts):
                yield from rec(used + [i])
            for e in support:
                counts[e] -= 1
    yield from rec([])


def components(mask, edges):
    remaining = {i for i in range(len(edges)) if mask >> i & 1}
    answer = []
    while remaining:
        part = {remaining.pop()}
        while True:
            vertices = {v for k in part for v in edges[k]}
            nxt = {k for k in remaining if vertices.intersection(edges[k])}
            if not nxt:
                break
            part.update(nxt)
            remaining.difference_update(nxt)
        answer.append(sum(1 << k for k in part))
    return answer


def local_automaton(graph, port=0):
    edges, matchings = perfect_matchings(graph)
    states = tuple(double_covers(matchings, len(edges)))
    star = tuple(k for k, e in enumerate(edges) if port in e)
    assert len(star) == 3
    signatures = {}
    def sig(st):
        return tuple(tuple(j for j, k in enumerate(st)
                           if matchings[k] >> e & 1) for e in star)
    index = {mask: k for k, mask in enumerate(matchings)}
    local_switches = defaultdict(set)
    boundary_switches = defaultdict(set)
    allstates = set(states)
    for st in states:
        signatures[st] = sig(st)
        for a, b in combinations(range(6), 2):
            for cyc in components(matchings[st[a]] ^ matchings[st[b]], edges):
                other = list(st)
                other[a] = index[matchings[st[a]] ^ cyc]
                other[b] = index[matchings[st[b]] ^ cyc]
                other = tuple(other)
                assert other in allstates
                crossed_ports = tuple(k for k, e in enumerate(star)
                                      if cyc >> e & 1)
                assert len(crossed_ports) in (0, 2)
                if len(crossed_ports) == 0:
                    local_switches[st].add(other)
                else:
                    boundary_switches[st].add((other, (a, b, crossed_ports)))

    grouped = defaultdict(set)
    for st in states:
        grouped[signatures[st]].add(st)
    assert len(grouped) == 90
    response_nodes = defaultdict(list)
    response_weights = {}
    state_to_response = {}
    for signature, fiber in grouped.items():
        remaining = set(fiber)
        while remaining:
            start = remaining.pop()
            reachable = [start]
            for st in reachable:
                for nxt in local_switches[st]:
                    if nxt in remaining:
                        remaining.remove(nxt)
                        reachable.append(nxt)
            key = (signature, len(response_nodes[signature]))
            response_nodes[signature].append(key)
            response_weights[key] = len(reachable)
            for st in reachable:
                state_to_response[st] = key

    typed_edges = set()
    for st, moves in boundary_switches.items():
        for nxt, tau in moves:
            typed_edges.add((state_to_response[st],
                             state_to_response[nxt], tau))
    print("LOCAL", graph.number_of_nodes(),
          "states", len(states),
          "signatures", len(grouped),
          "response_nodes", len(response_weights),
          "nodes_per_signature", dict(Counter(len(x) for x in response_nodes.values())),
          "typed_edges", len(typed_edges), flush=True)
    return response_nodes, response_weights, typed_edges


def synchronized_product(left, right):
    Ln, Lw, Le = left
    Rn, Rw, Re = right
    assert Ln.keys() == Rn.keys()
    quotient_nodes = set()
    weights = {}
    for sig in Ln:
        for a, b in product(Ln[sig], Rn[sig]):
            node = (a, b)
            quotient_nodes.add(node)
            weights[node] = Lw[a] * Rw[b]

    Lt = defaultdict(list)
    Rt = defaultdict(list)
    for a, b, tau in Le:
        Lt[(a[0], b[0], tau)].append((a, b))
    for a, b, tau in Re:
        Rt[(a[0], b[0], tau)].append((a, b))

    adjacent = defaultdict(set)
    for key in Lt.keys() & Rt.keys():
        for (a, b), (c, d) in product(Lt[key], Rt[key]):
            u, v = (a, c), (b, d)
            assert u in quotient_nodes and v in quotient_nodes
            adjacent[u].add(v)
            adjacent[v].add(u)

    remaining = set(quotient_nodes)
    answer = []
    while remaining:
        reachable = [remaining.pop()]
        for v in reachable:
            for w in adjacent[v]:
                if w in remaining:
                    remaining.remove(w)
                    reachable.append(w)
        answer.append((len(reachable), sum(weights[v] for v in reachable)))
    answer.sort()
    print("PRODUCT", len(quotient_nodes), "response nodes",
          "components", answer,
          "weighted total", sum(weights.values()), flush=True)
    return answer


def verify_all():
    K = local_automaton(nx.complete_bipartite_graph(3, 3))
    C = local_automaton(nx.cubical_graph())
    P = local_automaton(nx.petersen_graph())
    assert sorted(w for _, w in synchronized_product(K, C)) == (
        [4320, 4320, 34560])
    assert sorted(w for _, w in synchronized_product(P, C)) == [34560]
    assert sorted(w for _, w in synchronized_product(K, K)) == (
        [90, 90, 90, 90, 720, 720, 720, 720, 5760])
    assert sorted(w for _, w in synchronized_product(C, C)) == [207360]
    print("PASS: four independent exact typed-cut quotient benchmarks")


if __name__ == "__main__":
    verify_all()
