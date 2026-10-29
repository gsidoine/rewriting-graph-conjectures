"""Compare S3-voltage holonomy predictions to the full state graph."""
import networkx as nx
from applications.edge_coloring_rigidity import (
    rigid_family, proper_colorings, budget_graph, kempe_graph, components)
from applications.edge_coloring_voltage import (
    voltage_quotient, generated_subgroup, mul, inv, ONE)


def check(G, relation):
    E, states = proper_colorings(G)
    full = relation(G, E, states)
    reps, edges, response = voltage_quotient(states, full)
    actual = sorted(map(len,components(full)))
    predicted = sorted(size for _,_,count,size in response for _ in range(count))
    assert predicted == actual and len(states) == len(reps)*6
    return len(reps),response


def test_rigid_family_holonomy():
    for k in range(5):
        G = rigid_family(k)
        n = len(G)
        assert check(G,lambda g,e,s:budget_graph(s,n-1)) == (1,[(1,1,6,1)])
        assert check(G,lambda g,e,s:budget_graph(s,n)) == (1,[(1,6,1,6)])
        assert check(G,lambda g,e,s:kempe_graph(g,e,s)) == (1,[(1,6,1,6)])


def test_k33_kempe_vs_budget_holonomy():
    G=nx.complete_bipartite_graph(3,3)
    assert check(G,lambda g,e,s:kempe_graph(g,e,s)) == (
        2,[(1,6,1,6),(1,6,1,6)])
    assert check(G,lambda g,e,s:budget_graph(s,6)) == (2,[(2,6,1,12)])


def test_cube_cross_orbit_kempe_holonomy():
    G=nx.cubical_graph()
    assert check(G,lambda g,e,s:kempe_graph(g,e,s)) == (4,[(4,6,1,24)])
    assert check(G,lambda g,e,s:budget_graph(s,3)) == (4,[(1,1,6,1)]*4)
    assert check(G,lambda g,e,s:budget_graph(s,4)) == (4,[(4,6,1,24)])


def test_nonabelian_holonomy_group_operations():
    a,b,c=(1,0,2),(0,2,1),(1,2,0)
    assert len(generated_subgroup([]))==1
    assert len(generated_subgroup([a]))==2
    assert len(generated_subgroup([c]))==3
    assert len(generated_subgroup([a,b]))==6
    assert mul(a,inv(a))==ONE
