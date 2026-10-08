"""Exhaustive two-coordinate descent check on four cyclic cubic bipartite graphs.

These four graph families are not all cubic bipartite graphs of these orders.
A no-trap outcome is only computational evidence, not a universal theorem.
Requires numpy (already a repository dependency).
"""
from itertools import combinations, combinations_with_replacement, permutations
import numpy as np


def audit(h):
    edges=sorted((u,h+(u+j)%h) for u in range(h) for j in range(3))
    allowed=set(edges)
    pms=[]
    for perm in permutations(range(h)):
        matching={(u,h+perm[u]) for u in range(h)}
        if matching<=allowed:
            pms.append(np.asarray([int(e in matching) for e in edges],dtype=np.int8))
    p=np.stack(pms).astype(np.int16)
    k=len(p)
    pairs=np.stack([p[a]+p[b] for a,b in combinations_with_replacement(range(k),2)])
    opt={}
    for c in combinations_with_replacement(range(k),4):
        frozen=p[list(c)].sum(axis=0)
        opt[c]=int(((pairs+frozen-2)**2).sum(axis=1).min())
    total=0;strict_local_traps=0;solutions=0
    for c in combinations_with_replacement(range(k),6):
        total+=1
        q=int(((p[list(c)].sum(axis=0)-2)**2).sum())
        if q==0:
            solutions+=1;continue
        best=min(opt[tuple(c[i] for i in range(6) if i not in (a,b))]
                 for a,b in combinations(range(6),2))
        if best>=q:strict_local_traps+=1
    assert strict_local_traps==0
    return {'vertices':2*h,'perfect_matchings':k,'six_multisets':total,
            'Q_zero_states':solutions,'positive_Q_pair_traps':strict_local_traps}

if __name__=='__main__':
    out=[audit(h) for h in range(3,7)]
    for row in out:print(row)
    print('total_states',sum(row['six_multisets'] for row in out),'PASS')
