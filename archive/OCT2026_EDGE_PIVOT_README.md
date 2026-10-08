# October 2026: edge-connectivity partition research pivot

This is an **additive, experimental research branch**. All prior mathematical status ledgers and papers are preserved unchanged. No claim is made here that the DeVos--Johnson--Seymour edge-connectivity partition conjecture, the general 5-regular internal partition problem, or any other major graph-theory conjecture has been resolved.

The new branch lives in [`edge_partitioning/`](edge_partitioning/). Begin with [`edge_partitioning/RESEARCH_FINDINGS.md`](edge_partitioning/RESEARCH_FINDINGS.md), which describes formal theorem statements, complete proofs, limitations, literature, exact finite certificates, and reproduction commands.

The main outcomes are an exact Boolean (fundamental-cut) reduction for two disjoint spanning trees, an elementary infinite family showing why arbitrary frozen tree pairs cannot work even with arbitrarily large edge-connectivity, and an exhaustive 24,585,120-case finite theorem on the three-tree condition for K7. Additional positive Hamilton-splice families are included as constructions, **not** claimed novel.

## Verify

```bash
cd edge_partitioning
python bridge_completion.py
python test_bridge_completion.py
python test_k7_independent_sample.py
python hamiltonian_splice.py
g++ -O3 -std=c++17 k7_packed_tree_exhaustive.cpp -o /tmp/k7check
/tmp/k7check keep
```

The numerical exploratory code `partition_lab.py` and `third_tree_random_search.py` additionally requires NetworkX, NumPy, and SciPy.

Private GitHub default branch was not changed to create this snapshot.
