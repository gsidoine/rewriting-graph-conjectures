# Independent Audit Report

## Scope

The audit covered every supplied `.tex`, `.ipynb`, `.cpp`, `.txt`, and Markdown file; compared duplicate versions by SHA-256; extracted executable notebook cells; reran the feasible exact computations; checked theorem dependencies; rebuilt the manuscripts; and reviewed the closest literature available through 12 July 2026.

## File reconciliation

The duplicate copies of `barnette_big`, `barnette_results`, `bfr_results_all`, and the Berge–Fulkerson theorem notebook are byte-for-byte identical.  One canonical copy is used in the programme directories, while every original remains immutable under `archive/original_files/`.  Exact hashes are in `archive/SHA256SUMS_supplied.txt`.

## Proof corrections

### Berge–Fulkerson cyclic barrier

The supplied proof correctly identifies the relative-interior mechanism but jumps from excluding `Q=2n` to a six-unit improvement when `n` is divisible by six.  The corrected argument fixes an index `i`: equality `S_i=n/3` alone makes `x=1/3` minimize `w_i` at a relative-interior point, forcing `w_i` to be constant on the perfect-matching polytope and yielding the impossible value `1/3` on every edge.  Therefore every integer `S_i` is at most `n/3-1`; summing over six coordinates gives `Q<=2n-6`.

### 3-Decomposition safe exchanges

The original leaf-slide and tail-peel proofs were mathematically plausible but compressed.  The audited paper tracks the affected cotree component and the cotree degree of the receiving vertex, including the case where both ends lie in the same bad path.  These additions remove ambiguity about accidental component creation.

### NP-completeness source promise

The source problem is NP-complete for Hamiltonian fairly cubic graphs with two degree-two terminals.  The new reduction needs a Hamiltonian cycle to construct the supplied near-unicyclic matching.  The cited source construction explicitly produces such a cycle, so the strengthened promise is valid for the reduction family.  The audited statement says this directly instead of attributing the stronger theorem verbatim to the source.

### Barnette identity scope

`psi` is defined only for nonempty induced subgraphs, and the topological proof assumes a nontrivial colouring.  The audited theorem is restricted accordingly.  The statement “arbitrary binary colourings” was removed.

## Computational reruns

Fresh exact outputs are archived under `repro_runs/` and the programme `logs/` directories.

| Check | Fresh result |
|---|---|
| Berge–Fulkerson algebra | All four edgewise indicator cases and aggregate identities passed. |
| Petersen state space | 6 perfect matchings; 462 states; all normalize. |
| Flower snark `J5` | 32 perfect matchings; 2,324,784 states; 132 targets; zero unresolved. |
| 3-Decomposition through order 10 | 27 classes; 30,619 spanning trees; zero terminal positive plateau. |
| 16-vertex obstruction | All structural checks and exhaustive matching counts reproduced. |
| Barnette cube identity | All 62 nontrivial dual colourings passed. |
| Barnette 36-vertex trap | Complete reverse reachability over all \(2^{20}\) dual colourings leaves exactly six radius-two traps and zero radius-three traps. |
| Barnette selected batch | Historical `steps8res` reproduced exactly. |
| Historical 48-vertex masks | Failed consistency check against supplied graph; demoted to historical/inconsistent. |

## Build audit

Every supplied LaTeX file compiled successfully under repeated `latexmk` passes. The three audited manuscripts compile to 6, 6, and 5 pages, respectively. No unresolved citation or internal-reference marker remains in the audited PDFs. The repository Makefile and CI use `latexmk`, preventing the original single-pass `?` problem. Final PDFs were rendered page-by-page and visually inspected for clipping, overlaps, and broken glyphs.

## Publication assessment

- **Berge–Fulkerson paper:** strongest manuscript.  The universal descent theorem is clean and potentially publishable after external specialist review.  The cyclic barrier should receive particular scrutiny because it uses the affine hull of the perfect-matching polytope.
- **3-Decomposition paper:** potentially publishable as a structural/computational and complexity paper after an external complexity reviewer checks the promise-preserving reduction.
- **Barnette paper:** a research note or experimental paper, not yet a theorem-led resolution.  The inconsistent 48-vertex certificate must remain excluded; the 36-vertex and selected-batch evidence are retained.

No manuscript should be advertised as solving its headline conjecture.
