"""Independent stdlib verification of FR fibres and state graphs under K3,2 substitution."""
from itertools import product
from collections import Counter, deque, defaultdict

def local_data(P):
  out={}
  for B in product(range(2),repeat=3):
    C=Counter()
    for p,b in zip(P,B):
      others=[i for i in range(3) if i!=p]
      C[(others[b],0)]+=1;C[(others[1-b],1)]+=1
    if max(C.values())<=2:out[B]=6-len(C)
  return out

def local_check():
  allp=[p for p in product(range(3),repeat=3) if len(set(p))>1]
  for P in allp:
    D=local_data(P)
    expected={0:2,2:6} if len(set(P))==3 else {1:4,2:2}
    assert dict(Counter(D.values()))==expected,(P,D)
    # 1-bit local moves give connected cube or hexagon
    unseen=set(D);Q=[next(iter(unseen))];unseen.remove(Q[0])
    for x in Q:
      for j in range(3):
        y=(*x[:j],1-x[j],*x[j+1:])
        if y in unseen:unseen.remove(y);Q.append(y)
    assert not unseen
    assert len(D)==(8 if len(set(P))==3 else 6)
    # every admissible base move lifts from every valid configuration
    for B in D:
      for j in range(3):
        for new in range(3):
          Qport=(*P[:j],new,*P[j+1:])
          if len(set(Qport))==1:continue
          assert any((*B[:j],bit,*B[j+1:]) in local_data(Qport) for bit in (0,1)),(P,B,j,new)
  print('LOCAL: 24 ordered port triples, all cube/hexagon structures, exhaustive edge lifting passed')

def pm(n, E):
  inc=[[] for _ in range(n)]
  for i,(a,b) in enumerate(E):inc[a].append((b,i));inc[b].append((a,i))
  res=[]
  def go(free, mask):
    if not free:res.append(mask);return
    a=min(free)
    for b,i in inc[a]:
      if b in free:go(free-{a,b},mask|(1<<i))
  go(set(range(n)),0)
  return sorted(res)

def expand(n,E):
  inc=[[] for _ in range(n)]
  for i,(a,b) in enumerate(E):inc[a].append(i);inc[b].append(i)
  for a in inc:assert len(a)==3
  port={(v,e):5*v+sorted(inc[v]).index(e) for v in range(n) for e in inc[v]}
  Ed=[(port[(u,i)],port[(v,i)]) for i,(u,v) in enumerate(E)]
  Ed += [(port[(v,i)],5*v+3+k) for v in range(n) for i in sorted(inc[v]) for k in range(2)]
  return [tuple(sorted(p)) for p in Ed]

def FR_poly(n,E):
  M=pm(n,E);full=(1<<len(E))-1;D=Counter();fr=0
  for a in M:
    for b in M:
      for c in M:
        if a&b&c:continue
        fr+=1
        D[len(E)-((a|b|c)&full).bit_count()]+=1
  return M,D,fr

def mul(p,q):
  o=Counter()
  for a,x in p.items():
    for b,y in q.items():o[a+b]+=x*y
  return o

def predicted(n,F):
  A={0:2,2:6};B={1:4,2:2}
  res=Counter()
  for u,num in F.items():
    p={u:num}
    for _ in range(n-2*u):p=mul(p,A)
    for _ in range(2*u):p=mul(p,B)
    res.update(p)
  return res

def k4_check():
  E=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
  M,F,n=FR_poly(4,E);assert len(M)==3 and n==24
  T=expand(4,E)
  M2,F2,n2=FR_poly(20,T)
  exp=predicted(4,F)
  assert F2==exp,(F2,exp)
  assert len(M2)==len(M)*2**4
  assert n2==sum(exp.values())
  print('K4: PMs',len(M),'FR states',n,'poly',dict(sorted(F.items())))
  print('T(K4): PMs',len(M2),'FR ordered states',n2,'poly',dict(sorted(F2.items())))
  # full graph of unlabeled FR states on K4 expansion: test connectedness
  states=[];lookup=set(); full=(1<<len(T))-1
  for i,a in enumerate(M2):
    for j in range(i,len(M2)):
      b=M2[j]
      for k in range(j,len(M2)):
        c=M2[k]
        if a&b&c:continue
        tup=(i,j,k);states.append(tup);lookup.add(tup)
  q=[states[0]];visited={states[0]}
  for state in q:
    for j in range(3):
      pair=state[:j]+state[j+1:]
      forbidden=M2[pair[0]]&M2[pair[1]]
      for k,p in enumerate(M2):
        if p&forbidden:continue
        nxt=tuple(sorted((*pair,k)))
        if nxt not in visited:
          assert nxt in lookup
          visited.add(nxt);q.append(nxt)
  assert len(visited)==len(states)
  print('T(K4) full unordered FR reconfiguration graph: connected,',len(states),'states')

if __name__=='__main__':local_check();k4_check()

# The following list of six-bit legality masks covers every ordered boundary-port pattern.
def verify_five_round_schedule():
    from itertools import product
    masks=set()
    for P in product(range(3),repeat=3):
        if len(set(P))==1:continue
        legal=local_data(P)
        mask=sum(1<<sum(bit<<j for j,bit in enumerate(b)) for b in legal)
        masks.add(mask)
    assert len(masks)==5
    word=(0,1,0,2,0)
    def step(R,mask,j):
        nxt=R
        for a in range(8):
            b=a^(1<<j)
            if (R>>a)&1 and (mask>>b)&1:nxt|=1<<b
        return nxt
    for mask in masks:
        for s in range(8):
            if not (mask>>s)&1:continue
            reach=1<<s
            for j in word:reach=step(reach,mask,j)
            assert reach==mask,(mask,s,reach)
    # All words with <5 rounds fail for some legal local start/target pair.
    for length in range(5):
        for word2 in product(range(3),repeat=length):
            works=True
            for mask in masks:
                for s in range(8):
                    if not (mask>>s)&1:continue
                    reach=1<<s
                    for j in word2:reach=step(reach,mask,j)
                    if reach!=mask:works=False;break
                if not works:break
            assert not works,word2
    print('UNIVERSAL: word (0,1,0,2,0) routes every fibre pair; no <=4 round universal word')

if __name__=='__main__':verify_five_round_schedule()