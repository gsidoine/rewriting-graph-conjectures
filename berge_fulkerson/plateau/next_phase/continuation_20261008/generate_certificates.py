"""Generate explicitly checkable finite witnesses for first four 3-edge sums."""
import json
from pathlib import Path
from .glue_traps import construct

def create(k,out):
    R=construct(k)
    E=R['edges'];ids={e:i for i,e in enumerate(E)}
    states=[[hex(sum(1<<ids[e] for e in pm)) for pm in s] for s in R['trace']]
    obj={'statement':'k-copy 3-edge-sum of the 18-vertex stiff Q6 gadget',
         'k':k,'n':R['graph'].number_of_nodes(),'edges':E,'Q_trace':R['defects'],
         'six_matching_masks_per_stage':states,'original_copy_colour_maps':R['group_maps']}
    Path(out).write_text(json.dumps(obj,indent=2)+'\n')
    return obj

if __name__=='__main__':
    here=Path(__file__).resolve().parent
    for k in range(1,5):
        obj=create(k,here/f'three_sum_k{k}.json')
        print('created k',k,'n',obj['n'],'stages',len(obj['Q_trace']))
