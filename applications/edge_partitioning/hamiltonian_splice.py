"""Construct 6-edge-connected 6-regular vertex sums of K7 with 3 Hamilton cycles.
The result is a standard-style Hamiltonian splice, not a new solution to DJS.
"""
import random,networkx as nx

def canonical(a,b):return (a,b) if a<b else (b,a)

def base_cycle(n,step):
    return {canonical(i,(i+step)%n) for i in range(n)}

def build(number_of_K7s,seed=42):
    assert number_of_K7s>=1
    rng=random.Random(seed)
    colors=[base_cycle(7,j) for j in [1,2,3]]
    vertices=set(range(7));next_id=7
    for k in range(1,number_of_K7s):
        old_v=rng.choice(sorted(vertices))
        oldpairs=[]
        for color in colors:
            ns=[b if a==old_v else a for a,b in color if old_v in (a,b)]
            assert len(ns)==2
            oldpairs.append(tuple(ns))
        old_neighbours=[v for pair in oldpairs for v in pair]
        new_neighbours=list(range(next_id,next_id+6));next_id+=6
        rng.shuffle(new_neighbours)
        mapping=dict(zip(old_neighbours,new_neighbours))
        # Build the K7 local cycles via a relabeling preserving each old color pair
        perm={0:-1}
        for j,(a,b) in enumerate(oldpairs,1):
            perm[j]=mapping[a]
            perm[7-j]=mapping[b]
        local_colors=[]
        for j in [1,2,3]:
            local_colors.append({canonical(perm[a],perm[b]) for a,b in base_cycle(7,j) if 0 not in (a,b)})
        newcolors=[]
        for j in range(3):
            remaining={e for e in colors[j] if old_v not in e}
            extra={canonical(a,mapping[a]) for a in oldpairs[j]}
            newcolors.append(remaining|local_colors[j]|extra)
        vertices.remove(old_v)
        vertices.update(new_neighbours)
        colors=newcolors
        G=nx.Graph();G.add_nodes_from(vertices)
        for C in colors:G.add_edges_from(C)
        assert all(G.degree(v)==6 for v in G)
        assert len(set().union(*colors))==sum(map(len,colors))==3*len(vertices)
        assert all(len(C)==len(vertices) and nx.is_connected(nx.Graph(list(C))) for C in colors)
    G=nx.Graph();G.add_nodes_from(vertices)
    for C in colors:G.add_edges_from(C)
    return G,colors

if __name__=='__main__':
    for k in range(1,5):
        G,C=build(k)
        print('copies',k,'vertices',len(G),'edges',len(G.edges),'edgeconnectivity',nx.edge_connectivity(G),'hamiltoncycles',len(C),'color_lengths',[len(c) for c in C],flush=True)
        assert nx.edge_connectivity(G)==6
