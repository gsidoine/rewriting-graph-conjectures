"""Compact bipartite assignment LP-dual certificates of one-coordinate optimality.

The proof checker is purely finite integer arithmetic over 27 edges:
  a[left] + b[right] <= w(edge), equality on original matching.
This certifies optimality against *all* perfect matchings without enumeration.
"""
from __future__ import annotations
import json
from pathlib import Path
from .sharp_trap import load, multiplicities, graph, valid_pm

DUAL=Path(__file__).with_name('sharp_18_vertex_duals.json')

def make_dual(edges,state,i):
    # Original left side is vertices 0..8, right side 9..17.
    L=list(range(9));R=list(range(9,18))
    m=multiplicities(edges,state)
    weights=[2*(m[e]-2)+1-2*((state[i]>>e)&1) for e in range(len(edges))]
    matched={}
    for j,(u,v) in enumerate(edges):
        if state[i]>>j &1:
            assert 0<=u<9 and 9<=v<18
            matched[v]=(u,weights[j])
    # Constraints: a[u] - a[mate(w)] <= weight(u,w)-weight(mate(w),w).
    constraints=[(matched[v][0],u,weights[j]-matched[v][1]) for j,(u,v) in enumerate(edges)]
    a={u:0 for u in L}
    for it in range(len(L)):
        updated=False
        for source,target,cost in constraints:
            if a[target]>a[source]+cost:
                a[target]=a[source]+cost;updated=True
        if not updated:break
        assert it<len(L)-1 or not any(a[target]>a[source]+cost for source,target,cost in constraints)
    b={v:matched[v][1]-a[matched[v][0]] for v in R}
    assert all(a[u]+b[v]<=weights[j] for j,(u,v) in enumerate(edges))
    assert all(a[u]+b[v]==weights[j] for j,(u,v) in enumerate(edges) if state[i]>>j&1)
    return [a[u] for u in L]+[b[v] for v in R]


def verify_duals(duals):
    edges,path=load();state=path[0];m=multiplicities(edges,state)
    assert len(duals)==6
    for i,D in enumerate(duals):
        assert len(D)==18 and valid_pm(edges,state[i])
        weights=[2*(m[j]-2)+1-2*((state[i]>>j)&1) for j in range(len(edges))]
        assert all(D[u]+D[v]<=weights[j] for j,(u,v) in enumerate(edges))
        assert all(D[u]+D[v]==weights[j] for j,(u,v) in enumerate(edges) if state[i]>>j&1)
        assert sum(D)==sum(weights[j] for j in range(len(edges)) if state[i]>>j&1)
    return True

if __name__=='__main__':
    edges,path=load()
    duals=[make_dual(edges,path[0],i) for i in range(6)]
    assert verify_duals(duals)
    DUAL.write_text(json.dumps({'description':'Per-matching integer dual potentials, vertices 0..17',
                                'dual_potentials':duals},indent=2)+'\n')
    print('6 potential vectors:',*duals,sep='\n')
    print('PASS: all 6 bipartite assignment duals certify strict one-coordinate local minimum')
