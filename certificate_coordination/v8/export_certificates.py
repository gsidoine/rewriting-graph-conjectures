import json
from pathlib import Path
from hypergraph_realization import hypergraph_from_graph_edges,min_transversal
from complete_bipartite_realization import construct_complete,verify
from all_multiplicity_plateaux import construct as plateau_construct, F_ROW,F_COL
from high_connectivity_traps import ROW_DUAL,COL_DUAL

P=Path(__file__).resolve().parent/'certificates';P.mkdir(exist_ok=True)

h,E=hypergraph_from_graph_edges(5,[(0,1),(1,2),(2,3),(3,4),(0,4)],2)
D=construct_complete(h,E,2);verify(D)
(P/'complete_K25_25_k2_cycle5.json').write_text(json.dumps({
    'name':'complete_K25_25_k2_cycle5','k':2,'h':h,'hyperedges':D['hyperedges'],
    'd':D['d'],'D':D['D'],'permutations':[list(p) for p in D['permutations']],
    'minimum_transversal':list(min_transversal(h,E))},indent=1))

A,base,F=plateau_construct(8,2)
d=8;k=2
alpha=[];beta=[]
for z in range(len(A)):
    j=z%d
    if z<d:
        aa=list(ROW_DUAL[j])+[0]*(d-4) if j<4 else [0]*d
        bb=list(COL_DUAL[j])+[-1]*(d-4) if j<4 else [-1]*d
    else:
        aa=list(F_ROW[j])+[0]*(d-4) if j<4 else [0]*d
        bb=list(F_COL[j])+[-1]*(d-4) if j<4 else [-1]*d
    alpha.append(aa);beta.append(bb)
(P/'plateau_K8_8_k2.json').write_text(json.dumps({
    'name':'plateau_K8_8_k2','k':k,'d':d,
    'permutations':[list(p) for p in A], 'dual_alpha':alpha,'dual_beta':beta,
    'neutral_edit':{'coordinate':3,'corner':[2,0,1,3]},
    'strict_edit':{'coordinate':0,'corner':[3,1,2,0]}},indent=1))
print('EXPORTED',*(str(p) for p in P.iterdir()),sep='\n')
