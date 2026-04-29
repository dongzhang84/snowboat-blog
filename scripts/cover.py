#!/usr/bin/env python3
"""
生成封面图 · typography-dark 风格（黑底 + 第一行白 + 第二行橙 + 可选第三行灰）

用法：
    python3 scripts/cover.py <slug> "第一行文字" "第二行文字" ["第三行文字"]

例：
    python3 scripts/cover.py three-claude-skills \\
        "每个人都应该使用的" \\
        "三个最有用的 Claude Skill"

    python3 scripts/cover.py ai-why-coding \\
        "两万字科普" \\
        "AI 为什么会编程" \\
        "原理、历史与未来"

输出：cover-image/<slug>/cover.png
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_INDEX = 2
W, H = 2400, 1350
BG = (0, 0, 0)
C1 = (245, 245, 245)
C2 = (242, 107, 44)
C3 = (245, 245, 245)


def render(slug, line1, line2, line3=None):
    out = Path("cover-image") / slug / "cover.png"
    out.parent.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    max_w = int(W * 0.88)
    size = 100
    while size < 700:
        f = ImageFont.truetype(FONT_PATH, size, index=FONT_INDEX)
        if max(draw.textlength(line1, font=f), draw.textlength(line2, font=f)) >= max_w:
            break
        size += 10
    size -= 10
    font = ImageFont.truetype(FONT_PATH, size, index=FONT_INDEX)

    size3 = int(size * 0.45)
    font3 = ImageFont.truetype(FONT_PATH, size3, index=FONT_INDEX) if line3 else None

    w1, w2 = draw.textlength(line1, font=font), draw.textlength(line2, font=font)
    b1 = draw.textbbox((0, 0), line1, font=font)
    b2 = draw.textbbox((0, 0), line2, font=font)
    h1, h2 = b1[3] - b1[1], b2[3] - b2[1]
    gap = int(size * 0.22)

    if line3:
        w3 = draw.textlength(line3, font=font3)
        b3 = draw.textbbox((0, 0), line3, font=font3)
        h3 = b3[3] - b3[1]
        gap3 = int(size * 0.55)
        total_h = h1 + gap + h2 + gap3 + h3
    else:
        total_h = h1 + gap + h2

    y = (H - total_h) // 2 - int(size * 0.05)
    x_main = (W - max(w1, w2)) // 2

    draw.text((x_main, y), line1, font=font, fill=C1)
    draw.text((x_main, y + h1 + gap), line2, font=font, fill=C2)

    if line3:
        x3 = (W - w3) // 2
        draw.text((x3, y + h1 + gap + h2 + gap3), line3, font=font3, fill=C3)

    img.save(out, "PNG", optimize=True)
    print(f"saved: {out}  ({out.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    if len(sys.argv) not in (4, 5):
        print(__doc__)
        sys.exit(1)
    render(*sys.argv[1:])
