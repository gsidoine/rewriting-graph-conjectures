"""Three-edge-sums of sharp Q=6 one-matching traps.

For k copies, produces a simple 3-edge-connected cubic bipartite graph on 16*k+2
vertices, an initial sextuple with defect 6*k, and an explicit 2k-move path.
Every even-index path state has no strict one-coordinate improvement.

Input is an archived exact 18-vertex graph; this script uses only its edge-list
and matching masks and checks all compatibility assertions afresh.
"""
from itertools import permutations
import json
from pathlib import Path
import networkx as nx

BASE=str(Path(__file__).resolve().parents[2]/'sharp_18_vertex.json')
D=json.load(open(BASE))
BASE_E=[tuple(sorted(e)) for e in D['edges']]
BASE_STAGES=[D[k] for k in ('matching_masks_initial','matching_masks_neutral','matching_masks_target')]
PORT_A=0
PORT_B=16


def memberships(edges, masks):
    return {e:frozenset(i for i,m in enumerate(masks) if m>>j&1) for j,e in enumerate(edges)}

def port_groups(local_port, colour_map):
    # colour_map[global index] = original local index
    result={}
    for e in BASE_E:
        if local_port not in e:continue
        other=next(v for v in e if v!=local_port)
        j=BASE_E.index(e)
        colours=frozenset(gi for gi in range(6) if BASE_STAGES[0][colour_map[gi]]>>j&1)
        result[other]=colours
    assert len(result)==3 and all(len(s)==2 for s in result.values())
    assert set.union(*(set(v) for v in result.values()))==set(range(6))
    return result

def choice_map(groups_A, port_B=PORT_A):
    # For arbitrary enumerated neighbors, match the corresponding groups of two
    # colors by global relabelling of the new component.
    gA=[groups_A[x] for x in sorted(groups_A)]
    gB=port_groups(port_B, tuple(range(6)))
    gBseq=[gB[x] for x in sorted(gB)]
    transform=[None]*6
    for source_colours,target_colours in zip(gBseq,gA):
        for global_i, original_i in zip(sorted(target_colours),sorted(source_colours)):
            transform[global_i]=original_i
    assert sorted(transform)==list(range(6))
    return tuple(transform)

def construct(k):
    assert k>=1
    group_maps=[tuple(range(6))]
    bridges=[]
    for j in range(1,k):
        A=port_groups(PORT_B,group_maps[j-1])
        next_map=choice_map(A)
        B=port_groups(PORT_A,next_map)
        assert [A[x] for x in sorted(A)]==[B[x] for x in sorted(B)]
        group_maps.append(next_map)
        for x,y in zip(sorted(A),sorted(B)):
            bridges.append(tuple(sorted((18*(j-1)+x,18*j+y))))
    removed={18*j+v for j in range(k) for v in (([PORT_A] if j>0 else [])+([PORT_B] if j<k-1 else []))}
    assert len(removed)==2*(k-1)
    edges=[tuple(sorted((18*j+u,18*j+v))) for j in range(k) for u,v in BASE_E if 18*j+u not in removed and 18*j+v not in removed]
    edges+=bridges
    edges=sorted(edges)
    g=nx.Graph();g.add_edges_from(edges)
    assert g.number_of_nodes()==16*k+2
    assert g.number_of_edges()==3*(16*k+2)//2
    assert nx.is_bipartite(g) and nx.is_connected(g)
    assert all(d==3 for _,d in g.degree())
    # For all stages, matchings must be assembled by removing port edges and
    # inserting the unique linking bridge used by that colour.
    orig_pms=[]
    for j in range(k):
        rows=[]
        for phase in range(3):
            ms=[]
            for global_i in range(6):
                mask=BASE_STAGES[phase][group_maps[j][global_i]]
                m={tuple(sorted((18*j+u,18*j+v))) for z,(u,v) in enumerate(BASE_E) if mask>>z&1}
                m={e for e in m if e[0] not in removed and e[1] not in removed}
                ms.append(m)
            rows.append(ms)
        orig_pms.append(rows)
    stage_vectors=[]
    for j in range(k):
        if j==0:stage_vectors.append(tuple([0]*k))
        v=list(stage_vectors[-1]);v[j]=1;stage_vectors.append(tuple(v))
        v=list(stage_vectors[-1]);v[j]=2;stage_vectors.append(tuple(v))
    trace=[]
    for vec in stage_vectors:
        pm=[]
        for global_i in range(6):
            s=set(bridges)
            # Include a bridging edge only for two color labels assigned to it
            # at both ends. This is independent of the local phase.
            used_bridges=set()
            for j in range(1,k):
                A=port_groups(PORT_B,group_maps[j-1])
                for x,y in zip(sorted(A),sorted(port_groups(PORT_A,group_maps[j]))):
                    if global_i in A[x]:used_bridges.add(tuple(sorted((18*(j-1)+x,18*j+y))))
            s=used_bridges
            for j in range(k):s |= orig_pms[j][vec[j]][global_i]
            assert all(e in edges for e in s)
            assert len(s)==g.number_of_nodes()//2
            assert len(set(x for edge in s for x in edge))==g.number_of_nodes()
            pm.append(s)
        trace.append(pm)
    def q(st):
        counts={e:sum(e in match for match in st) for e in edges}
        return sum((v-2)**2 for v in counts.values())
    vals=[q(state) for state in trace]
    assert vals==[6*k - 6*(a//2) for a in range(len(trace))],vals
    for before,after in zip(trace,trace[1:]):
        assert sum(before[i]!=after[i] for i in range(6))==1
    assert all(q(trace[t])==q(trace[t+1]) for t in range(0,2*k,2))
    return {'k':k,'edges':edges,'trace':trace,'defects':vals,'graph':g,'removed_vertices':sorted(removed),'group_maps':group_maps}

def verify_one_coordinate_trap(R, phases=None):
    # Independent minimum-cost bipartite perfect matching oracle. An improving
    # single-coordinate move iff some global weight optimum beats current.
    G=R['graph'];E=R['edges'];trace=R['trace']
    color=nx.bipartite.color(G)
    L=[v for v in G if color[v]==0]
    phases=list(range(0,len(trace),2)) if phases is None else phases
    for t in phases:
        st=trace[t]
        for i in range(6):
            base={e:sum(e in st[j] for j in range(6) if j!=i) for e in E}
            Gweight=G.copy()
            for u,v in E:Gweight[u][v]['weight']=2*base[(u,v)]-3
            M=nx.algorithms.bipartite.minimum_weight_full_matching(Gweight,top_nodes=L,weight='weight')
            best=sum(2*base[e]-3 for e in E if e in {tuple(sorted((u,M[u]))) for u in L})
            existing=sum(2*base[e]-3 for e in st[i])
            assert best==existing,(R['k'],t,i,best,existing)
    return len(phases)*6

if __name__=='__main__':
    import sys,time
    ks=list(map(int,sys.argv[1:])) or [1,2,3,4]
    for k in ks:
        t=__import__('time').time();R=construct(k)
        mincut=nx.edge_connectivity(R['graph'])
        assert mincut==3,(k,mincut)
        oracle_calls=verify_one_coordinate_trap(R)
        print('PASS k=',k,'n=',R['graph'].number_of_nodes(),'m=',len(R['edges']),
              'edge_connectivity=',mincut,'Q_trace=',R['defects'],
              'oracle_checks=',oracle_calls,'sec=',round(__import__('time').time()-t,2),flush=True)
