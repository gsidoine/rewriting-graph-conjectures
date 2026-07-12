"""JSON certificate helpers with deterministic serialization."""
from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib
import json


def dump_json(path: str | Path, payload: Any) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text())


def sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()
