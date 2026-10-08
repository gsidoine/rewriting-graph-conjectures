"""Finite hitting-set boundary for low-defect two-coordinate cycle descent.

This is a finite set-system fact, not a graph counterexample: existence of
six surplus-edge membership triples with no hitting pair does not prove
that the corresponding colored defect cycle is realizable by matchings.
"""
from itertools import combinations

TRIPLES=tuple(combinations(range(6),3))
PAIRS=tuple(combinations(range(6),2))


def has_pair_hitting(family):
    return any(all(not set(pair).isdisjoint(t) for t in family) for pair in PAIRS)


def verify():
    count=0
    for ids in combinations(range(20),5):
        assert has_pair_hitting(tuple(TRIPLES[i] for i in ids))
        count+=1
    witness=None
    for ids in combinations(range(20),6):
        if not has_pair_hitting(tuple(TRIPLES[i] for i in ids)):
            witness=[TRIPLES[i] for i in ids]
            break
    assert witness is not None
    return {'five_triple_families_checked':count,'first_six_triple_blocker':witness,
            'first_possible_defect_level_from_this_hitting_method':12}

if __name__=='__main__':
    print(verify())
