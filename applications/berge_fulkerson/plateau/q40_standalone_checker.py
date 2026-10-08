"""Dependency-free exact verifier for the sharp Q=40 direct-repair obstruction.

It checks the supplied graph/matching certificate and 3-edge-connectivity
by all zero-, one-, and two-edge deletions. This avoids trusting the MILP
used during discovery. Does not assert 3-coordinate *strict descent* fails.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

DATA=Path(__file__).with_name('q40_cycle_blocker_40.json')

def q(E,state):return sum((sum((x>>j)&1 for x in state)-2)**2 for j in range(len(E)))
def is_pm(E,mask,n):
 d=Counter(v for i,e in enumerate(E) if mask>>i&1 for v in e)
 return len(d)==n and all(d[v]==1 for v in range(n))
def connected(E,n,removed=()):
 a=[[] for _ in range(n)]
 for i,(u,v) in enumerate(E):
  if i not in removed:a[u].append(v);a[v].append(u)
 seen={0};todo=[0]
 while todo:
  for v in a[todo.pop()]:
   if v not in seen:seen.add(v);todo.append(v)
 return len(seen)==n

def check():
 obj=json.loads(DATA.read_text())
 E=[tuple(e) for e in obj['edges']];S=[frozenset(s) for s in obj['edge_coordinate_memberships']]
 assert len(E)==60 and len(set(map(frozenset,E)))==60
 assert set(v for e in E for v in e)==set(range(40))
 assert all((u<20)!=(v<20) for u,v in E)
 assert all(Counter(v for e in E for v in e)[x]==3 for x in range(40))
 assert all(len(S[i])==3 for i in range(20))
 assert all(len(S[i])==1 for i in range(20,40))
 assert all(len(S[i])==2 for i in range(40,60))
 assert set(S[:20])==set(map(frozenset,combinations(range(6),3)))
 # 40-cycle core C with + edges followed by - edges
 adj={v:[] for v in range(40)}
 for u,v in E[:40]:adj[u].append(v);adj[v].append(u)
 assert all(len(adj[v])==2 for v in range(40))
 seen={0};todo=[0]
 while todo:
  for v in adj[todo.pop()]:
   if v not in seen:seen.add(v);todo.append(v)
 assert len(seen)==40
 assert connected(E,40)
 assert all(connected(E,40,(i,)) for i in range(60))
 assert all(connected(E,40,(i,j)) for i,j in combinations(range(60),2))
 st=[sum(1<<i for i,s in enumerate(S) if c in s) for c in range(6)]
 assert st==obj['witness_initial_masks']
 assert all(is_pm(E,m,40) for m in st)
 assert q(E,st)==40
 # every triple of indices misses the complementary positive triple
 assert all(any(set(I).isdisjoint(S[k]) for k in range(20))
            for I in combinations(range(6),3))
 after=obj['witness_four_coordinate_masks']
 assert all(is_pm(E,m,40) for m in after)
 assert q(E,after)==0
 assert sum(a!=b for a,b in zip(st,after))==4
 intermediate=obj['witness_improving_two_masks']
 assert all(is_pm(E,m,40) for m in intermediate)
 assert sum(a!=b for a,b in zip(st,intermediate))==2
 assert q(E,intermediate)==10
 return {'vertices':40,'edges':60,'edge_connectivity_at_least':3,
         'positive_triples':20,'all_triples_present':True,'Q_initial':40,
         'minimum_direct_replacement_coordinates':4,
         'certified_improving_pair_Q':10,'four_coordinate_target_Q':0}

if __name__=='__main__':print('PASS:',json.dumps(check(),sort_keys=True))
