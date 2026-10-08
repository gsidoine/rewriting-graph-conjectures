"""Construct locally exact bipartite repair certificates with 2- or 3-coordinate changes.

This implementation deliberately uses only the Python standard library. Given
an explicit edge-labelled bipartite graph, it repairs one connected component
of nonzero multiplicity defect at a time while preserving all other edge
multiplicities. The hitting condition is necessary and sufficient for the
single-component exact repair. NOT a proof that such a hit exists globally.
"""
from __future__ import annotations
import json
from collections import deque
from itertools import combinations
from pathlib import Path

Q34 = Path(__file__).resolve().parents[1] / 'q34_witness_32.json'

def load(path=Q34):
    raw=json.loads(Path(path).read_text())
    n=raw['vertices']; E=[(u,v) for u,v,_ in raw['edges']]
    assert n%2==0 and all(u<n//2<=v for u,v in E)
    assert len(E)==3*n//2 and len(set(E))==len(E)
    M=[{j for j,(_,_,S) in enumerate(raw['edges']) if i in S} for i in range(6)]
    assert all(len(mm)==n//2 for mm in M)
    for mm in M:
        deg=[0]*n
        for e in mm:
            u,v=E[e];deg[u]+=1;deg[v]+=1
        assert all(d==1 for d in deg)
    return n,E,M

def mult(E,M):
    return [sum(e in mm for mm in M) for e in range(len(E))]

def energy(E,M):
    return sum((v-2)**2 for v in mult(E,M))

def defect_components(n,E,M):
    m=mult(E,M)
    A=[[] for _ in range(n)]
    for e,(u,v) in enumerate(E):
        if m[e]!=2:
            A[u].append((v,e));A[v].append((u,e))
    seen=set(); comps=[]
    for start in range(n):
        if start in seen or not A[start]: continue
        seen.add(start);dq=deque([start]); es=set()
        while dq:
            u=dq.popleft()
            for v,e in A[u]:
                es.add(e)
                if v not in seen: seen.add(v);dq.append(v)
        comps.append(sorted(es))
    return comps

def hit(E,M,C,maxwidth=6):
    m=mult(E,M)
    for k in range(maxwidth+1):
        for I in combinations(range(6),k):
            if all(sum(e in M[i] for i in I) >= m[e]-2 for e in C if m[e]>2):
                return I
    return None

def factor_into_matchings(n,E,counts,r):
    """Find an r-edge-colouring of a balanced bipartite r-regular multigraph."""
    h=n//2; counts=list(counts); factors=[]
    assert all(0<=x<=r for x in counts)
    for t in range(r):
        adj=[[] for _ in range(h)]
        for e,(u,v) in enumerate(E):
            if counts[e]>0: adj[u].append((v-h,e))
        matched_right=[None]*h
        def extend(u,seen):
            for v,e in adj[u]:
                if v in seen:continue
                seen.add(v)
                if matched_right[v] is None or extend(matched_right[v][0],seen):
                    matched_right[v]=(u,e)
                    return True
            return False
        for u in range(h):
            assert extend(u,set()), 'The proposed residual is not r-regular bipartite'
        factor={e for u,e in matched_right if u is not None}
        assert len(factor)==h
        for e in factor: counts[e]-=1
        factors.append(factor)
    assert not any(counts)
    return factors

def repair_component(n,E,M,C,width=2):
    """Return a new sextuple fixing precisely component C, or None if no hit."""
    I=hit(E,M,C,width)
    if I is None: return None
    m=mult(E,M)
    counts=[sum(e in M[i] for i in I) for e in range(len(E))]
    for e in C: counts[e]+=2-m[e]
    assert all(x>=0 for x in counts)
    factors=factor_into_matchings(n,E,counts,len(I))
    out=[set(mm) for mm in M]
    for i,ff in zip(I,factors):out[i]=ff
    nm=mult(E,out)
    assert all(nm[e]==(2 if e in C else m[e]) for e in range(len(E)))
    return I,out

def full_component_repair(n,E,M,width=2):
    trace=[];cur=[set(mm) for mm in M]
    while (comps:=defect_components(n,E,cur)):
        successes=[]
        for C in comps:
            next_state=repair_component(n,E,cur,C,width)
            if next_state:successes.append((C,next_state))
        if not successes:break
        # favor smallest available defect component to make tests deterministic
        C,(I,nxt)=min(successes,key=lambda x:(len(x[0]),x[0]))
        trace.append({'before':energy(E,cur),'after':energy(E,nxt),'coordinates':list(I),
                      'edges_fixed':C,'replacement_edge_ids':[[int(j) for j in sorted(nxt[i])] for i in I]})
        assert energy(E,nxt)<energy(E,cur)
        cur=nxt
    return cur,trace


def demonstrate():
    n,E,M=load()
    comps=defect_components(n,E,M)
    print('Original Q =',energy(E,M),'components=',
          [(len(C),sum((mult(E,M)[e]-2)**2 for e in C),len(hit(E,M,C))) for C in comps])
    fixed,trace=full_component_repair(n,E,M,width=2)
    print('Defect trace =',[energy(E,M)]+[step['after'] for step in trace])
    assert energy(E,fixed)==0 and len(trace)==3
    destination=Path(__file__).with_name('q34_three_pair_repair.json')
    destination.write_text(json.dumps({'source':str(Q34.name),'n':n,'original_energy':34,'steps':trace},indent=2)+'\n')
    print('PASS: componentwise 2-coordinate exact repairs;',len(trace),'steps; written',destination.name)

if __name__=='__main__':demonstrate()
