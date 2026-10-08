"""Standalone verifier for archived v8 JSON certificates.

Does NOT import any constructor or use a graph solver. Python standard library only.
"""
import json,sys
from pathlib import Path

def inspect_matchings(P,D):
    assert P
    assert all(len(p)==D and sorted(p)==list(range(D)) for p in P)
    counts=[[0]*D for _ in range(D)]
    sig=[[set() for _ in range(D)] for __ in range(D)]
    for z,p in enumerate(P):
        for i,j in enumerate(p):counts[i][j]+=1;sig[i][j].add(z)
    return counts,sig

def quadratic(counts,k):return sum((v-k)**2 for row in counts for v in row)

def check_complete(C):
    k=C['k'];d=C['d'];D=C['D'];E=C['hyperedges'];P=C['permutations']
    assert D==len(E)*d and len(P)==k*D
    counts,sig=inspect_matchings(P,D)
    assert quadratic(counts,k)==2*d*len(E)
    for b,S in enumerate(E):
        for i in range(d):
            assert sig[b*d+i][b*d+i]==set(S)
            assert counts[b*d+i][b*d+i]==k+1
            assert counts[b*d+i][b*d+(i+1)%d]==k-1
    for i in range(D):
        for j in range(D):
            if i//d!=j//d or (j-i)%d not in (0,1): assert counts[i][j]==k
    # Exact transversal minimality by brute enumeration over input hypergraph labels
    from itertools import combinations
    optimum=C['minimum_transversal'];U=set(optimum)
    assert all(U.intersection(S) for S in E)
    for sz in range(len(U)):
        for I in combinations(range(C['h']),sz):
            assert any(set(I).isdisjoint(S) for S in E)
    # Explicit step-by-step strict path, without calling the researcher constructor.
    P=[p[:] for p in P];done=set();hist=[quadratic(counts,k)]
    for a in optimum:
        changed=False
        for b,S in enumerate(E):
            if b in done or a not in S:continue
            for i in range(d):
                assert P[a][b*d+i]==b*d+i
                P[a][b*d+i]=b*d+(i+1)%d
            done.add(b);changed=True
        assert changed
        cc,_=inspect_matchings(P,D)
        hist.append(quadratic(cc,k))
        assert hist[-1]<hist[-2]
    assert len(done)==len(E) and hist[-1]==0
    return {'case':C['name'],'D':D,'k':k,'transversal':len(U),'Q_path':hist}

def check_plateau(C):
    k=C['k'];d=C['d'];P=C['permutations']
    assert len(P)==k*d
    counts,_=inspect_matchings(P,d)
    assert quadratic(counts,k)==4
    for z,p in enumerate(P):
        alpha=C['dual_alpha'][z];beta=C['dual_beta'][z]
        assert len(alpha)==d and len(beta)==d
        for i in range(d):
            for j in range(d):
                weight=2*(counts[i][j]-int(p[i]==j)-k)+1
                assert alpha[i]+beta[j]<=weight
            j=p[i]
            assert alpha[i]+beta[j]==2*(counts[i][j]-1-k)+1
    hist=[4];P=[p[:] for p in P]
    for name in ['neutral_edit','strict_edit']:
        edit=C[name];P[edit['coordinate']][:4]=edit['corner']
        cc,_=inspect_matchings(P,d);hist.append(quadratic(cc,k))
    assert hist==[4,4,0]
    return {'case':C['name'],'d':d,'k':k,'duals_checked':k*d,'Q_path':hist}

if __name__=='__main__':
    folder=Path(__file__).resolve().parent/'certificates'
    for path in sorted(folder.glob('*.json')):
        C=json.loads(path.read_text())
        if C['name'].startswith('complete_'):print('PASS',check_complete(C),flush=True)
        else:print('PASS',check_plateau(C),flush=True)
    print('ALL INDEPENDENT V8 CERTIFICATES VERIFIED',flush=True)
