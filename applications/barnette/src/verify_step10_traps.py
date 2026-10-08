#!/usr/bin/env python3
"""Audit the historical step10 mask file against the supplied graph.

The result is intentionally a failure certificate: the masks do not match the
claimed pair-flip traps on this graph.  The script exits successfully after
recording the inconsistency so CI can guard against accidentally promoting the
claim again.
"""
from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
INSTANCE = ROOT / "applications/barnette/instances/step10.txt"
MASKS = ROOT / "applications/barnette/certificates/step10_unresolved_historical.txt"
OUT = ROOT / "applications/barnette/certificates/step10_inconsistency_report.json"

def read_instance():
    values=list(map(int,INSTANCE.read_text().split())); it=iter(values)
    assert next(it)==1
    steps,seed,n,m=[next(it) for _ in range(4)]
    edges=[(next(it),next(it)) for _ in range(m)]
    return steps,seed,n,edges

def components_edges(n,adj,mask):
    if not mask:return 0,0
    e=sum((adj[u]&mask).bit_count() for u in range(n) if mask>>u&1)//2
    rem=mask;c=0
    while rem:
        c+=1;frontier=rem&-rem;rem^=frontier
        while frontier:
            nb=0;w=frontier
            while w:
                bit=w&-w;w-=bit;nb|=adj[bit.bit_length()-1]
            nxt=nb&rem;rem^=nxt;frontier=nxt
    return c,e

def main():
    steps,seed,n,edges=read_instance();adj=[0]*n
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    full=(1<<n)-1
    def side(mask):
        if not mask:return n+1
        c,e=components_edges(n,adj,mask)
        return (c-1)+(e-mask.bit_count()+c)
    def phi(mask):return side(mask)+side(full^mask)
    rows=[tuple(map(int,line.split())) for line in MASKS.read_text().splitlines() if line.strip()]
    patches=[1<<u for u in range(n)]+[(1<<u)|(1<<v) for u,v in edges]
    report=[]
    certified={mask for mask,_ in rows}
    for mask,label in rows:
        successors=[]
        value=phi(mask)
        for patch in patches:
            nxt=mask^patch; nv=phi(nxt)
            if nv<=value:
                successors.append({"mask":nxt,"phi":nv,"inside_six_masks":nxt in certified})
        report.append({"mask":mask,"historical_second_column":label,"actual_phi":value,
                       "nonincreasing_size_le_2_successors":len(successors),
                       "all_successors_inside_six_masks":all(x["inside_six_masks"] for x in successors)})
    payload={"instance":{"steps":steps,"seed":seed,"vertices":n,"edges":len(edges)},
             "records":report,
             "conclusion":"The historical six-mask file is inconsistent with the supplied step10 graph and cannot serve as a trap certificate."}
    OUT.write_text(json.dumps(payload,indent=2)+"\n")
    print(payload["conclusion"])
    print("actual potentials",[row["actual_phi"] for row in report])
    assert [row["actual_phi"] for row in report]==[14,20,18,18,20,14]
    assert not all(row["all_successors_inside_six_masks"] for row in report)

if __name__=='__main__': main()
