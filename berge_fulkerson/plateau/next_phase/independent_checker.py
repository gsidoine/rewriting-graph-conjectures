"""Pure-standard-library independent finite witness checks.

Do not infer a proof of universal normalization from these tests.
"""
from itertools import combinations, combinations_with_replacement, permutations


def kappa_from_membership(states, edges):
    k = len(states)
    m = [sum(int(e in s) for s in states) for e in edges]
    for size in range(k + 1):
        for I in combinations(range(k), size):
            if all(sum(e in states[i] for i in I) >= max(0, me - 2)
                   for e, me in zip(edges, m)):
                return size
    raise AssertionError('no exact-repair mask')


def k33_q36():
    left = range(3)
    right = range(3, 6)
    edges = [(u,v) for u in left for v in right]
    # The two perfect matchings using edge (0,3) are complementary
    # within K_2,2 on the remaining four vertices.
    A = {(0,3),(1,4),(2,5)}
    B = {(0,3),(1,5),(2,4)}
    state = [A]*3 + [B]*3
    for M in state:
        assert len(M)==3 and {z for e in M for z in e} == set(range(6))
    count = {e:sum(e in M for M in state) for e in edges}
    q = sum((x-2)**2 for x in count.values())
    kap = kappa_from_membership(state,edges)
    assert q==36 and kap==4
    assert sorted(count.values())==[0]*4+[3]*4+[6]
    return q,kap


def minimal_pair_blocker():
    triples = list(combinations(range(6), 3))
    pairs = list(combinations(range(6), 2))
    cover = []
    for t in triples:
        complement = set(range(6)) - set(t)
        mask = sum(1<<i for i,p in enumerate(pairs) if set(p)<=complement)
        cover.append(mask)
    good = []
    for F in combinations(range(20), 6):
        mask=0
        for i in F: mask|=cover[i]
        if mask == (1<<15)-1:good.append(F)
    assert len(good)==30
    orbit=set()
    exemplar=good[0]
    for perm in permutations(range(6)):
        f=tuple(sorted(triples.index(tuple(sorted(perm[v] for v in triples[i]))) for i in exemplar))
        orbit.add(f)
    assert len(orbit)==30 and orbit==set(good)
    return len(good),len(orbit)


if __name__=='__main__':
    print('K3,3: Q, kappa =', k33_q36())
    print('Six-triple pair-blockers: labeled, orbit =',minimal_pair_blocker())
    print('PASS')
