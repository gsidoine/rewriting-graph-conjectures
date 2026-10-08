"""Exact finite reduction from vertex cover to direct-repair width.

Given a finite simple graph H and a prescribed edge-connectivity lower bound c,
construct a simple d-regular bipartite graph G and d explicitly listed perfect
matchings. The conflict graph of the matchings is exactly H plus isolated vertices.

No optimizer is trusted for construction or certificate checks.
"""
import json,math,itertools
from collections import defaultdict


def construct(h, host_edges, c):
    assert h>=2 and c>=1 and host_edges
    edges_h={tuple(sorted(e)) for e in host_edges}
    assert all(0<=a<b<h for a,b in edges_h)
    r=max(1,(c+1)//2)
    d=max(h+r,4*r+c)
    M=len(edges_h)
    blocks=sorted(edges_h)
    # vertices: left 0..M*d-1; right M*d..2*M*d-1
    def left(b,i):return b*d+i
    def right(b,j):return M*d+b*d+j
    edge_owners=defaultdict(set)
    anchor=list(range(h,h+r))
    factor=[]
    for b,(a,z) in enumerate(blocks):
        labels=[None]*d
        labels[a]=labels[z]=0
        f=1
        for j in range(d):
            if labels[j] is None:
                labels[j]=f;f+=1
        assert f==d-1
        factor.append(labels)
        for i in range(d):
            for k in range(d):
                edge_owners[(left(b,i),right(b,k))]=set()
        for j in range(d):
            for i in range(d):
                edge_owners[(left(b,i),right(b,(i+labels[j])%d))].add(j)
    # For each chain link select one singleton edge in each block per anchor,
    # with unique left and right endpoints across all incident chain links.
    used_left=[set() for _ in blocks]
    used_right=[set() for _ in blocks]
    swaps=[]
    for b in range(M-1):
        for j in anchor:
            pair=[]
            for block in (b,b+1):
                shift=factor[block][j]
                i=next(i for i in range(d) if i not in used_left[block] and (i+shift)%d not in used_right[block])
                k=(i+shift)%d
                used_left[block].add(i);used_right[block].add(k)
                pair.append((left(block,i),right(block,k)))
            (u,v),(x,y)=pair
            assert edge_owners[(u,v)]=={j} and edge_owners[(x,y)]=={j}
            del edge_owners[(u,v)];del edge_owners[(x,y)]
            assert (u,y) not in edge_owners and (x,v) not in edge_owners
            edge_owners[(u,y)].add(j);edge_owners[(x,v)].add(j)
            swaps.append((j,((u,v),(x,y)),((u,y),(x,v))))
    assert all(len(p)<=2 for p in edge_owners.values())
    return dict(h=h,H_edges=[list(e) for e in blocks],c=c,anchors=anchor,d=d,r=r,n=2*M*d,
                edges=[[u,v,sorted(q)] for (u,v),q in sorted(edge_owners.items())],
                swaps=len(swaps),nblocks=M)


def verify(data,exact_connectivity=False):
    h=data['h'];d=data['d'];n=data['n'];m=data['nblocks']
    E=data['edges']; assert len(E)==m*d*d
    assert len({(u,v) for u,v,_ in E})==len(E)
    degree=[0]*n;ownership=[set() for _ in range(d)]
    conflict=set()
    for u,v,colors in E:
        assert 0<=u<m*d<=v<n
        degree[u]+=1;degree[v]+=1
        for j in colors:
            assert 0<=j<d
            ownership[j].add((u,v))
        for a,b in itertools.combinations(colors,2):conflict.add((a,b))
    assert all(v==d for v in degree)
    assert all(len(S)==n//2 for S in ownership)
    for j,S in enumerate(ownership):
        deg=[0]*n
        for u,v in S:deg[u]+=1;deg[v]+=1
        assert all(x==1 for x in deg),(j,deg)
    assert conflict==set(map(tuple,data['H_edges']))
    assert data['d']-2*data['r']>=data['c'] and 2*data['r']>=data['c']
    # Every component is initially K_{d,d}; in the chain at most 2r edges
    # were removed per component. Therefore any cut splitting a block has
    # at least d-2r remaining internal edges. Whole-block cuts cross a chain
    # link containing 2r edges.
    # Optionally independently compute global edge connectivity.
    result=dict(n=n,edges=len(E),degree=d,matching_count=d,
                host_edges=len(data['H_edges']),conflict_edges=len(conflict),
                theoretical_lambda_lower_bound=min(d-2*data['r'],2*data['r']))
    if exact_connectivity:
        import networkx as nx
        G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from((u,v) for u,v,_ in E)
        result['actual_edge_connectivity']=nx.edge_connectivity(G)
        assert result['actual_edge_connectivity']>=data['c']
    return result


def vertex_cover_brute(h,edges):
    for z in range(h+1):
        for C in itertools.combinations(range(h),z):
            cs=set(C)
            if all(a in cs or b in cs for a,b in edges):return z
    raise AssertionError


def width_brute(data):
    d=data['d'];edges=data['edges']
    for z in range(d+1):
        for I in itertools.combinations(range(d),z):
            change=set(I)
            if all(len(set(colors)-change)<=1 for u,v,colors in edges):return z
    raise AssertionError

if __name__=='__main__':
    cases=[('P4',4,[(0,1),(1,2),(2,3)],2),
           ('C5',5,[(0,1),(1,2),(2,3),(3,4),(0,4)],4),
           ('K5',5,list(itertools.combinations(range(5),2)),4)]
    for name,h,H,c in cases:
        data=construct(h,H,c)
        res=verify(data,exact_connectivity=True)
        w=width_brute(data);v=vertex_cover_brute(h,H)
        assert w==v
        print(name,res,'width=',w,'vertex_cover=',v,flush=True)
        if name=='C5':
            with open('/mnt/data/campaign_v7/coordination_theory/c5_c4_certificate.json','w') as f:json.dump(data,f,indent=2)
    print('ALL CERTIFICATES VERIFIED')
