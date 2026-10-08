"""EXACT canonical bipartite adjacency under row/column permutations and transpose.
Every simple cubic bipartite graph is represented by three permutations (König).
"""
from itertools import permutations
import json,sys,time
from pathlib import Path

def classes(h):
  perms=list(permutations(range(h)))
  trans=[]
  for p in perms:
    pos=[1<<p[i] for i in range(h)]
    trans.append(tuple(sum(pos[i] for i in range(h) if mask & (1<<i)) for mask in range(1<<h)))
  def canonical(rows):
    # Each column permutation yields permuted row masks. Sort rows to quotiented left relabeling.
    return min(tuple(sorted(T[m] for m in rows)) for T in trans)
  canonical_seen={}; count=0; disconnected=0
  for p in perms:
    if any(p[i]==i for i in range(h)):continue
    for q in perms:
      if any(q[i]==i or q[i]==p[i] for i in range(h)): continue
      rows=tuple((1<<i)|(1<<p[i])|(1<<q[i]) for i in range(h))
      # BFS reach all left via right neighbors
      vis=1; changed=True
      while changed:
        nxt=vis
        reached=0
        for i in range(h):
          if (vis>>i)&1:reached|=rows[i]
        for i in range(h):
          if rows[i]&reached:nxt |= (1<<i)
        changed=nxt!=vis;vis=nxt
      if vis!=(1<<h)-1:
        disconnected+=1;continue
      count+=1
      transposed=tuple(sum(1<<i for i in range(h) if rows[i]&(1<<j)) for j in range(h))
      key=min(canonical(rows),canonical(transposed))
      if key not in canonical_seen: canonical_seen[key]=1
      else:canonical_seen[key]+=1
  result=[]
  for key, mult in canonical_seen.items():
    edges=[(i,h+j) for i,m in enumerate(key) for j in range(h) if m&(1<<j)]
    result.append({'edges':edges,'factorization_representations':mult})
  return {'h':h,'connected_labeled_factorizations':count,'disconnected_factorizations':disconnected,'isomorphism_classes':len(result),'graphs':result}

if __name__=='__main__':
    h=int(sys.argv[1]);t=time.time();D=classes(h);print(h,'classes',D['isomorphism_classes'],'factorization_representations',D['connected_labeled_factorizations'],'sec',round(time.time()-t,1),flush=True)
    with open(str(Path(__file__).resolve().parent/f'all_bipartite_{h}.json'),'w') as f:json.dump(D,f,indent=2)
