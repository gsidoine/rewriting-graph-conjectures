"""Small independent three-edge-cut synchronization checks.
Run: pytest -q tests/test_three_cut_synchronization.py
The host graph is the triangular prism; the 3-edge cut separates its triangles.
"""
from itertools import combinations, product
from collections import Counter,defaultdict,deque

E=[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
CUT=(6,7,8)
ADJ=[[i for i,(u,v) in enumerate(E) if x in (u,v)] for x in range(6)]

def is_even(mask):
    return all(sum(bool(mask&(1<<e)) for e in adjacent)%2==0 for adjacent in ADJ)

def is_matching(mask):
    return all(sum(bool(mask&(1<<e)) for e in adjacent)==1 for adjacent in ADJ)

def is_double(S):
    return all(sum(bool(m&(1<<e)) for m in S)==2 for e in range(9))

def sig(S):
    return tuple(frozenset(j for j,m in enumerate(S) if m&(1<<e)) for e in CUT)

def components(mask):
    pending={e for e in range(9) if mask&(1<<e)}
    result=[]
    while pending:
        component={pending.pop()}
        while True:
            verts={v for e in component for v in E[e]}
            nxt={j for j in pending if verts.intersection(E[j])}
            if not nxt:break
            component.update(nxt)
            pending.difference_update(nxt)
        result.append(sum(1<<e for e in component))
    return result

def verify_certificates(S,k):
    sign=sig(S)
    assert all(len(z)==2 for z in sign)
    count=Counter(i for z in sign for i in z)
    if k=="even":
        assert sorted(count.values())==[2,2,2]
        assert len({frozenset(p) for p in sign})==3
    else:assert sorted(count.values())==[1]*6
    checks=0
    for a,b in combinations(range(len(S)),2):
        for cycle in components(S[a]^S[b]):
            assert sum(bool(cycle&(1<<e)) for e in CUT) in (0,2)
            T=list(S);T[a]^=cycle;T[b]^=cycle
            assert is_double(T)
            assert all(is_even(t) if k=="even" else is_matching(t) for t in T)
            checks+=1
    return checks

def test_cycle_cover_cut_and_switches():
    even=[m for m in range(1<<9) if is_even(m)]
    covers=[x for x in product(even,repeat=3) if is_double(x)]
    assert len(covers)==6
    assert sum(verify_certificates(x,"even") for x in covers)==18

def test_matching_cover_cut_and_switches():
    pm=[m for m in range(1<<9) if is_matching(m)]
    covers=[x for x in product(pm,repeat=6) if is_double(x)]
    assert len(covers)==90
    assert sum(verify_certificates(x,"matching") for x in covers)==1080

def test_typed_fiber_product_components():
    # Two connected 2-point fibers over each of four signatures.
    # Local signature graphs each connected, intersection disconnected.
    S=range(4)
    Ha={(0,1),(1,2),(2,3)}
    Hb={(0,1),(1,3),(2,3)}
    common=Ha & Hb
    states=list(product(S,range(2),range(2)))
    def near(p,q):
        s,a,b=p;t,c,d=q
        if s==t:return (a!=c and b==d) or (a==c and b!=d)
        return tuple(sorted((s,t))) in common and a==b==c==d==0
    def reachable(start):
        seen={start};todo=deque([start])
        while todo:
            u=todo.popleft()
            for v in states:
                if v not in seen and near(u,v):
                    seen.add(v);todo.append(v)
        return {s for s,a,b in seen}
    assert reachable((0,1,1))=={0,1}
    assert reachable((2,1,1))=={2,3}

if __name__=="__main__":
    test_cycle_cover_cut_and_switches()
    test_matching_cover_cut_and_switches()
    test_typed_fiber_product_components()
    print("PASS 6 3-CDC states; 90 six-matching covers; exact synchronized-product toy model")
