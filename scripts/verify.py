#!/usr/bin/env python3
"""Read-only SHA-256 verification; no EFI mounting or installation."""
from pathlib import Path
import hashlib, sys
root = Path(__file__).resolve().parents[1]
failed = []
count = 0
for line in (root / "SHA256SUMS.txt").read_text().splitlines():
    expected, name = line.split("  ", 1)
    path = root / name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        failed.append(name)
    count += 1
print(f"Checked {count} files; mismatches: {len(failed)}")
for name in failed:
    print(name)
sys.exit(bool(failed))
