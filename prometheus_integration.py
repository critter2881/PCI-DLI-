from __future__ import annotations

from typing import Any


def to_prometheus_payload(signal: dict[str, Any]) -> dict[str, Any]:
    return {
        "metric": "pci_dli_signal",
        "labels": {
            "symbol": str(signal.get("symbol", "unknown")),
            "regime": str(signal.get("regime", "unknown")),
        },
        "value": float(signal.get("liquidity", 0.0) or 0.0),
    }
