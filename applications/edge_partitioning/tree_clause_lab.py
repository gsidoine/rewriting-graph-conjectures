import sys,json
import networkx as nx,numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix
from three_trees_search import pack3,graphs

def instance(G,E,T1,T2):
 m=len(E);R=np.flatnonzero(1-(T1|T2));labels=list(G.nodes());Rmap={int(e):j for j,e in enumerate(R)}
 clauses=[]
 for T,want_red in [(T1,True),(T2,False)]:
  H=nx.Graph();H.add_nodes_from(G);H.add_edges_from([(u,v) for e,(u,v,_) in enumerate(E) if T[e]])
  for e in np.flatnonzero(T):
   u,v,_=E[e];H.remove_edge(u,v)
   S=nx.node_connected_component(H,u)
   clause=[Rmap[j] for j in R if (E[j][0] in S)!=(E[j][1] in S)]
   clauses.append((bool(want_red),tuple(clause),int(e)))
   H.add_edge(u,v)
 return len(R),clauses

def satisfy(n,clauses):
 A=np.zeros((len(clauses),n),dtype=int)
 lo=[];hi=[]
 for i,(positive,cl,e) in enumerate(clauses):
  A[i,list(cl)]=1
  if positive:lo.append(1);hi.append(n)
  else:lo.append(0);hi.append(len(cl)-1)
 res=milp(np.zeros(n),integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=LinearConstraint(csr_matrix(A),lo,hi),options={'time_limit':5})
 return res.x is not None, np.rint(res.x).astype(int).tolist() if res.x is not None else None

if __name__=='__main__':
 for name,G in graphs():
  if len(G)>10:continue
  outcomes=[]
  for seed in range(20):
   p=pack3(G,seed)
   if p is None:continue
   E,Ts=p;n,cl=instance(G,E,Ts[0],Ts[1]);success,x=satisfy(n,cl)
   outcomes.append((success,max(len(c) for s,c,e in cl),min(len(c) for s,c,e in cl)))
  print(name,'pairs',len(outcomes),'feasible',sum(x[0] for x in outcomes),'unfeasible',sum(not x[0] for x in outcomes),'max width',max(x[1] for x in outcomes),'min width',min(x[2] for x in outcomes),flush=True)
