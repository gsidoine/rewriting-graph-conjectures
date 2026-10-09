"""Independent cube counterexample to pair-rigid type invariance.

Requires networkx. Run:
    python repro_runs/pair_rigid_cube_obstruction.py
"""
import itertools
from collections import Counter,defaultdict
import networkx as nx

G=nx.cubical_graph()
E=sorted(tuple(sorted(e)) for e in G.edges())
adj={v:[] for v in G}
for i,(u,v) in enumerate(E):
    adj[u].append((v,i));adj[v].append((u,i))

def pm(unused,mask=0):
    if not unused:
        yield mask;return
    v=min(unused)
    for w,i in adj[v]:
        if w in unused:
            yield from pm(unused-{v,w},mask|(1<<i))

PM=sorted(set(pm(frozenset(G))))
assert len(PM)==9
by_mask={mask:i for i,mask in enumerate(PM)}

def components(mask):
    pending={i for i in range(len(E)) if mask>>i&1}
    ans=[]
    while pending:
        bag={pending.pop()}
        while True:
            vs={v for i in bag for v in E[i]}
            extra={i for i in pending if vs.intersection(E[i])}
            if not extra:break
            bag.update(extra);pending.difference_update(extra)
        ans.append(sum(1<<e for e in bag))
    return ans

# Two different perfect matchings with two disjoint alternating cycles:
pair=next((a,b) for a,b in itertools.combinations(PM,2) if len(components(a^b))>=2)
a,b=pair
flip=components(a^b)[0]
c,d=a^flip,b^flip
assert {a,b}!={c,d}
assert (a&b)==(c&d) and (a|b)==(c|d)

count=[0]*len(E)
states=[]
def rec(choices):
    if len(choices)==6:
        if all(x==2 for x in count):states.append(tuple(choices))
        return
    missing=5-len(choices)
    for j,M in enumerate(PM):
        idx=[i for i in range(len(E)) if M>>i&1]
        if any(count[i]==2 for i in idx):continue
        for i in idx:count[i]+=1
        if all(x+missing>=2 for x in count):rec(choices+[j])
        for i in idx:count[i]-=1
rec([])
assert len(states)==4320 and len(set(states))==4320
S=set(states)
neighbors={}
for st in states:
    opts=set()
    for x,y in itertools.combinations(range(6),2):
        for C in components(PM[st[x]]^PM[st[y]]):
            nxt=list(st)
            nxt[x]=by_mask[PM[st[x]]^C]
            nxt[y]=by_mask[PM[st[y]]^C]
            nxt=tuple(nxt)
            assert nxt in S
            opts.add(nxt)
    neighbors[st]=opts

def cc(pool):
    pool=set(pool);sizes=[]
    while pool:
        Q=[pool.pop()]
        for st in Q:
            for x in neighbors[st]:
                if x in pool:
                    pool.remove(x);Q.append(x)
        sizes.append(len(Q))
    return sorted(sizes)

assert cc(states)==[4320]
star=sorted(i for i,e in enumerate(E) if 0 in e)
def signature(st):
    return tuple(tuple(j for j,M in enumerate(st) if PM[M]>>e&1) for e in star)
fixed=defaultdict(list)
for st in states:fixed[signature(st)].append(st)
assert len(fixed)==90
assert all(len(x)==48 and cc(x)==[48] for x in fixed.values())
different_multisets={tuple(sorted(st)) for st in states}
assert len(different_multisets)==11

if __name__=="__main__":
    print("PASS cube: 9 perfect matchings; 2-cycle pair gives nontrivial partial exchange")
    print("PASS cube: 4320 covers, all in one neutral component; 90 connected fibers of size 48")
    print("PASS cube: 11 unordered local matching multisets are not neutral invariants")
