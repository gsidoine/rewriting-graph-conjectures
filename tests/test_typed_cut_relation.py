"""Regression test for the exact component-enriched typed 3-cut product."""
from pathlib import Path
import runpy


def test_component_enriched_three_cut_quotient():
    script = (Path(__file__).resolve().parents[1]
              / "repro_runs" / "verify_typed_cut_quotient.py")
    audit = runpy.run_path(str(script))
    audit["verify_all"]()
