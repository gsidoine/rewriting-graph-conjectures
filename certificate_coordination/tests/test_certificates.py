import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from realize_conflict import construct,verify,vertex_cover_brute,width_brute
from check_strict_paths import check
from high_connectivity_traps import certify

def test_host_c5():
 H=[(0,1),(1,2),(2,3),(3,4),(0,4)]
 obj=construct(5,H,4)
 assert verify(obj)['theoretical_lambda_lower_bound']>=4
 assert width_brute(obj)==vertex_cover_brute(5,H)==3
 assert check(5,H,4)['defects']==[120,72,48,0]

def test_high_connectivity_traps():
 for d in (8,9,12):assert len(certify(d,verbose=False))==d
