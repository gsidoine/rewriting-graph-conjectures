# Literature Review and Novelty Audit

**Updated:** 12 July 2026

This document maps the audited claims to their closest known literature. It is intentionally cautious: “not located” means that the stated formulation was not found in the sources inspected, not that priority has been conclusively established. The publication manuscripts contain the concise bibliographies; this file records the broader comparison and the search terms used.

## 1. Berge–Fulkerson: six perfect matchings and quadratic discrepancy

### Classical framework

Fulkerson’s conjecture asks for six perfect matchings of a bridgeless cubic graph in which every edge appears exactly twice. The standard convex foundation is Edmonds’ perfect-matching polytope; in a bridgeless cubic graph the vector \(\frac13\mathbf 1\) is a fractional perfect matching. Mazzuoccolo established the equivalence of the Berge and Fulkerson formulations and studied covers by perfect matchings. Other nearby lines include:

- the perfect matching index and coverings by four, five, or six perfect matchings;
- the maximum fraction of edges covered by a prescribed number of perfect matchings;
- unions of 1-factors in \(r\)-graphs;
- colouring defect and regular colouring defect as measures of distance from 3-edge-colourability;
- cycle-cover consequences of small defect;
- oriented versions of Berge–Fulkerson;
- the computational complexity of the perfect matching index.

### Closest sources inspected

1. D. R. Fulkerson, “Blocking and anti-blocking pairs of polyhedra,” *Mathematical Programming* 1 (1971), 168–194.
2. J. Edmonds, “Maximum matching and a polyhedron with 0,1-vertices,” *J. Res. Nat. Bur. Standards Sect. B* 69B (1965), 125–130.
3. G. Mazzuoccolo, “The equivalence of two conjectures of Berge and Fulkerson,” *J. Graph Theory* 68 (2011), 125–128.
4. G. Mazzuoccolo, “Covering a cubic graph with perfect matchings,” *Discrete Mathematics* 313 (2013), 2292–2296.
5. L. Esperet and G. Mazzuoccolo, “On the maximum fraction of edges covered by \(t\) perfect matchings in a cubic bridgeless graph,” *Discrete Mathematics* 338 (2015), 1509–1514.
6. E. Steffen, “1-factor and cycle covers of cubic graphs,” *J. Graph Theory* 78 (2015), 195–206.
7. M. A. Fiol, G. Mazzuoccolo, and E. Steffen, “Measures of edge-uncolourability of cubic graphs,” *Electronic Journal of Combinatorics* 25 (2018), P4.54.
8. L. Jin and E. Steffen, “Unions of 1-factors in \(r\)-graphs and overfull graphs,” *Journal of Combinatorics* 11 (2020), 457–473; corrigendum 15 (2024), 409–412.
9. J. Karabáš, E. Máčajová, R. Nedela, and M. Škoviera, “Cubic graphs with colouring defect 3,” *Electronic Journal of Combinatorics* 31 (2024), P2.6.
10. The same authors, “Berge’s conjecture for cubic graphs with small colouring defect,” *Journal of Graph Theory* (online 2025), DOI 10.1002/jgt.23231.
11. The same authors, “Regular colouring defect of a cubic graph and the conjectures of Fan–Raspaud and Fulkerson,” arXiv:2312.13638, version 2 (2025).
12. The same authors, “Cubic graphs of colouring defect 3 and conjectures of Berge and Alon–Tarsi,” arXiv:2505.17569 (2025).
13. M. Škoviera and P. Varša, “NP-completeness of perfect matching index of cubic graphs,” *STACS 2022*, LIPIcs 219, Article 56.
14. N. Ulyanov, “Computational Graph Decompositions I: Oriented Berge–Fulkerson Conjecture,” arXiv:2501.05348 (2025).

### Comparison with the present programme

The ingredients “fractional perfect matching,” “minimum-weight perfect matching,” and “defect from an ideal cover” are established. The inspected sources did **not** formulate the state as an ordered or unordered sextuple of perfect matchings with

\[
Q=\sum_{e}(m(e)-2)^2,
\]

derive the exact one-coordinate replacement weight

\[
w_i(e)=2(m(e)-2)+1-2\mathbf 1_{e\in M_i},
\]

or prove that every one-coordinate local minimum lies in \(Q\le 2n\), with the residue-sensitive improvement under the audited cyclic-connectivity hypotheses. The low-defect alternating-cycle description is close in spirit to colouring-defect theory, but its six-matching incidence-set formulation is distinct.

**Recommended novelty wording:**

> We introduce a quadratic discrepancy potential for six perfect matchings and derive a polynomial coordinate-descent theorem. We are not aware of a previous local-search formulation yielding the \(2n\) local-minimum barrier.

This avoids claiming priority for optimization, fractional matching, or defect methods generally.

## 2. The 3-Decomposition Conjecture

### Established structural and computational context

The tree/cotree formulation is not new. Work on the conjecture already uses homeomorphically irreducible spanning trees, constrained complements of spanning trees, reducible configurations, perfect matchings, planar reductions, and SAT methods. Proven classes include Hamiltonian and traceable cubic graphs, plane cubic graphs, claw-free cubic graphs, and graphs with several restricted 2-factor structures.

The most relevant sources inspected are:

1. S. Akbari, T. R. Jensen, and M. Siggers, “Decompositions of graphs into trees, forests, and regular subgraphs,” *Discrete Mathematics* 338 (2015), 1322–1327.
2. K. Ozeki and D. Ye, “Decomposing plane cubic graphs,” *European Journal of Combinatorics* 52 (2016), 40–46.
3. A. Hoffmann-Ostenhof, T. Kaiser, and K. Ozeki, “Decomposing planar cubic graphs,” *J. Graph Theory* 88 (2018), 631–640.
4. K. S. Lyngsie and M. Merker, “Decomposing graphs into a spanning tree, an even graph, and a star forest,” *Electronic Journal of Combinatorics* 26 (2019), P1.33.
5. P. Li and W. Liu, “Decompositions of cubic traceable graphs,” *Discussiones Mathematicae Graph Theory* 40 (2020), 35–49.
6. Y. Hong, Q. Liu, and N. Yu, “Edge decomposition of connected claw-free cubic graphs,” *Discrete Applied Mathematics* 284 (2020), 246–250.
7. M. Xie, C. Zhou, and S. Zhou, “Decomposition of cubic graphs with a 2-factor consisting of three cycles,” *Discrete Mathematics* 343 (2020), 111839.
8. O. Bachtler and I. Heinrich, “Reductions for the 3-Decomposition Conjecture,” *Procedia Computer Science* 223 (2023), 1341–1348; arXiv:2104.15113.
9. O. Bachtler and S. O. Krumke, “Towards obtaining a 3-decomposition from a perfect matching,” *Electronic Journal of Combinatorics* 29 (2022), P4.23.
10. F. Protti and U. S. Souza, “Decycling a graph by the removal of a matching: new algorithmic and structural aspects in some classes of graphs,” *DMTCS* 20(2) (2018), Article 15.
11. G. Fan and C. Zhou, “Hoffmann-Ostenhof’s 3-Decomposition Conjecture,” *Discrete Mathematics* 348 (2025), Article 114454. This gives a quantitative relaxation with vertex-disjoint paths of length at most two.
12. T. Zhang and S. Szeider, “The 3-Decomposition Conjecture: A SAT-Based Approach with Specialized Propagators,” *CP 2025*, LIPIcs 340, Article 39. This verifies the conjecture through 28 vertices.
13. G. Fan, S. Guo, and C. Zhou, “The 3-decomposition conjecture of cubic graphs,” *Science China Mathematics* (2026), DOI 10.1007/s11425-025-2498-x. This further sharpens the bounded-number-of-\(P_2\) relaxation.

### Comparison with the present programme

The present work should not describe the cotree or the desire to minimize path components as new in itself. Its potentially new content is narrower:

- the integer potential \(b(T)\) as a rewrite height on the spanning-tree basis graph;
- the exact defect-edge identity \(|D(T)|=2b(T)\);
- the endpoint leaf-slide and tail-peel as universally non-increasing basis exchanges;
- the Monotone Exchange Conjecture, which asks for plateau escape from **every** spanning tree;
- the explicit failure of a fixed-cycle blossom-to-bridge lemma;
- the promise-preserving NP-completeness theorem for near-unicyclic matching decycling and its fixed-cycle corollary.

The hardness claim is adjacent to Protti–Souza, so the paper presents it as a constrained strengthening tailored to the one-defect repair problem, not as the first matching-decycling hardness result.

**Recommended novelty wording:**

> The tree/cotree viewpoint is classical. We propose a basis-exchange normalization framework, prove two safe exchanges, and isolate a fixed-cycle obstruction and complexity barrier that appear to be new.

## 3. Barnette’s Conjecture and two-tree colourings

### Classical and current context

For a Barnette graph \(G\), the dual is a simple Eulerian plane triangulation. The equivalence between a Hamiltonian cycle in \(G\) and a vertex partition of the dual into two induced trees is classical and must not be claimed as new. The literature includes dual colourings, reducible configurations, expansion operations, matching formulations, exact generation, and large computer-assisted proofs.

Sources inspected include:

1. D. A. Holton, B. Manvel, and B. D. McKay, “Hamiltonian cycles in cubic 3-connected bipartite planar graphs,” *J. Combin. Theory Ser. B* 38 (1985), 279–297.
2. J. Florek, “On Barnette’s conjecture,” *Discrete Mathematics* 310 (2010), 1531–1535.
3. X. Lu, “A note on Barnette’s conjecture,” *Discrete Mathematics* 312 (2012), 158–164.
4. H. Alt, M. S. Payne, J. M. Schmidt, and D. R. Wood, “Thoughts on Barnette’s conjecture,” *Australasian Journal of Combinatorics* 64 (2016), 354–365.
5. F. Kardoš, “A computer-assisted proof of the Barnette–Goodey conjecture: not only fullerene graphs are Hamiltonian,” *SIAM J. Discrete Math.* 34 (2020), 62–100.
6. J. Florek, “Remarks on Barnette’s conjecture,” *J. Combinatorial Optimization* 39 (2020), 149–155.
7. G. Brinkmann, J. Goedgebeur, and B. D. McKay, “The minimality of the Georges–Kelmans graph,” *Mathematics of Computation* 91 (2022), 1483–1500. Among its consequences is computational verification for Barnette graphs through 90 vertices.
8. M. Gorsky, R. Steiner, and S. Wiederrecht, “Matching theory and Barnette’s conjecture,” *Discrete Mathematics* 346 (2023), 113249.
9. M. A. Bekos, M. Kaufmann, and M. Pfister, “Approximating Barnette’s conjecture,” *Graph Drawing and Network Visualization 2025*, LIPIcs 357, Article 6.
10. T. Schnieders, “Barnette Graphs with Faces up to Size 8 are Hamiltonian,” arXiv:2508.03531 (2025). The proof includes a distinction of 339,068,624 cases.
11. S. Cambie, F. Dross, K. Knauer, H. La, and P. Valicov, “Partitions of planar (oriented) graphs into a connected acyclic and an independent set,” *Electronic Journal of Combinatorics* 33 (2026), P1.27, for related planar partition context.

### Comparison with the present programme

The identity

\[
\Phi=z(X)+2(t(X)-1)
\]

was not found in this exact form in the inspected sources. It is, however, an elementary Euler–Jordan reformulation and should be advertised as a useful exact potential, not as a deep resolution theorem. The new computational phenomenon is the complete failure of non-increasing connected one/two-face normalization on a verified 36-vertex example, together with universal escape on that example when connected triples are allowed. The resulting Three-Face Normalization Conjecture is substantially stronger than Barnette’s conjecture and remains open.

The archived six-mask claim for a 48-vertex example is inconsistent with its supplied graph and is excluded from verified evidence. This correction is important when comparing experimental scale with the literature.

**Recommended novelty wording:**

> We introduce an exact defect potential for the dual colouring landscape, exhibit a verified obstruction to radius-two monotone normalization, and formulate a radius-three normalization conjecture supported by finite exhaustive evidence.

## 4. Search strategy and limitations

Searches combined theorem names with the following concepts: quadratic discrepancy, multiplicity variance, balanced perfect-matching covers, coordinate descent, perfect-matching reconfiguration, colouring defect, regular defect, cotree path components, matroid basis exchange, spanning-tree local search, matching decyclability, fixed-cycle completion, two induced trees, Eulerian triangulation colourings, face flips, patch reconfiguration, and Barnette expansions.

The audit used publisher pages, DOI metadata, arXiv, DBLP/Dagstuhl proceedings, and references/citations from the closest papers. It does not replace:

- a MathSciNet and zbMATH review;
- checking unpublished theses and conference abstracts;
- direct consultation with specialists;
- independent referee verification of the proof repairs and complexity reduction.

Accordingly, the papers avoid “first” and “new” as categorical priority claims except where the statement is explicitly framed as “we introduce” and accompanied by “we are not aware of.”
