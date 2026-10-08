"""Exhaustively verify six-matching double covers on K3,3 three-summed to K3,3.

9,000 states, 151,200 directed neutral-switch transitions, exactly nine components.
No external packages. Run directly: python repro_runs/k33_two_block_multicover_components.py
This exhaustive check is deliberately outside default unit-test collection.
"""
from collections import Counter,defaultdict
from itertools import product, permutations, combinations

P=list(permutations(range(3)))
LOCALMATCH=[frozenset((r,3+p[r]) for r in range(3)) for p in P]
ELOC=[(r,3+c) for r in range(3) for c in range(3)]
sgn=lambda p: sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

def covered(st):
    return all(sum(e in LOCALMATCH[i] for i in st)==2 for e in ELOC)

def sig(st):
    return tuple(tuple(i for i,j in enumerate(st) if (0,3+c) in LOCALMATCH[j])
                 for c in range(3))

def local_type(st):
    even=sum(sgn(P[j])==0 for j in st)
    assert even in (0,3,6)
    return even//3

local=defaultdict(list)
for st in product(range(6),repeat=6):
    if covered(st):local[sig(st)].append((st,local_type(st)))
assert len(local)==90 and sum(map(len,local.values()))==900

# The three-sum deletes vertex 0 from each K3,3 tile.
edges=set()
for b in (0,1):
    for u,v in ELOC:
        if u!=0:edges.add(tuple(sorted(((b,u),(b,v)))))
for v in (3,4,5):
    edges.add(tuple(sorted(((0,v),(1,v)))))
edges=sorted(edges)
assert len(edges)==15
edgeid={e:i for i,e in enumerate(edges)}

def to_global(st1,st2):
    cover=[]
    for j in range(6):
        M=set()
        for block,idx in ((0,st1[j]),(1,st2[j])):
            for u,v in LOCALMATCH[idx]:
                if u!=0:M.add(tuple(sorted(((block,u),(block,v)))))
                elif block==0:M.add(tuple(sorted(((0,v),(1,v)))))
        assert len(M)==5
        cover.append(sum(1<<edgeid[e] for e in M))
    cover=tuple(cover)
    assert all(sum(bool(sh>>i&1) for sh in cover)==2 for i in range(len(edges)))
    return cover

states={}
for sg,opts in local.items():
    for (s,a),(t,b) in product(opts,repeat=2):
        st=to_global(s,t)
        assert st not in states
        states[st]=(a,b)
assert len(states)==9000

def cycles(mask):
    pending={i for i in range(len(edges)) if mask>>i&1}
    ans=[]
    while pending:
        cc={pending.pop()}
        while True:
            verts={v for i in cc for v in edges[i]}
            add={i for i in pending if any(x in verts for x in edges[i])}
            if not add:break
            cc.update(add);pending.difference_update(add)
        ans.append(sum(1<<i for i in cc))
    return ans

def neighbors(st):
    for a,b in combinations(range(6),2):
        for cc in cycles(st[a]^st[b]):
            other=list(st)
            other[a]^=cc;other[b]^=cc
            yield tuple(other)

movecount=0
for st,typ in states.items():
    for other in neighbors(st):
        assert other in states
        assert states[other]==typ
        movecount+=1
assert movecount==151200

def component_shapes(pool):
    pool=set(pool)
    shapes=defaultdict(list)
    while pool:
        seed=pool.pop()
        typ=states[seed]
        stack=[seed]
        size=1
        while stack:
            st=stack.pop()
            for z in neighbors(st):
                if z in pool:
                    pool.remove(z)
                    stack.append(z)
                    size+=1
        shapes[typ].append(size)
    return dict(shapes)

expected={(a,b):[90*(8 if a==1 else 1)*(8 if b==1 else 1)]
          for a in range(3) for b in range(3)}
assert component_shapes(states)==expected

# Exact fixed boundary signature at a retained vertex (0,1).
star=sorted(i for i,e in enumerate(edges) if (0,1) in e)
assert len(star)==3
def exposed_signature(st):
    return tuple(tuple(j for j,M in enumerate(st) if M>>i&1) for i in star)
target=exposed_signature(next(iter(states)))
fixed=[st for st in states if exposed_signature(st)==target]
assert len(fixed)==100
fixed_expected={(a,b):[(8 if a==1 else 1)*(8 if b==1 else 1)]
                for a in range(3) for b in range(3)}
assert component_shapes(fixed)==fixed_expected

if __name__=="__main__":
    print("PASS: 9000 exact double covers; 151200 neutral switches")
    print("PASS: 9 global components, sizes:", sorted(x[0] for x in expected.values()))
    print("PASS: fixed signature 100 states, 9 components, sizes:",
          sorted(x[0] for x in fixed_expected.values()))


def diameter(pool):
    pool=set(pool)
    result=0
    for seed in pool:
        distance={seed:0}
        q=[seed]
        for st in q:
            for nxt in neighbors(st):
                if nxt in pool and nxt not in distance:
                    distance[nxt]=distance[st]+1
                    q.append(nxt)
        assert len(distance)==len(pool)
        result=max(result,max(distance.values()))
    return result

fixed_by_type=defaultdict(list)
for st in fixed:
    fixed_by_type[states[st]].append(st)
for (a,b),part in fixed_by_type.items():
    predicted=3*(min(a,2-a)+min(b,2-b))
    assert diameter(part)==predicted

if __name__=="__main__":
    print("PASS: every fixed-signature component diameter matches 3*sum(min(t,2-t))")
