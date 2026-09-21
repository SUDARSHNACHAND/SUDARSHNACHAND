#!/usr/bin/env python3
"""
make_banners.py - Generate animated terminal HUD profile banners for SUDARSHNACHAND.
Cycles through:
  1. Dithered Portrait (Sudarshan Chand)
  2. DevOps Infinity Cycle Animation
  3. AWS Cloud Architecture Animation
"""

from __future__ import annotations
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

def get_b64(path: Path) -> str:
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode("ascii")
    return ""

def generate_banner(theme: str) -> str:
    is_dark = (theme == "dark")
    
    # Palette definition
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
        dot_color = "#aa9bef"
        glow = "rgba(170, 155, 239, 0.45)"
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
        dot_color = "#0284c7"
        glow = "rgba(2, 132, 199, 0.3)"

    portrait_b64 = get_b64(ASSETS / f"portrait-{theme}.png")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="460" viewBox="0 0 1180 460" fill="none">
  <defs>
    <!-- Background Grid Pattern -->
    <pattern id="grid-{theme}" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{grid_stroke}" stroke-width="0.8" opacity="0.7"/>
    </pattern>

    <!-- Linear Gradients -->
    <linearGradient id="infGrad-{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{cyan}"/>
      <stop offset="50%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{green}"/>
    </linearGradient>

    <linearGradient id="awsGrad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF9900"/>
      <stop offset="100%" stop-color="#FF5500"/>
    </linearGradient>
  </defs>

  <style>
    @keyframes cycleFrame1 {{
      0% {{ opacity: 0; transform: scale(0.98); }}
      3%, 30% {{ opacity: 1; transform: scale(1); }}
      33%, 100% {{ opacity: 0; transform: scale(0.98); }}
    }}
    @keyframes cycleFrame2 {{
      0%, 33% {{ opacity: 0; transform: scale(0.98); }}
      36%, 63% {{ opacity: 1; transform: scale(1); }}
      66%, 100% {{ opacity: 0; transform: scale(0.98); }}
    }}
    @keyframes cycleFrame3 {{
      0%, 66% {{ opacity: 0; transform: scale(0.98); }}
      69%, 96% {{ opacity: 1; transform: scale(1); }}
      100% {{ opacity: 0; transform: scale(0.98); }}
    }}

    @keyframes flowInfinity {{
      0% {{ stroke-dashoffset: 0; }}
      100% {{ stroke-dashoffset: -360; }}
    }}
    @keyframes pulseGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 4px {glow}); transform: scale(1); }}
      50% {{ filter: drop-shadow(0 0 12px {glow}); transform: scale(1.02); }}
    }}
    @keyframes livePulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.3; }}
    }}

    .mono {{ font-family: "JetBrains Mono", Consolas, "Courier New", monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}

    .frame-pic {{ animation: cycleFrame1 15s infinite ease-in-out; transform-origin: 200px 250px; }}
    .frame-devops {{ animation: cycleFrame2 15s infinite ease-in-out; transform-origin: 200px 250px; }}
    .frame-aws {{ animation: cycleFrame3 15s infinite ease-in-out; transform-origin: 200px 250px; }}

    .inf-flow {{
      stroke-dasharray: 18 12;
      animation: flowInfinity 4s linear infinite;
    }}
    .pulse-elem {{
      animation: pulseGlow 3s ease-in-out infinite;
      transform-origin: 200px 240px;
    }}
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

  <!-- ============================================================== -->
  <!-- LEFT PANEL: VISUAL.MAP (340 x 380)                             -->
  <!-- ============================================================== -->
  <g transform="translate(32, 60)">
    <!-- Header -->
    <text x="0" y="18" fill="{cyan}" font-size="13" font-weight="700" letter-spacing="1" class="mono">VISUAL.MAP</text>
    <text x="340" y="18" fill="{text_dim}" font-size="11" text-anchor="end" class="mono">300×340 / 1-BIT</text>

    <!-- Corner Brackets -->
    <!-- Top-Left -->
    <path d="M 0 35 L 0 50 M 0 35 L 15 35" stroke="{cyan}" stroke-width="2" fill="none"/>
    <!-- Top-Right -->
    <path d="M 340 35 L 340 50 M 340 35 L 325 35" stroke="{cyan}" stroke-width="2" fill="none"/>
    <!-- Bottom-Left -->
    <path d="M 0 335 L 0 320 M 0 335 L 15 335" stroke="{cyan}" stroke-width="2" fill="none"/>
    <!-- Bottom-Right -->
    <path d="M 340 335 L 340 320 M 340 335 L 325 335" stroke="{cyan}" stroke-width="2" fill="none"/>

    <!-- Content Area Background -->
    <rect x="8" y="42" width="324" height="286" rx="6" fill="{panel_bg}" opacity="0.6"/>

    <!-- ------------------------------------------------------------ -->
    <!-- FRAME 1: DITHERED PORTRAIT OF SUDARSHAN CHAND                -->
    <!-- ------------------------------------------------------------ -->
    <g class="frame-pic">
      <image href="data:image/png;base64,{portrait_b64}" x="40" y="44" width="260" height="282" preserveAspectRatio="xMidYMid slice"/>
      <text x="170" y="318" fill="{accent}" font-size="11" font-weight="600" text-anchor="middle" letter-spacing="1" class="mono">[ SUDARSHAN CHAND ]</text>
    </g>

    <!-- ------------------------------------------------------------ -->
    <!-- FRAME 2: DEVOPS CYCLE INFINITY LOOP ANIMATION                -->
    <!-- ------------------------------------------------------------ -->
    <g class="frame-devops pulse-elem">
      <!-- Outer/Inner Infinity loop curves -->
      <!-- Smooth lemniscate path centered at x=170, y=185 -->
      <path d="M 90,185 C 90,135 140,135 170,185 C 200,235 250,235 250,185 C 250,135 200,135 170,185 C 140,235 90,235 90,185 Z" 
            stroke="{border}" stroke-width="12" fill="none" stroke-linecap="round"/>
      
      <!-- Flowing neon stream -->
      <path d="M 90,185 C 90,135 140,135 170,185 C 200,235 250,235 250,185 C 250,135 200,135 170,185 C 140,235 90,235 90,185 Z" 
            stroke="url(#infGrad-{theme})" stroke-width="6" fill="none" stroke-linecap="round" class="inf-flow"/>

      <!-- DevOps Phase Nodes -->
      <!-- Plan (Top-Left) -->
      <circle cx="112" cy="148" r="5" fill="{cyan}"/>
      <text x="112" y="136" fill="{text_bright}" font-size="9" font-weight="700" text-anchor="middle" class="mono">PLAN</text>

      <!-- Build (Bottom-Left) -->
      <circle cx="112" cy="222" r="5" fill="{cyan}"/>
      <text x="112" y="240" fill="{text_bright}" font-size="9" font-weight="700" text-anchor="middle" class="mono">BUILD</text>

      <!-- Deploy (Top-Right) -->
      <circle cx="228" cy="148" r="5" fill="{green}"/>
      <text x="228" y="136" fill="{text_bright}" font-size="9" font-weight="700" text-anchor="middle" class="mono">DEPLOY</text>

      <!-- Operate/Monitor (Bottom-Right) -->
      <circle cx="228" cy="222" r="5" fill="{green}"/>
      <text x="228" y="240" fill="{text_bright}" font-size="9" font-weight="700" text-anchor="middle" class="mono">MONITOR</text>

      <!-- Center Logo & Label -->
      <circle cx="170" cy="185" r="14" fill="{panel_bg}" stroke="{accent}" stroke-width="2"/>
      <text x="170" y="189" fill="{accent}" font-size="10" font-weight="800" text-anchor="middle" class="mono">CI/CD</text>

      <!-- Bottom Tag -->
      <text x="170" y="285" fill="{cyan}" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1.5" class="mono">DEVOPS LIFECYCLE</text>
      <text x="170" y="305" fill="{text_dim}" font-size="10" text-anchor="middle" class="mono">CONTINUOUS INTEGRATION &amp; DEPLOY</text>
    </g>

    <!-- ------------------------------------------------------------ -->
    <!-- FRAME 3: AWS CLOUD ARCHITECTURE ANIMATION                    -->
    <!-- ------------------------------------------------------------ -->
    <g class="frame-aws pulse-elem">
      <!-- Stylized AWS Cloud -->
      <g transform="translate(95, 95)">
        <!-- Cloud outline -->
        <path d="M 40,80 A 28,28 0 0,1 78,40 A 42,42 0 0,1 138,48 A 30,30 0 0,1 155,75 A 24,24 0 0,1 150,110 L 40,110 A 25,25 0 0,1 40,80 Z" 
              fill="{panel_bg}" stroke="url(#awsGrad-{theme})" stroke-width="4" stroke-linejoin="round"/>
        
        <!-- AWS Smile Arrow -->
        <path d="M 42,128 Q 95,155 148,130" stroke="#FF9900" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        <path d="M 148,130 L 138,124 M 148,130 L 140,138" stroke="#FF9900" stroke-width="4" stroke-linecap="round"/>

        <!-- AWS Service Badges inside cloud -->
        <text x="96" y="82" fill="#FF9900" font-size="16" font-weight="900" text-anchor="middle" letter-spacing="2" class="mono">AWS</text>
        <text x="96" y="98" fill="{text_dim}" font-size="9" font-weight="600" text-anchor="middle" class="mono">CLOUD PLATFORM</text>
      </g>

      <!-- Floating Cloud Infrastructure Nodes -->
      <g transform="translate(45, 235)">
        <rect x="0" y="0" width="55" height="22" rx="4" fill="{panel_bg}" stroke="#FF9900" stroke-width="1"/>
        <text x="27" y="15" fill="{text_bright}" font-size="10" font-weight="700" text-anchor="middle" class="mono">EKS</text>

        <rect x="65" y="0" width="55" height="22" rx="4" fill="{panel_bg}" stroke="#FF9900" stroke-width="1"/>
        <text x="92" y="15" fill="{text_bright}" font-size="10" font-weight="700" text-anchor="middle" class="mono">EC2</text>

        <rect x="130" y="0" width="55" height="22" rx="4" fill="{panel_bg}" stroke="#FF9900" stroke-width="1"/>
        <text x="157" y="15" fill="{text_bright}" font-size="10" font-weight="700" text-anchor="middle" class="mono">S3</text>

        <rect x="195" y="0" width="55" height="22" rx="4" fill="{panel_bg}" stroke="#FF9900" stroke-width="1"/>
        <text x="222" y="15" fill="{text_bright}" font-size="10" font-weight="700" text-anchor="middle" class="mono">IAM</text>
      </g>

      <!-- Bottom Tag -->
      <text x="170" y="285" fill="#FF9900" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1.5" class="mono">AMAZON WEB SERVICES</text>
      <text x="170" y="305" fill="{text_dim}" font-size="10" text-anchor="middle" class="mono">HIGH AVAILABILITY · RESILIENT INFRA</text>
    </g>

    <!-- Visual Map Footer -->
    <text x="0" y="358" fill="{text_dim}" font-size="10" class="mono">PTS 18000 · FS/SERPENTINE</text>
  </g>

  <!-- ============================================================== -->
  <!-- RIGHT PANEL: SYSTEM.INFO (740 x 380)                           -->
  <!-- ============================================================== -->
  <g transform="translate(420, 60)">
    <!-- Header with Live badge -->
    <text x="0" y="18" fill="{cyan}" font-size="13" font-weight="700" letter-spacing="1" class="mono">SYSTEM.INFO</text>
    
    <!-- Live Beacon -->
    <g transform="translate(560, 6)">
      <circle cx="6" cy="9" r="4.5" fill="#ef4444" class="live-dot"/>
      <text x="18" y="13" fill="#ef4444" font-size="11" font-weight="700" class="mono">LIVE</text>
    </g>

    <!-- Handle Tag -->
    <g transform="translate(630, 2)">
      <rect width="105" height="22" rx="11" fill="{panel_bg}" stroke="{border}" stroke-width="1"/>
      <text x="52" y="15" fill="{accent}" font-size="11" font-weight="600" text-anchor="middle" class="mono">@SUDARSHNACHAND</text>
    </g>

    <line x1="0" y1="35" x2="735" y2="35" stroke="{border}" stroke-width="1"/>

    <!-- Table of Attributes -->
    <g transform="translate(0, 58)" font-size="12.5" class="mono">
      <!-- Row 1 -->
      <text x="0" y="0" fill="{text_dim}">Subject</text>
      <text x="150" y="0" fill="{border}">··············································</text>
      <text x="735" y="0" fill="{text_bright}" font-weight="700" text-anchor="end">Sudarshan Chand</text>

      <!-- Row 2 -->
      <text x="0" y="24" fill="{text_dim}">Role</text>
      <text x="150" y="24" fill="{border}">··············································</text>
      <text x="735" y="24" fill="{accent}" font-weight="700" text-anchor="end">DevOps Engineer · Cloud Specialist</text>

      <!-- Row 3 -->
      <text x="0" y="48" fill="{text_dim}">Origin</text>
      <text x="150" y="48" fill="{border}">··············································</text>
      <text x="735" y="48" fill="{text_norm}" text-anchor="end">India 🇮🇳</text>

      <!-- Row 4 -->
      <text x="0" y="72" fill="{text_dim}">Status</text>
      <text x="150" y="72" fill="{border}">··············································</text>
      <text x="735" y="72" fill="{green}" font-weight="600" text-anchor="end">Automating + Orchestrating + Deploying</text>

      <!-- Row 5 -->
      <text x="0" y="96" fill="{text_dim}">ToolChain</text>
      <text x="150" y="96" fill="{border}">··············································</text>
      <text x="735" y="96" fill="{text_bright}" text-anchor="end">Git · Jenkins · Docker · K8s · Terraform</text>

      <!-- Row 6 -->
      <text x="0" y="120" fill="{text_dim}">Core.Cloud</text>
      <text x="150" y="120" fill="{border}">··············································</text>
      <text x="735" y="120" fill="#FF9900" font-weight="600" text-anchor="end">AWS (EC2 · EKS · S3 · IAM · VPC · Lambda)</text>

      <!-- Row 7 -->
      <text x="0" y="144" fill="{text_dim}">Core.CI/CD</text>
      <text x="150" y="144" fill="{border}">··············································</text>
      <text x="735" y="144" fill="{cyan}" text-anchor="end">Jenkins Pipelines · GitHub Actions</text>

      <!-- Row 8 -->
      <text x="0" y="168" fill="{text_dim}">Core.IaC</text>
      <text x="150" y="168" fill="{border}">··············································</text>
      <text x="735" y="168" fill="{text_bright}" text-anchor="end">Terraform · Ansible · Helm Charts</text>

      <!-- Row 9 -->
      <text x="0" y="192" fill="{text_dim}">Core.Observ</text>
      <text x="150" y="192" fill="{border}">··············································</text>
      <text x="735" y="192" fill="{text_norm}" text-anchor="end">Prometheus · Grafana · CloudWatch</text>

      <!-- Row 10 -->
      <text x="0" y="216" fill="{text_dim}">Core.Lang</text>
      <text x="150" y="216" fill="{border}">··············································</text>
      <text x="735" y="216" fill="{text_bright}" text-anchor="end">Python · Bash · JavaScript · Java</text>

      <!-- Row 11 -->
      <text x="0" y="240" fill="{text_dim}">Core.Database</text>
      <text x="150" y="240" fill="{border}">··············································</text>
      <text x="735" y="240" fill="{text_norm}" text-anchor="end">MongoDB · MySQL</text>

      <!-- Row 12 -->
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
</svg>
'''
    return svg

def main():
    for theme in ("dark", "light"):
        svg = generate_banner(theme)
        out_file = ASSETS / f"banner-{theme}.svg"
        out_file.write_text(svg, encoding="utf-8")
        print(f"Generated {out_file}")

if __name__ == "__main__":
    main()
