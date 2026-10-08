"""Independent realization and verification of uniform obstruction hypergraphs.

An (k+1)-uniform hypergraph H on h labels is encoded in a d-regular
bipartite certificate with t=k*d labelled perfect matchings and target k.
The canonical monotone states have Q=2*d*(# hyperedges not yet hit).
This file uses only the Python standard library except for optional connectivity.
"""
from __future__ import annotations
from itertools import combinations
from collections import defaultdict
from math import ceil


def construct(h, hyperedges, k, c=1):
    E = sorted(set(tuple(sorted(s)) for s in hyperedges))
    assert k >= 1 and c >= 1 and h >= k+1 and E
    assert all(len(s)==k+1 and len(set(s))==k+1 and 0<=min(s) and max(s)<h for s in E)
    r=ceil(c/2)
    d=max(3,ceil((h+k)/k),c+2*r)
    t=k*d
    anchors=tuple(range(h,h+k))
    q=len(E)
    labels={}
    owners={}
    def edge(b,i,j): return (b*d+i,q*d+b*d+j)
    for b,S in enumerate(E):
        available=[a for a in range(t) if a not in S and a not in anchors]
        assert len(available)>=k-1
        labels[b]={0:tuple(S),1:tuple(available[:k-1]),2:anchors}
        rest=available[k-1:]
        assert len(rest)==(d-3)*k
        for f in range(3,d):labels[b][f]=tuple(rest[(f-3)*k:(f-2)*k])
        assert sorted(a for col in labels[b].values() for a in col)==list(range(t))
        for i in range(d):
            for j in range(d): owners[edge(b,i,j)]=set()
        for f,coords in labels[b].items():
            for i in range(d):
                owners[edge(b,i,(i+f)%d)].update(coords)
    for b in range(q-1):
        for step in range(r):
            # left endpoints disjoint on both adjacent links
            choices=[]
            for block in (b,b+1):
                ix=step+(r if block==b and b>0 else 0)
                # incoming link in block b used rows 0..r-1; outgoing rows r..2r-1.
                # block b+1 incoming uses 0..r-1.
                choices.append(edge(block,ix,(ix+2)%d))
            a,z=choices
            assert owners[a]==set(anchors) and owners[z]==set(anchors)
            del owners[a];del owners[z]
            new1=(a[0],z[1]);new2=(z[0],a[1])
            assert new1 not in owners and new2 not in owners
            owners[new1]=set(anchors);owners[new2]=set(anchors)
    return dict(h=h,k=k,c=c,d=d,t=t,r=r,q=q,hyperedges=E,anchors=anchors,
                labels=labels,owners=owners)


def potential(data):
    k=data['k']
    return sum((len(s)-k)**2 for s in data['owners'].values())


def verify(data, exact_connectivity=False):
    h,k,c,d,t,r,q=(data[x] for x in ['h','k','c','d','t','r','q'])
    owners=data['owners']; n=2*q*d
    assert t==k*d and len(owners)==q*d*d
    assert len(set(owners))==len(owners)
    deg=[0]*n;coorddeg=[[0]*n for _ in range(t)]
    for (a,b),S in owners.items():
        assert 0<=a<q*d<=b<n and len(S)<=t
        deg[a]+=1;deg[b]+=1
        for i in S:
            assert 0<=i<t
            coorddeg[i][a]+=1;coorddeg[i][b]+=1
    assert all(x==d for x in deg)
    assert all(all(x==1 for x in m) for m in coorddeg)
    assert potential(data)==2*d*q
    surplus={tuple(sorted(S)) for S in owners.values() if len(S)>k}
    assert surplus==set(data['hyperedges'])
    assert all(len(S) in (k-1,k,k+1) for S in owners.values())
    assert min(d-2*r,2*r)>=c
    out=dict(n=n,edges=len(owners),degree=d,coordinate_count=t,k=k,
             hyperedges=q,initial_Q=potential(data),connectivity_lower_bound=min(d-2*r,2*r))
    if exact_connectivity:
        import networkx as nx
        G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from(owners)
        out['actual_edge_connectivity']=nx.edge_connectivity(G)
        assert out['actual_edge_connectivity']>=c
    return out


def min_transversal(h,hyperedges):
    E=[set(s) for s in hyperedges]
    for sz in range(h+1):
        for I in combinations(range(h),sz):
            if all(set(I)&e for e in E):return I
    raise AssertionError


def direct_repair_width(data):
    k=data['k'];t=data['t'];owners=data['owners']
    for sz in range(t+1):
        for I in combinations(range(t),sz):
            fixed=set(range(t))-set(I)
            if all(len(S&fixed)<=k for S in owners.values()):return I
    raise AssertionError


def monotone_path(data,I):
    k,d,q=data['k'],data['d'],data['q']
    E=data['hyperedges'];owner={e:set(s) for e,s in data['owners'].items()}
    def potential_():return sum((len(s)-k)**2 for s in owner.values())
    history=[potential_()]
    done=set()
    for j in I:
        fresh=[b for b,S in enumerate(E) if j in S and b not in done]
        assert fresh,('nonminimal hitting set',j)
        for b in fresh:
            for x in range(d):
                a=(b*d+x, q*d+b*d+x)
                z=(b*d+x, q*d+b*d+(x+1)%d)
                assert j in owner[a] and j not in owner[z]
                owner[a].remove(j);owner[z].add(j)
            done.add(b)
        history.append(potential_())
        assert history[-1]<history[-2]
    assert len(done)==q and history[-1]==0
    n=2*q*d
    for j in range(data['t']):
        deg=[0]*n
        for (a,b),S in owner.items():
            if j in S:deg[a]+=1;deg[b]+=1
        assert all(x==1 for x in deg)
    return history


def hypergraph_from_graph_edges(h,edges,k):
    E=sorted(set(tuple(sorted(e)) for e in edges))
    assert all(0<=a<b<h for a,b in E)
    return h+(k-1)*len(E), [tuple([a,b]+list(range(h+(k-1)*i,h+(k-1)*(i+1)))) for i,(a,b) in enumerate(E)]


if __name__=='__main__':
    cases=[('triangle_k1',3,[(0,1),(1,2),(0,2)],1,2),
           ('triangle_k2',3,[(0,1),(1,2),(0,2)],2,4),
           ('cycle5_k3',5,[(0,1),(1,2),(2,3),(3,4),(0,4)],3,4),
           ('complete4_k2',4,list(combinations(range(4),2)),2,4)]
    for name,h,F,k,c in cases:
        hh,S=hypergraph_from_graph_edges(h,F,k)
        data=construct(hh,S,k,c)
        res=verify(data,exact_connectivity=True)
        width=min_transversal(hh,S)
        repair=direct_repair_width(data)
        history=monotone_path(data,width)
        assert len(width)==len(repair)
        print(name,res,'width',len(repair),'history',history,flush=True)
    print('ALL MULTICOVER CERTIFICATES VERIFIED',flush=True)
