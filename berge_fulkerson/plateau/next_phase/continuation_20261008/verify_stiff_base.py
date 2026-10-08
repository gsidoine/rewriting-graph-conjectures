"""Standard-library-only exact proof certificate for the 18-vertex glued gadget.

Enumerates every perfect matching and checks both the local minimum and the
stiff-port inequality. Input has exactly 18 vertices and 27 edges, and is
not assumed correct unless it passes all checks.
"""
import json
from collections import Counter
from pathlib import Path

BASE=Path(__file__).resolve().parents[2]/'sharp_18_vertex.json'
if not BASE.exists():
    BASE=Path('/mnt/data/work_oct8/rewriting-graph-conjectures-main/berge_fulkerson/plateau/sharp_18_vertex.json')

def verify(filepath=BASE):
    d=json.loads(Path(filepath).read_text())
    E=[tuple(sorted(e)) for e in d['edges']]
    n=18
    assert len(E)==27 and len(set(E))==27 and all(u!=v for u,v in E)
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(E):
        adj[u].append((v,i));adj[v].append((u,i))
    assert all(len(a)==3 for a in adj)
    all_pm=[]
    def recurse(left,chosen):
        if left==0:
            all_pm.append(chosen);return
        low=(left&-left).bit_length()-1
        for v,idx in adj[low]:
            if left>>v&1:
                recurse(left &~(1<<low)&~(1<<v),chosen|(1<<idx))
    recurse((1<<n)-1,0)
    assert len(set(all_pm))==47
    stages=[d[k] for k in ('matching_masks_initial','matching_masks_neutral','matching_masks_target')]
    for s in stages:
        assert all(m in all_pm for m in s)
    assert sum((sum((M>>i)&1 for M in stages[0])-2)**2 for i in range(27))==6
    assert sum((sum((M>>i)&1 for M in stages[1])-2)**2 for i in range(27))==6
    assert sum((sum((M>>i)&1 for M in stages[2])-2)**2 for i in range(27))==0
    assert sum(stages[0][j]!=stages[1][j] for j in range(6))==1
    assert sum(stages[1][j]!=stages[2][j] for j in range(6))==1
    ports={v:[z for z,e in enumerate(E) if v in e] for v in (0,16)}
    assert not any(set(E[z])&set(E[z2]) for z in ports[0] for z2 in ports[16])
    assert all(all(sum((M>>z)&1 for M in st)==2 for z in ports[v]) for st in stages for v in ports)
    # Boundary choices are stationary along the explicit neutral-exit path.
    def choice(m,v):
        return next(z for z in ports[v] if (m>>z)&1)
    for v in ports:
        assert all(choice(stages[0][j],v)==choice(stages[1][j],v)==choice(stages[2][j],v) for j in range(6))
    worst={}
    for phase in (0,2):
        s=stages[phase]
        min_margin=999
        for j in range(6):
            base=[sum((s[z]>>idx)&1 for z in range(6) if z!=j) for idx in range(27)]
            q0=sum((base[idx]+((s[j]>>idx)&1)-2)**2 for idx in range(27))
            for m in all_pm:
                qnew=sum((base[idx]+((m>>idx)&1)-2)**2 for idx in range(27))
                changed=choice(m,0)!=choice(s[j],0)
                margin=qnew-q0-2*int(changed)
                min_margin=min(min_margin,margin)
                assert margin>=0,(phase,j,m,margin)
        worst[phase]=min_margin
    return {'vertices':n,'edges':len(E),'perfect_matchings':len(all_pm),'stiff_port':0,'loose_port':16,
            'minimum_stiff_margin_initial':worst[0],'minimum_stiff_margin_target':worst[2],
            'Q_path':[6,6,0]}

if __name__=='__main__':
    print('PASS',verify())
