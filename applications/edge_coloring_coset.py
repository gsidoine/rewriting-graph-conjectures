"""Exact stabilizer-enriched coset holonomy of finite equivariant reconfigurations.

Elements of the finite group are permutation tuples; action is provided
by caller and may have nontrivial stabilizers.
"""
from .edge_coloring_voltage import mul, inv
from .edge_coloring_rigidity import components


def group_closure(generators, identity):
    gens = list(generators)
    gens += [inv(g) for g in gens]
    found = {identity}
    todo = [identity]
    while todo:
        x = todo.pop()
        for g in gens:
            y = mul(x,g)
            if y not in found:
                found.add(y)
                todo.append(y)
    return found


def position_action(g, state):
    """Permute positions, not alphabet labels."""
    result = [None] * len(state)
    for i, x in enumerate(state):
        result[g[i]] = x
    return tuple(result)


def coset_holonomy(states, adjacency, group, action):
    """Return representatives, stabilizers and exact neutral component data.

    An output record has (quotient_size,holonomy_order,count,component_size,
    stabilizer_orders). No freeness is required.
    """
    group = tuple(group)
    one = tuple(range(len(group[0])))
    index = {s:i for i,s in enumerate(states)}
    assert len(index) == len(states) and one in group
    unseen = set(states)
    reps, stabilizers, where = [], [], {}
    while unseen:
        rep = min(unseen)
        i = len(reps)
        reps.append(rep)
        orbit = {}
        H = []
        for g in group:
            s = action(g,rep)
            assert s in index
            orbit.setdefault(s,g)
            if s == rep:
                H.append(g)
        assert len(orbit) * len(H) == len(group)
        for s,g in orbit.items():
            where[index[s]] = (i,g)
            unseen.remove(s)
        stabilizers.append(H)
    assert sum(len(group)//len(H) for H in stabilizers)==len(states)
    edges = []
    for i,rep in enumerate(reps):
        for nxt in adjacency[index[rep]]:
            j,g = where[nxt]
            edges.append((i,j,g))
    qadj = [set() for _ in reps]
    for i,j,_ in edges:
        qadj[i].add(j)
        qadj[j].add(i)
    answer = []
    for B in components(qadj):
        root=min(B)
        paths={root:one}
        todo=[root]
        while todo:
            i=todo.pop()
            for a,j,g in edges:
                if a == i and j not in paths:
                    paths[j] = mul(paths[i],g)
                    todo.append(j)
        assert set(paths)==B
        gens=[mul(mul(paths[i],g),inv(paths[j]))
              for i,j,g in edges if i in B]
        for i in B:
            gens.extend(mul(mul(paths[i],h),inv(paths[i]))
                        for h in stabilizers[i])
        K=group_closure(gens,one)
        assert len(group)%len(K)==0
        assert all(len(K)%len(stabilizers[i])==0 for i in B)
        count=len(group)//len(K)
        size=sum(len(K)//len(stabilizers[i]) for i in B)
        answer.append((len(B),len(K),count,size,
                       tuple(len(stabilizers[i]) for i in sorted(B))))
    assert sum(count*size for _,_,count,size,_ in answer)==len(states)
    return reps,stabilizers,answer
