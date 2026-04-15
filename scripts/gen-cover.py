#!/usr/bin/env python3
"""
Generate cover images using Gemini 2.5 Flash Image (nano-banana).

Usage:
    python scripts/gen-cover.py cover-images/cursor-290亿/prompts/cover-cinematic.md
    python scripts/gen-cover.py cover-images/cursor-290亿/prompts/cover-square.md

Reads GEMINI_API_KEY from .env.local at the project root.
Writes the PNG next to the prompt file's parent directory as cover-{aspect-slug}.png.

Requires: pip install google-genai pillow
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_env_local() -> None:
    env_path = ROOT / ".env.local"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


def parse_prompt_file(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    meta: dict = {}
    body = text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body.strip()


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    prompt_file = Path(sys.argv[1]).resolve()
    if not prompt_file.exists():
        print(f"ERROR: prompt file not found: {prompt_file}", file=sys.stderr)
        return 1

    load_env_local()
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        print("ERROR: GEMINI_API_KEY is empty. Put it in .env.local", file=sys.stderr)
        return 1

    meta, body = parse_prompt_file(prompt_file)
    aspect = meta.get("aspect", "16:9")
    model = meta.get("model", "gemini-2.5-flash-image")

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    aspect_slug = aspect.replace(":", "x").replace(".", "_")
    out_dir = prompt_file.parent.parent
    stem = prompt_file.stem
    if stem.startswith("cover-"):
        out_file = out_dir / f"{stem.replace('cover-', 'cover-')}-{aspect_slug}.png"
    else:
        out_file = out_dir / f"{stem}-{aspect_slug}.png"
    if out_file.exists():
        backup = out_file.with_suffix(".bak.png")
        out_file.rename(backup)
        print(f"backed up existing → {backup.name}")

    print(f"model:  {model}")
    print(f"aspect: {aspect}")
    print(f"output: {out_file}")
    print("generating ...")

    response = client.models.generate_content(
        model=model,
        contents=body,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=aspect),
        ),
    )

    saved = False
    for part in response.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            out_file.write_bytes(part.inline_data.data)
            saved = True
            break

    if not saved:
        print("ERROR: no image returned from model", file=sys.stderr)
        return 1

    print(f"done → {out_file.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
