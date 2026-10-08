"""Independent brute force sanity check for K7 exhaustive C++ theorem."""
import random
from itertools import combinations,product
from bridge_completion import fundamental_clauses,bridge_free,is_tree

def random_tree(n,edges,available,rng):
    par=list(range(n))
    def root(v):
        while par[v]!=v:par[v]=par[par[v]];v=par[v]
        return v
    ids=list(available);rng.shuffle(ids);tree=set()
    for e in ids:
        a,b=edges[e];u,v=root(a),root(b)
        if u==v:continue
        par[u]=v;tree.add(e)
        if len(tree)==n-1:return tree
    return None

def run():
    n=7;edges=list(combinations(range(n),2));rng=random.Random(891102)
    complete=0;triple=0
    for i in range(1200):
        T1=random_tree(n,edges,range(len(edges)),rng)
        T2=random_tree(n,edges,set(range(len(edges)))-T1,rng)
        if T2 is None:continue
        R,C=fundamental_clauses(n,edges,T1,T2)
        residual_connected=False
        # Connectivity of R, checked by no disconnected cut with the simple graph BFS
        from bridge_completion import connected
        residual_connected=connected(n,[edges[j] for j in R])
        possible=False
        for x in product([False,True],repeat=len(R)):
            correct=all(any(x[j] if sign else not x[j] for j in cc) for sign,cc,e in C)
            if correct:
                red=[edges[j] for j in T1]+[edges[R[j]] for j,v in enumerate(x) if v]
                blue=[edges[j] for j in T2]+[edges[R[j]] for j,v in enumerate(x) if not v]
                assert bridge_free(n,red) and bridge_free(n,blue)
                possible=True
                break
        if residual_connected:
            triple+=1
            assert possible
        complete+=1
    print('K7 independent randomized pairs checked',complete,'with connected residual',triple,'all such cases extend')
if __name__=='__main__':run()
