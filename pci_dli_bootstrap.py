from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

sample_assets = [
    {"symbol": "BTC", "liquidity": 0.82, "regime": "expansion"},
    {"symbol": "ETH", "liquidity": 0.76, "regime": "balanced"},
    {"symbol": "SOL", "liquidity": 0.64, "regime": "volatile"},
]

sample_path = DATA_DIR / "sample_assets.json"
if not sample_path.exists():
    sample_path.write_text(json.dumps(sample_assets, indent=2), encoding="utf-8")
    print(f"created: {sample_path}")
else:
    print(f"skip existing: {sample_path}")
