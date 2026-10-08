"""Strict defect descent on the aggregate six-matching multiplicity state.

For cubic bipartite graphs the multiplicities x satisfying degree(x)=6
are all decomposable into six perfect matchings. The aggregate cycle move
is local, but rebuilding the 6 matching coordinates need not be local.
Do not confuse this result with one-coordinate descent.
"""
from __future__ import annotations
from collections import Counter
import networkx as nx
from .sharp_trap import graph, multiplicities, pm_masks, Q, valid_pm, load


def bipartition(edges):
    g=graph(edges)
    if not nx.is_bipartite(g):
        raise ValueError('graph must be bipartite')
    return nx.bipartite.color(g)


def normalize_multiplicities(edges, start):
    """Return vector trail and directed alternating-cycle witnesses."""
    color=bipartition(edges)
    x=list(start)
    assert all(sum(x[i] for i,e in enumerate(edges) if u in e)==6
               for u in graph(edges))
    q=lambda z:sum((a-2)**2 for a in z)
    trace=[x.copy()];cycles=[]
    while any(a!=2 for a in x):
        directed=nx.DiGraph()
        for i,(u,v) in enumerate(edges):
            if x[i]==2:continue
            if color[u]==0:u,v=v,u
            if x[i]>2:directed.add_edge(u,v,idx=i)
            else:directed.add_edge(v,u,idx=i)
        cyc=nx.find_cycle(directed)
        ids=[directed[u][v]['idx'] for u,v in cyc]
        old=q(x)
        for j in ids:x[j]+=(-1 if x[j]>2 else 1)
        assert q(x)<old and old-q(x)>=4
        trace.append(x.copy());cycles.append(ids)
    return trace,cycles


def decompose_into_six_matchings(edges, x):
    """König decomposition of the six-regular bipartite multigraph x."""
    g=graph(edges)
    side={v for v,c in bipartition(edges).items() if c==0}
    remaining=x.copy();factors=[]
    for _ in range(6):
        support=nx.Graph()
        support.add_nodes_from(g)
        support.add_edges_from(e for e,j in zip(edges,remaining) if j>0)
        match=nx.bipartite.maximum_matching(support,top_nodes=side)
        if len(match)!=len(g):
            raise AssertionError('remaining regular bipartite multigraph has no PM')
        sel={frozenset((v,match[v])) for v in side}
        mask=0
        for i,e in enumerate(edges):
            if frozenset(e) in sel:
                assert remaining[i]>0
                remaining[i]-=1;mask|=1<<i
        assert valid_pm(edges,mask)
        factors.append(mask)
    assert all(v==0 for v in remaining)
    return factors


def validate():
    edges,path=load()
    start=multiplicities(edges,path[0]);trace,cycles=normalize_multiplicities(edges,start)
    assert len(trace)==len(cycles)+1
    assert trace[0]==start and trace[-1]==[2]*len(edges)
    assert len(cycles)<=3*len(graph(edges))
    assert all(multiplicities(edges,decompose_into_six_matchings(edges,x))==x for x in trace)
    return dict(n_vertices=len(graph(edges)),aggregate_steps=len(cycles),
                Q_trace=[sum((v-2)**2 for v in x) for x in trace],
                aggregate_cycle_lengths=[len(c) for c in cycles])

if __name__=='__main__':
    print(validate());print('PASS aggregate cycle-cancellation / six perfect matching decomposition')
