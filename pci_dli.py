"""Core dataclasses for PCI-DLI."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class Signal:
    asset: str
    value: float
    regime: str = "unknown"
    timestamp: datetime = field(default_factory=_utcnow)
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass
class Prediction:
    asset: str
    score: float
    regime: str
    confidence: float = 1.0
    generated_at: datetime = field(default_factory=_utcnow)
