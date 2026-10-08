"""Small dependency-free verifier for the 18-vertex Q=12 hitting obstruction.

Everything important follows from the JSON certificate without scipy/networkx.
The finite optimal pair Q=4 is certified by exhaustive enumeration of the
perfect matchings (not by trusting the generating MILP or flow optimizer).
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json

DATA=Path(__file__).with_name('q12_cycle_blocker_18.json')

def load():
    x=json.loads(DATA.read_text())
    E=[tuple(e) for e in x['edges']]
    S=[frozenset(v) for v in x['edge_coordinate_memberships']]
    return x,E,S

def pm(E,mask):
    d=Counter(v for i,e in enumerate(E) if (mask>>i)&1 for v in e)
    return len(d)==18 and all(d[v]==1 for v in range(18))

def Q(state,E):
    return sum((sum((state[c]>>k)&1 for c in range(6))-2)**2 for k in range(len(E)))

def connected(E,deleted=()):
    adj=[[] for _ in range(18)]
    for i,(u,v) in enumerate(E):
        if i in deleted:continue
        adj[u].append(v);adj[v].append(u)
    seen={0};todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return len(seen)==18

def all_matchings(E):
    a=[[] for _ in range(18)]
    for j,(u,v) in enumerate(E):
        a[u].append((v,j));a[v].append((u,j))
    full=(1<<18)-1
    def rec(left):
        if not left:
            yield 0;return
        b=left&-left;u=b.bit_length()-1
        for v,j in a[u]:
            if left>>v&1:
                for suffix in rec(left&~(1<<u)&~(1<<v)):
                    yield suffix|(1<<j)
    return tuple(sorted(set(rec(full))))

def check():
    obj,E,S=load()
    assert len(E)==27 and len(set(map(frozenset,E)))==27
    assert set(v for e in E for v in e)==set(range(18))
    degrees=Counter(v for e in E for v in e)
    assert all(degrees[v]==3 for v in range(18))
    assert all((u<6 or 12<=u<15) != (v<6 or 12<=v<15) for u,v in E)
    assert all(0<=i<6 for s in S for i in s)
    assert all(len(S[i])==3 for i in range(6))
    assert all(len(S[i])==1 for i in range(6,12))
    assert all(len(S[i])==2 for i in range(12,27))
    assert connected(E)
    assert all(connected(E,(i,)) for i in range(27))
    assert all(connected(E,(i,j)) for i,j in combinations(range(27),2))
    start=[sum(1<<i for i,s in enumerate(S) if c in s) for c in range(6)]
    assert start==obj['witness_initial_masks']
    assert all(pm(E,m) for m in start)
    assert Q(start,E)==12
    assert all(any(not set(pair).intersection(S[i]) for i in range(6))
               for pair in combinations(range(6),2))
    cycle_edges=E[:12]
    deg=Counter(v for e in cycle_edges for v in e)
    assert len(deg)==12 and all(deg[v]==2 for v in deg)
    # The 12-cycle is connected (not two disjoint 6-cycles).
    todo=[0];seen={0};adj={v:[] for v in deg}
    for u,v in cycle_edges:adj[u].append(v);adj[v].append(u)
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    assert len(seen)==12
    mid=obj['witness_after_two_masks'];end=obj['witness_final_masks']
    assert all(pm(E,m) for m in mid+end)
    assert Q(mid,E)==4 and Q(end,E)==0
    assert sum(a!=b for a,b in zip(start,mid))==2
    assert sum(a!=b for a,b in zip(mid,end))==1
    assert sum(a!=b for a,b in zip(start,end))==3
    pms=all_matchings(E)
    assert all(pm(E,m) for m in pms)
    # independent exhaustive optimum over 6*5/2 pairs of coordinates
    pairbest=12
    for i,j in combinations(range(6),2):
        for a in pms:
            for b in pms:
                s=start.copy();s[i]=a;s[j]=b
                pairbest=min(pairbest,Q(s,E))
    assert pairbest==4
    return {'vertices':18,'edges':27,'edge_connectivity_at_least':3,
            'perfect_matchings':len(pms),'initial_Q':12,
            'two_coordinate_hitting_cycle':False,
            'best_two_coordinate_Q':pairbest,
            'certificate_path':[12,4,0]}

if __name__=='__main__':print('PASS:',json.dumps(check(),sort_keys=True))
