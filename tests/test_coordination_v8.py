"""Smoke tests for v8 proof certificates (also run the standalone exhaustives)."""
from pathlib import Path
import sys
V8=Path(__file__).resolve().parents[1]/'certificate_coordination'/'v8'
sys.path.insert(0,str(V8))
from hypergraph_realization import construct,verify,hypergraph_from_graph_edges,min_transversal,monotone_path
from complete_bipartite_realization import construct_complete,verify as verify_complete,repair_path,exact_width
from obstruction_width_dp import solve
from all_multiplicity_plateaux import certify


def test_universality_k2_complete():
    h,H=hypergraph_from_graph_edges(5,[(0,1),(1,2),(2,3),(3,4),(0,4)],2)
    data=construct_complete(h,H,2)
    assert verify_complete(data)['initial_Q']==50
    w,I,tw=exact_width(data)
    assert w==3 and tw==2
    assert repair_path(data,min_transversal(h,H))[-1]==0


def test_k3_complete():
    h,H=hypergraph_from_graph_edges(3,[(0,1),(1,2),(0,2)],3)
    data=construct_complete(h,H,3)
    assert verify_complete(data)['initial_Q']==18
    w,I,tw=exact_width(data)
    assert w==2


def test_arbitrary_connectivity_variant():
    h,H=hypergraph_from_graph_edges(4,[(0,1),(1,2),(2,3)],2)
    data=construct(h,H,2,c=4)
    assert verify(data,exact_connectivity=False)['initial_Q']==2*data['d']*3
    assert monotone_path(data,min_transversal(h,H))[-1]==0


def test_all_multiplicity_plateau_duals():
    for k in [1,2,3,5]:
        result=certify(8,k)
        assert result['Q_initial']==4 and result['Q_final']==0
