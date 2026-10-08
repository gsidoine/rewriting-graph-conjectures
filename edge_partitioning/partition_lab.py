"""Exact cut-constraint feasibility and cut-defect local-search lab.
No claim of resolving DeVos--Johnson--Seymour conjecture.
"""
import itertools,random,json,sys
import numpy as np
import networkx as nx
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix

def cuts(G):
    V=list(G.nodes);n=len(V); E=list(G.edges(keys=True)) if G.is_multigraph() else [(a,b,i) for i,(a,b) in enumerate(G.edges())]
    vpos={v:i for i,v in enumerate(V)}
    # Representatives: include first vertex and exclude whole vertex set
    c=[];subs=[]
    for t in range(0,(1<<(n-1))-1):
        S={V[0]}
        for i in range(1,n):
            if (t>>(i-1))&1:S.add(V[i])
        arr=np.fromiter((int((u in S)!=(v in S)) for u,v,_ in E),dtype=np.int8,count=len(E))
        if arr.sum():c.append(arr);subs.append(tuple(sorted(S)))
    return E,np.vstack(c),subs

def partition_milp(G):
    E,A,S=cuts(G);n,m=A.shape
    if np.any(A.sum(axis=1)<4):return False,None,{'badcuts':len(A[A.sum(axis=1)<4])}
    lower=2*np.ones(n); upper=A.sum(axis=1)-2
    res=milp(c=np.zeros(m),integrality=np.ones(m),bounds=Bounds(np.zeros(m),np.ones(m)),constraints=LinearConstraint(csr_matrix(A),lower,upper),options={'time_limit':30})
    if res.x is None: return False,None,{'status':res.status,'message':res.message}
    z=np.rint(res.x).astype(np.int8)
    return bool(np.all((A@z>=2)&(A@z<=upper))),z,{'n':G.number_of_nodes(),'m':m,'cut_constraints':n,'status':res.status}

def defect(A,z):
    r=A@z;s=A.sum(axis=1)
    return int(np.maximum(2-r,0).sum()+np.maximum(r-s+2,0).sum())

def descend_one(A,seed,steps=500):
    rng=np.random.default_rng(seed);m=A.shape[1];z=rng.integers(0,2,size=m).astype(np.int8)
    for step in range(steps):
        d=defect(A,z)
        if d==0:return 0,step,z
        best=d;which=-1
        for j in range(m):
            z[j]^=1
            nd=defect(A,z)
            z[j]^=1
            if nd<best:best=nd;which=j
        if which<0:return d,step,z
        z[which]^=1
    return defect(A,z),steps,z

def graphs():
    for n in [7,8,9,10,12]:
      for sd in range(3 if n<11 else 2):
        if n==7:G=nx.complete_graph(n)
        elif n==8:G=nx.complement(nx.Graph([(i,i+4) for i in range(4)]));G.add_nodes_from(range(8));G=nx.complement(nx.Graph([(i,i+4) for i in range(4)]))
        else:G=nx.random_regular_graph(6,n,seed=111+n*9+sd)
        if nx.edge_connectivity(G)>=6: yield f'reg6_n{n}_{sd}',G
    yield 'K6_6',nx.complete_bipartite_graph(6,6)
    yield 'K8',nx.complete_graph(8)

if __name__=='__main__':
    report=[]
    for name,G in graphs():
      try:
        ok,z,detail=partition_milp(G)
        E,A,S=cuts(G)
        trials=[descend_one(A,3*i+17) for i in range(12)]
        traps=[{'defect':q,'step':s,'color_bits':''.join(map(str,v.tolist()))} for q,s,v in trials if q>0]
        record={'name':name,'edge_connectivity':nx.edge_connectivity(G),'feasible':ok,'details':detail,'local_search_trials':len(trials),'single_edge_terminal_positive':len(traps),'traps':traps[:2]}
        report.append(record)
        print(json.dumps({k:v for k,v in record.items() if k!='traps'}),flush=True)
      except Exception as e: print(name,'ERROR',repr(e),flush=True)
    with open('/mnt/data/edge_pivot_oct2026/exact_search_results.json','w') as f:json.dump(report,f,indent=2)
