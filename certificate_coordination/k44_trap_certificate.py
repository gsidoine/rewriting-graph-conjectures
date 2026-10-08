"""Exact enumeration of the lex-first Q=4 strict 1-coordinate trap on K4,4."""
import itertools
F=list(itertools.permutations(range(4)))
picks=[0,3,10,17]
M=[F[i] for i in picks]
def Q(S):
 mat=[[0]*4 for _ in range(4)]
 for f in S:
  for u,v in enumerate(f):mat[u][v]+=1
 return sum((mat[u][v]-1)**2 for u in range(4) for v in range(4))
q=Q(M);print('initial',q,'permutations',M)
mins=[]
neutral=None
for i in range(4):
 scores=[Q(M[:i]+[p]+M[i+1:]) for p in F]
 mins.append(min(scores))
 for p in F:
  if p!=M[i] and Q(M[:i]+[p]+M[i+1:])==q:
   mid=M[:i]+[p]+M[i+1:]
   for j in range(4):
    for p2 in F:
     end=mid[:j]+[p2]+mid[j+1:]
     if Q(end)<q:neutral=(i,p,j,p2,Q(end));break
    if neutral:break
   if neutral:break
print('one-coordinate minima',mins)
print('neutral then strict',neutral)
best=(999,None)
for inds in itertools.combinations(range(4),2):
 for a in F:
  for b in F:
   N=M.copy();N[inds[0]]=a;N[inds[1]]=b
   if Q(N)<best[0]:best=(Q(N),(inds,a,b))
print('pair minimum',best)
assert q==4 and mins==[4]*4 and best[0]==0 and neutral is not None
