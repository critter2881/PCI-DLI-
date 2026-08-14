"""Convert PCI-DLI signals to Prometheus-compatible payloads."""
from __future__ import annotations
from typing import Any

from pci_dli import Signal


def to_prometheus_payload(signal: Signal) -> dict[str, Any]:
    return {
        "metric": "pci_dli_liquidity_score",
        "labels": {
            "asset": signal.asset,
            "regime": signal.regime,
        },
        "value": signal.value,
        "timestamp_ms": int(signal.timestamp.timestamp() * 1000),
    }
