#!/usr/bin/env python3
"""
make_banners.py - Generate 100% native vector SVG banners for SUDARSHNACHAND.
Features:
  - Left Panel (VISUAL.MAP): Pure vector dithered portrait of Sudarshan Chand (steady).
  - Right Panel (SYSTEM.INFO): Live terminal HUD attributes for DevOps Engineer role.
"""

from __future__ import annotations
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

def load_portrait_path() -> str:
    txt_file = ASSETS / "portrait-points.txt"
    if not txt_file.exists():
        return ""
    
    points = []
    with open(txt_file, "r", encoding="ascii") as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = line.split(",")
                points.append((int(x), int(y)))

    # Sort by Y then X
    unique = sorted(set(points), key=lambda p: (p[1], p[0]))
    chunks = []
    i = 0
    n = len(unique)
    while i < n:
        x0, y = unique[i]
        x1 = x0
        i += 1
        while i < n and unique[i][1] == y and unique[i][0] <= x1 + 1:
            x1 = unique[i][0]
            i += 1
        chunks.append(f"M{x0} {y}h{x1 - x0 + 1}")
    return "".join(chunks)

def generate_banner(theme: str, portrait_path_data: str) -> str:
    is_dark = (theme == "dark")
    
    if is_dark:
        bg = "#070c18"
        panel_bg = "#0a1122"
        border = "#1c2a44"
        text_dim = "#5a6e8c"
        text_norm = "#c8d6e5"
        text_bright = "#f1f5f9"
        accent = "#aa9bef"      # Neon Lavender
        cyan = "#22d3ee"        # Neon Cyan
        green = "#10b981"       # Mint Green
        grid_stroke = "#111c30"
    else:
        bg = "#f8fafc"
        panel_bg = "#ffffff"
        border = "#cbd5e1"
        text_dim = "#64748b"
        text_norm = "#334155"
        text_bright = "#0f172a"
        accent = "#0284c7"      # Sky Blue
        cyan = "#0f766e"        # Deep Teal
        green = "#16a34a"       # Emerald
        grid_stroke = "#e2e8f0"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="460" viewBox="0 0 1180 460" fill="none">
  <defs>
    <!-- Background Grid Pattern -->
    <pattern id="grid-{theme}" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_stroke}" stroke-width="0.8" opacity="0.7"/>
    </pattern>
  </defs>

  <style>
    @keyframes livePulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.3; }}
    }}

    .mono {{ font-family: "JetBrains Mono", Consolas, "Courier New", monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}

    .live-dot {{
      animation: livePulse 2s infinite ease-in-out;
    }}
  </style>

  <!-- Base Window Shell -->
  <rect width="1180" height="460" rx="14" fill="{bg}" stroke="{border}" stroke-width="1.5"/>
  <rect width="1180" height="460" rx="14" fill="url(#grid-{theme})"/>

  <!-- Window Header Bar -->
  <rect x="0" y="0" width="1180" height="42" rx="14" fill="{panel_bg}" opacity="0.9"/>
  <line x1="0" y1="42" x2="1180" y2="42" stroke="{border}" stroke-width="1.2"/>
  
  <!-- Window Controls -->
  <circle cx="28" cy="21" r="5.5" fill="#ef4444"/>
  <circle cx="46" cy="21" r="5.5" fill="#f59e0b"/>
  <circle cx="64" cy="21" r="5.5" fill="#10b981"/>

  <!-- Centered Title -->
  <text x="590" y="26" fill="{text_dim}" font-size="13" text-anchor="middle" class="mono">profile.sh --live</text>

  <!-- LEFT PANEL: VISUAL.MAP -->
  <g transform="translate(32, 60)">
    <!-- Header -->
    <text x="0" y="18" fill="{cyan}" font-size="13" font-weight="700" letter-spacing="1" class="mono">VISUAL.MAP</text>
    <text x="340" y="18" fill="{text_dim}" font-size="11" text-anchor="end" class="mono">300x340 / 1-BIT</text>

    <!-- Corner Brackets -->
    <path d="M 0 35 L 0 50 M 0 35 L 15 35" stroke="{cyan}" stroke-width="2" fill="none"/>
    <path d="M 340 35 L 340 50 M 340 35 L 325 35" stroke="{cyan}" stroke-width="2" fill="none"/>
    <path d="M 0 335 L 0 320 M 0 335 L 15 335" stroke="{cyan}" stroke-width="2" fill="none"/>
    <path d="M 340 335 L 340 320 M 340 335 L 325 335" stroke="{cyan}" stroke-width="2" fill="none"/>

    <!-- Content Area Background -->
    <rect x="8" y="42" width="324" height="286" rx="6" fill="{panel_bg}" opacity="0.6"/>

    <!-- PURE VECTOR DITHERED PORTRAIT (SUDARSHAN CHAND) -->
    <g>
      <path d="{portrait_path_data}" stroke="{accent}" stroke-width="1.1" fill="none"/>
      <text x="170" y="318" fill="{accent}" font-size="11" font-weight="600" text-anchor="middle" letter-spacing="1" class="mono">[ SUDARSHAN CHAND ]</text>
    </g>

    <text x="0" y="358" fill="{text_dim}" font-size="10" class="mono">PTS 18000 · FS/SERPENTINE</text>
  </g>

  <!-- RIGHT PANEL: SYSTEM.INFO -->
  <g transform="translate(420, 60)">
    <text x="0" y="18" fill="{cyan}" font-size="13" font-weight="700" letter-spacing="1" class="mono">SYSTEM.INFO</text>
    
    <g transform="translate(560, 6)">
      <circle cx="6" cy="9" r="4.5" fill="#ef4444" class="live-dot"/>
      <text x="18" y="13" fill="#ef4444" font-size="11" font-weight="700" class="mono">LIVE</text>
    </g>

    <g transform="translate(630, 2)">
      <rect width="105" height="22" rx="11" fill="{panel_bg}" stroke="{border}" stroke-width="1"/>
      <text x="52" y="15" fill="{accent}" font-size="11" font-weight="600" text-anchor="middle" class="mono">@SUDARSHNACHAND</text>
    </g>

    <line x1="0" y1="35" x2="735" y2="35" stroke="{border}" stroke-width="1"/>

    <g transform="translate(0, 58)" font-size="12.5" class="mono">
      <text x="0" y="0" fill="{text_dim}">Subject</text>
      <text x="150" y="0" fill="{border}">··············································</text>
      <text x="735" y="0" fill="{text_bright}" font-weight="700" text-anchor="end">Sudarshan Chand</text>

      <text x="0" y="24" fill="{text_dim}">Role</text>
      <text x="150" y="24" fill="{border}">··············································</text>
      <text x="735" y="24" fill="{accent}" font-weight="700" text-anchor="end">DevOps Engineer · Cloud Specialist</text>

      <text x="0" y="48" fill="{text_dim}">Origin</text>
      <text x="150" y="48" fill="{border}">··············································</text>
      <text x="735" y="48" fill="{text_norm}" text-anchor="end">India 🇮🇳</text>

      <text x="0" y="72" fill="{text_dim}">Status</text>
      <text x="150" y="72" fill="{border}">··············································</text>
      <text x="735" y="72" fill="{green}" font-weight="600" text-anchor="end">Automating + Orchestrating + Deploying</text>

      <text x="0" y="96" fill="{text_dim}">ToolChain</text>
      <text x="150" y="96" fill="{border}">··············································</text>
      <text x="735" y="96" fill="{text_bright}" text-anchor="end">Git · Jenkins · Docker · K8s · Terraform</text>

      <text x="0" y="120" fill="{text_dim}">Core.Cloud</text>
      <text x="150" y="120" fill="{border}">··············································</text>
      <text x="735" y="120" fill="#FF9900" font-weight="600" text-anchor="end">AWS (EC2 · EKS · S3 · IAM · VPC · Lambda)</text>

      <text x="0" y="144" fill="{text_dim}">Core.CI/CD</text>
      <text x="150" y="144" fill="{border}">··············································</text>
      <text x="735" y="144" fill="{cyan}" text-anchor="end">Jenkins Pipelines · GitHub Actions</text>

      <text x="0" y="168" fill="{text_dim}">Core.IaC</text>
      <text x="150" y="168" fill="{border}">··············································</text>
      <text x="735" y="168" fill="{text_bright}" text-anchor="end">Terraform · Ansible · Helm Charts</text>

      <text x="0" y="192" fill="{text_dim}">Core.Observ</text>
      <text x="150" y="192" fill="{border}">··············································</text>
      <text x="735" y="192" fill="{text_norm}" text-anchor="end">Prometheus · Grafana · CloudWatch</text>

      <text x="0" y="216" fill="{text_dim}">Core.Lang</text>
      <text x="150" y="216" fill="{border}">··············································</text>
      <text x="735" y="216" fill="{text_bright}" text-anchor="end">Python · Bash · JavaScript · Java</text>

      <text x="0" y="240" fill="{text_dim}">Core.Database</text>
      <text x="150" y="240" fill="{border}">··············································</text>
      <text x="735" y="240" fill="{text_norm}" text-anchor="end">MongoDB · MySQL</text>

      <text x="0" y="264" fill="{text_dim}">Grid.GitHub</text>
      <text x="150" y="264" fill="{border}">··············································</text>
      <text x="735" y="264" fill="{cyan}" text-anchor="end">SUDARSHNACHAND</text>
    </g>

    <!-- Bottom Status Line -->
    <line x1="0" y1="340" x2="735" y2="340" stroke="{border}" stroke-width="1"/>
    <g transform="translate(0, 358)" font-size="11" class="mono">
      <circle cx="5" cy="-3" r="3.5" fill="{green}"/>
      <text x="16" y="0" fill="{green}" font-weight="600">ALL SYSTEMS NOMINAL</text>
      <text x="735" y="0" fill="{text_dim}" text-anchor="end">UTC+5:30 · ASIA/KOLKATA NODE</text>
    </g>
  </g>
</svg>'''
    return svg

def main():
    print("Loading portrait points...")
    portrait_path_data = load_portrait_path()
    print(f"Portrait path loaded ({len(portrait_path_data)} chars).")

    for theme in ("dark", "light"):
        svg = generate_banner(theme, portrait_path_data)
        out_file = ASSETS / f"banner-{theme}.svg"
        out_file.write_text(svg, encoding="utf-8")
        
        # Verify XML validity!
        ET.fromstring(svg)
        print(f"Validated and generated {out_file} ({len(svg) // 1024} KB)")

if __name__ == "__main__":
    main()
