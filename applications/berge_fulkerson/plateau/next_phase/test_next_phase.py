from itertools import combinations
from .independent_checker import k33_q36, minimal_pair_blocker
from .q34_standalone_checker import check


def test_q34_exact_cert():
    assert check()


def test_q36_k33():
    assert k33_q36() == (36,4)


def test_minimal_blocker_classification():
    assert minimal_pair_blocker() == (30,30)


def test_five_triples_cannot_block_every_pair():
    triples=list(combinations(range(6),3))
    pairs=list(combinations(range(6),2))
    for fam in combinations(triples,5):
        assert any(all(set(p)&set(t) for t in fam) for p in pairs)
