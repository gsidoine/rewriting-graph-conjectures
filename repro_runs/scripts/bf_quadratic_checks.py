
# --- notebook cell 1 ---
import sympy as sp
import pandas as pd

n, Q = sp.symbols("n Q", integer=True, nonnegative=True)
d = sp.symbols("d", integer=True)

remove_delta = sp.expand((d - 1)**2 - d**2)

print("Removing an incident matching edge changes d^2 by:", remove_delta)

# --- notebook cell 3 ---
# Verify the edgewise replacement identity for the four binary membership cases.
I, J = sp.symbols("I J", integer=True)
for i_value in (0, 1):
    for j_value in (0, 1):
        direct = sp.expand(
            (d - i_value + j_value)**2 - d**2
        )
        proposed = sp.expand(
            i_value * (-2*d + 1)
            + j_value * (2*d + 1 - 2*i_value)
        )
        assert sp.expand(direct - proposed) == 0

print("Edgewise replacement identity verified in all four binary cases.")

# --- notebook cell 5 ---
S = sp.symbols("S", real=True)
assert sp.simplify(
    sp.solve(sp.Eq(2*S - n/2, n/6), S)[0] - n/3
) == 0

m = sp.symbols("m")
assert sp.expand(
    m*(m-2) - ((m-2)**2 + 2*(m-2))
) == 0

print("Coordinate bound and summation identity verified.")

# --- notebook cell 7 ---
triples = [
    (a, b, 6-a-b)
    for a in range(7)
    for b in range(7-a)
]
values = [
    ((a-2)**2 + (b-2)**2 + (c-2)**2, (a,b,c))
    for a,b,c in triples
]
maximum = max(values)
print("Maximum vertex contribution:", maximum)
assert maximum[0] == 24

# --- notebook cell 9 ---
def sharp_barrier(n_value):
    if n_value % 2:
        raise ValueError("A cubic graph has even order.")
    if n_value % 6 == 0:
        return 2*n_value - 6
    if n_value % 6 == 2:
        return 2*n_value - 4
    return 2*n_value - 2

table = pd.DataFrame(
    {
        "n mod 6": [0, 2, 4],
        "local-minimum upper bound": ["2n-6", "2n-4", "2n-2"],
    }
)
table
