"""Quantum Theory home-screen icon and favicon. Run: python build_icons.py"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = Path(__file__).resolve().parent
SIZE = 180
S = SIZE / 120.0


def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def lerp_rgb(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return tuple(int(x + (y - x) * t) for x, y in zip(a, b))


def bg_at(gx: float, gy: float) -> tuple[int, int, int]:
    d = (100.0, -100.0)
    v = (gx - 10.0, gy - 110.0)
    denom = d[0] ** 2 + d[1] ** 2
    t = max(0.0, min(1.0, (v[0] * d[0] + v[1] * d[1]) / denom))
    c0, c45, c1 = hex_rgb("0c1638"), hex_rgb("2d1b69"), hex_rgb("0e4a6e")
    if t < 0.5:
        return lerp_rgb(c0, c45, t / 0.5)
    return lerp_rgb(c45, c1, (t - 0.5) / 0.5)


def load_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    names = ["segoeuib.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"]
    for name in names:
        try:
            return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_interference(draw: ImageDraw.ImageDraw, cx: float, cy: float, t: float) -> None:
    """Two-slit style ripples behind the psi symbol."""
    for ring in range(1, 9):
        r = ring * 11 * S + 4 * math.sin(t + ring * 0.7)
        alpha = max(12, 90 - ring * 10)
        col = (56, 189, 248, alpha) if ring % 2 else (167, 139, 250, alpha)
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=col, width=max(1, int(1.2 * S)))


def draw_wave_glow(draw: ImageDraw.ImageDraw) -> None:
  w = max(2, int(2.4 * S))
  pts = []
  for i in range(121):
    x = 8 * S + i * S
    y = 62 * S + 14 * S * math.sin(i / 120 * math.pi * 4)
    pts.append((x, y))
  for i in range(len(pts) - 1):
    t = i / max(1, len(pts) - 2)
    col = lerp_rgb(hex_rgb("22d3ee"), hex_rgb("c084fc"), t) + (200,)
    draw.line([pts[i], pts[i + 1]], fill=col, width=w, joint="curve")


def build_apple_touch_icon() -> None:
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            gx = (x + 0.5) / S
            gy = (y + 0.5) / S
            r, g, b = bg_at(gx, gy)
            px[x, y] = (r, g, b, 255)

    mask = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, SIZE - 1, SIZE - 1), radius=int(28 * S), fill=255)
    img.putalpha(mask)

    glow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = 60 * S, 58 * S
    draw_interference(gd, cx, cy, 0.0)
    glow = glow.filter(ImageFilter.GaussianBlur(int(1.1 * S)))
    img = Image.alpha_composite(img, glow)

    layer = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw_wave_glow(draw)

    font_psi = load_font(max(14, int(52 * S)))
    psi = "\u03c8"
    bbox = draw.textbbox((0, 0), psi, font=font_psi)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = cx - tw / 2 - bbox[0]
    ty = cy - th / 2 - bbox[1] + 2 * S
    draw.text((tx + 1, ty + 1), psi, font=font_psi, fill=(8, 20, 48, 220))
    draw.text((tx, ty), psi, font=font_psi, fill=(224, 242, 255, 255))

    bar_w = int(34 * S)
    bar_h = max(2, int(3 * S))
    bx = cx - bar_w / 2
    by = ty + th + 6 * S
    for i in range(bar_w):
      t = i / max(1, bar_w - 1)
      col = lerp_rgb(hex_rgb("34d399"), hex_rgb("38bdf8"), t)
      h = bar_h * (0.35 + 0.65 * (0.5 + 0.5 * math.sin(t * math.pi * 3)))
      draw.rectangle((bx + i, by + bar_h - h, bx + i + 1.2, by + bar_h), fill=col + (255,))

    img = Image.alpha_composite(img, layer)
    out = BASE / "apple-touch-icon.png"
    img.save(out, "PNG", optimize=True)
    print("Wrote", out)


def build_favicon_svg() -> None:
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0c1638"/>
      <stop offset="50%" stop-color="#2d1b69"/>
      <stop offset="100%" stop-color="#0e4a6e"/>
    </linearGradient>
    <linearGradient id="wave" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#22d3ee"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>
  <rect width="32" height="32" rx="7" fill="url(#bg)"/>
  <path d="M4 18 Q8 12 12 18 T20 18 T28 18" fill="none" stroke="url(#wave)" stroke-width="2" stroke-linecap="round" opacity="0.85"/>
  <text x="16" y="21" text-anchor="middle" font-family="Segoe UI, system-ui, sans-serif" font-size="14" font-weight="700" fill="#f0f9ff">&#x3c8;</text>
</svg>
"""
    out = BASE / "favicon.svg"
    out.write_text(svg, encoding="utf-8")
    print("Wrote", out)


if __name__ == "__main__":
    build_apple_touch_icon()
    build_favicon_svg()
