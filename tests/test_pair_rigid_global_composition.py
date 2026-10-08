"""Regression tests execute the standalone mixed K3,3/Petersen exhaustive enumerator."""
from repro_runs.verify_mixed_pair_rigid import check

def test_k33_petersen():
    check("KP")

def test_petersen_k33():
    check("PK")

def test_petersen_petersen():
    check("PP")

def test_k33_cube_nonrigid():
    check("KC")

def test_petersen_cube_nonrigid():
    check("PC")
