"""Exact nonabelian voltage quotient of S3-equivariant coloring reconfigurations."""
from itertools import permutations
from applications.edge_coloring_rigidity import components

S3 = tuple(permutations(range(3)))
ONE = (0, 1, 2)


def mul(a, b):
    return tuple(a[b[i]] for i in range(3))


def inv(a):
    return tuple(a.index(i) for i in range(3))


def act(g, state):
    return tuple(g[c] for c in state)


def generated_subgroup(generators):
    generators = list(generators)
    generators += [inv(g) for g in generators]
    found = {ONE}
    stack = [ONE]
    while stack:
        x = stack.pop()
        for g in generators:
            y = mul(x, g)
            if y not in found:
                found.add(y)
                stack.append(y)
    return found


def orbit_coordinates(states):
    """Identify each state uniquely as a color permutation of an orbit representative."""
    index = {s: i for i,s in enumerate(states)}
    assert len(index) == len(states)
    reps, where = [], {}
    unseen = set(states)
    while unseen:
        representative = min(unseen)
        j = len(reps)
        reps.append(representative)
        orbit = {act(g,representative):g for g in S3}
        assert len(orbit) == 6 and all(s in index for s in orbit)
        for state,g in orbit.items():
            where[index[state]] = j,g
            unseen.remove(state)
    return reps,where


def voltage_quotient(states, adjacency):
    """Recover exact full component sizes from orbit quotient holonomy.

    A quotient edge (i,j,g) lifts to (i,h) -> (j,h*g).
    Only works for symmetric S3-equivariant relations and FREE S3 actions.
    """
    reps, where = orbit_coordinates(states)
    index = {s:i for i,s in enumerate(states)}
    assert len(adjacency) == len(states)
    for i,opts in enumerate(adjacency):
        for j in opts:
            assert i in adjacency[j]
        for g in S3:
            gi = index[act(g,states[i])]
            assert {index[act(g,states[j])] for j in opts} == adjacency[gi]
    edges = []
    for i,s in enumerate(reps):
        for nxt in adjacency[index[s]]:
            j,g = where[nxt]
            edges.append((i,j,g))
    adj = [set() for _ in reps]
    for i,j,g in edges:
        adj[i].add(j)
        adj[j].add(i)
    result = []
    for B in components(adj):
        root = min(B)
        paths = {root:ONE}
        todo = [root]
        while todo:
            i = todo.pop()
            for a,j,g in edges:
                if a == i and j not in paths:
                    paths[j] = mul(paths[i],g)
                    todo.append(j)
        assert set(paths) == B
        generators = [mul(mul(paths[i],g),inv(paths[j]))
                      for i,j,g in edges if i in B]
        K = generated_subgroup(generators)
        assert 6 % len(K) == 0
        result.append((len(B),len(K),6//len(K),len(B)*len(K)))
    assert sum(count*size for _,_,count,size in result) == len(states)
    return reps,edges,result
