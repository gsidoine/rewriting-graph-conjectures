"""Independent strict-descent path construction & checker for vertex-cover gadgets."""
import sys,itertools
from collections import defaultdict
from realize_conflict import construct,verify,vertex_cover_brute

def least_cover(h,H):
 for r in range(h+1):
  for I in itertools.combinations(range(h),r):
   S=set(I)
   if all(a in S or b in S for a,b in H):return list(I)
 raise AssertionError

def check(h,H,c):
 dat=construct(h,H,c);verify(dat)
 d=dat['d'];m=dat['nblocks'];E={(u,v):tuple(cols) for u,v,cols in dat['edges']};n=dat['n']
 owner={j:set() for j in range(d)}
 for e,cs in E.items():
  for j in cs:owner[j].add(e)
 def valid():
  for j,S in owner.items():
   assert len(S)==n//2
   deg=[0]*n
   for u,v in S:
    assert (u,v) in E
    deg[u]+=1;deg[v]+=1
   assert all(a==1 for a in deg)
 def defect():
  from collections import Counter
  counts=Counter(e for M in owner.values() for e in M)
  return sum((counts.get(e,0)-1)**2 for e in E)
 valid();q0=defect(); assert q0==2*d*m
 cover=least_cover(h,H)
 fixed=set();order=[q0]
 for j in cover:
  new=set(owner[j]);before=defect()
  for b,(a,z) in enumerate(dat['H_edges']):
   if j not in (a,z) or (a in fixed or z in fixed):continue
   # Original F0 on this block, replace with unused factor F_{d-1}.
   L=lambda i:b*d+i
   R=lambda i:m*d+b*d+i
   old={(L(i),R(i)) for i in range(d)}
   fresh={(L(i),R((i+d-1)%d)) for i in range(d)}
   assert old<=new and fresh<=E.keys() and all(len(E[e])==0 for e in fresh)
   new=(new-old)|fresh
  assert new!=owner[j]
  owner[j]=new;valid();q=defect();assert q<before
  fixed.add(j);order.append(q)
 assert order[-1]==0 and len(order)-1==vertex_cover_brute(h,H)
 return dict(h=h,host_edges=len(H),c=c,degree=d,n=n,cover=cover,defects=order)

if __name__=='__main__':
 print(check(4,[(0,1),(1,2),(2,3)],2),flush=True)
 print(check(5,[(0,1),(1,2),(2,3),(3,4),(0,4)],4),flush=True)
 print(check(5,list(itertools.combinations(range(5),2)),4),flush=True)
 print('STRICT PATHS PASS',flush=True)
