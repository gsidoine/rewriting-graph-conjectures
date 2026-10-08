"""Exact direct-repair width from edge signatures via binary variable elimination.

No external dependencies. Complexity exponential in the induced width of the
supplied elimination order on the PRIMAL graph of surplus constraints.
"""
from itertools import product


def repair_constraints(edge_signatures, k):
    """Deduplicated (scope,minimum number selected) constraints."""
    out=set()
    for S in edge_signatures:
        T=tuple(sorted(S))
        if len(T)>k:out.add((T,len(T)-k))
    return sorted(out)


def min_fill_order(t, constraints):
    adj=[set() for _ in range(t)]
    for scope,threshold in constraints:
        for i in scope:
            adj[i].update(set(scope)-{i})
    alive=set(range(t));order=[]
    while alive:
        candidates=[]
        for i in alive:
            ne=sorted(adj[i]&alive)
            fill=sum(b not in adj[a] for z,a in enumerate(ne) for b in ne[z+1:])
            candidates.append((fill,len(ne),i))
        _,_,i=min(candidates)
        ne=adj[i]&alive
        for a in ne:adj[a].update(ne-{a})
        alive.remove(i);order.append(i)
    return order


def width_from_order(t,constraints,order):
    adj=[set() for _ in range(t)]
    for scope,threshold in constraints:
        for i in scope:adj[i].update(set(scope)-{i})
    alive=set(range(t));width=0
    for i in order:
        ne=adj[i]&alive
        width=max(width,len(ne))
        for a in ne:adj[a].update(ne-{a})
        alive.remove(i)
    return width


def solve(t,edge_signatures,k,order=None):
    """Return (minimum coordinates, optimal index tuple, induced width).

    Includes unary selection costs, and surplus incidence constraints;
    checks all resulting factor tables exactly.
    """
    cons=repair_constraints(edge_signatures,k)
    if order is None:order=min_fill_order(t,cons)
    assert sorted(order)==list(range(t))
    width=width_from_order(t,cons,order)
    INF=t+1
    factors=[]
    for v in range(t):factors.append(((v,),{(0,):0,(1,):1}))
    for S,lim in cons:
        table={bits:(0 if sum(bits)>=lim else INF) for bits in product((0,1),repeat=len(S))}
        factors.append((S,table))
    elimination=[]
    for v in order:
        bucket=[factor for factor in factors if v in factor[0]]
        factors=[factor for factor in factors if v not in factor[0]]
        scope=tuple(sorted(set().union(*(s for s,_ in bucket))-{v}))
        newtab={};choose={}
        for bits in product((0,1),repeat=len(scope)):
            vals=dict(zip(scope,bits));best=None;opt=None
            for val in (0,1):
                vals[v]=val
                cost=0
                for S,tab in bucket:
                    cost+=tab[tuple(vals[i] for i in S)]
                if best is None or cost<best:best=cost;opt=val
            newtab[bits]=best;choose[bits]=opt
        factors.append((scope,newtab))
        elimination.append((v,scope,choose))
    assert all(scope==() for scope,_ in factors)
    optimum=sum(tab[()] for scope,tab in factors)
    assert optimum<INF, 'all coordinates always repair; therefore an optimum exists'
    selected={}
    for v,scope,choice in reversed(elimination):
        selected[v]=choice[tuple(selected[u] for u in scope)]
    I=tuple(i for i in range(t) if selected[i])
    assert len(I)==optimum
    assert all(len(set(S)&set(I))>=lim for S,lim in cons)
    return optimum,I,width


if __name__=='__main__':
    from hypergraph_realization import construct,hypergraph_from_graph_edges,min_transversal,verify
    for k in (1,2,3):
        h,edges=hypergraph_from_graph_edges(5,[(0,1),(1,2),(2,3),(3,4),(0,4)],k)
        d=construct(h,edges,k,c=4)
        verify(d)
        best,I,width=solve(d['t'],[s for s in d['owners'].values()],k)
        expected=len(min_transversal(h,edges))
        assert best==expected
        print('k',k,'t',d['t'],'width',width,'optimum',best,'witness',I,flush=True)
    print('ALL TREEWIDTH DP CHECKS PASSED')
