"""A (k+1)-uniform obstruction hypergraph embedded in a complete bipartite
K_(D,D), with D=q*d, t=k*D perfect matchings covering every edge k times
except one +1/-1 pair of one-factors inside each diagonal block.

No graph libraries or optimizers. Exact combinatorial certificate.
"""
from itertools import combinations
from math import ceil


def construct_complete(h, hyperedges, k):
    E=sorted(set(tuple(sorted(e)) for e in hyperedges))
    assert h>=k+1 and k>=1 and E
    assert all(len(s)==k+1 and len(set(s))==k+1 and min(s)>=0 and max(s)<h for s in E)
    q=len(E)
    d=max(2,ceil(h/k))
    assert k*d>=h
    D=q*d;t=k*D
    local_labels={}
    # For each gadget assign all active kd coordinates to local one-factors.
    for b,S in enumerate(E):
        other=[i for i in range(k*d) if i not in S]
        factors={0:tuple(S),1:tuple(other[:k-1])}
        tail=other[k-1:]
        assert len(tail)==(d-2)*k
        for j in range(2,d):factors[j]=tuple(tail[(j-2)*k:(j-1)*k])
        local_labels[b]=factors
    # Representation is by coordinate permutation (position -> right endpoint),
    # not by dense edge-signature arrays. A cheap representation even for large D.
    permutations=[]
    for coord in range(k*d):
        perm=[None]*D
        for b in range(q):
            shift=next(f for f,coords in local_labels[b].items() if coord in coords)
            for i in range(d):perm[b*d+i]=b*d+(i+shift)%d
        permutations.append(tuple(perm))
    # Offdiagonal one-factorization of K_(D,D) - union of q K_(d,d) blocks.
    for bshift in range(1,q):
        for ishift in range(d):
            p=tuple((((i//d+bshift)%q)*d+(i%d+ishift)%d) for i in range(D))
            for _ in range(k):permutations.append(p)
    assert len(permutations)==t
    return dict(h=h,hyperedges=E,k=k,q=q,d=d,D=D,t=t,
                permutations=permutations,local_labels=local_labels)


def verify(data):
    k,q,d,D,t=(data[x] for x in ('k','q','d','D','t'))
    assert D==q*d and t==k*D
    assert len(data['permutations'])==t
    assert all(len(p)==D and len(set(p))==D and min(p)==0 and max(p)==D-1 for p in data['permutations'])
    counts=[[0]*D for _ in range(D)]
    signatures=[[set() for _ in range(D)] for __ in range(D)]
    for coord,p in enumerate(data['permutations']):
        for i,j in enumerate(p):counts[i][j]+=1;signatures[i][j].add(coord)
    qval=sum((x-k)**2 for row in counts for x in row)
    assert qval==2*d*q
    assert set(tuple(sorted(signatures[b*d+i][b*d+i])) for b in range(q) for i in range(d)) == set(data['hyperedges'])
    assert all(counts[i][j] == (k+1 if i//d==j//d and j%d==i%d else k-1 if i//d==j//d and j%d==(i%d+1)%d else k) for i in range(D) for j in range(D))
    return dict(vertices=2*D, edges=D*D,degree=D,edge_connectivity=D,
                cover_multiplicity=k,coordinates=t,hyperedges=q,initial_Q=qval)


def exact_width(data):
    from obstruction_width_dp import solve
    d=data['d'];q=data['q'];k=data['k'];D=data['D'];t=data['t']
    # constraint scopes on surplus factor, each repeated d times
    return solve(t,data['hyperedges'],k)


def repair_path(data,I):
    k,d,q,D,t=(data[x] for x in ('k','d','q','D','t'))
    P=[list(p) for p in data['permutations']]
    repaired=set()
    def defect():
        counts=[[0]*D for _ in range(D)]
        for p in P:
            for i,j in enumerate(p):counts[i][j]+=1
        return sum((x-k)**2 for row in counts for x in row)
    history=[defect()]
    for z in I:
        changed=False
        for b,S in enumerate(data['hyperedges']):
            if b in repaired or z not in S:continue
            for i in range(d):
                u=b*d+i
                assert P[z][u]==b*d+i
                P[z][u]=b*d+(i+1)%d
            repaired.add(b);changed=True
        assert changed
        assert all(sorted(p)==list(range(D)) for p in P)
        history.append(defect())
        assert history[-1]<history[-2]
    assert len(repaired)==q and history[-1]==0
    return history


if __name__=='__main__':
    from hypergraph_realization import hypergraph_from_graph_edges,min_transversal
    from itertools import combinations
    tests=[('edge_k1',2,[(0,1)],1),
           ('cycle5_k2',5,[(0,1),(1,2),(2,3),(3,4),(0,4)],2),
           ('triangle_k3',3,[(0,1),(1,2),(0,2)],3),
           ('complete4_k2',4,list(combinations(range(4),2)),2)]
    for name,h,H,k in tests:
        hh,E=hypergraph_from_graph_edges(h,H,k)
        data=construct_complete(hh,E,k)
        res=verify(data)
        optimum,I,w=exact_width(data)
        τ=min_transversal(hh,E)
        assert optimum==len(τ)
        hist=repair_path(data,τ)
        print(name,res,'width',optimum,'DP_width',w,'history',hist,flush=True)
    print('ALL COMPLETE BIPARTITE CERTIFICATES VERIFIED',flush=True)
