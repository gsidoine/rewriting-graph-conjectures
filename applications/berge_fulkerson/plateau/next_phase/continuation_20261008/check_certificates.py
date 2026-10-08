"""Dependency-free validation of explicit 3-edge-sum matching witnesses."""
from pathlib import Path
from collections import defaultdict, deque
import json

def check(path):
    d=json.loads(Path(path).read_text()); E=[tuple(e) for e in d['edges']]
    n=d['n'];k=d['k']; assert n==16*k+2
    assert len(E)==3*n//2 and len(set(E))==len(E)
    assert len({v for e in E for v in e})==n
    adj=[set() for _ in range(max(v for e in E for v in e)+1)]
    for u,v in E:
        assert u!=v and v not in adj[u];adj[u].add(v);adj[v].add(u)
    active={v for e in E for v in e}
    assert all(len(adj[v])==3 for v in active)
    colour={};cc=0
    for v in active:
        if v in colour:continue
        colour[v]=0;Q=deque([v]);cc+=1
        while Q:
            x=Q.popleft()
            for y in adj[x]:
                if y in colour:assert colour[y]==1-colour[x]
                else:colour[y]=1-colour[x];Q.append(y)
    assert cc==1
    # Every pair of deleted edges: graph stays connected => edge connectivity >=3.
    from itertools import combinations
    for rem in [()] + [(j,) for j in range(len(E))] + list(combinations(range(len(E)),2)):
        banned=set(rem);seen={next(iter(active))};queue=list(seen)
        inc=defaultdict(list)
        for ix,(a,b) in enumerate(E):
            if ix in banned:continue
            inc[a].append(b);inc[b].append(a)
        for x in queue:
            for y in inc[x]:
                if y not in seen:seen.add(y);queue.append(y)
        assert len(seen)==n,(k,rem)
    trace=[]
    for stage in d['six_matching_masks_per_stage']:
        assert len(stage)==6
        matching=[]
        for bittext in stage:
            b=int(bittext,16)
            assert b>=0 and b.bit_count()==n//2 and b>>len(E)==0
            vertices=[]
            for j,(u,v) in enumerate(E):
                if b>>j&1:vertices.extend((u,v))
            assert len(set(vertices))==n
            matching.append(b)
        trace.append(matching)
    Qvals=[]
    for matchings in trace:
        mult=[sum((m>>i)&1 for m in matchings) for i in range(len(E))]
        Qvals.append(sum((v-2)**2 for v in mult))
    assert Qvals==d['Q_trace']
    assert Qvals==[6*k-6*(a//2) for a in range(2*k+1)]
    for a,b in zip(trace,trace[1:]):assert sum(x!=y for x,y in zip(a,b))==1
    return {'k':k,'vertices':n,'edges':len(E),'Q_trace':Qvals,'one_coordinate_changes':len(trace)-1,'cut_checks':1+len(E)+len(E)*(len(E)-1)//2}

if __name__=='__main__':
    here=Path(__file__).resolve().parent
    for k in range(1,5):print('PASS',check(here/f'three_sum_k{k}.json'))
