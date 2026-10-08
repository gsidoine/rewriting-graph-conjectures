"""Exact 84-state boundary-response algebra for 3-edge sums of cubic shores.

A matching crosses a 3-cut at either one edge (codes 0,1,2), or all
three edges (code 3). The multiset of six codes has C(6+4-1,3)=84
possibilities. This is a standard finite-interface reduction, *not* a
claim to have solved Berge-Fulkerson on 3-connected graphs.
"""
from itertools import combinations_with_replacement
from .sharp_trap import pm_masks, Q


def signatures():
    return list(combinations_with_replacement(range(4),6))


def cut_defect(signature):
    # The all-3 signature appears on every one of the three cut edges.
    return sum((sum(code==j or code==3 for code in signature)-2)**2
               for j in range(3))


def triangle_shore_defect(signature):
    # For triangle ports 0,1,2: crossing just port j uses interior
    # edge joining the other two terminals. Crossing all three uses none.
    return sum((signature.count(j)-2)**2 for j in range(3))


def triangular_prism_edges():
    return [(0,1),(1,2),(0,2), (3,4),(4,5),(3,5),
            (0,3),(1,4),(2,5)]


def test_gluing_formula():
    edges=triangular_prism_edges()
    masks=pm_masks(edges)
    assert len(masks)==4
    edgeids={frozenset(e):i for i,e in enumerate(edges)}
    # Determine cut signature of each exact perfect matching.
    codes={}
    for m in masks:
        touched=[j for j,(u,v) in enumerate(edges[6:]) if (m>>(6+j))&1]
        assert len(touched) in (1,3)
        codes[m]=(touched[0] if len(touched)==1 else 3)
    assert set(codes.values())=={0,1,2,3}
    computed={}
    for six in combinations_with_replacement(masks,6):
        profile=tuple(sorted(codes[x] for x in six))
        expected=(2*triangle_shore_defect(profile)+cut_defect(profile))
        measured=Q(edges,six)
        assert measured==expected,(profile,measured,expected)
        computed[profile]=measured
    assert len(computed)==84
    assert min(computed.values())==0
    return dict(graph='triangular prism',three_cut_signatures=84,
                exact_six_matching_states=84,gluing_identity_verified=True)

if __name__=='__main__':
    print(test_gluing_formula())
