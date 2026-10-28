"""Independent full-state 900-certificate K3,3 PM(2) and nonfree orbit audits."""
from itertools import permutations, product, combinations
from applications.edge_coloring_rigidity import components
from applications.edge_coloring_coset import coset_holonomy, position_action
from applications.edge_coloring_voltage import S3, act


def pm2_k33():
    """Enumerate 6^6 possible tuples; retain each edge count exactly 2."""
    P = list(permutations(range(3)))
    states = []
    for s in product(range(6), repeat=6):
        incidences = [0]*9
        for m in s:
            for i,j in enumerate(P[m]):
                incidences[3*i+j] += 1
        if all(x == 2 for x in incidences):
            states.append(s)
    assert len(states) == 900
    idx = {s:i for i,s in enumerate(states)}
    adj = []
    for s in states:
        opts = set()
        for i,j in combinations(range(6),2):
            t = list(s)
            t[i],t[j] = t[j],t[i]
            if tuple(t) != s:
                opts.add(idx[tuple(t)])
        adj.append(opts)
    return P, states, adj


def test_pm2_k33_900_states_nonfree():
    P,states,adj = pm2_k33()
    # Every pair of distinct perfect matchings has one alternating cycle,
    # hence every nontrivial coordinate transposition is a valid neutral move.
    for a,b in combinations(P,2):
        E1={(i, a[i]) for i in range(3)}
        E2={(i, b[i]) for i in range(3)}
        D=E1^E2
        assert len(D) in (4,6)
        # Symmetric difference is connected as a bipartite cycle.
        import networkx as nx
        H=nx.Graph((("L",i),("R",j)) for i,j in D)
        assert nx.is_connected(H) and all(d==2 for _,d in H.degree())
    group=tuple(permutations(range(6)))
    reps,H,quot=coset_holonomy(states,adj,group,position_action)
    assert len(reps)==3
    assert sorted(map(len,H))==[1,8,8]
    assert sorted(len(group)//len(h) for h in H)==[90,90,720]
    predicted=sorted(size for _,_,count,size,_ in quot for _ in range(count))
    assert predicted==sorted(map(len,components(adj)))==[90,90,720]
    assert all(holonomy_order==720 for _,holonomy_order,_,_,_ in quot)


def test_three_constant_colorings_nonfree():
    states=[(a,a,a) for a in range(3)]
    reps,H,quot=coset_holonomy(states,[set() for _ in states],S3,act)
    assert len(reps)==1 and len(H[0])==2
    assert quot==[(1,2,3,1,(2,))]
    A=[set(range(3))-{i} for i in range(3)]
    reps,H,quot=coset_holonomy(states,A,S3,act)
    assert quot==[(1,6,1,3,(2,))]
