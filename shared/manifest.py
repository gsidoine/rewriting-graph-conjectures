"""Create a SHA-256 manifest for the active checkout (not historical snapshots)."""
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parents[1]
out=root/'docs/sha256_current_tree_2026-10-08.txt'
paths=sorted(p for p in root.rglob('*') if p.is_file()
             and p!=out and '.git' not in p.relative_to(root).parts
             and '__pycache__' not in p.parts and '.pytest_cache' not in p.parts
             and not p.name.endswith('.pyc')
             and 'build' not in p.relative_to(root).parts
             and not any(v.endswith('.egg-info') for v in p.relative_to(root).parts))
out.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(root).as_posix()+'\n' for p in paths))
print(f'Wrote {len(paths)} checksums to {out.relative_to(root)}')
