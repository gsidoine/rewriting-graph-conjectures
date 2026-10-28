"""Independent brute-force audits of finite-group potential repair."""
from itertools import product
import random

from certificate_coordination.gauge_repair import (
    cyclic_group, permutation_group_3, valid, exact_repair,
    reconfiguration_components, sharp_mode_family,
)


def oracle_repair(n, old, added, x0, grp, weights):
    feasible = [sum(weights[i] for i in range(n) if z[i] != x0[i])
                for z in product(grp.elements,repeat=n)
                if valid(z,old+added,grp)]
    return min(feasible,default=None)


def random_instances(group, seed, repetitions, max_n):
    rng=random.Random(seed)
    for _ in range(repetitions):
        n=rng.randrange(2,max_n+1)
        x0=[rng.choice(group.elements) for _ in range(n)]
        edges=[]
        for u in range(n):
            for v in range(u+1,n):
                if rng.random()<.28:
                    edges.append((u,v,group.mul(x0[v],group.inv(x0[u]))))
        additions=[]
        for _ in range(rng.randint(0,n+2)):
            u=rng.randrange(n)
            v=rng.randrange(n)
            if rng.random()<.50:
                gain=group.mul(x0[v],group.inv(x0[u]))
            else:
                gain=rng.choice(group.elements)
            additions.append((u,v,gain))
        weights=[rng.randrange(1,5) for _ in range(n)]
        result=exact_repair(n,edges,additions,x0,group,weights)
        brute=oracle_repair(n,edges,additions,x0,group,weights)
        assert result.feasible == (brute is not None)
        assert result.min_cost == brute
        if brute is not None:
            assert valid(result.corrected,edges+additions,group)
            assert sum(weights[i] for i in range(n)
                       if x0[i]!=result.corrected[i])==brute


def test_cyclic2_random():
    random_instances(cyclic_group(2),1007,200,7)


def test_cyclic3_random():
    random_instances(cyclic_group(3),2343,120,6)


def test_nonabelian_s3_random():
    random_instances(permutation_group_3(),3199,55,4)


def test_linear_repair_width_family():
    grp=cyclic_group(2)
    for m in range(2,23):
        n=2*m
        old=[(i,i+1,0) for i in range(m-1)]
        old += [(i,i+1,0) for i in range(m,2*m-1)]
        new=[(m-1,m,1)]
        x0=[0]*n
        result=exact_repair(n,old,new,x0,grp)
        assert result.min_cost==m
        assert reconfiguration_components(n,old,grp,m-1)==(4,1)
        assert reconfiguration_components(n,old,grp,m)==(1,4)
        assert reconfiguration_components(n,old+new,grp,n-1)==(2,1)
        assert reconfiguration_components(n,old+new,grp,n)==(1,2)


def test_reconfiguration_components_exact_state_graphs():
    rng=random.Random(102)
    for n in range(2,7):
        for _ in range(13):
            grp=cyclic_group(2)
            assignment=[rng.randrange(2) for _ in range(n)]
            edges=[(i,j,(assignment[j]-assignment[i])%2)
                   for i in range(n) for j in range(i+1,n)
                   if rng.random()<.25]
            states=[z for z in product(grp.elements,repeat=n)
                    if valid(z,edges,grp)]
            for k in range(n+1):
                neighbors={a:[] for a in states}
                for a in states:
                    for b in states:
                        if a!=b and sum(x!=y for x,y in zip(a,b))<=k:
                            neighbors[a].append(b)
                seen=set(); sizes=[]
                for a in states:
                    if a in seen: continue
                    todo=[a];seen.add(a);size=0
                    while todo:
                        b=todo.pop();size+=1
                        for c in neighbors[b]:
                            if c not in seen:
                                seen.add(c);todo.append(c)
                    sizes.append(size)
                cnt,each=reconfiguration_components(n,edges,grp,k)
                assert len(sizes)==cnt and set(sizes)=={each}


def test_sharp_mode_bound_all_group_elements():
    for group in [cyclic_group(2),cyclic_group(3),permutation_group_3()]:
        for m in (1,2,4):
            n,old,new,x0=sharp_mode_family(group,m)
            result=exact_repair(n,old,new,x0,group)
            assert result.min_cost == n*(1-1/len(group.elements))
            assert reconfiguration_components(n,old+new,group,n-1) == (
                len(group.elements),1)


def test_inconsistent_quotient_cycle():
    grp=cyclic_group(2)
    # Three isolated initial components; odd gain sum on a triangle.
    new=[(0,1,1),(1,2,1),(2,0,1)]
    result=exact_repair(3,[],new,[0,0,0],grp)
    assert result.feasible is False and result.min_cost is None
