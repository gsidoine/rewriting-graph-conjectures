"""Pure Python, dependency-free validation for the Q=34 direct 4-width witness.

Checks simple cubic bipartite, six perfect matchings, Q=34,
3-edge-connectivity (all 0-,1-,2-edge deletions), kappa=4.
"""
import json
from collections import deque
from itertools import combinations
from pathlib import Path

INSTANCE = Path(__file__).with_name('q34_witness_32.json')


def check(path=INSTANCE):
    data=json.loads(Path(path).read_text())
    n=data['vertices']; edges=data['edges']
    assert n==32 and len(edges)==3*n//2
    assert all(len(e)==3 for e in edges)
    ed=[];members=[]
    for u,v,ss in edges:
        assert isinstance(u,int) and isinstance(v,int) and u<v
        assert 0<=u<n//2<=v<n
        assert len(ss)==len(set(ss)) and all(0<=i<6 for i in ss)
        ed.append((u,v));members.append(set(ss))
    assert len(set(ed))==len(ed)
    deg=[0]*n
    for u,v in ed:deg[u]+=1;deg[v]+=1
    assert all(d==3 for d in deg)
    for color in range(6):
        md=[0]*n
        for (u,v),s in zip(ed,members):
            if color in s:md[u]+=1;md[v]+=1
        assert all(d==1 for d in md)
    Q=sum((len(s)-2)**2 for s in members)
    assert Q==34
    kappa=next(k for k in range(7) if any(
        all(sum(i in s for i in I)>=max(0,len(s)-2) for s in members)
        for I in combinations(range(6),k)))
    assert kappa==4
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(ed):adj[u].append((v,i));adj[v].append((u,i))
    def connected(removed):
        seen={0};todo=deque([0])
        while todo:
            u=todo.popleft()
            for v,i in adj[u]:
                if i in removed or v in seen:continue
                seen.add(v);todo.append(v)
        return len(seen)==n
    assert connected(set())
    for a in range(len(ed)):
        assert connected({a})
        for b in range(a+1,len(ed)):
            assert connected({a,b})
    from collections import Counter
    print('PASS: n=',n,'edges=',len(ed),'Q=',Q,'kappa=',kappa,
          'multiplicities=',dict(sorted(Counter(map(len,members)).items())),
          '3-edge-connected; checked',1+len(ed)+len(ed)*(len(ed)-1)//2,'deletion sets')
    return True

if __name__=='__main__':check()
