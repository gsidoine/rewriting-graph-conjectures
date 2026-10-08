"""Sample independent tree pairs and exact CNF; not a universal proof."""
import sys,random,time,json
import networkx as nx
from tree_clause_lab import instance,satisfy
from partition_lab import cuts
import numpy as np

def kruskal_tree(n, edges, available, rng):
 p=list(range(n));size=[1]*n
 def root(v):
  while p[v]!=v:p[v]=p[p[v]];v=p[v]
  return v
 ids=list(available);rng.shuffle(ids)
 tree=set()
 for j in ids:
  u,v,_=edges[j];a,b=root(u),root(v)
  if a==b:continue
  if size[a]<size[b]:a,b=b,a
  p[b]=a;size[a]+=size[b];tree.add(j)
  if len(tree)==n-1:return tree
 return None

def run(G,label,count=400):
 n=len(G);E,_,_=cuts(G);m=len(E);rng=random.Random(20261008+n);stats={'graph':label,'n':n,'edges':m,'samples':0,'third_tree_samples':0,'sat':0,'unsat':0}
 st=time.time()
 for j in range(count):
  T1=kruskal_tree(n,E,range(m),rng)
  T2=kruskal_tree(n,E,set(range(m))-T1,rng)
  if T2 is None:continue
  stats['samples']+=1
  R=set(range(m))-T1-T2
  T3=kruskal_tree(n,E,R,rng)
  if T3 is None:continue
  stats['third_tree_samples']+=1
  z1=np.array([int(e in T1) for e in range(m)]);z2=np.array([int(e in T2) for e in range(m)])
  nv,cl=instance(G,E,z1,z2)
  sat,x=satisfy(nv,cl)
  stats['sat' if sat else 'unsat']+=1
  if not sat:
   stats['counterexample']={'edge_list':[list(e[:2]) for e in E],'T1':sorted(T1),'T2':sorted(T2),'T3':sorted(T3)}
   break
 stats['seconds']=round(time.time()-st,2)
 print(json.dumps(stats),flush=True)
 return stats

if __name__=='__main__':
 G=nx.complement(nx.Graph([(i,i+4) for i in range(4)]));G.add_nodes_from(range(8))
 out=[run(G,'K8_minus_1factor',700)]
 for n in [9,10,12]:
  G=nx.random_regular_graph(6,n,seed=111+n)
  out.append(run(G,'random6regular_'+str(n),280))
 with open('/mnt/data/edge_pivot_oct2026/third_tree_search.json','w') as f:json.dump(out,f,indent=2)
