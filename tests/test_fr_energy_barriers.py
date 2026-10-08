"""Exact 10/24-vertex barriers and structural expansion tests."""
from itertools import product
from collections import Counter
import json
from pathlib import Path

from applications.berge_fulkerson.plateau.energy_barriers.standalone_audit import study
from applications.berge_fulkerson.plateau.energy_barriers.balanced_lift import lift_fr, expand

BASE = Path(__file__).resolve().parents[1]/'applications/berge_fulkerson/plateau/energy_barriers'


def test_ten_vertex_exact_barrier():
    d=study('ten_vertex_witness.json')
    assert d['state_count']==23
    assert d['bad']==[1]


def test_flower_host_exact_barrier():
    d=study('flower_host24_witness.json')
    assert d['state_count']==13508
    assert d['bad']==[36]


def test_local_k32_defect_bound_and_attainment():
    """All distinct/nontriple port choices, all local matching phases."""
    for ports in product(range(3),repeat=3):
        if len(set(ports))==1: continue
        optimal=0 if len(set(ports))==3 else 1
        possibilities=[]
        for phases in product((0,1),repeat=3):
            inc=[]
            for port,phase in zip(ports,phases):
                other=[i for i in range(3) if i!=port]
                inc.append([(other[phase],0),(other[1-phase],1)])
            counter=Counter(q for matching in inc for q in matching)
            missing=6-len(counter)
            if max(counter.values())<=2:
                assert missing>=optimal
                possibilities.append(missing)
        assert possibilities and min(possibilities)==optimal
        # Lifting any 1-coordinate base move from any valid local state:
        for frozen_port0,frozen_port1 in product(range(3),repeat=2):
            for f0,f1 in product((0,1),repeat=2):
                def local(port,phase):
                    p=[i for i in range(3) if i!=port]
                    return {(p[phase],0),(p[1-phase],1)}
                common=local(frozen_port0,f0)&local(frozen_port1,f1)
                for new_port in range(3):
                    if frozen_port0==frozen_port1==new_port:continue
                    assert any(not (common&local(new_port,phase)) for phase in (0,1))


def test_250_vertex_iterated_lift():
    x=json.loads((BASE/'ten_vertex_witness.json').read_text())
    n,E,M=x['n'],x['edges'],x['FR_matchings_example']
    for t in (1,2):
        n,E,M=lift_fr(n,E,M)
        assert n==10*5**t
        cov=Counter(tuple(e) for m in M for e in m)
        assert sum(cov[tuple(e)]==0 for e in E)==3*3**t
        assert all(cov[tuple(e)]<=2 for e in E)
    assert len(E)==375
