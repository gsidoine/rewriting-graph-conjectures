"""Exact FR-triple fibre and defect-transfer checks for the K_{3,2} three-pole.

Independent of networkx, scipy or a solver. Run directly for exhaustive local
checks and exact full-tuple checks on expanded K4 and K3,3.
"""
from collections import Counter
from itertools import product
from math import comb


def matching_edges(ports, bits):
    out=[]
    for chosen,b in zip(ports,bits):
        other=[v for v in range(3) if v != chosen]
        out.append(frozenset(((other[b],0),(other[1-b],1))))
    return out


def fr_legal(ports,bits):
    a,b,c=matching_edges(ports,bits)
    return not a.intersection(b,c)


def local_u(ports,bits):
    return 6-len(set.union(*map(set,matching_edges(ports,bits))))


def local_fibre(ports):
    return {bits:local_u(ports,bits) for bits in product((0,1),repeat=3) if fr_legal(ports,bits)}


def verify_local():
    counts={}
    checks=0
    for ports in product(range(3),repeat=3):
        if len(set(ports))==1:continue
        states=local_fibre(ports)
        kind='distinct' if len(set(ports))==3 else 'repeated'
        count=Counter(states.values())
        goal=Counter({0:2,2:6}) if kind=='distinct' else Counter({1:4,2:2})
        assert count==goal,(ports,count,goal)
        # Single-bit edges span a connected local fibre.
        reach={next(iter(states))}
        for _ in range(len(states)):
            reach |= {t for v in list(reach) for t in states if sum(x!=y for x,y in zip(t,v))==1}
        assert len(reach)==len(states)
        counts[kind]=goal
        for bits in states:
            for coordinate in range(3):
                for newport in range(3):
                    nxt=list(ports);nxt[coordinate]=newport
                    if len(set(nxt))==1:continue
                    assert any(fr_legal(nxt,bits[:coordinate]+(newbit,)+bits[coordinate+1:]) for newbit in (0,1)),(ports,bits,coordinate,newport)
                    checks+=1
    assert checks==1296,checks
    return counts,checks


def perfect_matchings(n,E):
    inc=[[] for _ in range(n)]
    for i,(v,w) in enumerate(E):inc[v].append((w,i));inc[w].append((v,i))
    result=[]
    def visit(free,mask):
        if not free:result.append(mask);return
        v=min(free)
        for w,i in inc[v]:
            if w in free:visit(free-{v,w},mask|(1<<i))
    visit(set(range(n)),0)
    assert len(set(result))==len(result)
    return result


def expand(n,E):
    inc=[[] for _ in range(n)]
    for i,(v,w) in enumerate(E):inc[v].append(i);inc[w].append(i)
    assert all(len(x)==3 for x in inc)
    ports={(v,e):5*v+sorted(inc[v]).index(e) for v in range(n) for e in inc[v]}
    out=[tuple(sorted((ports[v,i],ports[w,i]))) for i,(v,w) in enumerate(E)]
    out += [tuple(sorted((5*v+p,5*v+3+c))) for v in range(n) for p in range(3) for c in range(2)]
    return out


def defect_distribution(n,E):
    matches=perfect_matchings(n,E)
    Z=Counter();universe=len(E)
    for a,b,c in product(matches,repeat=3):
        if a&b&c:continue
        Z[universe-(a|b|c).bit_count()]+=1
    return Z,len(matches)


def predicted_distribution(n,Z):
    out=Counter()
    for u,multiplicity in Z.items():
        assert 2*u<=n
        for i in range(n-2*u+1):
            for j in range(2*u+1):
                exponent=u+2*i+(2*u-j)+2*j
                coefficient=comb(n-2*u,i)*6**i*2**(n-2*u-i)*comb(2*u,j)*2**j*4**(2*u-j)
                out[exponent]+=multiplicity*coefficient
    return out


def verify_global(n,E):
    Z,m=defect_distribution(n,E)
    newE=expand(n,E)
    Z2,m2=defect_distribution(5*n,newE)
    assert m2==m*2**n
    assert Z2==predicted_distribution(n,Z)
    # Integer version of Z_T(1)=8^n Z_G(9/16).
    assert sum(Z2.values())*16**(max(Z) if Z else 0)==8**n*sum(v*9**u*16**((max(Z) if Z else 0)-u) for u,v in Z.items())
    return {'base_pm':m,'expanded_pm':m2,'ordered_fr':sum(Z2.values()),'expanded_distribution':dict(sorted(Z2.items()))}

if __name__=='__main__':
    count,checks=verify_local();print('PASS local',checks,count)
    K4=[(i,j) for i in range(4) for j in range(i+1,4)]
    K33=[(i,j) for i in range(3) for j in range(3,6)]
    for name,n,E in [('K4',4,K4),('K3,3',6,K33)]:
        print('PASS global',name,verify_global(n,E))
