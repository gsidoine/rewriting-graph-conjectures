"""Independent, exact K3,3/Petersen six-matching multicover reconfiguration audit.

Requires networkx. Invoke:
    python repro_runs/pair_rigid_mixed_tile_audit.py

For KP, PK, PP: exhaustive valid 6-tuples, exact neutral switches, connected
components and fixed-star fibers. For KP: exact 3-coordinate trade witnesses.
"""
import itertools
from collections import Counter
import networkx as nx


def build(word):
    tiles=[]
    for ch in word:
        if ch=="K":
            tiles.append((nx.complete_bipartite_graph(3,3),(0,1)))
        elif ch=="P":
            tiles.append((nx.petersen_graph(),(0,2)))
        else:
            raise ValueError(word)
    removed=set()
    E=set()
    V=set()
    for i,(graph,(left,right)) in enumerate(tiles):
        if i: removed.add((i,left))
        if i<len(tiles)-1: removed.add((i,right))
        V.update((i,v) for v in graph)
        E.update(tuple(sorted(((i,u),(i,v)))) for u,v in graph.edges())
    for i in range(len(tiles)-1):
        g,(l,r)=tiles[i]
        h,(ll,rr)=tiles[i+1]
        for a,b in zip(sorted(g.neighbors(r)),sorted(h.neighbors(ll))):
            E.add(tuple(sorted(((i,a),(i+1,b)))))
    G=nx.Graph()
    G.add_nodes_from(V-removed)
    G.add_edges_from(e for e in E if not (set(e)&removed))
    assert all(d==3 for _,d in G.degree())
    assert nx.edge_connectivity(G)==3
    return G,tiles


def matchings(G):
    E=sorted(tuple(sorted(e)) for e in G.edges())
    adj={v:[] for v in G}
    for i,(u,v) in enumerate(E):
        adj[u].append((v,i))
        adj[v].append((u,i))
    def rec(unused,mask):
        if not unused:
            yield mask
            return
        v=min(unused)
        for w,i in adj[v]:
            if w in unused:
                yield from rec(unused-{v,w},mask|(1<<i))
    return E,sorted(set(rec(frozenset(G),0)))


def local_k_parities(E, PM, tile_id, ports):
    # Recover the deleted tile port vertex, recreating its 3 incident spokes.
    left,right=ports
    out=[]
    for mask in PM:
        pairs=[]
        for e,(u,v) in enumerate(E):
            if not mask>>e&1:
                continue
            if u[0]==v[0]==tile_id:
                pairs.append(tuple(sorted((u[1],v[1]))))
            elif u[0]==tile_id:
                pairs.append(tuple(sorted((left,u[1]))))
            elif v[0]==tile_id:
                pairs.append(tuple(sorted((left,v[1]))))
        assert len(pairs)==3
        perm=tuple(next((v-3 if u==row else u-3) for u,v in pairs if row in (u,v)) for row in range(3))
        out.append(sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2)
    return out


def neutral_cycles(mask,E):
    todo={i for i in range(len(E)) if mask>>i&1}
    cycles=[]
    while todo:
        cc={todo.pop()}
        while True:
            vtx={v for i in cc for v in E[i]}
            add={i for i in todo if vtx.intersection(E[i])}
            if not add: break
            cc.update(add)
            todo.difference_update(add)
        cycles.append(sum(1<<i for i in cc))
    return cycles


def component_labels(pool, adjacency, types):
    pool=set(pool)
    components=[]
    while pool:
        start=pool.pop()
        stack=[start]
        for st in stack:
            for next_state in adjacency[st]:
                if next_state in pool:
                    pool.remove(next_state)
                    stack.append(next_state)
        components.append((types[start],len(stack)))
    return sorted(components)


def audit(word):
    G, tiles=build(word)
    assert not (word.count("P")==0)
    assert G.number_of_nodes()==4*word.count("K")+8*word.count("P")+2
    E,PM=matchings(G)
    Es=[{i for i in range(len(E)) if mask>>i&1} for mask in PM]
    bymask={mask:i for i,mask in enumerate(PM)}
    counts=[0]*len(E)
    states=[]
    def rec(cur):
        if len(cur)==6:
            if all(x==2 for x in counts):
                states.append(tuple(cur))
            return
        rem=5-len(cur)
        for j,sel in enumerate(Es):
            if any(counts[e]==2 for e in sel):
                continue
            for e in sel: counts[e]+=1
            if all(c+rem>=2 for c in counts):
                rec(cur+[j])
            for e in sel: counts[e]-=1
    rec([])
    allstates=set(states)
    assert len(allstates)==len(states)
    ktypes=[local_k_parities(E,PM,i,ports) for i,(_,ports) in enumerate(tiles) if word[i]=="K"]
    types={st:tuple(sum(1-parity[j] for j in st)//3 for parity in ktypes) for st in states}
    adjacency={}
    move_count=0
    for st in states:
        next_states=set()
        for i,j in itertools.combinations(range(6),2):
            for C in neutral_cycles(PM[st[i]]^PM[st[j]],E):
                q=list(st)
                q[i]=bymask[PM[st[i]]^C]
                q[j]=bymask[PM[st[j]]^C]
                q=tuple(q)
                assert q in allstates and types[q]==types[st]
                next_states.add(q)
        adjacency[st]=next_states
        move_count+=len(next_states)
    comps=component_labels(states,adjacency,types)
    k=word.count("K");p=word.count("P")
    exp=sorted((t,90*(8**p)*(8**sum(v==1 for v in t))) for t in itertools.product(range(3),repeat=k))
    assert comps==exp,(comps,exp)
    first=(0,tiles[0][1][0])
    star=sorted(i for i,e in enumerate(E) if first in e)
    assert len(star)==3
    def sig(st):
        return tuple(tuple(j for j,m in enumerate(st) if PM[m]>>e&1) for e in star)
    target=sig(states[0])
    fixed=[st for st in states if sig(st)==target]
    fcomps=component_labels(fixed,adjacency,types)
    exp_fixed=sorted((t,(8**p)*(8**sum(v==1 for v in t))) for t in itertools.product(range(3),repeat=k))
    assert fcomps==exp_fixed,(fcomps,exp_fixed)
    print(word, "V",len(G),"PM",len(PM),"covers",len(states),"moves",move_count,
          "components",comps,"fixed",fcomps)
    if word=="KP":
        # Different states all have the same edge multiplicity vector.
        # A 3-coordinate trade is therefore exactly two states that differ
        # in three named matching coordinates.
        transitions={}
        for ta,tb in ((0,1),(1,2)):
            A=[s for s in fixed if types[s]==(ta,)]
            B=[s for s in fixed if types[s]==(tb,)]
            witness=next(((u,v,tuple(i for i in range(6) if u[i]!=v[i]))
                for u in A for v in B
                if sum(u[i]!=v[i] for i in range(6))==3),None)
            assert witness is not None
            transitions[(ta,tb)]=witness
        print("KP fixed-boundary 3-coordinate trade witnesses:",transitions)
        return transitions


if __name__=="__main__":
    for word in ("KP","PP","PK"):
        audit(word)
    print("ALL MIXED PAIR-RIGID CHECKS PASSED")
