"""Dependency-free independent verifier of the Q34 componentwise pair-repair trace."""
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'q34_witness_32.json'
CERT=HERE/'q34_three_pair_repair.json'

def verify():
    original=json.loads(BASE.read_text());proof=json.loads(CERT.read_text())
    n=original['vertices'];E=[tuple(item[:2]) for item in original['edges']]
    M=[{e for e,(_,_,S) in enumerate(original['edges']) if i in S} for i in range(6)]
    assert n==32 and len(E)==48 and len(set(E))==48
    assert proof['n']==n and proof['original_energy']==34
    defects=[]
    def mult(): return [sum(e in row for row in M) for e in range(len(E))]
    def energy(): return sum((m-2)**2 for m in mult())
    def ispm(row):
        degree=[0]*n
        for e in row:
            u,v=E[e];degree[u]+=1;degree[v]+=1
        return all(x==1 for x in degree)
    assert all(ispm(row) for row in M)
    assert energy()==34
    for step in proof['steps']:
        old=mult();qold=energy()
        assert step['before']==qold
        indices=step['coordinates']
        assert len(indices)==2 and len(set(indices))==2
        C=set(step['edges_fixed'])
        assert C and all(old[e]!=2 for e in C)
        assert len(step['replacement_edge_ids'])==2
        for i,new in zip(indices,step['replacement_edge_ids']):
            assert len(new)==len(set(new)); row=set(new)
            assert all(0<=e<len(E) for e in row) and ispm(row)
            M[i]=row
        updated=mult()
        assert all(updated[e] == (2 if e in C else old[e]) for e in range(len(E)))
        assert step['after']==energy()<qold
        defects.append(energy())
    assert energy()==0
    assert len(proof['steps'])==3
    print('PASS independent component-repair certificate: Q trace', [34]+defects,'each step replaces exactly two matchings and fixes one defect component')
    return True

if __name__=='__main__':verify()
