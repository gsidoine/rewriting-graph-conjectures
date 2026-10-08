"""Tiny standard-library-only checker for the 18-vertex plateau certificate.

Does not depend on NetworkX, search code, LP solvers, or the historic repo.
Run from any current working directory:
  python berge_fulkerson/plateau/standalone_checker.py
"""
import json
from pathlib import Path
from itertools import combinations

HERE=Path(__file__).resolve().parent
base=json.loads((HERE/'sharp_18_vertex.json').read_text())
dual=json.loads((HERE/'sharp_18_vertex_duals.json').read_text())['dual_potentials']
E=[tuple(e) for e in base['edges']]
P=[base[key] for key in ('matching_masks_initial','matching_masks_neutral','matching_masks_target')]


def is_pm(mask):
    d=[0]*18
    for i,(u,v) in enumerate(E):
        if mask>>i&1:d[u]+=1;d[v]+=1
    return all(x==1 for x in d)


def q(state):
    return sum((sum(m>>e&1 for m in state)-2)**2 for e in range(len(E)))


def connected_after(removal):
    adj=[[] for _ in range(18)]
    for i,(u,v) in enumerate(E):
        if i not in removal:adj[u].append(v);adj[v].append(u)
    visited={0};todo=[0]
    for u in todo:
        for v in adj[u]:
            if v not in visited:visited.add(v);todo.append(v)
    return len(visited)==18


def verify():
    assert len(E)==27 and len(set(frozenset(e) for e in E))==27
    assert all(0<=u<=8< v<=17 for u,v in E)
    degree=[0]*18
    for u,v in E:degree[u]+=1;degree[v]+=1
    assert set(degree)=={3}
    assert all(connected_after(removal) for k in (0,1,2)
               for removal in combinations(range(27),k))
    assert all(len(st)==6 and all(is_pm(m) for m in st) for st in P)
    assert [q(st) for st in P]==[6,6,0]
    assert [sum(a!=b for a,b in zip(P[j],P[j+1])) for j in (0,1)]==[1,1]
    mult=[sum(m>>e&1 for m in P[0]) for e in range(27)]
    assert len(dual)==6
    for i,(mask,pot) in enumerate(zip(P[0],dual)):
        assert len(pot)==18
        weights=[2*(mult[j]-2)+1-2*((mask>>j)&1) for j in range(27)]
        for j,(u,v) in enumerate(E):
            assert pot[u]+pot[v]<=weights[j]
            if mask>>j&1:assert pot[u]+pot[v]==weights[j]
    return {'n':18,'edges':27,'checked_edge_deletions':1+27+351,
            'coordinate_dual_witnesses':6,'path_Q':[6,6,0],
            'result':'PASS'}

if __name__=='__main__':
    print(json.dumps(verify(),sort_keys=True))
