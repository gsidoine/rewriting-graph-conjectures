
# --- notebook cell 1 ---
from collections import Counter, defaultdict, deque
from itertools import combinations_with_replacement
import math
import networkx as nx
import pandas as pd
import sympy as sp

print("NetworkX:", nx.__version__)

# --- notebook cell 3 ---
def plane_faces(G):
    planar, embedding = nx.check_planarity(G)
    assert planar
    seen = set()
    faces = []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            faces.append(embedding.traverse_face(u, v, seen))
    return faces, embedding


def dual_with_edge_map(G):
    faces, _ = plane_faces(G)
    edge_faces = defaultdict(list)
    for i, face in enumerate(faces):
        for j, u in enumerate(face):
            v = face[(j + 1) % len(face)]
            edge_faces[tuple(sorted((u, v)))].append(i)

    H = nx.Graph()
    H.add_nodes_from(range(len(faces)))
    dual_to_primal = {}
    for primal_edge, indices in edge_faces.items():
        assert len(indices) == 2
        a, b = indices
        H.add_edge(a, b)
        dual_to_primal[tuple(sorted((a, b)))] = primal_edge
    return H, dual_to_primal


def side_psi(H, vertices):
    vertices = set(vertices)
    if not vertices:
        raise ValueError("Use only nontrivial colourings.")
    F = H.subgraph(vertices)
    c = nx.number_connected_components(F)
    beta = F.number_of_edges() - F.number_of_nodes() + c
    return (c - 1) + beta


def barnette_quantities(G, mask):
    H, dual_to_primal = dual_with_edge_map(G)
    n = H.number_of_nodes()
    A = {v for v in H if (mask >> v) & 1}
    B = set(H) - A
    if not A or not B:
        raise ValueError("Trivial colouring.")

    phi = side_psi(H, A) + side_psi(H, B)
    X = []
    for u, v in H.edges():
        if ((mask >> u) & 1) != ((mask >> v) & 1):
            X.append(dual_to_primal[tuple(sorted((u, v)))])

    F = nx.Graph()
    F.add_nodes_from(G)
    F.add_edges_from(X)
    nonisolated = [v for v, d in F.degree() if d > 0]
    z = G.number_of_nodes() - len(nonisolated)
    t = nx.number_connected_components(F.subgraph(nonisolated)) if nonisolated else 0
    return phi, z, t


# Verify the identity for every nontrivial colouring of the cube dual.
cube = nx.cubical_graph()
H_cube, _ = dual_with_edge_map(cube)
for mask in range(1, (1 << H_cube.number_of_nodes()) - 1):
    phi, z, t = barnette_quantities(cube, mask)
    assert phi == z + 2 * (t - 1)

print(
    "Exact Barnette identity verified on all",
    (1 << H_cube.number_of_nodes()) - 2,
    "nontrivial cube-dual colourings."
)

# --- notebook cell 5 ---
barnette36_graph6 = (
    "c?_OG?@?gG`@_?O?_G??DO??_??_?C??S??G??@H???_O?DO????O??_?"
    "C?G?A?D?@????_??G??_?GO???S??C?????_?G_????c????D"
)
G36 = nx.from_graph6_bytes(barnette36_graph6.encode())
H36, _ = dual_with_edge_map(G36)

assert G36.number_of_nodes() == 36
assert set(dict(G36.degree()).values()) == {3}
assert nx.is_bipartite(G36)
assert nx.node_connectivity(G36) >= 3

def colouring_phi(H, mask):
    A = {v for v in H if (mask >> v) & 1}
    B = set(H) - A
    if not A or not B:
        return H.number_of_nodes() + 1
    return side_psi(H, A) + side_psi(H, B)

path = [176722, 176212, 188500]
patches = [
    {v for v in H36 if ((path[0] ^ path[1]) >> v) & 1},
    {v for v in H36 if ((path[1] ^ path[2]) >> v) & 1},
]

print("Dual order:", H36.number_of_nodes())
print("Potential values:", [colouring_phi(H36, mask) for mask in path])
print("Flipped patches:", patches)
print("Patch connectedness:", [nx.is_connected(H36.subgraph(P)) for P in patches])

assert [colouring_phi(H36, mask) for mask in path] == [2, 2, 0]
assert len(patches[0]) == 3 and nx.is_connected(H36.subgraph(patches[0]))
assert len(patches[1]) == 2 and nx.is_connected(H36.subgraph(patches[1]))

# --- notebook cell 8 ---
a, c = sp.symbols("a c", integer=True, nonnegative=True)
b = 4*a + 5*c
cut_size = sp.simplify(a + b + c)
print("|delta(S)| =", cut_size)
assert sp.expand(cut_size - (5*a + 6*c)) == 0

# --- notebook cell 11 ---
d = sp.symbols("d", integer=True)
m = d + 2

# I: removed current matching contains the edge, P(I=1)=m/6.
# J: added random matching contains the edge, P(J=1)=1/3.
# They are independent.
E_Z = -m/sp.Integer(6) + sp.Rational(1, 3)
E_Z2 = m/sp.Integer(6) + sp.Rational(1, 3) - 2*(m/sp.Integer(6))*sp.Rational(1, 3)
edge_delta = sp.expand(2*d*E_Z + E_Z2)

print("Expected edge contribution:", sp.factor(edge_delta))
# Summing uses sum d_e=0 and |E|=3n/2.
Q, n = sp.symbols("Q n", nonnegative=True)
total = sp.simplify(-Q/sp.Integer(3) + sp.Rational(4, 9)*(3*n/sp.Integer(2)))
print("Expected total change:", total)
assert sp.simplify(total - (2*n-Q)/3) == 0

# --- notebook cell 13 ---
k = sp.symbols("k", integer=True, positive=True)
d = sp.symbols("d", integer=True)
m = d + 2

var_removed = k*(6-k)*m*(6-m)/(36*5)
var_added = k*(6-k)*2*4/(36*5)
mean_z = -k*d/6
edge_change = sp.expand(2*d*mean_z + var_removed + var_added + mean_z**2)
print("Edgewise:", sp.factor(edge_change))

formula = k/sp.Integer(30) * ((k-11)*Q + 4*(6-k)*n)
print("Total:", formula)

thresholds = {
    1: sp.Rational(2, 1),
    2: sp.Rational(16, 9),
    3: sp.Rational(3, 2),
    4: sp.Rational(8, 7),
    5: sp.Rational(2, 3),
}
pd.DataFrame(
    [{"k": kk, "strict descent when Q/n >": str(v)}
     for kk, v in thresholds.items()]
)

# --- notebook cell 15 ---
def perfect_matchings(G):
    nodes = tuple(G.nodes())
    result = []

    def rec(remaining, chosen):
        if not remaining:
            result.append(frozenset(tuple(sorted(e)) for e in chosen))
            return
        u = min(remaining)
        for v in G.neighbors(u):
            if v in remaining:
                rec(
                    remaining - {u, v},
                    chosen + [(u, v)],
                )

    rec(set(nodes), [])
    return sorted(set(result), key=lambda M: sorted(M))


def state_Q(edge_list, pms, state):
    mult = Counter()
    for index in state:
        mult.update(pms[index])
    return sum((mult[e] - 2)**2 for e in edge_list)


P = nx.petersen_graph()
edges = sorted(tuple(sorted(e)) for e in P.edges())
pms = perfect_matchings(P)
states = list(combinations_with_replacement(range(len(pms)), 6))
qvals = {state: state_Q(edges, pms, state) for state in states}
targets = [state for state in states if qvals[state] == 0]

reverse = defaultdict(list)
for state in states:
    current = list(state)
    for position in range(6):
        base = current[:position] + current[position+1:]
        for replacement in range(len(pms)):
            new_state = tuple(sorted(base + [replacement]))
            if qvals[new_state] <= qvals[state]:
                reverse[new_state].append(state)

reached = set(targets)
queue = deque(targets)
while queue:
    state = queue.popleft()
    for predecessor in reverse[state]:
        if predecessor not in reached:
            reached.add(predecessor)
            queue.append(predecessor)

print("Perfect matchings:", len(pms))
print("States:", len(states))
print("Fulkerson covers:", len(targets))
print("States reaching a cover:", len(reached))

assert len(pms) == 6
assert len(states) == 462
assert len(reached) == len(states)
