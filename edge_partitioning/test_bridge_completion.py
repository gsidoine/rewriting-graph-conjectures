"""Adversarial independent small-instance tests of tree-cut CNF equivalence."""
from itertools import combinations,product
from bridge_completion import *

def run():
 n=5;edges=list(combinations(range(n),2));ms=list(range(len(edges)))
 trees=[]
 for ids in combinations(ms,n-1):
  if is_tree(n,[edges[j] for j in ids]):trees.append(frozenset(ids))
 checked=0;satisfiable=0;unsat=0;twosat_count=0;example=None
 for red in trees:
  for blue in trees:
   if red&blue:continue
   R,clauses=fundamental_clauses(n,edges,red,blue)
   solutions=[]
   for x in product([False,True], repeat=len(R)):
    f,b=evaluate(n,edges,red,blue,R,clauses,x)
    assert f==b, (red,blue,x,f,b)
    if f:solutions.append(x)
   checked+=1
   if solutions:satisfiable+=1;example=example or (red,blue,R,clauses,solutions[0])
   else:unsat+=1
   if max(len(c) for s,c,e in clauses)<=2:
    sat=twosat(len(R),[[(j,s) for j in c] for s,c,e in clauses])
    assert (sat is not None)==bool(solutions)
    twosat_count+=1
 print('K5 fixed pair equivalence:', checked,'disjoint tree pairs;',satisfiable,'sat;',unsat,'unsat;',twosat_count,'2SAT cases')
 assert example is not None
 print('Exemplar satisfiable tree pair',sorted(example[0]),sorted(example[1]),'residual',example[2])
 return checked
if __name__=='__main__':run()
