import Mathlib

/-!
  A finite Boolean formulation of the C5 one-edge-swap obstruction.
  The proofs use `by decide`; no claim of local Lean compilation.
  Neither theorem proves the general Murty–Simon problem.
-/
namespace Erdos742C5

def edges : List (Nat × Nat) :=
  [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]

def adjacent (E : List (Nat × Nat)) (a b : Nat) : Bool :=
  E.any fun e =>
    (e.1 == a && e.2 == b) || (e.1 == b && e.2 == a)

def reachableWithinTwo (E : List (Nat × Nat)) (a b : Nat) : Bool :=
  a == b || adjacent E a b ||
    (List.range 5).any (fun w => adjacent E a w && adjacent E w b)

def diameterAtMostTwo (E : List (Nat × Nat)) : Bool :=
  (List.range 5).all fun a =>
    (List.range 5).all fun b => reachableWithinTwo E a b

def eraseEdge (E : List (Nat × Nat)) (a b : Nat) : List (Nat × Nat) :=
  E.filter fun e =>
    !((e.1 == a && e.2 == b) || (e.1 == b && e.2 == a))

def critical (E : List (Nat × Nat)) : Bool :=
  diameterAtMostTwo E &&
    E.all (fun e => !(diameterAtMostTwo (eraseEdge E e.1 e.2)))

def hasNontrivialSwap : Bool :=
  (List.range 5).any fun a =>
    (List.range 5).any fun b =>
      if decide (a < b) && adjacent edges a b then
        (List.range 5).any fun x =>
          (List.range 5).any fun y =>
            decide (x < y) && !adjacent edges x y &&
              diameterAtMostTwo ((eraseEdge edges a b) ++ [(x, y)])
      else false

theorem c5_is_critical : critical edges = true := by
  decide

theorem c5_has_no_single_edge_swap : hasNontrivialSwap = false := by
  decide

end Erdos742C5
