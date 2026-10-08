"""Exact colour-resistance to Fan--Raspaud residual-kernel realization."""
from __future__ import annotations
from itertools import combinations
from collections import defaultdict
import json
from pathlib import Path

# Independent from the prior certificate module except the final verifier.
def dangling_colouring(n, E, omitted):
    """Colour edges E minus omitted and the two stubs of each omitted edge
    with 0,1,2 so that every vertex sees the three colours.
    Return (colours_on_edges, colours_on_stubs) or None.
    """
    omitted=set(omitted)
    inc=[[] for _ in range(n)]
    # Variables: one for each present edge, one per missing endpoint.
    variables=[]
    for i,(u,v) in enumerate(E):
        if i in omitted:
            variables.extend([(i,u),(i,v)])
        else:
            variables.append((i,None))
    for j,key in enumerate(variables):
        i, endpoint=key
        vs=[endpoint] if endpoint is not None else list(E[i])
        for v in vs:inc[v].append(j)
    assert all(len(x)==3 for x in inc)
    adj=[[] for _ in variables]
    for ids in inc:
        for i in ids:
            adj[i].extend(j for j in ids if j!=i)
    assignment=[-1]*len(variables)
    # force one edge label symmetry break
    assignment[0]=0
    def dfs(left):
        if left==0:return True
        choices=[]
        for j in range(len(variables)):
            if assignment[j]!=-1:continue
            taken={assignment[z] for z in adj[j] if assignment[z]!=-1}
            opt=[c for c in range(3) if c not in taken]
            if not opt:return False
            choices.append((len(opt),j,opt))
        _,j,opt=min(choices)
        for c in opt:
            assignment[j]=c
            if dfs(left-1):return True
        assignment[j]=-1
        return False
    if not dfs(len(variables)-1):return None
    cols={};stubs={}
    for (i,endpoint),c in zip(variables,assignment):
        if endpoint is None:cols[i]=c
        else:stubs[(i,endpoint)]=c
    return cols,stubs


def realize(n, E, omitted, colouring):
    """Return simple cubic G and frozen matching indices from K deleting A."""
    edgecolors,stubs=colouring
    om=set(omitted)
    assert all(stubs[(i,u)]!=stubs[(i,v)] for i in omitted for u,v in [E[i]])
    G=[]; labels=[];classes=[]
    def add(a,b,lab):
        G.append(tuple(sorted((a,b))));labels.append(frozenset(lab));classes.append((a,b,tuple(sorted(lab))))
    for i,(u,v) in enumerate(E):
        if i not in om:add(u,v,(edgecolors[i],))
    groups=defaultdict(list)
    for j,i in enumerate(sorted(om)):
        u,v=E[i];p=n+2*j;q=p+1
        add(u,p,(stubs[(i,u)],));add(v,q,(stubs[(i,v)],));add(p,q,())
        groups[stubs[(i,u)]].append((p,i));groups[stubs[(i,v)]].append((q,i))
    for c, ports in groups.items():
        assert len(ports)%2==0
        # by minimality every missing edge has two different stub colours.
        assert len({idx for _,idx in ports})==len(ports)
        for j in range(0,len(ports),2):
            add(ports[j][0],ports[j+1][0],tuple(x for x in range(3) if x!=c))
    N=n+2*len(om)
    assert len(G)==3*N//2 and len(set(G))==len(G)
    assert all(sum(v in e for e in G)==3 for v in range(N))
    Ms=[sorted(G[j] for j,L in enumerate(labels) if c in L) for c in range(3)]
    assert all(len(x)==N//2 and len({v for e in x for v in e})==N for x in Ms)
    return N,sorted(G),Ms,classes


def petersen():
    E=set(tuple(sorted((i,(i+1)%5))) for i in range(5))
    E.update(tuple(sorted((i+5,(i+2)%5+5))) for i in range(5))
    E.update((i,i+5) for i in range(5))
    return 10,sorted(E)

