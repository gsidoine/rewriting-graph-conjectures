"""Exact graph-certified FR extension obstructions, including infinite triangle lifts."""
import json
from pathlib import Path

from applications.berge_fulkerson.plateau.fr_extension_core import (
    check_certificate, check_expansion, coverage, edges_of_certificate,
    expand_good_vertex, residual_kernel, all_perfect_matchings,
    three_edge_colorable, connected_without,
)
from shared.three_colour_boundaries import split_data

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / 'applications/berge_fulkerson/plateau/fr_n14_petersen_kernel.json'


def test_petersen_kernel_nonextension():
    data = json.loads(CERT.read_text())
    r = check_certificate(data)
    assert r['vertices'] == 14
    assert r['uncovered_edges'] == 2
    assert r['kernel_perfect_matchings_tested'] == 6
    assert r['residual_bridgeless'] and not r['residual_3_edge_colourable']
    assert r['host_3_edge_connected'] and r['host_3_edge_colourable']


def test_arbitrarily_extendable_obstruction_construction_first_four():
    data = json.loads(CERT.read_text())
    for n in (16, 18, 20, 22):
        edges = edges_of_certificate(data)
        f = coverage(data['n'], edges, [[tuple(e) for e in M] for M in data['frozen_matchings']])
        good = next(v for v in range(data['n']) if all(f[e] == 1 for e in edges if v in e))
        data = expand_good_vertex(data, good)
        q = check_expansion(data)
        assert q['n'] == n and q['uncovered'] == 2


def test_petersen_four_pole_incompatible():
    # Canonical Petersen edge list; the two open pieces have locally feasible
    # 3-edge-colourings, but their 4-port response sets are disjoint.
    E = sorted({tuple(sorted((i, (i + 1) % 5))) for i in range(5)} |
               {tuple(sorted((i + 5, (i + 2) % 5 + 5))) for i in range(5)} |
               {(i, i + 5) for i in range(5)})
    data = split_data(10, E, {0, 1})
    assert len(data['cut_edges']) == 4
    assert data['A'] and data['B']
    assert data['intersection'] == []
    assert set(data['A']) == {'(0, 1, 0, 1)', '(0, 1, 1, 0)'}
    assert set(data['B']) == {'(0, 0, 0, 0)', '(0, 0, 1, 1)'}


def test_suppression_matches_direct_residual_colouring_j5():
    # Independent factor enumeration on 2010 collision-free FR-triples.
    J = json.loads((ROOT / 'applications/berge_fulkerson/instances/j5/j5_instance.json').read_text())
    n, edges = J['vertices'], [tuple(e) for e in J['edges']]
    P = list(all_perfect_matchings(n, edges))
    assert len(P) == 32
    from itertools import combinations_with_replacement
    eligible = nonextend = 0
    for ii in combinations_with_replacement(range(len(P)), 3):
        f = [sum(j in P[z] for z in ii) for j in range(len(edges))]
        if max(f) > 2:
            continue
        eligible += 1
        residual = [2 - x for x in f]
        kernel = residual_kernel(n, edges, residual)
        kernel_colorable = three_edge_colorable(len(kernel['vertices']), kernel['edges'])
        # Direct 3-colour search on residual multigraph, with each copy as an edge.
        R = [e for j, e in enumerate(edges) for _ in range(residual[j])]
        direct = three_edge_colorable(n, R)
        assert direct == kernel_colorable
        if not kernel_colorable:
            nonextend += 1
    assert (eligible, nonextend) == (2010, 330)


def test_single_coordinate_strict_escape_of_nonextendable_FR_triple():
    D=json.loads(CERT.read_text())
    E=set(edges_of_certificate(D))
    F=[{tuple(e) for e in M} for M in D['frozen_matchings']]
    assert len(F[0] & F[1])==1 and len(F[0] & F[2])==1
    assert F[1].isdisjoint(F[2])
    new=E - (F[1] | F[2])
    assert len(new)==7
    assert sum((sum(e in X for X in F)-1)**2 for e in E)==4
    assert sum((sum(e in X for X in (new,F[1],F[2]))-1)**2 for e in E)==0
