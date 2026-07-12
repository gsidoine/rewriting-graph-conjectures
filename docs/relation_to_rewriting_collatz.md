# Relation to the Rewriting-Collatz Programme

This project was directly inspired by the research architecture of:

- Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule, *An Automated Approach to the Collatz Conjecture*;
- the companion repository [`emreyolcu/rewriting-collatz`](https://github.com/emreyolcu/rewriting-collatz).

That work encodes Collatz-like dynamics as formal string-rewriting systems, develops an automated termination prover, and uses matrix interpretations and SAT solving to find termination proofs for nontrivial variants.

The present project transfers the **research strategy**, not the literal formalism. Its graph-theoretic states are sextuples of perfect matchings, spanning trees, or dual colourings. Its local moves are matching replacements, basis exchanges, or connected patch flips. These are not claimed to be term- or string-rewriting systems in the technical automated-reasoning sense.

The common pattern is:

1. enrich the original object with a certificate state;
2. define an exact defect or ranking quantity;
3. distinguish strict descent from neutral plateau motion;
4. study relative termination of the induced rewrite graph;
5. automate finite rule testing and reverse reachability;
6. extract counterexamples and structural obstructions from failed normalization;
7. redesign the rule system and repeat.

This methodological distinction is important both mathematically and for publication: the current graph papers are primarily graph theory and experimental/computational mathematics, whereas the Collatz paper makes a direct contribution to automated reasoning through formal rewriting, termination methods, a dedicated prover, and SAT-based proof search.
