"""Small exact regression tests for sharp unit-defect direct-repair width."""
from applications.berge_fulkerson.plateau.q12_standalone_checker import check as check_q12
from applications.berge_fulkerson.plateau.q40_standalone_checker import check as check_q40
from applications.berge_fulkerson.plateau.q12_cycle_blocker import infinite_family


def test_q12_certified_exact_pair_gap():
    x=check_q12()
    assert x['best_two_coordinate_Q']==4
    assert x['certificate_path']==[12,4,0]


def test_q40_certified_sharp_direct_width():
    x=check_q40()
    assert x['minimum_direct_replacement_coordinates']==4
    assert x['certified_improving_pair_Q']==10


def test_q12_infinite_sharp_family_first_extensions():
    rows=infinite_family(2)
    assert [r['vertices'] for r in rows]==[18,22,26]
    assert all(r['Q']==12 and not r['cycle_hitting_pair'] for r in rows)
