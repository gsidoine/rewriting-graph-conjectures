"""K_{3,2} all-vertex replacement and certificate lift for Fan-Raspaud triples."""
from __future__ import annotations
from itertools import product
from collections import Counter

def expand(n, edges):
    # Original edge i is replaced with an external edge joining its corresponding terminals.
    E=[tuple(sorted(x)) for x in edges];inc=[[] for _ in range(n)]
    for i,(u,v) in enumerate(E):inc[u].append(i);inc[v].append(i)
    assert all(len(x)==3 for x in inc)
    inc=[sorted(x) for x in inc]
    port={(v,e):5*v+z for v in range(n) for z,e in enumerate(inc[v])}
    core={(v,k):5*v+3+k for v in range(n) for k in range(2)}
    newE=[tuple(sorted((port[(u,e)],port[(v,e)]))) for e,(u,v) in enumerate(E)]
    newE+= [tuple(sorted((port[(v,e)],core[(v,k)]))) for v in range(n) for e in inc[v] for k in range(2)]
    newE.sort()
    assert len(newE)==(5*n)*3//2
    assert len(set(newE))==len(newE)
    return 5*n,newE,inc,port,core

def lift_fr(n,E,M):
    """Lift a supplied FR triple with exact u' = 3u."""
    allm=[{tuple(sorted(e)) for e in matching} for matching in M]
    assert len(allm)==3
    E=[tuple(sorted(e)) for e in E]
    n2,E2,inc,port,core=expand(n,E)
    chosen=[set() for j in range(3)]
    for i,(a,b) in enumerate(E):
        for j in range(3):
            if (a,b) in allm[j]:chosen[j].add(tuple(sorted((port[(a,i)],port[(b,i)]))))
    for v in range(n):
        ports=[]
        for j in range(3):
            matches=[z for z,e in enumerate(inc[v]) if E[e] in allm[j]]
            assert len(matches)==1
            ports.append(matches[0])
        assert len(set(ports))>=2,('not FR',v)
        phases=None
        min_u=0 if len(set(ports))==3 else 1
        for bits in product((0,1),repeat=3):
            cov=Counter()
            zips=[]
            for j,(p,b) in enumerate(zip(ports,bits)):
                other=[z for z in range(3) if z!=p]
                pairs=[(other[b],0),(other[1-b],1)]
                zips.append(pairs)
                cov.update(pairs)
            if max(cov.values())<=2 and 6-len(cov)==min_u:
                phases=zips;break
        assert phases is not None
        for j,pairs in enumerate(phases):
            for pos,k in pairs:
                chosen[j].add(tuple(sorted((5*v+pos,core[v,k]))))
    for j in range(3):
        assert len(chosen[j])==n2//2
        assert len({x for a,b in chosen[j] for x in (a,b)})==n2
    assert not chosen[0]&chosen[1]&chosen[2]
    u=lambda E,Ms: sum(all(e not in m for m in Ms) for e in E)
    assert u(E2,chosen)==3*u(E,allm),(u(E2,chosen),u(E,allm))
    return n2,E2,[sorted(x) for x in chosen]

