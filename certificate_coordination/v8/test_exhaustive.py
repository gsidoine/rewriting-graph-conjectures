"""Exhaustive and randomized adversarial verification of K_DD universality."""
import random
from itertools import combinations
from hypergraph_realization import hypergraph_from_graph_edges,min_transversal
from complete_bipartite_realization import construct_complete,verify,exact_width,repair_path
from obstruction_width_dp import solve


def checks():
    totals={}
    for k,h in [(1,4),(2,4),(3,5)]:
        ground=list(combinations(range(h),k+1))
        assert len(ground)<=10
        n=0
        for mask in range(1,1<<len(ground)):
            H=[ground[i] for i in range(len(ground)) if mask>>i&1]
            data=construct_complete(h,H,k)
            report=verify(data)
            value,I,width=exact_width(data)
            brute=min_transversal(h,H)
            assert value==len(brute),(k,h,H,value,brute)
            assert repair_path(data,brute)[-1]==0
            n+=1
        totals[(k,h)]=n
        print('EXHAUSTIVE k=%s h=%s checked=%s'%(k,h,n),flush=True)
    rng=random.Random(144)
    for k in (1,2,3):
        for rep in range(15):
            h=k+2+rng.randrange(3)
            ground=list(combinations(range(h),k+1))
            H=rng.sample(ground,min(len(ground),1+rng.randrange(min(7,len(ground)))))
            data=construct_complete(h,H,k)
            verify(data)
            val,indices,w=exact_width(data)
            assert val==len(min_transversal(h,H))
            assert repair_path(data,min_transversal(h,H))[-1]==0
        print('RANDOM k=%s passed=15'%k,flush=True)
    print('ALL EXHAUSTIVE AND RANDOM CERTIFICATES PASSED',flush=True)

if __name__=='__main__':checks()
