"""Exact polynomial-time optimization of a TWO-matching coordinate block.

The two new matchings form an integral 2-regular bipartite multigraph,
so their optimal aggregate can be obtained via convex-cost min-cost flow
with two unit-capacity marginal arcs per graph edge.

This block optimizer is not a proof of global two-coordinate convergence.
"""
from itertools import combinations
import networkx as nx
from .sharp_trap import graph, multiplicities,Q,valid_pm
from .aggregate_descent import bipartition
from .bounded_coordinate_descent import decompose


def optimize_two(edges,state,i,j):
    assert 0 <= i < j < 6
    G=graph(edges);color=bipartition(edges)
    L={u for u,c in color.items() if c==0};R=set(G)-L
    base=[sum((state[z]>>t)&1 for z in range(6) if z not in (i,j)) for t in range(len(edges))]
    net=nx.DiGraph()
    source=('source',); sink=('sink',)
    net.add_node(source,demand=-2*len(L));net.add_node(sink,demand=2*len(L))
    for u in L:net.add_edge(source,('l',u),capacity=2,weight=0)
    for v in R:net.add_edge(('r',v),sink,capacity=2,weight=0)
    slots=[]
    for idx,(u,v) in enumerate(edges):
        if u not in L:u,v=v,u
        for order in (0,1):
            node=('edge',idx,order)
            cost=2*(base[idx]-2)+1+2*order
            net.add_edge(('l',u),node,capacity=1,weight=cost)
            net.add_edge(node,('r',v),capacity=1,weight=0)
            slots.append(node)
    flux=nx.min_cost_flow(net)
    updated=[sum(flux[('l',u)][('edge',idx,order)] for order in (0,1))
             for idx,(u,v) in enumerate(edges) for u in ([u] if u in L else [v])]
    assert len(updated)==len(edges)
    assert all(0<=v<=2 for v in updated)
    factors=decompose(edges,updated,2)
    nxt=state.copy();nxt[i]=factors[0];nxt[j]=factors[1]
    assert all(valid_pm(edges,m) for m in nxt)
    return nxt,Q(edges,nxt)


def optimize_best_pair(edges,state):
    value=Q(edges,state);best=state.copy();pair=None
    for i,j in combinations(range(6),2):
        nxt,q=optimize_two(edges,state,i,j)
        if q<value:value=q;best=nxt;pair=(i,j)
    return best,value,pair


def validate():
    from .sharp_trap import load,pm_masks
    from random import Random
    edges,path=load()
    A=pm_masks(edges);rnd=Random(20261008)
    for trial in range(12):
        state=rnd.choices(A,k=6)
        nxt,optimal,pair=optimize_best_pair(edges,state)
        brute=min(Q(edges,state[:i]+[a]+state[i+1:j]+[b]+state[j+1:])
                  for i,j in combinations(range(6),2) for a in A for b in A)
        assert optimal==brute,(trial,optimal,brute)
    return {'random_cases':12,'perfect_matchings':len(A),'all_two_coordinate_pairs':15,
            'validation':'exact flow optimizer = brute force'}

if __name__=='__main__':print(validate())
