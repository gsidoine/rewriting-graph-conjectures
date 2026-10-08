from partition_lab import *
from scipy.sparse import hstack,vstack,identity

def pack3(G,seed=0):
 E,A,S=cuts(G);n=G.number_of_nodes();m=len(E);c=len(A)
 # x[k*m+e], each tree has n-1 edges and meets every proper cut; at most one tree uses an edge
 mats=[];lo=[];hi=[]
 mats.append(hstack([identity(m,format='csr')]*3));lo.extend(np.zeros(m));hi.extend(np.ones(m))
 for k in range(3):
  mats.append(hstack([csr_matrix(A if i==k else np.zeros((c,m))) for i in range(3)]));lo.extend(np.ones(c));hi.extend([np.inf]*c)
  mats.append(csr_matrix([[int(j//m==k)]*(n-1) if False else [int((j//m)==k) for j in range(3*m)]]));lo.append(n-1);hi.append(n-1)
 M=vstack(mats,format='csr')
 res=milp(c=np.random.default_rng(seed).uniform(0,1,size=3*m),integrality=np.ones(3*m),bounds=Bounds(np.zeros(3*m),np.ones(3*m)),constraints=LinearConstraint(M,np.array(lo),np.array(hi)),options={'time_limit':35})
 if res.x is None:return None
 z=np.rint(res.x).astype(int).reshape((3,m));return E,z

def bridges(G,E,subset):
 H=nx.Graph();H.add_nodes_from(G)
 H.add_edges_from([(u,v) for ix,(u,v,_) in enumerate(E) if subset[ix]])
 return len(list(nx.bridges(H))) if nx.is_connected(H) else 999

def experiment(G,name):
 t=pack3(G)
 if t is None:print('no packing',name,flush=True);return
 E,trees=t;m=len(E);A=1-(trees[1]|trees[2]);B=trees[1]|trees[2];ca=bridges(G,E,A);cb=bridges(G,E,B)
 options=[]
 for e in np.flatnonzero(B):
  aa=A.copy();bb=B.copy();aa[e]=1;bb[e]=0
  if bridges(G,E,bb)==0 and bridges(G,E,aa)<ca:options.append(e)
 print(name,'n',len(G),'m',m,'A bridges',ca,'B bridges',cb,'safe transfers',len(options),'three tree sizes',trees.sum(axis=1),flush=True)
 return E,trees,A,B,ca,options

if __name__=='__main__':
 for name,G in graphs():
  if name.startswith('reg6_n12'):continue
  experiment(G,name)
 G=nx.disjoint_union(nx.complete_graph(7),nx.complete_graph(7))
 for i in range(3):G.remove_edge(2*i,2*i+1);G.remove_edge(7+2*i,7+2*i+1)
 for i in range(6):G.add_edge(i,7+i)
 experiment(G,'K7_cut6_K7')
