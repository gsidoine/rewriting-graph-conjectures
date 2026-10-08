"""Tests of the FR three-pole transfer operator against independent enumerators."""
from itertools import combinations, product
from collections import Counter, deque
from math import log

from applications.berge_fulkerson.plateau.energy_barriers.transfer_operator import (
    local_states, local_components, audited_local_move_lifts,
    three_pole_operator, direct_FR_polynomial, expanded_graph,
    perfect_matchings, universal_pressure, projected_fibre_size,
)


def test_local_signatures():
    assert Counter(u for _,u in local_states((0,1,2))) == Counter({0:2,2:6})
    assert Counter(u for _,u in local_states((0,0,1))) == Counter({1:4,2:2})
    assert local_components((0,1,2)) == (8,1,3)
    assert local_components((0,0,1)) == (6,1,3)


def test_all_local_projected_moves_lift():
    assert audited_local_move_lifts() == (156,828)


def k4_expansion():
    E=sorted(combinations(range(4),2))
    n2,E2=expanded_graph(4,E)
    return E,n2,E2


def independent_matchings(n, edges):
    adj=[set() for _ in range(n)]
    mapping={}
    for i,(a,b) in enumerate(edges):
        adj[a].add(b);adj[b].add(a)
        mapping[(min(a,b),max(a,b))]=i
    out=set()
    def rec(left,chosen):
        if not left:
            out.add(frozenset(chosen));return
        a=min(left)
        for b in adj[a]&left:
            key=(min(a,b),max(a,b))
            rec(left-{a,b},chosen+(mapping[key],))
    rec(set(range(n)),())
    return out


def brute_polynomial(pm, edge_count):
    full=set(range(edge_count))
    out=Counter()
    for a,b,c in product(pm,repeat=3):
        if a&b&c:continue
        out[len(full-(a|b|c))] += 1
    return out


def test_exact_polynomial_K4():
    E,n2,E2=k4_expansion()
    P0=independent_matchings(4,E)
    P1=independent_matchings(n2,E2)
    assert len(P0)==3 and len(P1)==48 and len(E2)==30
    base=brute_polynomial(P0,len(E))
    expanded=brute_polynomial(P1,len(E2))
    assert base == Counter({0:6,2:18})
    pred=three_pole_operator(4,[base.get(i,0) for i in range(4//2+1)])
    assert Counter({i:c for i,c in enumerate(pred) if c}) == expanded
    assert sum(expanded.values())==47904
    assert expanded==Counter({0:96,2:1152,4:5184,6:14976,7:9216,8:14688,9:2304,10:288})


def test_global_reconfiguration_connected_for_expanded_K4():
    _,N,E=k4_expansion()
    # Independent bitset implementation of perfect-matching enumeration
    P=sorted(sum(1<<i for i in s) for s in independent_matchings(N,E))
    states={(i,j,k) for i,j,k in product(range(len(P)),repeat=3) if not P[i]&P[j]&P[k]}
    assert len(states)==47904
    remaining=states.copy();comp_sizes=[]
    while remaining:
        start=remaining.pop();q=deque([start]);size=1
        while q:
            t=q.popleft()
            for pos in range(3):
                others=[t[h] for h in range(3) if h!=pos]
                forbidden=P[others[0]]&P[others[1]]
                for m in range(len(P)):
                    if P[m]&forbidden:continue
                    x=list(t);x[pos]=m;st=tuple(x)
                    if st in remaining:
                        remaining.remove(st);q.append(st);size+=1
        comp_sizes.append(size)
    assert comp_sizes == [47904]


def test_min_defect_and_minimizer_counts():
    z=[6,0,18]
    n=4
    for t in range(3):
        nz=[(i,x) for i,x in enumerate(z) if x]
        assert nz[0][0] == 0
        assert nz[0][1] == 6*(2**(4*(5**t-1)//4))
        if t<2:
            z=three_pole_operator(n,z)
            n*=5


def test_fixed_component_fibre_sizes():
    assert projected_fibre_size(10,0)==8**10
    assert projected_fibre_size(10,3)==8**4 * 6**6
    assert projected_fibre_size(10,5)==6**10


def test_universal_pressure_numeric():
    p,rho=universal_pressure(1.0)
    assert abs(p-.4792835312641251683)<1e-13
    assert abs(rho-.3296843222147383361)<1e-13
    p0,rho0=universal_pressure(1e-6)
    assert abs(p0-log(2)/4)<1e-5
    assert rho0>=0


def test_petersen_snark_defect_multiplicity_scaling():
    E=set()
    for i in range(5):
        for a,b in ((i,(i+1)%5),(i,i+5),(i+5,5+(i+2)%5)):
            E.add((min(a,b),max(a,b)))
    E=sorted(E)
    assert len(independent_matchings(10,E))==6
    # Petersen has no proper 3-edge-colouring; all ordered FR states have u=3.
    assert brute_polynomial(independent_matchings(10,E),len(E))==Counter({3:120})
    z=three_pole_operator(10,[0,0,0,120,0,0])
    assert next(i for i,c in enumerate(z) if c)==9
    assert z[9]==120*(2**(10+2*3))
