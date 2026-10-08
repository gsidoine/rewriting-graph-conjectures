"""Dependency-free independent exact audit of FR-triple uphill barriers.

Run as: python applications/berge_fulkerson/plateau/energy_barriers/standalone_audit.py
Computation: complete PM enumeration, sublevel connectivity, explicit path,
3-edge-connectivity by all edge deletions of size 0,1,2.
"""
from __future__ import annotations
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def all_pm(n, E):
    # Independent DFS using a vertex-set of uncovered vertices.
    inc=[[] for _ in range(n)]
    for a,(u,v) in enumerate(E):inc[u].append((v,a));inc[v].append((u,a))
    result=[]
    def go(free, matching):
        if not free:
            result.append(frozenset(matching));return
        v=min(free)
        for w,i in inc[v]:
            if w in free:go(free-{v,w},matching+(i,))
    go(frozenset(range(n)),())
    assert len(result)==len(set(result))
    return sorted(result,key=lambda s:tuple(sorted(s)))


def cubic_3_connected(n,E):
    assert n%2==0 and len(E)==3*n//2
    assert len({tuple(sorted(p)) for p in E})==len(E)
    degrees=Counter(v for uv in E for v in uv)
    assert [degrees[i] for i in range(n)]==[3]*n
    def connected(ignore):
        adj=[[] for _ in range(n)]
        for k,(v,w) in enumerate(E):
            if k not in ignore:adj[v].append(w);adj[w].append(v)
        seen={0};Q=[0]
        for v in Q:
            for w in adj[v]:
                if w not in seen:seen.add(w);Q.append(w)
        return len(seen)==n
    assert connected(set())
    for size in (1,2):
        for omitted in combinations(range(len(E)),size):
            assert connected(set(omitted)),('low edge connectivity',omitted)
    return True


def study(filename):
    x=json.loads((HERE/filename).read_text())
    n=x['n'];E=[tuple(sorted(z)) for z in x['edges']]
    assert cubic_3_connected(n,E)
    pm=all_pm(n,E)
    pmap={m:i for i,m in enumerate(pm)}
    inv={tuple(e):i for i,e in enumerate(E)}
    def decode(M):return frozenset(inv[tuple(sorted(e))] for e in M)
    def valid(t):return not(pm[t[0]]&pm[t[1]]&pm[t[2]])
    def uncovered(t):return len(set(range(len(E)))-(pm[t[0]]|pm[t[1]]|pm[t[2]]))
    states=[]
    for s in combinations_with_replacement(range(len(pm)),3):
        if valid(s):states.append(s)
    u={s:uncovered(s) for s in states}
    byu=Counter(u.values())
    low={s for s in states if u[s]<=3}
    def neighbors(s):
        out=set()
        for j in range(3):
            f=s[:j]+s[j+1:]
            forbidden=pm[f[0]]&pm[f[1]]
            for m,p in enumerate(pm):
                if p&forbidden:continue
                t=tuple(sorted(f+(m,)))
                if t!=s:out.add(t)
        return out
    initial=tuple(sorted(pmap[decode(m)] for m in x['FR_matchings_example']))
    assert u[initial]==x['initial_u']==3
    Q=deque([initial]);seen={initial}
    while Q:
        for t in neighbors(Q.popleft()):
            if t in low and t not in seen:seen.add(t);Q.append(t)
    assert not any(u[s]==0 for s in seen)
    # Every path entry is independently decoded from edge lists and checked.
    path=[]
    for st in x['path']:
        t=tuple(sorted(pmap[decode(M)] for M in st['matchings']))
        assert valid(t) and uncovered(t)==st['uncovered']
        path.append(t)
    assert path[0]==initial and uncovered(path[-1])==0
    assert path[1:]
    assert all(y in neighbors(v) for v,y in zip(path,path[1:]))
    expected=[3,4,3,0] if n==10 else [3,4,3,2,0]
    assert [u[s] for s in path]==expected
    # All states in the sublevel-three graph can be partitioned into components.
    U=set(low);comps=[]
    while U:
        start=next(iter(U));cc={start};q=[start];U.remove(start)
        for s in q:
            for t in neighbors(s):
                if t in U:U.remove(t);cc.add(t);q.append(t)
        comps.append(cc)
    bad=sorted([len(c) for c in comps if all(u[s]>0 for s in c)])
    assert initial in next(c for c in comps if initial in c)
    if n==10:
        assert len(pm)==6 and len(states)==23 and len(low)==8 and bad==[1]
        assert len(neighbors(initial))==6 and {u[s] for s in neighbors(initial)}=={4}
    if n==24:
        assert len(pm)==64 and len(states)==13508 and len(low)==152 and bad==[36]
    print(f'PASS n={n} edges={len(E)} PM={len(pm)} FR={len(states)} sublevel3={len(low)} bad_component_sizes={bad} path={[u[s] for s in path]}')
    return {'n':n,'edges':E,'pm':pm,'initial':initial,'u':u,'state_count':len(states),'bad':bad}


if __name__=='__main__':
    study('ten_vertex_witness.json')
    study('flower_host24_witness.json')
