from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]


def test_supplied_manifest_files_exist():
    manifest = ROOT / "archive" / "SHA256SUMS_supplied.txt"
    assert manifest.exists()
    assert len([line for line in manifest.read_text().splitlines() if line.strip()]) >= 30


def test_reproduced_logs_present():
    expected = [
        ROOT / "repro_runs/scripts/bf_quadratic_checks.stdout",
        ROOT / "repro_runs/scripts/blossom_certificate.stdout",
        ROOT / "repro_runs/scripts/three_decomposition_exhaustive.stdout",
        ROOT / "repro_runs/scripts/combined_checks.stdout",
        ROOT / "berge_fulkerson/logs/j5res_reproduced.txt",
        ROOT / "barnette/logs/steps8res_reproduced.txt",
    ]
    assert all(path.exists() and path.stat().st_size for path in expected)
