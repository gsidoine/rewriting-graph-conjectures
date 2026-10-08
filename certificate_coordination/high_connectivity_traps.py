"""Dependency-free high-edge-connectivity Q=4 one-coordinate local-trap certificates.

For every d>=8 constructs d permutations of [d] inducing a six/variable
matchings system on K_{d,d}, with target multiplicity 1, defect 4, and
coordinate-wise local optimality. Local optimality is certified by integer
Hungarian dual witnesses, not assumed from enumeration.
"""
import itertools

CORNER=[(0,1,2,3),(0,2,3,1),(1,3,0,2),(2,3,1,0)]
ROW_DUAL=[(2,0,0,2),(2,0,2,0),(0,2,2,0),(0,2,0,2)]
COL_DUAL=[(-1,-1,-1,-3),(-1,-1,-1,-3),(-3,-1,-1,-1),(-3,-1,-1,-1)]

def perfect_matching_from_edges(n, allowed):
    # Simple augmenting paths, O(n^3); no external graph package required.
    nbrs=[[j for j in range(n) if (i,j) in allowed] for i in range(n)]
    matched=[-1]*n
    def augment(i,seen):
        for j in nbrs[i]:
            if j in seen:continue
            seen.add(j)
            if matched[j]<0 or augment(matched[j],seen):
                matched[j]=i;return True
        return False
    for i in range(n):
        if not augment(i,set()):raise RuntimeError('residual regular graph lacks a perfect matching')
    out=[-1]*n
    for j,i in enumerate(matched):out[i]=j
    assert sorted(out)==list(range(n))
    return tuple(out)

def construct(d):
    assert d>=8
    s=d-4
    M=[tuple(list(CORNER[k])+[4+(i+k)%s for i in range(s)]) for k in range(4)]
    used={(i,p[i]) for p in M for i in range(4,d)}
    allowed={(i,j) for i in range(d) for j in range(d) if not(i<4 and j<4) and (i,j) not in used}
    for _ in range(s):
        p=perfect_matching_from_edges(d,allowed)
        assert all((i,p[i]) in allowed for i in range(d))
        M.append(p)
        allowed.difference_update((i,p[i]) for i in range(d))
    assert len(M)==d and not allowed
    return M

def certify(d,verbose=True):
    M=construct(d)
    counts=[[0]*d for _ in range(d)]
    for p in M:
        assert sorted(p)==list(range(d))
        for i,j in enumerate(p):counts[i][j]+=1
    q=sum((counts[i][j]-1)**2 for i in range(d) for j in range(d))
    assert q==4
    assert all(counts[i][j]==1 for i in range(d) for j in range(d) if not (i<4 and j<4))
    assert [[counts[i][j] for j in range(4)] for i in range(4)]==[[2,1,1,0],[0,1,1,2],[1,1,1,1],[1,1,1,1]]
    for k,p in enumerate(M):
        alpha=list(ROW_DUAL[k])+[0]*(d-4) if k<4 else [0]*d
        beta=list(COL_DUAL[k])+[-1]*(d-4) if k<4 else [-1]*d
        for i in range(d):
            for j in range(d):
                frozen=counts[i][j]-(p[i]==j)
                weight=2*frozen-1
                assert alpha[i]+beta[j]<=weight,(d,k,i,j,alpha[i],beta[j],weight)
            j=p[i]
            assert alpha[i]+beta[j]==2*(counts[i][j]-1)-1
    # Explicit two-step neutral-then-strict escape that changes only the corner.
    def potential(A):
        mult=[[0]*d for _ in range(d)]
        for perm in A:
            for i,j in enumerate(perm):mult[i][j]+=1
        return sum((mult[i][j]-1)**2 for i in range(d) for j in range(d))
    mid=list(M)
    mid[3]=tuple([2,0,1,3]+list(M[3][4:]))
    assert potential(mid)==4
    end=list(mid)
    end[0]=tuple([3,1,2,0]+list(mid[0][4:]))
    assert potential(end)==0
    if verbose:print('PASS Kdd',d,'n',2*d,'connectivity',d,'defect path',[q,4,0],'min_one_coordinate',q,'all_duals_integral',True)
    return M

if __name__=='__main__':
    for d in (8,9,10,12,16,24,32):certify(d)
