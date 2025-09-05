#!/usr/bin/env python3
import sys
from pathlib import Path

def rename_files(parent: Path):
    for sub in parent.iterdir():
        if not sub.is_dir():
            continue
        for f in sub.iterdir():
            if not f.is_file():
                continue
            new_name = f"{sub.name}{f.suffix.lower()}"
            target   = f.with_name(new_name)
            if target.exists():
                print(f"SKIP (would overwrite): {target}")
                continue
            f.rename(target)
            print(f"{f.name} → {target.name}")

def main():
    parent = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        input("Enter the parent folder path: ").strip('"')
    )
    parent = parent.expanduser().resolve()
    if not parent.is_dir():
        sys.exit("Not a valid folder.")
    rename_files(parent)

if __name__ == "__main__":
    main()
