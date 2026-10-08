"""Independent exact arithmetic check of two- and three-coordinate drift identities.
No dependency on the older graph-rewriting repository or numerical optimizer.
"""
from itertools import combinations, combinations_with_replacement, permutations
from random import Random
import json
from pathlib import Path


def setup(graph,h):
    E=[tuple(e) for e in graph['edges']]; eset=set(E)
    P=[]
    for p in permutations(range(h)):
        s={ (i,h+p[i]) for i in range(h) }
        if s <= eset: P.append(sum(1<<j for j,e in enumerate(E) if e in s))
    factor=None
    full=(1<<len(E))-1
    for a in P:
        for b in P:
            if a&b: continue
            c=full^(a|b)
            if c in P: factor=(a,b,c);break
        if factor:break
    assert factor and len(E)==3*h
    return E,P,factor

def Q(masks, E):
    return sum((sum((z>>e)&1 for z in masks)-2)**2 for e in range(len(E)))

def drift(state,edge_count,F):
    n=2*edge_count//3
    q=Q(state,range(edge_count))
    sum2=0
    sum3=0
    for i,j in combinations(range(6),2):
        for a,b in combinations(range(3),2):
            after=state.copy();after[i]=F[a];after[j]=F[b]
            sum2+=Q(after,range(edge_count))
    for ijk in combinations(range(6),3):
        after=state.copy()
        for i,f in zip(ijk,F): after[i]=f
        sum3+=Q(after,range(edge_count))
    assert sum2==18*q+39*n,(q,sum2,18*q+39*n)
    assert sum3==4*q+12*n,(q,sum3,4*q+12*n)
    return q,sum2//45,sum3//20

def main():
    R=Random(20261008);tested=0
    for h in range(3,7):
        D=json.load(open(str(Path(__file__).resolve().parent/f'all_bipartite_{h}.json')))
        for j,g in enumerate(D['graphs']):
            E,P,F=setup(g,h)
            if h==3:
                states=combinations_with_replacement(P,6)
            else:
                states=(tuple(R.choices(P,k=6)) for _ in range(70))
            local=0
            for st in states:
                drift(list(st),len(E),F);local+=1;tested+=1
            print('PASS h=',h,'class=',j,'states=',local,'matching_count=',len(P))
    print('TOTAL PASS',tested)
if __name__=='__main__':main()
