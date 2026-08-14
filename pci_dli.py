"""Core dataclasses for PCI-DLI."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Signal:
    asset: str
    value: float
    regime: str = "unknown"
    timestamp: datetime = field(default_factory=datetime.utcnow)
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass
class Prediction:
    asset: str
    score: float
    regime: str
    confidence: float = 1.0
    generated_at: datetime = field(default_factory=datetime.utcnow)
