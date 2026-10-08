"""Independent standalone exact 3-edge-colouring boundary signatures of cubic shores."""
from collections import Counter
from itertools import combinations
import json,networkx as nx

def canonical(profile):
    label={};a=[]
    for c in profile:
        if c not in label:label[c]=len(label)
        a.append(label[c])
    return tuple(a)

def shore_signatures(n,edges,side,cut_indices):
    side=set(side);boundary=[];owned=[]
    for i in cut_indices:
        u,v=edges[i];assert (u in side)!=(v in side)
        boundary.append((u if u in side else v,))
    for i,(u,v) in enumerate(edges):
        if u in side and v in side: owned.append((u,v))
    S=[*boundary,*owned]
    incident={u:[] for u in side}
    for j,e in enumerate(S):
        for v in e:incident[v].append(j)
    assert all(len(q)==3 for q in incident.values()),(side,incident)
    used={v:0 for v in side};assign=[-1]*len(S)
    out=Counter();example={}
    def rec(idx):
        if idx==len(S):
            p=canonical(assign[:len(boundary)])
            out[p]+=1
            example.setdefault(p,tuple(assign))
            return
        e=S[idx];ban=0
        for v in e:ban|=used[v]
        for c in range(3):
            bit=1<<c
            if ban&bit:continue
            assign[idx]=c
            for v in e:used[v]|=bit
            rec(idx+1)
            for v in e:used[v]^=bit
    rec(0)
    return out,example

def split_data(n,edges,side):
    cut=[i for i,(u,v) in enumerate(edges) if (u in side)!=(v in side)]
    if len(cut)==0:return None
    A,exA=shore_signatures(n,edges,side,cut)
    B,exB=shore_signatures(n,edges,set(range(n))-set(side),cut)
    return {'cut_edges':[edges[i] for i in cut], 'A':{str(p):count for p,count in A.items()},'B':{str(p):count for p,count in B.items()},'intersection':[list(p) for p in A.keys()&B.keys()]}

