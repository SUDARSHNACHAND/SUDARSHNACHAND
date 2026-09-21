#!/usr/bin/env python3
"""
cards.py - render GitHub stat cards as standalone SVGs (dark & light).
Self-hosted inside the repository so it never fails due to third-party outages.

Usage:
    python scripts/cards.py --user SUDARSHNACHAND --out assets
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

UA = {"User-Agent": "cards.py/1.0"}

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "border": "#30363d",
        "title": "#aa9bef",
        "text": "#c9d1d9",
        "muted": "#8b949e",
        "value": "#e6edf3",
        "accent": "#aa9bef",
    },
    "light": {
        "bg": "#ffffff",
        "border": "#d0d7de",
        "title": "#1a7f37",
        "text": "#1f2328",
        "muted": "#57606a",
        "value": "#1f2328",
        "accent": "#1a7f37",
    },
}

def fetch_stats(username: str, token: str | None) -> dict:
    headers = dict(UA)
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # 1. User details (public repos, followers)
    try:
        req_user = urllib.request.Request(f"https://api.github.com/users/{username}", headers=headers)
        with urllib.request.urlopen(req_user, timeout=20) as r:
            user_data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"Warning: Failed to fetch user data: {e}", file=sys.stderr)
        user_data = {"public_repos": 1, "followers": 0}

    # 2. Public repositories (count stars)
    stars = 0
    forks = 0
    try:
        req_repos = urllib.request.Request(f"https://api.github.com/users/{username}/repos?per_page=100", headers=headers)
        with urllib.request.urlopen(req_repos, timeout=20) as r:
            repos_data = json.loads(r.read().decode("utf-8"))
            for repo in repos_data:
                stars += repo.get("stargazers_count", 0)
                forks += repo.get("forks_count", 0)
    except Exception as e:
        print(f"Warning: Failed to fetch repo data: {e}", file=sys.stderr)

    return {
        "repos": user_data.get("public_repos", 0),
        "stars": stars,
        "forks": forks,
        "followers": user_data.get("followers", 0),
    }

def render_stat_card(stats: dict, theme: dict) -> str:
    w, h = 480, 160
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <style>
    text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
  </style>
  <rect width="{w}" height="{h}" rx="10" fill="{theme['bg']}" stroke="{theme['border']}" stroke-width="1"/>
  
  <text x="24" y="38" fill="{theme['title']}" font-size="16" font-weight="600">GitHub Statistics</text>
  
  <g transform="translate(24, 72)">
    <text x="0" y="0" fill="{theme['muted']}" font-size="13">Public Repos</text>
    <text x="0" y="32" fill="{theme['value']}" font-size="24" font-weight="700">{stats['repos']}</text>
  </g>
  
  <g transform="translate(150, 72)">
    <text x="0" y="0" fill="{theme['muted']}" font-size="13">Total Stars</text>
    <text x="0" y="32" fill="{theme['value']}" font-size="24" font-weight="700">{stats['stars']}</text>
  </g>
  
  <g transform="translate(260, 72)">
    <text x="0" y="0" fill="{theme['muted']}" font-size="13">Forks</text>
    <text x="0" y="32" fill="{theme['value']}" font-size="24" font-weight="700">{stats['forks']}</text>
  </g>
  
  <g transform="translate(360, 72)">
    <text x="0" y="0" fill="{theme['muted']}" font-size="13">Followers</text>
    <text x="0" y="32" fill="{theme['value']}" font-size="24" font-weight="700">{stats['followers']}</text>
  </g>
</svg>'''

def main():
    parser = argparse.ArgumentParser(description="Generate self-hosted GitHub stat cards")
    parser.add_argument("--user", required=True, help="GitHub username")
    parser.add_argument("--out", default="assets", help="Output directory")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    stats = fetch_stats(args.user, token)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    for mode in ("dark", "light"):
        svg = render_stat_card(stats, THEMES[mode])
        out_path = out_dir / f"card-stats-{mode}.svg"
        out_path.write_text(svg, encoding="utf-8")
        print(f"Generated {out_path}")

if __name__ == "__main__":
    main()
