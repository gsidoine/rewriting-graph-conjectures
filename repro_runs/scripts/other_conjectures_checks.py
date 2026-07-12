
# --- notebook cell 1 ---
from collections import defaultdict, deque
import itertools
import random
import networkx as nx
import pandas as pd

print("NetworkX:", nx.__version__)

# --- notebook cell 3 ---
def planar_faces(G):
    planar, embedding = nx.check_planarity(G)
    if not planar:
        raise ValueError("Nonplanar graph.")
    seen, faces = set(), []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            faces.append(embedding.traverse_face(u, v, seen))
    return faces


def planar_dual(G):
    faces = planar_faces(G)
    edge_faces = defaultdict(list)
    for index, face in enumerate(faces):
        for j, u in enumerate(face):
            v = face[(j + 1) % len(face)]
            edge_faces[tuple(sorted((u, v)))].append(index)

    assert all(len(items) == 2 for items in edge_faces.values())
    dual = nx.Graph()
    dual.add_nodes_from(range(len(faces)))
    for items in edge_faces.values():
        dual.add_edge(items[0], items[1])
    return dual, faces


def c4_expansion_candidates(G):
    candidates = []
    for face in planar_faces(G):
        length = len(face)
        for i in range(length):
            for j in range(i + 1, length):
                a, b = face[i], face[(i + 1) % length]
                c, d = face[j], face[(j + 1) % length]
                if len({a, b, c, d}) < 4:
                    continue

                first = max(G.nodes()) + 1
                p, q, r, s = range(first, first + 4)

                for crossed in (False, True):
                    H = G.copy()
                    H.remove_edge(a, b)
                    H.remove_edge(c, d)
                    H.add_edges_from([
                        (a, p), (p, q), (q, b),
                        (c, r), (r, s), (s, d),
                    ])
                    H.add_edges_from(
                        [(p, s), (q, r)] if crossed else [(p, r), (q, s)]
                    )

                    if set(dict(H.degree()).values()) != {3}:
                        continue
                    if not nx.is_bipartite(H):
                        continue
                    if not nx.check_planarity(H)[0]:
                        continue
                    candidates.append(H)
    return candidates


def generated_barnette_graph(steps, seed):
    rng = random.Random(seed)
    G = nx.cubical_graph()
    for _ in range(steps):
        choices = c4_expansion_candidates(G)
        if not choices:
            raise RuntimeError("No valid C4 expansion.")
        G = rng.choice(choices)

    assert nx.is_bipartite(G)
    assert nx.node_connectivity(G) >= 3
    assert set(dict(G.degree()).values()) == {3}
    return G

# --- notebook cell 5 ---
class BinaryColourRewrite:
    def __init__(self, H):
        self.H = nx.convert_node_labels_to_integers(H)
        self.n = self.H.number_of_nodes()
        self.full = (1 << self.n) - 1
        self.adj = [0] * self.n
        for u, v in self.H.edges():
            self.adj[u] |= 1 << v
            self.adj[v] |= 1 << u

    def components(self, mask):
        count = 0
        unseen = mask
        while unseen:
            count += 1
            seed = unseen & -unseen
            frontier = seed
            unseen ^= seed
            while frontier:
                reached = 0
                work = frontier
                while work:
                    bit = work & -work
                    work ^= bit
                    vertex = bit.bit_length() - 1
                    reached |= self.adj[vertex]
                frontier = reached & unseen
                unseen ^= frontier
        return count

    def side_defect(self, mask):
        if mask == 0:
            return self.n + 1

        vertices = mask.bit_count()
        twice_edges = 0
        work = mask
        while work:
            bit = work & -work
            work ^= bit
            vertex = bit.bit_length() - 1
            twice_edges += (self.adj[vertex] & mask).bit_count()

        edges = twice_edges // 2
        components = self.components(mask)
        cycle_rank = edges - vertices + components
        return (components - 1) + cycle_rank

    def all_values(self):
        return [
            self.side_defect(mask) + self.side_defect(self.full ^ mask)
            for mask in range(1 << self.n)
        ]

    def normalization_report(self, pair_flips=False):
        values = self.all_values()
        patches = [1 << v for v in range(self.n)]
        if pair_flips:
            patches += [(1 << u) | (1 << v) for u, v in self.H.edges()]

        targets = [mask for mask, value in enumerate(values) if value == 0]
        reached = bytearray(1 << self.n)
        queue = deque(targets)
        for mask in targets:
            reached[mask] = 1

        while queue:
            current = queue.popleft()
            current_value = values[current]
            for patch in patches:
                predecessor = current ^ patch
                # predecessor -> current is an allowed non-increasing move
                if not reached[predecessor] and values[predecessor] >= current_value:
                    reached[predecessor] = 1
                    queue.append(predecessor)

        return {
            "states": 1 << self.n,
            "targets": len(targets),
            "states_reaching_target": int(sum(reached)),
            "states_not_reaching_target": (1 << self.n) - int(sum(reached)),
        }

# --- notebook cell 7 ---
specifications = [
    (0, 1000),
    (1, 1100),
    (2, 1200),
    (3, 1300),
    (3, 1301),
    (4, 1400),
    (4, 1402),
    (5, 2000),
]

rows = []
for steps, seed in specifications:
    primal = generated_barnette_graph(steps, seed)
    dual, _ = planar_dual(primal)
    system = BinaryColourRewrite(dual)

    single = system.normalization_report(pair_flips=False)
    pair = system.normalization_report(pair_flips=True)

    rows.append({
        "C4_expansions": steps,
        "seed": seed,
        "primal_vertices": primal.number_of_nodes(),
        "dual_vertices": dual.number_of_nodes(),
        "states": single["states"],
        "targets": single["targets"],
        "single_flip_unresolved_states":
            single["states_not_reaching_target"],
        "pair_flip_unresolved_states":
            pair["states_not_reaching_target"],
    })

results = pd.DataFrame(rows)
results

# --- notebook cell 8 ---
print("Generated Barnette graphs:", len(results))
print("Complete colouring states checked:", f"{results['states'].sum():,}")
print(
    "Graphs with single-flip traps:",
    int((results["single_flip_unresolved_states"] > 0).sum()),
)
print(
    "Unresolved states with adjacent-pair flips:",
    int(results["pair_flip_unresolved_states"].sum()),
)

assert results["pair_flip_unresolved_states"].sum() == 0

# --- notebook cell 11 ---
terminals = ("a", "b", "c", "d")
internal = ("p", "q", "r", "s")
patch_edges = [
    ("a", "p"), ("p", "q"), ("q", "b"),
    ("c", "r"), ("r", "s"), ("s", "d"),
    ("p", "r"), ("q", "s"),
]

patterns = []
for mask in range(1 << len(patch_edges)):
    chosen = [patch_edges[i] for i in range(len(patch_edges)) if (mask >> i) & 1]
    degree = defaultdict(int)
    for u, v in chosen:
        degree[u] += 1
        degree[v] += 1

    if any(degree[v] != 2 for v in internal):
        continue
    if any(degree[v] not in (0, 1) for v in terminals):
        continue

    F = nx.Graph()
    F.add_nodes_from(terminals + internal)
    F.add_edges_from(chosen)

    relevant = [
        set(component)
        for component in nx.connected_components(F)
        if any(v in internal for v in component)
    ]
    if not all(any(degree[t] == 1 and t in component for t in terminals)
               for component in relevant):
        continue

    pairings = []
    for component in relevant:
        ends = [t for t in terminals if t in component and degree[t] == 1]
        if len(ends) == 2:
            pairings.append("-".join(sorted(ends)))

    patterns.append({
        "used_terminals": "".join(t for t in terminals if degree[t] == 1),
        "path_pairing": ", ".join(sorted(pairings)),
        "selected_edges": " ".join(f"{u}{v}" for u, v in chosen),
    })

pd.DataFrame(patterns)
