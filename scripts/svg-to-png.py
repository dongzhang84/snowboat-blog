#!/usr/bin/env python3
"""
Convert SVG to PNG, handling CSS variables and prefers-color-scheme that
rsvg-convert doesn't support.

Usage:
    python3 scripts/svg-to-png.py path/to/diagram.svg [--width 1600]

Strips @media (prefers-color-scheme: dark) block and inlines :root
CSS variables using light-mode values, then shells out to rsvg-convert.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def preprocess(svg_text: str) -> str:
    root_match = re.search(r':root\s*\{([^}]*)\}', svg_text)
    if root_match:
        vars_block = root_match.group(1)
        var_map = dict(re.findall(r'--([\w-]+):\s*([^;]+?);', vars_block + ';'))
    else:
        var_map = {}

    out = re.sub(
        r'@media\s*\(prefers-color-scheme:\s*dark\)\s*\{[^{}]*\{[^}]*\}\s*\}',
        '',
        svg_text,
    )

    if var_map:
        out = re.sub(
            r'var\(--([\w-]+)\)',
            lambda m: var_map.get(m.group(1), m.group(0)),
            out,
        )

    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('svg', type=Path)
    parser.add_argument('-w', '--width', type=int, default=1600)
    parser.add_argument('-o', '--output', type=Path, default=None)
    args = parser.parse_args()

    src = args.svg.read_text()
    processed = preprocess(src)

    tmp = args.svg.with_suffix('.light.svg')
    tmp.write_text(processed)

    out = args.output or args.svg.with_suffix('.png')
    subprocess.run(
        ['rsvg-convert', '-w', str(args.width), '-o', str(out), str(tmp)],
        check=True,
    )
    tmp.unlink()
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
