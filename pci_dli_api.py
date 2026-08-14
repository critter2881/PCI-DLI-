"""FastAPI application for PCI-DLI."""
from __future__ import annotations
from typing import Any
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from pci_dli import Signal, Prediction
from pci_dli_ui import build_ui
from prometheus_integration import to_prometheus_payload

app = FastAPI(title="PCI-DLI", version="0.1.0")

# In-memory store
_signals: list[dict[str, Any]] = []
_scores: dict[str, float] = {}


class IngestRequest(BaseModel):
    asset: str
    value: float
    regime: str = "unknown"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ui", response_class=HTMLResponse)
def ui() -> str:
    return build_ui(_scores)


@app.post("/ingest")
def ingest(req: IngestRequest) -> dict[str, Any]:
    sig = Signal(asset=req.asset, value=req.value, regime=req.regime)
    _signals.append({"asset": sig.asset, "value": sig.value, "regime": sig.regime})
    _scores[sig.asset] = sig.value
    return {"accepted": True, "prometheus": to_prometheus_payload(sig)}


@app.get("/assets")
def assets() -> dict[str, list[str]]:
    return {"assets": list(_scores.keys())}


@app.get("/score/{asset}")
def score(asset: str) -> dict[str, Any]:
    if asset not in _scores:
        return {"asset": asset, "score": None, "error": "not found"}
    pred = Prediction(asset=asset, score=_scores[asset], regime="live")
    return {"asset": pred.asset, "score": pred.score, "regime": pred.regime}
