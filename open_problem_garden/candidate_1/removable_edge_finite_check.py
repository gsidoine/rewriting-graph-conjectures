#!/usr/bin/env python3
"""Finite check of Hoffmann-Ostenhof's removable-edge conjecture.

Checks every connected simple cubic graph through 10 vertices in the graph6
catalogue used by the 3-Decomposition notebook.  This is finite evidence only.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
from pathlib import Path
import networkx as nx

GRAPH6 = {
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


def edge_records(graph: nx.MultiGraph):
    return [(u, v, k) for u, v, k in graph.edges(keys=True)]


def is_three_edge_colorable(graph: nx.MultiGraph):
    """Exact backtracking for a loopless cubic multigraph."""
    if any(u == v for u, v, _ in graph.edges(keys=True)):
        return False, None
    edges = edge_records(graph)
    incident = {v: [] for v in graph.nodes()}
    for i, (u, v, _k) in enumerate(edges):
        incident[u].append(i); incident[v].append(i)
    if any(len(indices) != 3 for indices in incident.values()):
        return False, None
    colors = [-1] * len(edges)
    used = {v: 0 for v in graph.nodes()}

    def available(i):
        u, v, _ = edges[i]
        return (~(used[u] | used[v])) & 0b111

    def recurse(colored):
        if colored == len(edges):
            return True
        best = None; options = None
        for i, c in enumerate(colors):
            if c != -1:
                continue
            mask = available(i)
            count = mask.bit_count()
            if count == 0:
                return False
            if options is None or count < options.bit_count():
                best, options = i, mask
                if count == 1:
                    break
        u, v, _ = edges[best]
        while options:
            bit = options & -options; options -= bit
            color = bit.bit_length() - 1
            colors[best] = color; used[u] |= bit; used[v] |= bit
            if recurse(colored + 1):
                return True
            used[u] ^= bit; used[v] ^= bit; colors[best] = -1
        return False

    ok = recurse(0)
    return ok, colors[:] if ok else None


def as_multigraph(graph: nx.Graph) -> nx.MultiGraph:
    result = nx.MultiGraph(); result.add_nodes_from(graph.nodes()); result.add_edges_from(graph.edges())
    return result


def suppress_after_edge_deletion(graph: nx.Graph, edge):
    u, v = edge
    nu = [x for x in graph.neighbors(u) if x != v]
    nv = [x for x in graph.neighbors(v) if x != u]
    assert len(nu) == len(nv) == 2
    result = nx.MultiGraph()
    result.add_nodes_from(x for x in graph.nodes() if x not in {u, v})
    for a, b in graph.edges():
        if a not in {u, v} and b not in {u, v}:
            result.add_edge(a, b)
    result.add_edge(nu[0], nu[1])
    result.add_edge(nv[0], nv[1])
    return result


def main():
    records=[]
    colorable=0; good=0
    for n, encodings in GRAPH6.items():
        for graph6 in encodings:
            graph = nx.from_graph6_bytes(graph6.encode())
            ok,_=is_three_edge_colorable(as_multigraph(graph))
            removable=[]
            if ok:
                colorable += 1
                for edge in graph.edges():
                    reduced=suppress_after_edge_deletion(graph, edge)
                    reduced_ok,_=is_three_edge_colorable(reduced)
                    if reduced_ok:
                        removable.append(tuple(sorted(edge)))
                assert removable
                good += 1
            records.append({"n":n,"graph6":graph6,"three_edge_colorable":ok,"removable_edges":removable})
    payload={
        "graph_classes":sum(map(len,GRAPH6.values())),
        "three_edge_colorable_classes":colorable,
        "classes_with_verified_removable_edge":good,
        "records":records,
        "scope":"All connected simple cubic graph classes through 10 vertices in the supplied catalogue. Finite verification only."
    }
    out=Path(__file__).with_name("finite_check_result.json")
    out.write_text(json.dumps(payload,indent=2)+"\n")
    print(payload["scope"])
    print("classes",payload["graph_classes"],"3-edge-colourable",colorable,"verified",good)
    print("minimum removable edges",min(len(r["removable_edges"]) for r in records if r["three_edge_colorable"]))

if __name__ == "__main__":
    main()
