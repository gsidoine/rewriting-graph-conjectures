"""Independent audits of exact cycle transfer, using NetworkX simple_cycles."""
from collections import Counter
import random

import networkx as nx

from applications.erdos_gyarfas.cycle_transfer import (
    profile, glue, transfer_counts, defect, permutation_defects, rewrite_delta
)


def pole(edges, ports, prefix):
    nodes = sorted(set(ports) | {u for edge in edges for u in edge})
    return (
        [f"{prefix}{v}" for v in nodes],
        [(f"{prefix}{u}", f"{prefix}{v}") for u, v in edges],
        [f"{prefix}{v}" for v in ports],
    )


def prism_pole(prefix):
    return pole([(1, 2), (1, 4), (2, 5), (3, 4), (3, 5), (4, 5)],
                [1, 2, 3], prefix)


def triangle(prefix):
    return pole([(1, 2), (1, 3), (2, 3)], [1, 2, 3], prefix)


def octet_pole(prefix):
    return pole([(1, 7), (1, 3), (2, 4), (2, 7), (2, 5),
                 (3, 4), (3, 6), (4, 5), (5, 6)],
                [1, 6, 7], prefix)


def oracle(vertices, edges):
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(edges)
    return Counter(map(len, nx.simple_cycles(graph)))


def test_triangle_prism():
    left = triangle("L")
    right = triangle("R")
    vertices, edges = glue(*left, *right)
    expected = Counter({3: 2, 4: 3, 5: 6, 6: 3})
    assert transfer_counts(profile(*left), profile(*right)) == expected
    assert oracle(vertices, edges) == expected


def test_context_reversal():
    a, b = triangle("A"), prism_pole("B")
    contexts = [triangle("X"), octet_pole("Y")]
    expected = {(0, 0): 3, (1, 0): 5, (0, 1): 14, (1, 1): 13}
    for i, left in enumerate([a, b]):
        for j, right in enumerate(contexts):
            vertices, edges = glue(*left, *right)
            assert set(dict(nx.Graph(edges).degree()).values()) == {3}
            actual = defect(oracle(vertices, edges))
            predicted = defect(transfer_counts(profile(*left), profile(*right)))
            assert actual == predicted == expected[(i, j)]
    assert rewrite_delta(profile(*a), profile(*b), profile(*contexts[0])) == 2
    assert rewrite_delta(profile(*a), profile(*b), profile(*contexts[1])) == -1


def test_six_port_reconnections():
    left, right = prism_pole("B"), octet_pole("R")
    costs = permutation_defects(profile(*left), *right)
    assert list(costs.values()) == [13, 14, 13, 10, 14, 10]
    for perm, number in costs.items():
        new_ports = [right[2][i] for i in perm]
        vertices, edges = glue(*left, right[0], right[1], new_ports)
        assert defect(oracle(vertices, edges)) == number
        assert set(dict(nx.Graph(edges).degree()).values()) == {3}


def test_random_general_shores():
    rng = random.Random(8286)
    for index in range(120):
        shores = []
        for side in "LR":
            n = rng.randrange(3, 8)
            vertices = [f"{side}{index}_{k}" for k in range(n)]
            edges = [
                (vertices[i], vertices[j])
                for i in range(n)
                for j in range(i + 1, n)
                if rng.random() < 0.32
            ]
            shores.append((vertices, edges, vertices[:3]))
        left, right = shores
        vertices, edges = glue(*left, *right)
        assert oracle(vertices, edges) == transfer_counts(
            profile(*left), profile(*right))
