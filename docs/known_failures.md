# Known Failures, Disproofs, and Non-Reproducible Claims

## Fixed-cycle blossom-to-bridge lemma — false

The 16-vertex graph

```text
O??DQ?[C?AaAA?@O??wGS
```

has the promised near-unicyclic matching but no matching whose complement is a tree, while every bridge has leaves on both sides.  The fixed-cycle structural lemma is therefore disproved.

## Barnette radius two — inadequate

The verified 36-vertex certificate shows that a connected three-face plateau move can be necessary before a strict decrease.  This refutes the proposed universal one/two-face rule family, not Barnette's conjecture.

## Historical 48-vertex mask file — inconsistent

The six decimal masks in `step10_unresolved_historical.txt` were described as pair-flip traps for `step10.txt`.  Direct evaluation on that graph gives potentials

```text
14, 20, 18, 18, 20, 14
```

and many non-increasing one/pair successors outside the six masks.  Possible causes include an unarchived vertex permutation, a mismatched graph version, or a mislabeled output column.  Without the missing mapping, this certificate is unusable.

## Large historical runs

Several logs report millions or more than one hundred million states.  They are evidence of prior runs but are not upgraded to independently reproducible results unless the exact generator, inputs, and verifier were reconstructed and rerun.

## No headline conjecture solved

The strongest results delimit obstruction regions or rule out restricted proof strategies.  Berge–Fulkerson, 3-Decomposition, Barnette, and Tutte 5-Flow remain open in this repository.
