from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import Any

ROOT = Path(__file__).resolve().parent
ASSETS_FILE = ROOT / "data" / "sample_assets.json"


@dataclass
class Signal:
    symbol: str
    liquidity: float
    regime: str


@dataclass
class Prediction:
    symbol: str
    score: float
    regime: str
    rationale: str


def load_assets() -> list[dict[str, Any]]:
    if not ASSETS_FILE.exists():
        return []
    return json.loads(ASSETS_FILE.read_text(encoding="utf-8"))


def score_asset(symbol: str) -> Prediction:
    assets = load_assets()
    match = next((a for a in assets if a.get("symbol", "").lower() == symbol.lower()), None)
    if not match:
        return Prediction(symbol=symbol, score=0.0, regime="unknown", rationale="No sample data available")

    liquidity = float(match.get("liquidity", 0.0))
    regime = str(match.get("regime", "unknown"))
    score = round(min(max(liquidity, 0.0), 1.0) * 100.0, 2)
    return Prediction(symbol=symbol, score=score, regime=regime, rationale="Derived from sample liquidity signal")


def prediction_to_dict(prediction: Prediction) -> dict[str, Any]:
    return asdict(prediction)
