"""Planar dual construction with a dual-to-primal edge map."""
from __future__ import annotations
from collections import defaultdict
import networkx as nx


def plane_faces(graph: nx.Graph):
    planar, embedding = nx.check_planarity(graph)
    if not planar:
        raise ValueError("graph is not planar")
    seen = set(); faces = []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            faces.append(embedding.traverse_face(u, v, seen))
    return faces, embedding


def dual_with_edge_map(graph: nx.Graph):
    faces, _ = plane_faces(graph)
    edge_faces = defaultdict(list)
    for index, face in enumerate(faces):
        for j, u in enumerate(face):
            v = face[(j + 1) % len(face)]
            edge_faces[tuple(sorted((u, v)))].append(index)
    dual = nx.Graph(); dual.add_nodes_from(range(len(faces)))
    mapping = {}
    for edge, incident in edge_faces.items():
        if len(incident) != 2:
            raise ValueError("embedding edge does not have two incident faces")
        u, v = incident
        dual.add_edge(u, v)
        mapping[tuple(sorted((u, v)))] = edge
    return dual, mapping
