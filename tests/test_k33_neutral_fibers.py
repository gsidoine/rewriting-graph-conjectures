"""Independent exhaustive K3,3 neutral-fiber audit.
Run: python tests/test_k33_neutral_fibers.py  OR  pytest -q tests/test_k33_neutral_fibers.py
Standard library only; no imported research generator.
"""
from itertools import permutations, product, combinations
from collections import defaultdict, deque

E = [(r,c) for r in range(3) for c in range(3)]
ED = {e:i for i,e in enumerate(E)}
MATCH = [frozenset(ED[r,p[r]] for r in range(3)) for p in permutations(range(3))]

def valid_double(S):
    return all(sum(i in sh for sh in S)==2 for i in range(9))

def signature(S):
    return tuple(frozenset(j for j,sh in enumerate(S) if ED[0,c] in sh) for c in range(3))

def components_of_symmetric_diff(A,B):
    pending=set(A^B)
    result=[]
    while pending:
        e=pending.pop()
        component={e}
        vertices={E[e][0], 3+E[e][1]}
        while True:
            nxt={j for j in pending if E[j][0] in vertices or 3+E[j][1] in vertices}
            if not nxt:break
            component.update(nxt)
            pending.difference_update(nxt)
            vertices.update(v for j in nxt for v in (E[j][0],3+E[j][1]))
        result.append(component)
    return result

def fiber_shapes(states):
    grouped=defaultdict(list)
    for x in states:grouped[signature(x)].append(x)
    shapes=[]
    for group in grouped.values():
        all_states=set(group)
        sizes=[]
        while all_states:
            start=next(iter(all_states))
            visited={start}
            q=deque([start])
            while q:
                x=q.popleft()
                for a,b in combinations(range(len(x)),2):
                    for C in components_of_symmetric_diff(x[a],x[b]):
                        y=list(x)
                        y[a]=frozenset(x[a]^C)
                        y[b]=frozenset(x[b]^C)
                        y=tuple(y)
                        if y in all_states and y not in visited and signature(y)==signature(x):
                            visited.add(y)
                            q.append(y)
            sizes.append(len(visited))
            all_states.difference_update(visited)
        shapes.append(tuple(sorted(sizes)))
    return grouped,shapes

def test_three_sheet_cdc_fibers():
    colors=[]
    for rows in product(list(permutations(range(3))),repeat=3):
        if all({rows[r][c] for r in range(3)}=={0,1,2} for c in range(3)):
            colors.append(rows)
    sheets=[tuple(frozenset(i for i,(r,c) in enumerate(E) if rows[r][c]!=j)
                  for j in range(3)) for rows in colors]
    assert all(valid_double(x) for x in sheets)
    fibers, shapes=fiber_shapes(sheets)
    assert len(sheets)==12 and len(fibers)==6
    assert set(shapes)=={(1,1)}
    assert all(len(F)==2 for F in fibers.values())

def test_six_matching_double_cover_fibers():
    sheets=[tuple(S) for S in product(MATCH,repeat=6) if valid_double(S)]
    fibers,shapes=fiber_shapes(sheets)
    assert len(sheets)==900 and len(fibers)==90
    assert set(shapes)=={(1,1,8)}
    assert all(len(F)==10 for F in fibers.values())

if __name__=="__main__":
    test_three_sheet_cdc_fibers()
    print("PASS: 3-CDC -> 12 states, 6 signatures, isolated pairs")
    test_six_matching_double_cover_fibers()
    print("PASS: 6-PM -> 900 states, 90 signatures, components of sizes 1,1,8")
