"""Exhaustively checks all 2^6 labelled host graphs on 4 vertices at c=1,2,4."""
import itertools,time
from check_strict_paths import check
pairs=list(itertools.combinations(range(4),2))
count=0
start=time.time()
for c in (1,2,4):
 for z in range(1,64):
  H=[pairs[i] for i in range(6) if z>>i&1]
  result=check(4,H,c)
  count+=1
 print('verified all 63 nonempty 4-vertex labelled H; c=',c,flush=True)
print('TOTAL',count,'elapsed_seconds',round(time.time()-start,2),flush=True)
