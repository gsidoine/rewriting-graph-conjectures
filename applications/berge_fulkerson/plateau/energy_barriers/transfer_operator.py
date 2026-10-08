"""Exact K_{3,2} three-pole operator for ordered Fan--Raspaud triples.

A research verification module; no external dependencies.
States are ordered triples of perfect matchings.  The coefficient of z^u
counts FR triples leaving u graph edges uncovered.  The local phase model
is proved in the accompanying manuscript, not assumed by the tests.
"""
from __future__ import annotations
from collections import Counter, deque
from itertools import product
from math import comb


def internal_edges(port: int, bit: int) -> frozenset[tuple[int, int]]:
    assert port in (0, 1, 2) and bit in (0, 1)
    other = [x for x in range(3) if x != port]
    return frozenset(((other[bit], 0), (other[1 - bit], 1)))


def local_states(ports: tuple[int, int, int]) -> list[tuple[tuple[int, int, int], int]]:
    """(phase triple, uncovered internal edges) for a projected FR local pattern."""
    assert len(ports) == 3 and len(set(ports)) >= 2
    result = []
    for bits in product((0, 1), repeat=3):
        chosen = [internal_edges(p, b) for p, b in zip(ports, bits)]
        if chosen[0] & chosen[1] & chosen[2]:
            continue
        uncovered_internal = 6 - len(set().union(*chosen))
        result.append((bits, uncovered_internal))
    return result


def local_components(ports: tuple[int, int, int]) -> tuple[int, int, int]:
    """Number of local states, connected components, and graph diameter."""
    vertices = [bits for bits, _ in local_states(ports)]
    unseen = set(vertices)
    components = 0
    diameter = 0
    for s in vertices:
        distance = {s: 0}
        frontier = deque([s])
        while frontier:
            a = frontier.popleft()
            for b in vertices:
                if b not in distance and sum(x != y for x, y in zip(a, b)) == 1:
                    distance[b] = distance[a] + 1
                    frontier.append(b)
        assert len(distance) == len(vertices)
        diameter = max(diameter, max(distance.values()))
    while unseen:
        components += 1
        frontier = [unseen.pop()]
        while frontier:
            a = frontier.pop()
            nbrs = [b for b in unseen if sum(x != y for x, y in zip(a, b)) == 1]
            for b in nbrs:
                unseen.remove(b)
                frontier.append(b)
    return len(vertices), components, diameter


def audited_local_move_lifts() -> tuple[int, int]:
    """Independently enumerate all valid local FR phase states and projected moves.

    A projected move is valid exactly when its three external ports are
    not all the same.  The two unchanged phases must remain fixed.
    """
    valid_count = tested_moves = 0
    for ports in product(range(3), repeat=3):
        if len(set(ports)) < 2:
            continue
        for bits, _ in local_states(ports):
            valid_count += 1
            for coordinate in range(3):
                for target_port in range(3):
                    if target_port == ports[coordinate]:
                        continue
                    updated_ports = list(ports)
                    updated_ports[coordinate] = target_port
                    if len(set(updated_ports)) < 2:
                        continue
                    tested_moves += 1
                    success = False
                    for target_phase in range(2):
                        phases = list(bits)
                        phases[coordinate] = target_phase
                        if tuple(phases) in dict(local_states(tuple(updated_ports))):
                            success = True
                            break
                    assert success, (ports, bits, coordinate, target_port)
    return valid_count, tested_moves


def multiply_polynomials(left: list[int], right: list[int]) -> list[int]:
    out = [0]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b: out[i+j] += a*b
    return out


def poly_power(coefficients: list[int], exponent: int) -> list[int]:
    assert exponent >= 0
    out = [1]
    base = coefficients
    while exponent:
        if exponent % 2:
            out = multiply_polynomials(out, base)
        exponent //= 2
        if exponent:
            base = multiply_polynomials(base, base)
    return out


def three_pole_operator(n: int, base_coefficients: list[int]) -> list[int]:
    """For a cubic n-vertex graph, return the exact polynomial for T(G).

    Base coefficients are indexed by number of uncovered original edges.
    Formula: z^u (2+6z^2)^(n-2u) (4z+2z^2)^(2u).
    """
    assert n > 0 and n % 2 == 0
    out = [0]*(5*n//2+1)
    for u, count in enumerate(base_coefficients):
        if count == 0:
            continue
        assert 2*u <= n, (n, u)
        p = multiply_polynomials(poly_power([2, 0, 6], n-2*u),
                                 poly_power([0, 4, 2], 2*u))
        for j, c in enumerate(p):
            out[j+u] += count*c
    return out


def perfect_matchings(n: int, edges: list[tuple[int,int]]) -> list[int]:
    inc = [[] for _ in range(n)]
    for i, (a,b) in enumerate(edges):
        inc[a].append((b,i));inc[b].append((a,i))
    found = []
    def dfs(remaining: frozenset[int], chosen: int):
        if not remaining:
            found.append(chosen);return
        a = min(remaining)
        for b, e in inc[a]:
            if b in remaining:
                dfs(remaining-{a,b}, chosen | (1<<e))
    dfs(frozenset(range(n)), 0)
    assert len(found) == len(set(found))
    return found


def direct_FR_polynomial(n: int, edges: list[tuple[int,int]]) -> list[int]:
    """Independent brute-force reference, only for small instances."""
    pm=perfect_matchings(n,edges)
    all_edges=(1<<len(edges))-1
    out=[0]*(n//2+1)
    for a,b,c in product(pm,repeat=3):
        if a&b&c:continue
        uncovered = (all_edges & ~(a|b|c)).bit_count()
        out[uncovered] += 1
    return out


def expanded_graph(n: int, edges: list[tuple[int,int]]) -> tuple[int,list[tuple[int,int]]]:
    """Independent implementation of balanced K3,2 replacement."""
    incident=[[] for _ in range(n)]
    for i,(a,b) in enumerate(edges):
        incident[a].append(i);incident[b].append(i)
    assert all(len(x)==3 for x in incident)
    incident=[sorted(x) for x in incident]
    p={(v,e):5*v+j for v in range(n) for j,e in enumerate(incident[v])}
    E=[tuple(sorted((p[a,i],p[b,i]))) for i,(a,b) in enumerate(edges)]
    E.extend(tuple(sorted((5*v+j,5*v+3+k))) for v in range(n)
             for j in range(3) for k in range(2))
    return 5*n,sorted(E)


def projected_fibre_size(n: int, u: int) -> int:
    assert 0 <= 2*u <= n
    return 8**(n-2*u)*6**(2*u)


def R(z: float) -> float:
    return z**3*((z+2)/(1+3*z*z))**2


def universal_pressure(z: float, iterations: int=100) -> tuple[float,float]:
    """Limiting (log FR count)/vertex and z*d/dz pressure at z.

    Returns numerical research values, not certified rounding intervals.
    """
    from math import log
    assert z>0
    x=z;dx=1.;p=0.;dp=0.
    for j in range(iterations):
        a=2+6*x*x
        weight=5.**(-j-1)
        p+=weight*log(a)
        dp+=weight*(12*x/a)*dx
        if x <= 1e-100:
            # R iterations converge to zero, but the pressure tail remains
            # constant: sum_{i=j+1}^inf 5^(-i-1) * log 2.
            dp=dp
            p+= log(2)/(4*5**(j+1))
            break
        xn=R(x)
        dx=xn*(3/x+2/(2+x)-12*x/(1+3*x*x))*dx
        x=xn
    return p,z*dp


if __name__ == '__main__':
    print('local signatures:')
    for x in ((0,1,2),(0,0,1)):
        print(x,Counter(v for _,v in local_states(x)),local_components(x))
    print('local valid states and movable port changes:',audited_local_move_lifts())
    K4=list(__import__('itertools').combinations(range(4),2))
    n,E=expanded_graph(4,K4)
    predicted=three_pole_operator(4,direct_FR_polynomial(4,K4))
    brute=direct_FR_polynomial(n,E)
    print('K4 signature full polynomial equal:',predicted==brute,'total',sum(brute))
    assert predicted==brute
    print('universal pressure and density:',universal_pressure(1.))
