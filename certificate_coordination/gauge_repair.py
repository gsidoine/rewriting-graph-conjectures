"""Exact weighted repair for finite-group edge-potential certificates.

An oriented constraint (u,v,g) means x[v] = g * x[u].
The group need not be abelian. The initial x0 must satisfy all old edges.
"""
from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=True)
class FiniteGroup:
    elements: tuple
    identity: object
    mul: object
    inv: object


def cyclic_group(q):
    assert q >= 2
    return FiniteGroup(tuple(range(q)), 0, lambda a,b:(a+b)%q, lambda a:(-a)%q)


def permutation_group_3():
    from itertools import permutations
    elems = tuple(permutations(range(3)))
    e = (0,1,2)
    def mul(a,b):
        return tuple(a[b[i]] for i in range(3))
    def inv(a):
        return tuple(a.index(i) for i in range(3))
    return FiniteGroup(elems, e, mul, inv)


def valid(labels, edges, grp):
    return all(labels[v] == grp.mul(g, labels[u]) for u,v,g in edges)


def old_components(n, old):
    adj = [[] for _ in range(n)]
    for u,v,_ in old:
        adj[u].append(v)
        adj[v].append(u)
    comp = [-1]*n
    blocks = []
    for s in range(n):
        if comp[s] >= 0:
            continue
        j = len(blocks)
        comp[s] = j
        todo = [s]
        block = []
        while todo:
            v = todo.pop()
            block.append(v)
            for w in adj[v]:
                if comp[w] < 0:
                    comp[w] = j
                    todo.append(w)
        blocks.append(block)
    return comp, blocks


@dataclass
class RepairResult:
    feasible: bool
    min_cost: int | None
    corrected: list | None
    comp: list
    quotient_blocks: list
    labels: list | None
    reason: str


def exact_repair(n, old, added, x0, grp, vertex_weights=None):
    """Exact optimum or inconsistency, using quotient-group transport."""
    assert len(x0) == n and valid(x0, old, grp)
    weights = list(vertex_weights if vertex_weights is not None else [1]*n)
    assert len(weights) == n and all(w >= 0 for w in weights)
    comp, blocks = old_components(n, old)
    k = len(blocks)
    adj = [[] for _ in range(k)]
    for u,v,g in added:
        h = grp.mul(grp.mul(grp.inv(x0[v]),g),x0[u])
        cu,cv = comp[u],comp[v]
        adj[cu].append((cv,h))
        adj[cv].append((cu,grp.inv(h)))
    offsets = [None]*k
    quotient_blocks = []
    roots = {}
    for s in range(k):
        if offsets[s] is not None:
            continue
        offsets[s] = grp.identity
        todo = [s]
        block = []
        while todo:
            a = todo.pop()
            block.append(a)
            for b,h in adj[a]:
                expected = grp.mul(h, offsets[a])
                if offsets[b] is None:
                    offsets[b] = expected
                    todo.append(b)
                elif offsets[b] != expected:
                    return RepairResult(False,None,None,comp,quotient_blocks,None,
                                        'inconsistent quotient holonomy')
        quotient_blocks.append(block)
        weight_groups = defaultdict(int)
        for c in block:
            weight_groups[offsets[c]] += sum(weights[v] for v in blocks[c])
        mode = max(grp.elements, key=lambda x:weight_groups[x])
        roots[s] = grp.inv(mode)
        for c in block:
            roots[c] = roots[s]
    corrected = [grp.mul(x0[v],grp.mul(offsets[comp[v]],roots[comp[v]]))
                 for v in range(n)]
    assert valid(corrected,old+added,grp)
    cost = sum(weights[i] for i in range(n) if corrected[i] != x0[i])
    return RepairResult(True,cost,corrected,comp,quotient_blocks,offsets,'ok')


def reconfiguration_components(n, edges, grp, max_move):
    """(#components, states/component) under moves changing <=max_move vertices.

    Assumes the edge-potential system is feasible.
    """
    _, blocks = old_components(n,edges)
    frozen = sum(len(block)>max_move for block in blocks)
    movable = len(blocks)-frozen
    return len(grp.elements)**frozen, len(grp.elements)**movable


def sharp_mode_family(grp, block_size):
    """All distinct quotient offsets: minimum (|group|-1)*block_size."""
    assert block_size >= 1
    members = [grp.identity] + [a for a in grp.elements if a != grp.identity]
    q = len(members)
    n = q * block_size
    e = grp.identity
    old = []
    for i in range(q):
        old.extend((i*block_size+j, i*block_size+j+1, e)
                   for j in range(block_size-1))
    new = []
    for i in range(q-1):
        h = grp.mul(members[i+1],grp.inv(members[i]))
        new.append(((i+1)*block_size-1, (i+1)*block_size, h))
    x0 = [e]*n
    assert exact_repair(n,old,new,x0,grp).min_cost == (q-1)*block_size
    return n, old, new, x0
