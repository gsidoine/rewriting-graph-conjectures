import itertools,numpy as np
from scipy.optimize import linprog
F=list(itertools.permutations(range(4)))
M=[F[i] for i in (0,3,10,17)]
mult=np.zeros((4,4),dtype=int)
for p in M:
 for i,j in enumerate(p):mult[i,j]+=1
print('matrix',mult.tolist())
for k,p in enumerate(M):
 b=mult.copy()
 for i,j in enumerate(p):b[i,j]-=1
 W=2*b-1
 A=[];ubs=[]
 for i in range(4):
  for j in range(4):
   r=np.zeros(8);r[i]=1;r[4+j]=1;A.append(r);ubs.append(W[i,j])
 E=[];vals=[]
 for i,j in enumerate(p):
  r=np.zeros(8);r[i]=1;r[4+j]=1;E.append(r);vals.append(W[i,j])
 sol=linprog(np.zeros(8),A_ub=np.array(A),b_ub=ubs,A_eq=np.array(E),b_eq=vals,bounds=[(None,2)]*4+[(None,1)]*4,method='highs')
 print('coord',k,'matching',p,'success',sol.success,'dual',sol.x if sol.success else sol.message,'weights',W.tolist())
 assert sol.success
 assert all(abs(x-round(x))<1e-7 for x in sol.x)
