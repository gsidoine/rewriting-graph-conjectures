"""Research regression tests: local FR matching fibres and transfer polynomial."""
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'applications'/'berge_fulkerson'/'plateau'/'energy_barriers'/'fibre_transfer.py'
spec=importlib.util.spec_from_file_location('fr_fibre_transfer',SRC)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_exact_local_fibre_and_lift():
    results,n=mod.verify_local()
    assert n==1296
    assert results['distinct']=={0:2,2:6}
    assert results['repeated']=={1:4,2:2}


def test_k4_full_defect_distribution():
    edges=[(i,j) for i in range(4) for j in range(i+1,4)]
    result=mod.verify_global(4,edges)
    assert result['ordered_fr']==47904
    assert result['expanded_distribution'][0]==96


def test_k33_full_defect_distribution():
    edges=[(i,j) for i in range(3) for j in range(3,6)]
    result=mod.verify_global(6,edges)
    assert result['ordered_fr']==13783296
    assert result['expanded_distribution'][0]==768
