"""Exact two-spanning-tree bridge-free edge-partition reduction.
Research implementation 2026-10-08. Uses only standard Python.

The fixed-tree CNF test is mathematically exact. It does NOT prove the
DeVos-Johnson-Seymour edge-connectivity partition conjecture.
"""
from collections import deque
from itertools import combinations, product


def connected(n, edges):
    if n==0:return True
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    seen={0};Q=[0]
    for x in Q:
        for y in adj[x]:
            if y not in seen:seen.add(y);Q.append(y)
    return len(seen)==n


def is_tree(n,edges):
    return len(edges)==n-1 and connected(n,edges)


def bridge_free(n, edges):
    if not connected(n,edges):return False
    return all(connected(n,edges[:j]+edges[j+1:]) for j in range(len(edges)))


def fundamental_clauses(n, edges, tree_red_ids, tree_blue_ids):
    assert not (set(tree_red_ids)&set(tree_blue_ids))
    assert is_tree(n,[edges[i] for i in tree_red_ids])
    assert is_tree(n,[edges[i] for i in tree_blue_ids])
    R=[j for j in range(len(edges)) if j not in tree_red_ids and j not in tree_blue_ids]
    constraints=[]
    for tree,positive in ((tree_red_ids,True),(tree_blue_ids,False)):
        for e in sorted(tree):
            keep=[edges[i] for i in tree if i != e]
            # find one shore of the fundamental cut
            adj=[[] for _ in range(n)]
            for a,b in keep: adj[a].append(b);adj[b].append(a)
            Q=[edges[e][0]]; S=set(Q)
            for v in Q:
                for w in adj[v]:
                    if w not in S:S.add(w);Q.append(w)
            clause=[pos for pos,idx in enumerate(R) if (edges[idx][0] in S)!=(edges[idx][1] in S)]
            constraints.append((positive,clause,e))
    return R,constraints


def twosat(n, clauses):
    # Each clause is a list of signed literals (var, is_positive).
    # literal node 2*i when x_i true; 2*i+1 when false.
    graph=[[] for _ in range(2*n)]; reverse=[[] for _ in range(2*n)]
    def add(u,v):graph[u].append(v);reverse[v].append(u)
    def nid(lit):i,pos=lit;return 2*i+(0 if pos else 1)
    for clause in clauses:
        if not clause:return None
        if len(clause)==1:
            u=nid(clause[0]);add(u^1,u)
        elif len(clause)==2:
            a,b=map(nid,clause);add(a^1,b);add(b^1,a)
        else:raise ValueError('not 2-SAT')
    seen=set();post=[]
    for v in range(2*n):
        if v in seen:continue
        stack=[(v,0)];seen.add(v)
        while stack:
            u,i=stack[-1]
            if i<len(graph[u]):
                w=graph[u][i];stack[-1]=(u,i+1)
                if w not in seen:seen.add(w);stack.append((w,0))
            else:post.append(u);stack.pop()
    comp=[-1]*(2*n);ci=0
    for v in reversed(post):
        if comp[v]>=0:continue
        Q=[v];comp[v]=ci
        for u in Q:
            for w in reverse[u]:
                if comp[w]<0:comp[w]=ci;Q.append(w)
        ci+=1
    if any(comp[2*i]==comp[2*i+1] for i in range(n)):return None
    return [comp[2*i]>comp[2*i+1] for i in range(n)]


def evaluate(n,edges,red,blue,R,clauses,choice):
    partred=[edges[e] for e in red]+[edges[R[i]] for i,x in enumerate(choice) if x]
    partblue=[edges[e] for e in blue]+[edges[R[i]] for i,x in enumerate(choice) if not x]
    formula=all(any(choice[i] if sign else not choice[i] for i in c) for sign,c,e in clauses)
    valid=bridge_free(n,partred) and bridge_free(n,partblue)
    return formula,valid


def kn_barrier(n):
    assert n>=7
    edges=list(combinations(range(n),2));idx={e:i for i,e in enumerate(edges)}
    # Tree red: vertex 1 is a leaf joined to 0. Remaining vertices form a star
    # at 0 except vertex 2, which is joined through vertex 3.
    T1={(0,1),(2,3)}|{(0,j) for j in range(3,n)}
    # Tree blue: vertex 1 sees all other neighbors but 0, and vertex 0
    # is connected through vertex 2.
    T2={(1,j) for j in range(2,n)}|{(0,2)}
    red={idx[tuple(sorted(e))] for e in T1}
    blue={idx[tuple(sorted(e))] for e in T2}
    R,C=fundamental_clauses(n,edges,red,blue)
    empty=[(s,e) for s,c,e in C if not c]
    assert empty and all(1 not in edges[R[i]] for i in range(len(R)))
    # An independent global partition exists: Walecki Hamilton decomposition.
    # For n odd, steps 1 and 2 are independent Hamilton cycles.
    # For even n, choose any coprime step besides 1 or n-1.
    from math import gcd
    step=next(j for j in range(2,n-1) if gcd(j,n)==1)
    def cycle(step):return {tuple(sorted((i,(i+step)%n))) for i in range(n)}
    C1,C2=cycle(1),cycle(step)
    assert len(C1)==n and len(C2)==n and not C1&C2
    assert bridge_free(n,list(C1)) and bridge_free(n,list(C2))
    return {'n':n,'connectivity':n-1,'red_tree':sorted(T1),'blue_tree':sorted(T2),
            'residual_edges':len(R),'empty_clauses':len(empty),'hamilton_step':step,
            'global_decomposition_exists':True,'fixed_trees_extendable':False}


def test_all_small_twosat():
    import random
    random.seed(20261008)
    checked=0
    for nvars in range(1,6):
        for _ in range(250):
            clauses=[]
            for _ in range(random.randint(0,9)):
                k=random.randint(1,2)
                clauses.append([(random.randrange(nvars),bool(random.randrange(2))) for i in range(k)])
            answer=twosat(nvars,clauses)
            brute=[x for x in product([False,True],repeat=nvars) if all(any(x[i]==pos for i,pos in clause) for clause in clauses)]
            assert (answer is not None)==bool(brute), (nvars,clauses,answer,brute)
            if answer is not None: assert all(any(answer[i]==pos for i,pos in clause) for clause in clauses)
            checked+=1
    return checked


if __name__=='__main__':
    assert test_all_small_twosat()==1250
    for n in [7,8,9,10,11,12]:
        print('BARRIER',kn_barrier(n))
    print('PASS: 1250 2-SAT versus exhaustive tests, six independent Kn barriers')
