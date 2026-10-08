"""Two-fold graph covering with lifted LP dual certificates.

A cover replicates matching multiplicities and bipartite dual potentials.
Hence local optimality is stable under *any* finite cover of this base graph.
"""
from __future__ import annotations
import json
import networkx as nx
from .sharp_trap import load, Q, graph, valid_pm, minimum_deltas
from .dual_certificate import DUAL, verify_duals


def double_cover(edges,path,twisted_edge_indices):
    twisted=set(twisted_edge_indices)
    newedges=[]
    for j,(u,v) in enumerate(edges):
        for t in (0,1):
            newedges.append((2*u+t,2*v+(t^(j in twisted))))
    lifted=[]
    for state in path:
        lifted.append([sum(1<<(2*j+t) for j in range(len(edges)) if m>>j&1 for t in (0,1))
                      for m in state])
    return newedges,lifted


def girth(g):
    shortest=10**9
    for v in g:
        # exact BFS lengths to detect shortest cycle
        distance={v:0};parent={v:-1};queue=[v]
        for u in queue:
            for w in g[u]:
                if w not in distance:
                    distance[w]=distance[u]+1;parent[w]=u;queue.append(w)
                elif parent[u]!=w:
                    shortest=min(shortest,distance[u]+distance[w]+1)
    return shortest


def verify_cover_duals(newedges,newpath,old_duals):
    from .sharp_trap import multiplicities
    m=multiplicities(newedges,newpath[0])
    for i,D in enumerate(old_duals):
        pot=[D[j//2] for j in range(36)]
        w=[2*(m[j]-2)+1-2*((newpath[0][i]>>j)&1) for j in range(len(newedges))]
        assert all(pot[u]+pot[v]<=w[j] for j,(u,v) in enumerate(newedges))
        assert all(pot[u]+pot[v]==w[j] for j,(u,v) in enumerate(newedges)
                   if newpath[0][i]>>j&1)
    return True


def validate():
    edges,path=load()
    duals=json.loads(DUAL.read_text())['dual_potentials']
    assert verify_duals(duals)
    newedges,newpath=double_cover(edges,path,{0,6})
    g=graph(newedges)
    assert len(g)==36 and all(g.degree(v)==3 for v in g)
    assert nx.is_bipartite(g) and nx.is_connected(g)
    assert girth(g)>=6
    assert [Q(newedges,s) for s in newpath]==[12,12,0]
    assert all(all(valid_pm(newedges,mask) for mask in state) for state in newpath)
    assert verify_cover_duals(newedges,newpath,duals)
    return dict(vertices=len(g),girth=girth(g),edge_connectivity=nx.edge_connectivity(g),
                Q_path=[Q(newedges,s) for s in newpath],
                dual_certificates=6,twisted_edges=[0,6])

if __name__=='__main__':
    print(json.dumps(validate(),sort_keys=True))
    print('PASS: connected bipartite girth >=6 cover inherits all 6 matching dual certificates')
