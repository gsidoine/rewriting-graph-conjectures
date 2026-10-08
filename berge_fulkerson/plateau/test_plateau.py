"""Fresh regression tests for the coordinated matching-rewrite results."""
import random
from .sharp_trap import validate_base,validate_family,load,graph,Q,pm_masks,expand_balanced_vertex
from .dual_certificate import verify_duals,DUAL
from .standalone_checker import verify
from .bounded_coordinate_descent import coordinated_step,normalize
from .aggregate_descent import validate as validate_aggregate
from .cover_lifting import validate as validate_cover
import json


def test_small_certificate_and_duals():
    assert verify()['result']=='PASS'
    assert verify_duals(json.loads(DUAL.read_text())['dual_potentials'])
    validate_base()


def test_vertex_expansion_family():
    vals=validate_family(3)
    assert [v['vertices'] for v in vals]==[18,22,26,30]
    assert all(v['min_one_replacement_change']==0 for v in vals)


def test_bounded_coordinate_descent_on_generated_states():
    edges,path=load()
    r=random.Random(39071)
    options=pm_masks(edges)
    for _ in range(80):
        start=r.choices(options,k=6)
        target,trace,mods=normalize(edges,start,keep_trace=True)
        assert trace[-1]==0
        assert len(trace)-1<=3*len(graph(edges))
        assert all(a>b for a,b in zip(trace,trace[1:]))
        assert all(len(x)<=4 for x in mods)
        for i,q in enumerate(trace[:-1]):
            if q<=10:assert len(mods[i])<=2
            if q<=38:assert len(mods[i])<=3


def test_sharp_Q6_two_coordinates():
    edges,path=load()
    solution,indices=coordinated_step(edges,path[0])
    assert len(indices)==2 and Q(edges,solution)==0
    assert Q(edges,path[0])==6


def test_double_cover_and_aggregate():
    assert validate_cover()['girth']>=6
    assert validate_aggregate()['Q_trace']==[6,0]

def test_three_cut_toy_algebra():
    from .three_cut_profile import test_gluing_formula
    assert test_gluing_formula()['three_cut_signatures']==84

def test_general_q6_pair_criterion():
    from .general_q6_pair import validate
    r=validate()
    assert r['Q_initial']==6 and len(r['valid_completion_pairs'])>=1


def test_two_coordinate_flow_equals_exhaustive():
    from .flow_optimize_two import validate
    r=validate()
    assert r['random_cases']==12

def test_transversal_boundary():
    from .transversal_boundary import verify
    out=verify()
    assert out['five_triple_families_checked']==15504
    assert out['first_possible_defect_level_from_this_hitting_method']==12
