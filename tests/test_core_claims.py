from collections import Counter
import random
import networkx as nx

from berge_fulkerson.src.perfect_matchings import enumerate_perfect_matchings
from berge_fulkerson.src.state_encoding import quadratic_potential
from berge_fulkerson.src.coordinate_descent import replacement_delta
from three_decomposition.src.cotree_defect import bad_path_count, defect_edges
from barnette.src.planar_embedding import dual_with_edge_map
from barnette.src.colouring_potential import phi


def test_replacement_identity_random_petersen_states():
    graph = nx.petersen_graph()
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
    pms = enumerate_perfect_matchings(graph)
    rng = random.Random(20260712)
    for _ in range(100):
        state = [rng.choice(pms) for _ in range(6)]
        index = rng.randrange(6)
        replacement = rng.choice(pms)
        q0 = quadratic_potential(edges, state)
        changed = list(state); changed[index] = replacement
        assert quadratic_potential(edges, changed) - q0 == replacement_delta(edges, state, index, replacement)


def test_cotree_defect_identity_on_k4():
    graph = nx.complete_graph(4)
    for tree in nx.SpanningTreeIterator(graph):
        edges = frozenset(tuple(sorted(edge)) for edge in tree.edges())
        assert len(defect_edges(graph, edges)) == 2 * bad_path_count(graph, edges)


def test_barnette_identity_cube_all_colourings():
    primal = nx.cubical_graph()
    dual, mapping = dual_with_edge_map(primal)
    n = dual.number_of_nodes()
    for mask in range(1, (1 << n) - 1):
        bichromatic = []
        for u, v in dual.edges():
            if ((mask >> u) & 1) != ((mask >> v) & 1):
                bichromatic.append(mapping[tuple(sorted((u, v)))])
        even = nx.Graph(); even.add_nodes_from(primal.nodes()); even.add_edges_from(bichromatic)
        used = [v for v, d in even.degree() if d]
        z = primal.number_of_nodes() - len(used)
        t = nx.number_connected_components(even.subgraph(used)) if used else 0
        assert phi(dual, mask) == z + 2 * (t - 1)
