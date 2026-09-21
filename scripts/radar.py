#!/usr/bin/env python3
"""
radar.py - render a spider / radar chart as a standalone SVG. Python standard library only.

Usage:
    python scripts/radar.py --data assets/skills.json -o assets/radar
    python scripts/radar.py --data assets/langmix.json -o assets/radar-langs --values
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

THEMES = {
    "dark": {
        "grid": "#30363d",
        "spoke": "#21262d",
        "label": "#c9d1d9",
        "value": "#8b949e",
        "title": "#e6edf3",
        "fill": "#aa9bef",
        "stroke": "#7ee787",
        "vertex": "#aa9bef",
        "bg": "none",
    },
    "light": {
        "grid": "#d0d7de",
        "spoke": "#e6eaef",
        "label": "#1f2328",
        "value": "#57606a",
        "title": "#1f2328",
        "fill": "#2da44e",
        "stroke": "#1a7f37",
        "vertex": "#116329",
        "bg": "none",
    },
}

def render_svg(title: str, axes: list[tuple[str, float]], theme: dict, show_values: bool = False) -> str:
    w, h = 420, 370
    cx, cy = w / 2, (h / 2) + 12
    radius = 115
    n = len(axes)
    angle_step = 2 * math.pi / n

    # Concentric rings (25%, 50%, 75%, 100%)
    rings_svg = []
    for level in [0.25, 0.5, 0.75, 1.0]:
        pts = []
        for i in range(n):
            a = i * angle_step - math.pi / 2
            r = radius * level
            pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
        rings_svg.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{theme["grid"]}" stroke-width="1" stroke-dasharray="3 3"/>')

    # Spokes, labels, and data points
    spokes_svg = []
    labels_svg = []
    poly_pts = []
    vertices_svg = []

    for i, (label, val) in enumerate(axes):
        a = i * angle_step - math.pi / 2
        cos_a, sin_a = math.cos(a), math.sin(a)

        # Spoke line
        spokes_svg.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + radius * cos_a:.1f}" y2="{cy + radius * sin_a:.1f}" stroke="{theme["spoke"]}" stroke-width="1"/>')

        # Data point
        r_val = radius * (min(max(val, 0), 100) / 100.0)
        px, py = cx + r_val * cos_a, cy + r_val * sin_a
        poly_pts.append(f"{px:.1f},{py:.1f}")
        vertices_svg.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="{theme["vertex"]}"/>')

        # Text label position
        lx = cx + (radius + 26) * cos_a
        ly = cy + (radius + 18) * sin_a
        anchor = "middle" if abs(cos_a) < 0.25 else ("start" if cos_a > 0 else "end")
        val_text = f" ({int(val)}%)" if show_values else ""
        labels_svg.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" fill="{theme["label"]}" font-size="11.5" font-weight="500" '
            f'text-anchor="{anchor}" dominant-baseline="central">{label}{val_text}</text>'
        )

    polygon_svg = (
        f'<polygon points="{" ".join(poly_pts)}" fill="{theme["fill"]}" fill-opacity="0.22" '
        f'stroke="{theme["stroke"]}" stroke-width="2.2"/>'
    )
    title_svg = (
        f'<text x="{cx}" y="26" fill="{theme["title"]}" font-size="14.5" font-weight="600" '
        f'text-anchor="middle" letter-spacing="0.5">{title}</text>'
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <style>
    text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
  </style>
  {title_svg}
  {''.join(rings_svg)}
  {''.join(spokes_svg)}
  {polygon_svg}
  {''.join(vertices_svg)}
  {''.join(labels_svg)}
</svg>'''

def main():
    parser = argparse.ArgumentParser(description="Generate radar charts for GitHub profile")
    parser.add_argument("--data", required=True, type=Path, help="Path to JSON data file")
    parser.add_argument("-o", "--out", required=True, help="Base output path (without -dark.svg/-light.svg)")
    parser.add_argument("--values", action="store_true", help="Display percentage numbers next to labels")
    args = parser.parse_args()

    data = json.loads(args.data.read_text(encoding="utf-8"))
    title = data.get("title", "Radar Chart")
    axes = [(item["label"], float(item["value"])) for item in data["axes"]]

    for mode in ("dark", "light"):
        svg = render_svg(title, axes, THEMES[mode], show_values=args.values)
        out_path = Path(f"{args.out}-{mode}.svg")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(svg, encoding="utf-8")
        print(f"Generated {out_path}")

if __name__ == "__main__":
    main()
