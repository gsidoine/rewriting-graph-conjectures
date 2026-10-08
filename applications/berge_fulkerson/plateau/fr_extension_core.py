"""Exact, standard-library verification of FR-triple nonextension certificates.

Notation: G is simple cubic and F is three labelled perfect matchings,
with no edge in all three. R=2G-F is a cubic multigraph. Its parallel
pairs (copies of uncovered edges) can be suppressed to a cubic kernel.
"""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import json


def edges_of_certificate(data):
    return [tuple(e) for e in data['edges']]


def is_perfect_matching(n, matching):
    return len(matching) * 2 == n and sorted(v for e in matching for v in e) == list(range(n))


def coverage(n, edges, matchings):
    E = set(edges)
    assert len(E) == len(edges)
    for matching in matchings:
        assert is_perfect_matching(n, matching)
        assert all(tuple(e) in E for e in matching)
    counts = {e: 0 for e in edges}
    for matching in matchings:
        for e in matching:
            counts[tuple(e)] += 1
    return counts


def residual_kernel(n, edges, multiplicities):
    """Suppress parallel-double-edge gadgets; return cubic kernel and its paths.

    Pure doubled/single alternating cycles without degree-three vertices are
    automatically 3-edge-colourable and disappear from the kernel.
    """
    double_partner = {}
    singles = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        r = multiplicities[e]
        assert r in (0, 1, 2)
        if r == 2:
            assert u not in double_partner and v not in double_partner
            double_partner[u] = v
            double_partner[v] = u
        elif r == 1:
            singles[u].append((v, e))
            singles[v].append((u, e))
    core_vertices = [v for v in range(n) if v not in double_partner]
    index = {v: i for i, v in enumerate(core_vertices)}
    assert all(len(singles[v]) == (3 if v in index else 1) for v in range(n))
    used = set()
    kernel_edges = []
    walks = []
    for source in core_vertices:
        for u, e in singles[source]:
            if e in used:
                continue
            used.add(e)
            walk = [e]
            while u in double_partner:
                far = double_partner[u]
                u, e = singles[far][0]
                assert e not in used
                walk.append(e)
                used.add(e)
            kernel_edges.append((index[source], index[u]))
            walks.append(walk)
    assert len(kernel_edges) == 3 * len(core_vertices) // 2
    return {'vertices': core_vertices, 'edges': kernel_edges, 'walks': walks,
            'doubled_count': len(double_partner) // 2}


def all_perfect_matchings(n, edges):
    assert n % 2 == 0
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        assert u != v
        adj[u].append((v, i))
        adj[v].append((u, i))
    def rec(mask, matching):
        if mask == 0:
            yield frozenset(matching)
            return
        v = (mask & -mask).bit_length() - 1
        for u, i in adj[v]:
            if mask >> u & 1:
                yield from rec(mask ^ (1 << v) ^ (1 << u), (*matching, i))
    yield from rec((1 << n) - 1, ())


def even_cycle_complement(n, edges, matching):
    # Complement of a perfect matching in a cubic multigraph is a 2-factor.
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if i not in matching:
            adj[u].append(v)
            adj[v].append(u)
    assert all(len(a) == 2 for a in adj)
    visited = set()
    for s in range(n):
        if s in visited:
            continue
        todo = [s]
        visited.add(s)
        for v in todo:
            for u in adj[v]:
                if u not in visited:
                    visited.add(u)
                    todo.append(u)
        if len(todo) % 2:
            return False
    return True


def three_edge_colorable(n, edges):
    if n == 0:
        return True
    if any(u == v for u, v in edges):
        return False
    return any(even_cycle_complement(n, edges, m)
               for m in all_perfect_matchings(n, edges))


def connected_without(n, edges, excluded=()):
    excluded = set(excluded)
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if i not in excluded:
            adj[u].append(v)
            adj[v].append(u)
    seen = {0}
    todo = [0]
    for u in todo:
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == n


def edge_connectivity_at_least_three(n, edges):
    if not connected_without(n, edges):
        return False
    for i in range(len(edges)):
        if not connected_without(n, edges, (i,)):
            return False
        for j in range(i + 1, len(edges)):
            if not connected_without(n, edges, (i, j)):
                return False
    return True


def check_certificate(data, verify_connectivity=True):
    n = data['n']
    edges = edges_of_certificate(data)
    assert len(edges) == 3 * n // 2 and len(set(edges)) == len(edges)
    assert all(0 <= u < v < n for u, v in edges)
    assert all(sum(v in e for e in edges) == 3 for v in range(n))
    fms = [[tuple(e) for e in M] for M in data['frozen_matchings']]
    assert len(fms) == 3
    f = coverage(n, edges, fms)
    assert all(x <= 2 for x in f.values())
    values = list(f.values())
    residual = [2 - v for v in values]
    assert all(sum(residual[i] for i, e in enumerate(edges) if v in e) == 3 for v in range(n))
    expanded = [e for i, e in enumerate(edges) for _ in range(residual[i])]
    assert len(expanded) == 3 * n // 2
    assert all(connected_without(n, expanded, (i,)) for i in range(len(expanded)))
    kern = residual_kernel(n, edges, residual)
    # The two independent equivalence tests below must both say NO.
    assert not three_edge_colorable(len(kern['vertices']), kern['edges'])
    if verify_connectivity:
        assert edge_connectivity_at_least_three(n, edges)
    col = [[tuple(e) for e in M] for M in data['host_edge_colouring']]
    assert len(col) == 3
    assert all(is_perfect_matching(n, M) for M in col)
    assert sorted(e for M in col for e in M) == sorted(edges)
    iso = {int(i): j for i, j in data['petersen_kernel_isomorphism'].items()}
    assert len(kern['vertices']) == 10 and set(iso) == set(range(10)) and set(iso.values()) == set(range(10))
    # Standard Petersen graph: outer cycle, inner pentagram, spokes.
    P = {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}
    P |= {tuple(sorted((i + 5, (i + 2) % 5 + 5))) for i in range(5)}
    P |= {(i, i + 5) for i in range(5)}
    assert {tuple(sorted((iso[u], iso[v]))) for u, v in kern['edges']} == P
    return {'vertices': n, 'host_edges': len(edges), 'uncovered_edges': values.count(0),
            'host_3_edge_connected': bool(verify_connectivity),
            'host_3_edge_colourable': True, 'FR_triple': True,
            'residual_bridgeless': True, 'residual_3_edge_colourable': False,
            'kernel_vertices': len(kern['vertices']),
            'kernel_is_Petersen': True,
            'kernel_perfect_matchings_tested': sum(1 for _ in all_perfect_matchings(10, kern['edges']))}


def expand_good_vertex(data, vertex):
    """Expand a vertex with three distinct frozen-coordinate incidences to triangle.

    Preserves: simplicity, cubicity, host 3-edge-colourability, host
    3-edge-connectivity, bridgeless residual, and residual non-3-colourability.
    """
    oldn = data['n']
    edges = edges_of_certificate(data)
    incident = [e for e in edges if vertex in e]
    assert len(incident) == 3
    f = coverage(oldn, edges, [[tuple(e) for e in M] for M in data['frozen_matchings']])
    assert all(f[e] == 1 for e in incident)
    ports = (vertex, oldn, oldn + 1)
    replacement = {}
    for edge, port in zip(incident, ports):
        u, v = edge
        replacement[edge] = tuple(sorted((port, v if u == vertex else u)))
    inside = [tuple(sorted((ports[i], ports[j]))) for i, j in combinations(range(3), 2)]
    output_edges = sorted(replacement.get(e, e) for e in edges if e not in incident) + sorted(replacement.values()) + inside
    output_edges = sorted(output_edges)
    assert len(set(output_edges)) == len(output_edges)
    new_fms = []
    for M in data['frozen_matchings']:
        M = [tuple(e) for e in M]
        chosen = [i for i, e in enumerate(incident) if e in M]
        assert len(chosen) == 1
        i = chosen[0]
        pair = tuple(sorted(ports[j] for j in range(3) if j != i))
        new_fms.append(sorted(replacement.get(e, e) for e in M) + [pair])
    new_col = []
    for M in data['host_edge_colouring']:
        M = [tuple(e) for e in M]
        chosen = [i for i, e in enumerate(incident) if e in M]
        assert len(chosen) == 1
        i = chosen[0]
        pair = tuple(sorted(ports[j] for j in range(3) if j != i))
        new_col.append(sorted(replacement.get(e, e) for e in M) + [pair])
    return {'n': oldn + 2, 'edges': [list(e) for e in output_edges],
            'frozen_matchings': [[list(e) for e in sorted(M)] for M in new_fms],
            'host_edge_colouring': [[list(e) for e in sorted(M)] for M in new_col]}


def check_expansion(data):
    n=data['n'];edges=edges_of_certificate(data)
    assert edge_connectivity_at_least_three(n,edges)
    frozen=[[tuple(e) for e in M] for M in data['frozen_matchings']]
    host=[[tuple(e) for e in M] for M in data['host_edge_colouring']]
    f=coverage(n,edges,frozen)
    assert all(x<=2 for x in f.values())
    assert all(is_perfect_matching(n,m) for m in host)
    assert sorted(e for M in host for e in M)==sorted(edges)
    r=[2-f[e] for e in edges]
    multiedges=[e for i,e in enumerate(edges) for _ in range(r[i])]
    assert all(connected_without(n,multiedges,(j,)) for j in range(len(multiedges)))
    K=residual_kernel(n,edges,r)
    assert not three_edge_colorable(len(K['vertices']),K['edges'])
    return dict(n=n,uncovered=sum(x==0 for x in f.values()),kernel_vertices=len(K['vertices']))


if __name__ == '__main__':
    source = Path(__file__).with_name('fr_n14_petersen_kernel.json')
    data=json.loads(source.read_text())
    print('base',check_certificate(data))
    for i in range(1,5):
        f=coverage(data['n'], edges_of_certificate(data),
                   [[tuple(e) for e in M] for M in data['frozen_matchings']])
        good=next(v for v in range(data['n'])
                  if all(f[e] == 1 for e in edges_of_certificate(data) if v in e))
        data=expand_good_vertex(data,good)
        print('expanded',i,check_expansion(data))
