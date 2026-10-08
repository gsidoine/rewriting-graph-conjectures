"""Independently reproducible exact 18-vertex trap and arbitrarily large lifts.

Run: PYTHONPATH=. python -m berge_fulkerson.plateau.sharp_trap

All graph edges use one-based bit positions in prose but zero-based here.
This module intentionally does NOT import historical BF experimental code.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import networkx as nx

DATA = Path(__file__).with_name('sharp_18_vertex.json')


def load():
    obj = json.loads(DATA.read_text())
    return [tuple(e) for e in obj['edges']], [obj[k] for k in
      ('matching_masks_initial','matching_masks_neutral','matching_masks_target')]


def graph(edges):
    g = nx.Graph()
    g.add_edges_from(edges)
    return g


def valid_pm(edges, mask):
    degrees = Counter(v for i,e in enumerate(edges) if mask >> i & 1 for v in e)
    return set(degrees) == set(graph(edges)) and all(d == 1 for d in degrees.values())


def pm_masks(edges):
    g = graph(edges)
    ids = {frozenset(e): i for i,e in enumerate(edges)}
    def recur(remaining):
        if not remaining:
            yield 0
        else:
            v=min(remaining)
            for w in g.neighbors(v):
                if w in remaining:
                    for partial in recur(remaining-{v,w}):
                        yield partial | (1 << ids[frozenset((v,w))])
    return sorted(set(recur(set(g))))


def multiplicities(edges, states):
    return [sum(mask >> j & 1 for mask in states) for j in range(len(edges))]


def Q(edges, states):
    return sum((m-2)**2 for m in multiplicities(edges, states))


def minimum_deltas(edges, states, candidates=None):
    if candidates is None:
        candidates=pm_masks(edges)
    start=Q(edges,states)
    return [min(Q(edges,states[:i]+[new]+states[i+1:])-start
                for new in candidates) for i in range(6)]


def expand_balanced_vertex(edges, path, vertex):
    """Replace a 2,2,2 vertex by a K_{3,2} 3-pole.

    Six coordinate-labelled matching tuples in `path` must have exactly
    the same external choice at `vertex` in every step. The internal six-edge
    multiplier starts and remains identically 2 throughout the path.
    """
    neighbors=sorted(graph(edges).neighbors(vertex))
    assert len(neighbors)==3
    n=max(max(e) for e in edges)+1
    ports=(n,n+1,n+2)
    hubs=(n+3,n+4)
    old_edges=[]
    for u,v in edges:
        if u==vertex:
            old_edges.append((ports[neighbors.index(v)],v))
        elif v==vertex:
            old_edges.append((u,ports[neighbors.index(u)]))
        else:
            old_edges.append((u,v))
    internal=[(p,h) for p in ports for h in hubs]
    new_edges=old_edges+internal
    internal_ids={frozenset(e):len(edges)+k for k,e in enumerate(internal)}
    choices=[]
    for state in path:
        ch=[]
        for m in state:
            hits=[j for j,z in enumerate(neighbors) for k,e in enumerate(edges)
                   if vertex in e and z in e and (m>>k)&1]
            assert len(hits)==1 and valid_pm(edges,m)
            ch.append(hits[0])
        choices.append(ch)
    assert all(c==choices[0] for c in choices)
    assert Counter(choices[0])=={0:2,1:2,2:2}
    seen=Counter();addon=[]
    for j in choices[0]:
        pair=[k for k in range(3) if k!=j]
        flip=seen[j]; seen[j]+=1
        assert flip in (0,1)
        add=((1<<internal_ids[frozenset((ports[pair[0]],hubs[flip]))]) |
             (1<<internal_ids[frozenset((ports[pair[1]],hubs[1-flip]))]))
        addon.append(add)
    lifted=[[mask|extra for mask,extra in zip(state,addon)] for state in path]
    assert all(all(valid_pm(new_edges,m) for m in st) for st in lifted)
    assert [Q(new_edges,s) for s in lifted]==[Q(edges,s) for s in path]
    return new_edges,lifted,hubs[0]


def validate_base():
    edges, path=load()
    g=graph(edges)
    assert len(g)==18 and len(edges)==27
    assert nx.is_connected(g) and nx.is_bipartite(g)
    assert all(g.degree(v)==3 for v in g)
    assert nx.edge_connectivity(g)==3
    assert all(all(valid_pm(edges,m) for m in state) for state in path)
    allm=pm_masks(edges)
    assert len(allm)==47
    assert all(m in allm for st in path for m in st)
    assert [Q(edges,st) for st in path]==[6,6,0]
    assert sum(a!=b for a,b in zip(path[0],path[1]))==1
    assert sum(a!=b for a,b in zip(path[1],path[2]))==1
    assert minimum_deltas(edges,path[0],allm)==[0]*6
    return edges,path


def validate_family(max_extensions=3):
    edges,path=validate_base()
    rows=[]
    v=json.loads(DATA.read_text())['expansion_vertex']
    for k in range(max_extensions+1):
        g=graph(edges)
        allm=pm_masks(edges)
        assert len(allm)==47 * 2**k
        assert nx.is_bipartite(g) and nx.is_connected(g)
        assert nx.edge_connectivity(g)==3
        assert [Q(edges,s) for s in path]==[6,6,0]
        assert minimum_deltas(edges,path[0],allm)==[0]*6
        rows.append(dict(expansions=k,vertices=len(g),perfect_matchings=len(allm),
                         starting_Q=6,first_move_Q=6,second_move_Q=0,
                         min_one_replacement_change=0,edge_connectivity=3))
        if k<max_extensions:
            edges,path,v=expand_balanced_vertex(edges,path,v)
    return rows

if __name__=='__main__':
    for record in validate_family():
        print(json.dumps(record,sort_keys=True))
    print('PASS: 18-vertex certificate and first three balanced lifts')
