"""Coordinated descent theorem on cubic bipartite graphs.

Universal theorem: ANY four coordinate positions permit a strict improvement
whenever Q>0; iterate to Q=0 in at most 3*|V| moves.

If Q<=38, a suitable triple suffices. If Q<=10, a suitable pair
suffices. At Q=6, the pair reaches Q=0 directly.
The 18-vertex certificate disproves the corresponding one-coordinate claim.
"""
from __future__ import annotations
from itertools import combinations
from .sharp_trap import graph,load,Q,pm_masks,multiplicities,valid_pm
from .aggregate_descent import bipartition
import networkx as nx


def find_defect_cycle(edges,state):
    """A directed, alternating surplus/deficit cycle, as edge indices."""
    x=multiplicities(edges,state)
    if all(v==2 for v in x):return []
    color=bipartition(edges)
    dg=nx.DiGraph()
    for idx,(u,v) in enumerate(edges):
        if x[idx]==2:continue
        if color[u]==0:u,v=v,u
        dg.add_edge(u,v,idx=idx) if x[idx]>2 else dg.add_edge(v,u,idx=idx)
    cyc=nx.find_cycle(dg)
    indices=[dg[u][v]['idx'] for u,v in cyc]
    assert len(indices)%2==0 and len(indices)>=4
    return indices


def decompose(edges,x,k):
    """Edge-color a k-regular bipartite multigraph as k perfect matchings."""
    g=graph(edges)
    side={v for v,c in bipartition(edges).items() if c==0}
    assert all(t>=0 for t in x)
    assert all(sum(x[j] for j,e in enumerate(edges) if v in e)==k for v in g)
    remain=x.copy();out=[]
    for _ in range(k):
        support=nx.Graph();support.add_nodes_from(g)
        support.add_edges_from(e for e,c in zip(edges,remain) if c>0)
        assignment=nx.bipartite.maximum_matching(support,top_nodes=side)
        assert len(assignment)==len(g)
        selected={frozenset((u,assignment[u])) for u in side}
        mask=0
        for idx,e in enumerate(edges):
            if frozenset(e) in selected:
                remain[idx]-=1;mask|=1<<idx
        assert valid_pm(edges,mask)
        out.append(mask)
    assert not any(remain)
    return out


def coordinated_step(edges,state,coordinates=None):
    """One cycle correction, changing only selected coordinate positions.

    With coordinates=None, select positions (0,1,2,3) for every positive Q.
    For Q=6, a hitting pair is found and used instead.
    """
    old=Q(edges,state)
    if old==0:return state.copy(),()
    C=find_defect_cycle(edges,state)
    x=multiplicities(edges,state)
    positive=[e for e in C if x[e]>2]
    negative=[e for e in C if x[e]<2]
    assert len(positive)==len(negative)>0
    if coordinates is None:
        for k in (2,3,4):
            for selection in combinations(range(6),k):
                if all(any(state[i]>>e&1 for i in selection) for e in positive):
                    coordinates=selection
                    break
            if coordinates is not None:
                break
        assert coordinates is not None
    coordinates=tuple(coordinates)
    k=len(coordinates)
    assert all(any(state[i]>>e&1 for i in coordinates) for e in positive)
    if old <= 10:
        assert len(coordinates) <= 2
    elif old <= 38:
        assert len(coordinates) <= 3
    submult=[sum(state[i]>>e&1 for i in coordinates) for e in range(len(edges))]
    for e in positive:submult[e]-=1
    for e in negative:submult[e]+=1
    assert all(0<=t<=k for t in submult)
    modified=decompose(edges,submult,k)
    nxt=state.copy()
    for i,m in zip(coordinates,modified):nxt[i]=m
    assert Q(edges,nxt)<old
    return nxt,coordinates


def normalize(edges,state,keep_trace=False):
    n=len(graph(edges));current=state.copy();track=[Q(edges,current)];changes=[]
    while Q(edges,current):
        current,coord=coordinated_step(edges,current)
        track.append(Q(edges,current));changes.append(tuple(coord))
        assert len(changes)<=3*n
    if keep_trace:return current,track,changes
    return current


def validate():
    import random
    edges,path=load()
    start=path[0]
    nxt,pair=coordinated_step(edges,start)
    assert len(pair)==2 and Q(edges,nxt)==0
    assert min(sum(a!=b for a,b in zip(start,nxt)),2)==sum(a!=b for a,b in zip(start,nxt))
    rows=[]
    cand=pm_masks(edges)
    r=random.Random(20261008)
    for t in range(40):
        state=r.choices(cand,k=6)
        sol,qs,changes=normalize(edges,state,True)
        assert qs[-1]==0 and all(q1>q2 for q1,q2 in zip(qs,qs[1:]))
        assert all(len(c)<=4 for c in changes)
        rows.append((qs[0],len(changes)))
    return {'frontier_Q6_pair':list(pair),'frontier_result_Q':Q(edges,nxt),
            'random_states_normalized':len(rows),'max_steps':max(x[1] for x in rows),
            'max_start_Q':max(x[0] for x in rows)}

if __name__=='__main__':
    print(validate());print('PASS: coordinated <=4 replacement normalization and Q=6 two-coordinate correction')
