"""Exhaustive local-type and neutral-fiber checks for K3,3 matching multicovers.

Pure Python stdlib. pytest -q tests/test_k33_multicover_types.py
m=1 and m=2 also compared against complete brute-force 6^(3m) matching assignments.
m=3 constructs and checks every one of the predicted 94080 states.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import comb, factorial

PERMS = list(permutations(range(3)))
EDGES = [(r, c) for r in range(3) for c in range(3)]
MATCH = [frozenset((r, p[r]) for r in range(3)) for p in PERMS]

def sign(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2

def local_choices():
    out = []
    for c in range(3):
        even = next(i for i, p in enumerate(PERMS) if p[0] == c and sign(p) == 0)
        odd = next(i for i, p in enumerate(PERMS) if p[0] == c and sign(p) == 1)
        out.append((even, odd))
    return out

OPTIONS = local_choices()

def is_cover(state, m):
    return all(sum(edge in MATCH[j] for j in state) == m for edge in EDGES)

def signature(state):
    return tuple(tuple(i for i, p in enumerate(state) if PERMS[p][0] == c)
                 for c in range(3))

def states(m):
    coords = tuple(range(3 * m))
    for a in combinations(coords, m):
        remainder = set(coords) - set(a)
        for b in combinations(sorted(remainder), m):
            c = tuple(sorted(remainder - set(b)))
            groups = (a, b, c)
            for t in range(m + 1):
                choices = [list(combinations(g, t)) for g in groups]
                for even_groups in product(*choices):
                    state = [None] * (3 * m)
                    for port, labels in enumerate(groups):
                        e, o = OPTIONS[port]
                        for label in labels:
                            state[label] = e if label in even_groups[port] else o
                    yield tuple(state), t, groups

def check(m):
    counted = Counter()
    unique = set()
    fixed = defaultdict(list)
    reference = tuple(tuple(range(c * m, (c + 1) * m)) for c in range(3))
    for state, t, groups in states(m):
        assert state not in unique
        unique.add(state)
        assert is_cover(state, m)
        assert signature(state) == groups
        assert sum(sign(PERMS[p]) == 0 for p in state) == 3 * t
        counted[t] += 1
        if groups == reference:
            fixed[t].append(state)
    S = factorial(3 * m) // (factorial(m) ** 3)
    assert counted == {t: S * comb(m, t)**3 for t in range(m + 1)}
    if m <= 2:
        brute = set(st for st in product(range(6), repeat=3 * m) if is_cover(st, m))
        assert brute == unique
    fiber = set(sum((v for v in fixed.values()), []))
    component_sizes = []
    while fiber:
        seed = fiber.pop()
        queue = [seed]
        size = 1
        while queue:
            st = queue.pop()
            for i,j in combinations(range(3 * m),2):
                if st[i]==st[j] or PERMS[st[i]][0] != PERMS[st[j]][0]:
                    continue
                nxt = list(st)
                nxt[i],nxt[j]=nxt[j],nxt[i]
                nxt=tuple(nxt)
                if nxt in fiber:
                    fiber.remove(nxt)
                    queue.append(nxt)
                    size+=1
        component_sizes.append(size)
    assert sorted(component_sizes) == sorted(comb(m, t)**3 for t in range(m+1))
    return S,len(unique),sorted(component_sizes)

def test_local_m1():
    assert check(1)==(6,12,[1,1])

def test_local_m2():
    assert check(2)==(90,900,[1,1,8])

def test_local_m3():
    assert check(3)==(1680,94080,[1,1,27,27])

if __name__=="__main__":
    for m in (1,2,3):
        print("m",m,"(signatures, states, fiber components)",check(m))
    print("ALL PASS")
