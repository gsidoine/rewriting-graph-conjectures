"""Independent tests of the resistance--FR kernel construction."""
from pathlib import Path
import itertools
import json

import networkx as nx

from applications.berge_fulkerson.plateau.resistance_kernel_lift import (
    dangling_colouring, petersen, realize,
)
from applications.berge_fulkerson.plateau.fr_extension_core import residual_kernel, three_edge_colorable

BASE = Path(__file__).resolve().parents[1] / 'applications' / 'berge_fulkerson' / 'plateau'


def check_cert(name):
    c=json.loads((BASE / 'resistance_certificates' / f'{name}.json').read_text())
    n=c['kernel_n']; E=list(map(tuple,c['kernel_edges']))
    removed=c['removed_edge_indices']; col=(
        {int(i):color for i,color in c['partial_colouring'].items()},
        {tuple(map(int,s.split(':'))): color for s,color in c['port_colouring'].items()})
    N,G,Ms,_=realize(n,E,removed,col)
    assert N==c['host_n'] and G==list(map(tuple,c['host_edges']))
    assert Ms==[list(map(tuple,M)) for M in c['FR_matchings']]
    H=nx.Graph(); H.add_edges_from(G)
    assert nx.edge_connectivity(H)==3
    if len(removed)==2:
        assert three_edge_colorable(N,G)
    counts={e:sum(e in M for M in Ms) for e in G}
    assert all(v in (0,1,2) for v in counts.values())
    R=nx.MultiGraph()
    R.add_nodes_from(range(N))
    for e,v in counts.items():
        for _ in range(2-v):R.add_edge(*e)
    assert nx.edge_connectivity(R)>=2
    assert sum(v==0 for v in counts.values())==len(removed)
    k=residual_kernel(N,G,[2-counts[e] for e in G])
    assert k['vertices']==list(range(n))
    assert sorted(map(tuple,k['edges']))==E
    assert all(len(M)==N//2 for M in Ms)
    return n,E,removed,col


def test_petersen_universality():
    n,E,removed,col=check_cert('petersen')
    assert n==10 and len(removed)==2
    assert not three_edge_colorable(n,E)
    # Independent resistance minimality: no one-edge deletion can be coloured.
    for e in range(len(E)):
        assert dangling_colouring(n,E,(e,)) is None
    assert dangling_colouring(n,E,removed) is not None


def test_j5_universality():
    n,E,removed,col=check_cert('flower_j5')
    assert n==20 and len(removed)==2
    assert not three_edge_colorable(n,E)
    for e in range(len(E)):
        assert dangling_colouring(n,E,(e,)) is None


def test_every_petersen_two_edge_port_realization():
    n,E=petersen()
    valid=0;noniso=[]
    for pair in itertools.combinations(range(len(E)),2):
        col=dangling_colouring(n,E,pair)
        if col is None:continue
        N,G,Ms,_=realize(n,E,pair,col)
        H=nx.Graph();H.add_edges_from(G)
        assert nx.edge_connectivity(H)==3
        f={e:sum(e in M for M in Ms) for e in G}
        k=residual_kernel(N,G,[2-f[e] for e in G])
        assert k['vertices']==list(range(n))
        assert sorted(map(tuple,k['edges']))==E
        valid+=1
        if not any(nx.is_isomorphic(H,X) for X in noniso):noniso.append(H)
    assert valid==75
    assert len(noniso)==3


def test_parity_and_partner_distinct():
    for name in ('petersen','flower_j5'):
        n,E,removed,(cols,stubs)=check_cert(name)
        for i in removed:
            u,v=E[i]
            assert stubs[i,u]!=stubs[i,v]
        for color in range(3):
            assert sum(c==color for c in stubs.values())%2==0


def test_zero_resistance_base_case():
    K=nx.complete_graph(4)
    E=sorted(tuple(sorted(e)) for e in K.edges())
    c=dangling_colouring(4,E,[])
    assert c is not None
    n,G,Ms,_=realize(4,E,[],c)
    assert n==4 and G==E
    assert sorted(e for M in Ms for e in M)==E
    assert sorted(map(tuple,residual_kernel(4,G,[1]*len(G))['edges']))==E


def test_bridgeless_two_edge_connected_kernel():
    """The construction applies to bridgeless kernels with a real 2-edge cut."""
    n,E=petersen()
    E=set(E)
    E.remove((0,1))
    E.update(tuple(sorted((a+10,b+10))) for a,b in nx.complete_graph(4).edges()
             if (a,b)!=(0,1))
    E.update({(0,10),(1,11)})
    E=sorted(E)
    K=nx.Graph();K.add_edges_from(E)
    assert nx.edge_connectivity(K)==2
    solution=next(((pair,dangling_colouring(14,E,pair))
                   for pair in itertools.combinations(range(len(E)),2)
                   if dangling_colouring(14,E,pair) is not None))
    pair,col=solution
    assert dangling_colouring(14,E,[]) is None
    assert all(dangling_colouring(14,E,(i,)) is None for i in range(len(E)))
    N,G,Ms,_=realize(14,E,pair,col)
    H=nx.Graph();H.add_edges_from(G)
    assert nx.edge_connectivity(H)==2
    counts={e:sum(e in M for M in Ms) for e in G}
    residual=nx.MultiGraph();residual.add_nodes_from(range(N))
    for e in G:
        for _ in range(2-counts[e]):residual.add_edge(*e)
    assert nx.edge_connectivity(residual)==2
    core=residual_kernel(N,G,[2-counts[e] for e in G])
    assert sorted(core['edges'])==E
    assert core['vertices']==list(range(14))
