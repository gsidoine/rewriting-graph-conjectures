"""Fast regression tests for October 8 follow-on theorems and certificates."""
from pathlib import Path
from berge_fulkerson.plateau.next_phase.continuation_20261008 import (
    verify_stiff_base, glue_traps, check_certificates, verify_drift,
    verify_component_certificate, componentwise_repair,
)

def test_stiffness_all_perfect_matchings():
    out=verify_stiff_base.verify()
    assert out['perfect_matchings']==47
    assert out['minimum_stiff_margin_initial']==0

def test_connected_three_sum():
    for k in (1,2,3):
        result=glue_traps.construct(k)
        assert result['graph'].number_of_nodes()==16*k+2
        assert result['defects'][0]==6*k
        assert result['defects'][-1]==0

def test_independent_glued_witnesses():
    here=Path(check_certificates.__file__).parent
    for k in (1,2,3,4):
        result=check_certificates.check(here/f'three_sum_k{k}.json')
        assert result['vertices']==16*k+2

def test_drift_on_explicit_k33_states():
    import json
    here=Path(verify_drift.__file__).parent
    graph=json.loads((here/'all_bipartite_3.json').read_text())['graphs'][0]
    E,P,F=verify_drift.setup(graph,3)
    from itertools import combinations_with_replacement
    for s in combinations_with_replacement(P,6):
        verify_drift.drift(list(s),len(E),F)

def test_q34_two_coordinate_component_certificate():
    assert verify_component_certificate.verify()

def test_component_repair_is_defect_local():
    n,E,M=componentwise_repair.load()
    old=componentwise_repair.mult(E,M)
    for C in componentwise_repair.defect_components(n,E,M):
        found=componentwise_repair.repair_component(n,E,M,C,width=2)
        assert found is not None
        I,new=found
        assert len(I)==2
        m=componentwise_repair.mult(E,new)
        assert all(m[e]==(2 if e in C else old[e]) for e in range(len(E)))
    fixed,trace=componentwise_repair.full_component_repair(n,E,M,width=2)
    assert componentwise_repair.energy(E,fixed)==0
    assert len(trace)==3
