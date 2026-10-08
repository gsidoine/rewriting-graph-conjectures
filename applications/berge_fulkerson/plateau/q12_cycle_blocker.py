"""Exact realization of first failure of two-label *cycle* hitting at Q=12.

The obstruction is to the specific one-cycle monotone correction scheme,
NOT to arbitrary two-coordinate strict improvement.

The graph was discovered by integer linear programming, then made immutable
by its explicit edge list and membership list. The verifier uses no MILP.
"""
from __future__ import annotations
import json
from itertools import combinations
from pathlib import Path
import networkx as nx
from .sharp_trap import Q, valid_pm, graph, multiplicities, expand_balanced_vertex
from .bounded_coordinate_descent import coordinated_step
from .flow_optimize_two import optimize_best_pair

DATA = Path(__file__).with_name('q12_cycle_blocker_18.json')


def load():
    record=json.loads(DATA.read_text())
    edges=[tuple(e) for e in record['edges']]
    labels=[frozenset(e) for e in record['edge_coordinate_memberships']]
    state=[sum(1<<i for i,S in enumerate(labels) if c in S) for c in range(6)]
    return edges,state,labels


def inspect():
    edges,state,labels=load()
    g=graph(edges)
    assert len(g)==18 and len(edges)==27 and nx.is_bipartite(g)
    assert len(set(tuple(sorted(e)) for e in edges))==27
    assert all(g.degree(v)==3 for v in g)
    assert nx.edge_connectivity(g)==3
    assert all(valid_pm(edges,m) for m in state)
    assert Q(edges,state)==12
    m=multiplicities(edges,state)
    assert m[:6]==[3]*6 and m[6:12]==[1]*6 and m[12:]==[2]*15
    # Only defect is the unique alternating 12-cycle.
    defect=nx.Graph();defect.add_edges_from(edges[:12])
    assert nx.is_connected(defect) and len(defect)==12
    assert all(defect.degree(v)==2 for v in defect)
    pos=[labels[i] for i in range(6)]
    assert len(set(pos))==6
    # Every two-coordinate set misses at least one surplus edge.
    assert all(any(set(pair).isdisjoint(S) for S in pos)
               for pair in combinations(range(6),2))
    # Exhaustive cardinality check of abstract blocker.
    assert any(all(set(triple).intersection(S) for S in pos)
               for triple in combinations(range(6),3))
    nxt,q,pair=optimize_best_pair(edges,state)
    assert q==4 and pair is not None and Q(edges,nxt)==4
    next3,coords=coordinated_step(edges,state)
    assert len(coords)==3 and Q(edges,next3)==0
    return dict(vertices=18,edges=27,edge_connectivity=3,initial_Q=12,
                surplus_membership_triples=[sorted(S) for S in pos],
                two_coordinate_cycle_hit_possible=False,
                exact_best_two_coordinate_Q=q,
                selected_two_coordinate_pair=list(pair),
                three_coordinate_Q=0)


def infinite_family(kmax=3):
    edges,state,labels=load()
    # Vertex 12 lies outside all defective edges. Each incident edge has m=2.
    v=12
    records=[]
    for k in range(kmax+1):
        g=graph(edges)
        assert nx.is_bipartite(g) and nx.edge_connectivity(g)==3
        assert all(valid_pm(edges,m) for m in state)
        assert Q(edges,state)==12
        m=multiplicities(edges,state)
        plus=[frozenset(c for c in range(6) if (state[c]>>j)&1)
              for j,x in enumerate(m) if x==3]
        assert len(plus)==6
        assert all(any(set(pair).isdisjoint(S) for S in plus)
                   for pair in combinations(range(6),2))
        records.append({'expansions':k,'vertices':len(g),'Q':12,
                        'edge_connectivity':3,'cycle_hitting_pair':False})
        if k<kmax:
            edges,path,v=expand_balanced_vertex(edges,[state,state],v)
            state=path[0]
    return records

if __name__=='__main__':
    print(json.dumps(inspect(),indent=2))
    print('infinite-family sample:',infinite_family())
    print('PASS: real 18-vertex Q12 cycle-blocking graph, and first three lifts')
