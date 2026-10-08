"""Exact two-coordinate Q=6 completion criterion for arbitrary cubic graphs.

After freezing four matchings, the nonnegative residual multiplicities
form a spanning 2-regular multigraph. They can be split into two PMs
if and only if no odd cycle remains. This isolates the nonbipartite gap.
"""
from itertools import combinations
import networkx as nx


def q(edges,state):
    return sum((sum(m>>j&1 for m in state)-2)**2 for j in range(len(edges)))


def qualifying_pairs(edges,state):
    assert q(edges,state)==6
    out=[]
    for i,j in combinations(range(6),2):
        remaining=[2-sum((state[t]>>e)&1 for t in range(6) if t not in (i,j))
                   for e in range(len(edges))]
        if any(k<0 for k in remaining):continue
        H=nx.MultiGraph()
        H.add_nodes_from(v for uv in edges for v in uv)
        H.add_edges_from((u,v) for (u,v),k in zip(edges,remaining) for _ in range(k))
        assert all(d==2 for v,d in H.degree())
        if nx.is_bipartite(H):out.append((i,j))
    return out


def validate():
    from .sharp_trap import load
    edges,states=load()
    return {'Q_initial':q(edges,states[0]),
            'valid_completion_pairs':qualifying_pairs(edges,states[0])}

if __name__=='__main__':print(validate())
