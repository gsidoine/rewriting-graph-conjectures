
# --- notebook cell 1 ---
from collections import Counter, deque
from dataclasses import dataclass
import time

import networkx as nx
import pandas as pd
from networkx.algorithms.tree.mst import SpanningTreeIterator

print("NetworkX", nx.__version__)

# --- notebook cell 3 ---
class CubicRewriteSystem:
    """Bit-mask representation of spanning trees and cotree rewrites."""

    def __init__(self, G):
        G = nx.convert_node_labels_to_integers(G)
        if not nx.is_connected(G) or set(dict(G.degree()).values()) != {3}:
            raise ValueError("G must be a connected simple cubic graph.")
        self.G = G
        self.n = G.number_of_nodes()
        self.edges = [tuple(sorted(e)) for e in G.edges()]
        self.m = len(self.edges)
        self.index = {e: i for i, e in enumerate(self.edges)}
        self.full_mask = (1 << self.m) - 1

    def edge_index(self, u, v):
        return self.index[tuple(sorted((u, v)))]

    def tree_adjacency(self, mask):
        adj = [[] for _ in range(self.n)]
        for i, (u, v) in enumerate(self.edges):
            if (mask >> i) & 1:
                adj[u].append(v)
                adj[v].append(u)
        return adj

    def cotree_adjacency(self, mask):
        adj = [[] for _ in range(self.n)]
        for i, (u, v) in enumerate(self.edges):
            if not ((mask >> i) & 1):
                adj[u].append(v)
                adj[v].append(u)
        return adj

    def bad_paths(self, mask):
        H = self.cotree_adjacency(mask)
        seen = [False] * self.n
        result = []
        for start in range(self.n):
            if seen[start] or not H[start]:
                continue
            stack = [start]
            seen[start] = True
            component = []
            while stack:
                v = stack.pop()
                component.append(v)
                for w in H[v]:
                    if not seen[w]:
                        seen[w] = True
                        stack.append(w)
            edge_count = sum(len(H[v]) for v in component) // 2
            if edge_count < 2:
                continue
            ends = [v for v in component if len(H[v]) == 1]
            if len(ends) != 2:
                continue  # cycle component
            path = [ends[0]]
            previous = None
            current = ends[0]
            while current != ends[1]:
                nxt = next(w for w in H[current] if w != previous)
                path.append(nxt)
                previous, current = current, nxt
            result.append(path)
        return result

    def b(self, mask):
        return len(self.bad_paths(mask))

    def p2_only(self, mask):
        return all(len(path) == 3 for path in self.bad_paths(mask))

    def defect_edge_count(self, mask):
        T = self.tree_adjacency(mask)
        count = 0
        for i, (u, v) in enumerate(self.edges):
            if (mask >> i) & 1:
                continue
            if sorted((len(T[u]), len(T[v]))) == [1, 2]:
                count += 1
        return count

    def spanning_tree_masks(self):
        for tree in SpanningTreeIterator(self.G):
            mask = 0
            for u, v in tree.edges():
                mask |= 1 << self.edge_index(u, v)
            yield mask

    @staticmethod
    def tree_path(T, source, target):
        parent = {source: None}
        queue = deque([source])
        while queue:
            v = queue.popleft()
            if v == target:
                break
            for w in T[v]:
                if w not in parent:
                    parent[w] = v
                    queue.append(w)
        path = [target]
        v = target
        while v != source:
            v = parent[v]
            path.append(v)
        path.reverse()
        return path

    def basis_exchange_neighbors(self, mask):
        T = self.tree_adjacency(mask)
        neighbors = set()
        for i, (u, v) in enumerate(self.edges):
            if (mask >> i) & 1:
                continue
            path = self.tree_path(T, u, v)
            for a, b in zip(path, path[1:]):
                remove = self.edge_index(a, b)
                neighbors.add((mask | (1 << i)) & ~(1 << remove))
        return neighbors

    def endpoint_leaf_slides(self, mask):
        T = self.tree_adjacency(mask)
        before = self.b(mask)
        moves = set()
        for path in self.bad_paths(mask):
            for oriented in (path, list(reversed(path))):
                v0, v1 = oriented[0], oriented[1]
                assert len(T[v1]) == 1
                x = T[v1][0]
                add = self.edge_index(v0, v1)
                remove = self.edge_index(v1, x)
                nxt = (mask | (1 << add)) & ~(1 << remove)
                assert self.b(nxt) <= before
                moves.add(nxt)
        return moves

    def tail_peels(self, mask):
        T = self.tree_adjacency(mask)
        before = self.b(mask)
        moves = set()
        for path in self.bad_paths(mask):
            if len(path) < 4:
                continue
            for oriented in (path, list(reversed(path))):
                a, b = oriented[-3], oriented[-2]
                assert len(T[a]) == 1
                x = T[a][0]
                add = self.edge_index(a, b)
                remove = self.edge_index(a, x)
                nxt = (mask | (1 << add)) & ~(1 << remove)
                assert self.b(nxt) <= before
                moves.add(nxt)
        return moves

    def safe_moves(self, mask):
        return self.endpoint_leaf_slides(mask) | self.tail_peels(mask)

    def endpoint_transports(self, mask):
        T = self.tree_adjacency(mask)
        before = self.b(mask)
        moves = set()
        for path in self.bad_paths(mask):
            if len(path) != 3:
                continue
            for endpoint, center in ((path[0], path[1]), (path[2], path[1])):
                tree_path = self.tree_path(T, endpoint, center)
                x = tree_path[1]
                add = self.edge_index(endpoint, center)
                remove = self.edge_index(endpoint, x)
                nxt = (mask | (1 << add)) & ~(1 << remove)
                assert self.b(nxt) <= before
                moves.add(nxt)
        return moves

# --- notebook cell 8 ---
graph6_classes = {
    4: ["C~"],
    6: ["EZfG", "E]NG"],
    8: ["GqCilO", "GU`_zO", "GsSJHg", "GHqouC", "GLdBKW"],
    10: [
        "IAiKJ@PK_", "IG`iSaPK_", "IOKcmHOQG", "IGdV@a@BG",
        "IIEcJOIcG", "ICSlADo`O", "IKt@?gb`_", "IPPEGgXi?",
        "IlCCAKMJ?", "IqGSWoDWG", "ISHCq`DJ?", "ICWQZAccO",
        "I@oJAiad?", "IPPIDaQB_", "ILFGR?B_g", "IrAIH?XAo",
        "I?CwvBAw?", "IBYJ?IBcO", "IM@GpEg`O",
    ],
}

@dataclass
class ExhaustiveReport:
    graph: str
    vertices: int
    spanning_trees: int
    positive_neutral_components: int
    closed_positive_plateaux: int
    terminal_safe_components: int
    terminal_safe_components_without_target: int
    verified_safe_moves: int
    verified_endpoint_transports: int
    seconds: float


def analyze_graph(G, name):
    start = time.time()
    system = CubicRewriteSystem(G)
    states = list(system.spanning_tree_masks())
    state_set = set(states)
    bvals = {}

    neutral = nx.Graph()
    safe = nx.DiGraph()
    neutral.add_nodes_from(states)
    safe.add_nodes_from(states)

    safe_checks = 0
    transport_checks = 0

    for state in states:
        bvals[state] = system.b(state)
        assert system.defect_edge_count(state) == 2 * bvals[state]

    for state in states:
        for nxt in system.basis_exchange_neighbors(state):
            assert nxt in state_set
            if bvals[nxt] == bvals[state]:
                neutral.add_edge(state, nxt)

        for nxt in system.safe_moves(state):
            assert nxt in state_set
            assert bvals[nxt] <= bvals[state]
            safe.add_edge(state, nxt)
            safe_checks += 1

        if system.p2_only(state):
            for nxt in system.endpoint_transports(state):
                assert nxt in state_set
                assert bvals[nxt] <= bvals[state]
                transport_checks += 1

    positive_components = 0
    closed_plateaux = 0
    for component in nx.connected_components(neutral):
        level = bvals[next(iter(component))]
        assert all(bvals[state] == level for state in component)
        if level == 0:
            continue
        positive_components += 1
        has_strict_exit = any(
            bvals[nxt] < level
            for state in component
            for nxt in system.basis_exchange_neighbors(state)
        )
        if not has_strict_exit:
            closed_plateaux += 1

    terminal_safe = 0
    terminal_safe_without_target = 0
    for component in nx.strongly_connected_components(safe):
        terminal = not any(
            nxt not in component
            for state in component
            for nxt in safe.successors(state)
        )
        if not terminal:
            continue
        terminal_safe += 1
        target = any(
            bvals[state] == 0 or system.p2_only(state)
            for state in component
        )
        if not target:
            terminal_safe_without_target += 1

    return ExhaustiveReport(
        graph=name,
        vertices=G.number_of_nodes(),
        spanning_trees=len(states),
        positive_neutral_components=positive_components,
        closed_positive_plateaux=closed_plateaux,
        terminal_safe_components=terminal_safe,
        terminal_safe_components_without_target=terminal_safe_without_target,
        verified_safe_moves=safe_checks,
        verified_endpoint_transports=transport_checks,
        seconds=round(time.time() - start, 3),
    )

reports = []
for n, encodings in graph6_classes.items():
    for i, encoding in enumerate(encodings, start=1):
        G = nx.from_graph6_bytes(encoding.encode())
        reports.append(analyze_graph(G, f"n={n}, class={i}"))

report_table = pd.DataFrame([r.__dict__ for r in reports])
summary = (
    report_table.groupby("vertices", as_index=False)
    .agg(
        graph_classes=("graph", "count"),
        spanning_tree_states=("spanning_trees", "sum"),
        positive_neutral_components=("positive_neutral_components", "sum"),
        closed_positive_plateaux=("closed_positive_plateaux", "sum"),
        terminal_safe_components=("terminal_safe_components", "sum"),
        terminal_safe_without_target=("terminal_safe_components_without_target", "sum"),
        verified_safe_moves=("verified_safe_moves", "sum"),
        verified_endpoint_transports=("verified_endpoint_transports", "sum"),
        seconds=("seconds", "sum"),
    )
)
summary

# --- notebook cell 9 ---
total_classes = len(reports)
total_states = sum(r.spanning_trees for r in reports)
total_closed = sum(r.closed_positive_plateaux for r in reports)
total_bad_safe = sum(r.terminal_safe_components_without_target for r in reports)
total_safe_moves = sum(r.verified_safe_moves for r in reports)
total_transports = sum(r.verified_endpoint_transports for r in reports)

print(f"Graph isomorphism classes: {total_classes}")
print(f"Spanning-tree states: {total_states:,}")
print(f"Verified safe rewrites: {total_safe_moves:,}")
print(f"Verified P2 endpoint transports: {total_transports:,}")
print(f"Closed positive neutral plateaux: {total_closed}")
print(f"Terminal safe SCCs without a target: {total_bad_safe}")

assert total_classes == 27
assert total_states == 30_619
assert total_closed == 0
assert total_bad_safe == 0
