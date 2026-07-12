
# --- notebook cell 1 ---
from collections import Counter
import itertools
import networkx as nx

print("NetworkX", nx.__version__)

# --- notebook cell 3 ---
graph6 = b"O??DQ?[C?AaAA?@O??wGS"
R = nx.from_graph6_bytes(graph6)

print("vertices:", R.number_of_nodes())
print("edges:", R.number_of_edges())
print("leaves:", [v for v, d in R.degree() if d == 1])
print("degree counts:", Counter(dict(R.degree()).values()))
print("edge list:")
for e in sorted(tuple(sorted(e)) for e in R.edges()):
    print(e)

assert R.number_of_nodes() == 16
assert R.number_of_edges() == 21
assert Counter(dict(R.degree()).values()) == Counter({3: 13, 1: 3})

# --- notebook cell 5 ---
leaves = {v for v, d in R.degree() if d == 1}
bridges = list(nx.bridges(R))

bridge_table = []
for u, v in bridges:
    H = R.copy()
    H.remove_edge(u, v)
    sides = [set(c) for c in nx.connected_components(H)]
    leaf_sets = [sorted(side & leaves) for side in sides]
    bridge_table.append(((u, v), leaf_sets))
    assert all(side & leaves for side in sides)

print("bridges and leaves on their two sides:")
for row in bridge_table:
    print(row)

# --- notebook cell 7 ---
N0 = {
    (3, 8),
    (4, 12),
    (5, 13),
    (7, 10),
    (9, 11),
}

U = R.copy()
U.remove_edges_from(N0)

cycle_rank = (
    U.number_of_edges()
    - U.number_of_nodes()
    + nx.number_connected_components(U)
)

print("matching N0:", sorted(N0))
print("connected:", nx.is_connected(U))
print("cycle rank:", cycle_rank)
print("unique cycle:", nx.cycle_basis(U))

assert nx.is_matching(R, N0)
assert nx.is_connected(U)
assert cycle_rank == 1

# --- notebook cell 9 ---
edges = [tuple(sorted(e)) for e in R.edges()]

def is_matching(edge_set):
    used = set()
    for u, v in edge_set:
        if u in used or v in used:
            return False
        used.add(u)
        used.add(v)
    return True

results = {}
for size in (5, 6):
    number_of_matchings = 0
    connected_complements = 0
    connected_ranks = Counter()

    for candidate in itertools.combinations(edges, size):
        if not is_matching(candidate):
            continue

        number_of_matchings += 1
        complement = R.copy()
        complement.remove_edges_from(candidate)

        if nx.is_connected(complement):
            connected_complements += 1
            rank = (
                complement.number_of_edges()
                - complement.number_of_nodes()
                + 1
            )
            connected_ranks[rank] += 1

    results[size] = (
        number_of_matchings,
        connected_complements,
        connected_ranks,
    )

for size, result in results.items():
    print(f"size {size}: {result}")

assert results[5][0] == 1448
assert results[5][1] == 105
assert results[5][2] == Counter({1: 105})

assert results[6][0] == 615
assert results[6][1] == 0

# --- notebook cell 11 ---
core_vertices = set(R) - {0, 1, 2, 6}
H = R.subgraph(core_vertices).copy()
core_edges = [tuple(sorted(e)) for e in H.edges()]

candidates = []
for chosen in itertools.combinations(core_edges, H.number_of_nodes() - 1):
    degree = Counter()
    for u, v in chosen:
        degree[u] += 1
        degree[v] += 1

    correct_degrees = all(
        degree[v] == (1 if v in {4, 7} else 2)
        for v in H
    )
    if not correct_degrees:
        continue

    K = nx.Graph()
    K.add_nodes_from(H)
    K.add_edges_from(chosen)
    candidates.append(K)

print("degree-feasible candidates:", len(candidates))
print("connected candidates:", sum(nx.is_connected(K) for K in candidates))

assert len(candidates) == 5
assert all(not nx.is_connected(K) for K in candidates)

def describe_component(C):
    degrees = dict(C.degree())
    if all(d == 2 for d in degrees.values()):
        return "cycle", nx.cycle_basis(C)[0]

    endpoints = [v for v, d in degrees.items() if d == 1]
    return "path", nx.shortest_path(C, endpoints[0], endpoints[1])

for index, K in enumerate(candidates, start=1):
    description = []
    for component_vertices in nx.connected_components(K):
        C = K.subgraph(component_vertices).copy()
        description.append(describe_component(C))
    print(index, description)

# --- notebook cell 14 ---
G = R.copy()
triangle = {(0, 1), (1, 2), (0, 2)}
G.add_edges_from(triangle)

assert set(dict(G.degree()).values()) == {3}
assert list(nx.bridges(G)) == []

# Split N0 into a harmless matching and one passive defect edge.
passive = (7, 10)
cycle_edge = (10, 15)
M = N0 - {passive}
P2 = {passive, cycle_edge}

tree_edges = {
    tuple(sorted(e))
    for e in U.edges()
    if tuple(sorted(e)) != tuple(sorted(cycle_edge))
}

T = nx.Graph()
T.add_nodes_from(G)
T.add_edges_from(tree_edges)

partition = tree_edges | M | P2 | triangle
all_edges = {tuple(sorted(e)) for e in G.edges()}

print("cubic graph6:", nx.to_graph6_bytes(G, header=False).strip())
print("tree edges:", sorted(tree_edges))
print("fixed triangle:", sorted(triangle))
print("matching:", sorted(M))
print("P2 defect:", sorted(P2))

assert nx.is_tree(T)
assert nx.is_matching(G, M)
assert partition == all_edges
assert sum(map(len, [tree_edges, M, P2, triangle])) == len(all_edges)
