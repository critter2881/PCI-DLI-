from __future__ import annotations

from typing import Any


def render_ui(assets: list[dict[str, Any]]) -> str:
    rows = "".join(
        f"<tr><td>{a.get('symbol','')}</td><td>{a.get('liquidity','')}</td><td>{a.get('regime','')}</td></tr>"
        for a in assets
    )
    return f"""<!doctype html>
<html>
<head>
  <meta charset='utf-8'>
  <title>PCI-DLI</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 2rem; }}
    table {{ border-collapse: collapse; width: 100%; max-width: 720px; }}
    th, td {{ border: 1px solid #ccc; padding: 0.5rem; text-align: left; }}
    th {{ background: #f5f5f5; }}
  </style>
</head>
<body>
  <h1>PCI-DLI</h1>
  <p>Liquidity intelligence starter UI.</p>
  <table>
    <thead><tr><th>Symbol</th><th>Liquidity</th><th>Regime</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</body>
</html>"""
