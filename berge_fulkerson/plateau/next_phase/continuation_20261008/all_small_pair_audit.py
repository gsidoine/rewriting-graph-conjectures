"""Exhaustive six-matching multiset two-block local-minimality audit.
Graph list from exact canonical generation; uses numpy vectorization for block optimization.
"""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
import math,json,sys,time
from pathlib import Path
import numpy as np

def audit(graph, h):
    edges = [tuple(e) for e in graph['edges']]
    eset=set(edges)
    pm=[]
    for p in permutations(range(h)):
        selected=set((i,h+p[i]) for i in range(h))
        if selected <= eset:
            pm.append(np.array([int(e in selected) for e in edges],dtype=np.int16))
    A=np.stack(pm)
    k=len(A)
    pairs=np.stack([A[a]+A[b] for a,b in combinations_with_replacement(range(k),2)])
    pair_res=pairs-2
    # Store minimal objective when the other four coordinates are frozen.
    best4={}
    for four in combinations_with_replacement(range(k),4):
        base=np.sum(A[list(four)],axis=0)
        best4[four]=int(np.sum((pair_res+base)**2,axis=1).min())
    n=0;nq0=0;ntraps=0;minimumtrap=None
    q_hist=Counter();min_gain=1000000
    positions=tuple(combinations(range(6),2))
    for c in combinations_with_replacement(range(k),6):
        n+=1
        m=np.sum(A[list(c)],axis=0)
        q=int(np.sum((m-2)**2))
        if not q: nq0+=1;continue
        q_hist[q]+=1
        best=min(best4[tuple(c[i] for i in range(6) if i not in (a,b))] for a,b in positions)
        if best>=q:
            ntraps+=1
            if minimumtrap is None or q<minimumtrap['q']:
                minimumtrap={'q':q,'state':list(c),'best_pair_q':best,'edges':edges,'perfect_matchings':[p.tolist() for p in A]}
        min_gain=min(min_gain, q-best)
    return {'h':h,'perfect_matchings':k,'six_matching_multisets':n,'zero_defect':nq0,'positive_q_pair_traps':ntraps,'minimum_positive_gain':min_gain,'minimum_trap':minimumtrap,'top_q_hist':q_hist.most_common(5)}

def main():
    out=[];start=time.time()
    for h in range(3,7):
        info=json.load(open(str(Path(__file__).resolve().parent/f'all_bipartite_{h}.json')))
        for j,graph in enumerate(info['graphs']):
            t=time.time();result=audit(graph,h);result['class_index']=j;result['seconds']=round(time.time()-t,2)
            out.append(result);print('CLASS',h,j,'PMS',result['perfect_matchings'],'STATES',result['six_matching_multisets'],'TRAPS',result['positive_q_pair_traps'],'SECONDS',result['seconds'],flush=True)
            if result['minimum_trap']:print('COUNTEREXAMPLE',result['minimum_trap'],flush=True)
    print('FINAL CLASSES',len(out),'STATES',sum(z['six_matching_multisets'] for z in out),'TRAPS',sum(z['positive_q_pair_traps'] for z in out),'TOTAL_SECS',round(time.time()-start,1),flush=True)
    with open(str(Path(__file__).resolve().parent/'exhaustive_audit.json'),'w') as f:json.dump(out,f,indent=2)

if __name__=='__main__':main()
