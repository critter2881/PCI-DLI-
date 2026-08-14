"""Minimal HTML UI for PCI-DLI dashboard."""
from __future__ import annotations


def build_ui(scores: dict[str, float]) -> str:
    rows = "".join(
        f"<tr><td>{asset}</td><td>{score:.4f}</td></tr>"
        for asset, score in scores.items()
    ) or "<tr><td colspan='2'>No data yet.</td></tr>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PCI-DLI Dashboard</title>
  <style>
    body {{ font-family: sans-serif; padding: 1rem; background: #0d1117; color: #c9d1d9; }}
    h1 {{ color: #58a6ff; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #30363d; padding: 0.5rem 1rem; text-align: left; }}
    th {{ background: #161b22; }}
  </style>
</head>
<body>
  <h1>PCI-DLI Live Scores</h1>
  <table>
    <thead><tr><th>Asset</th><th>Score</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</body>
</html>"""
