from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from pci_dli import score_asset, load_assets
from pci_dli_ui import render_ui
from prometheus_integration import to_prometheus_payload

app = FastAPI(title="PCI-DLI")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/assets")
def assets() -> list[dict[str, Any]]:
    return load_assets()


@app.get("/score/{asset}")
def score(asset: str) -> dict[str, Any]:
    prediction = score_asset(asset)
    return prediction.__dict__


@app.post("/ingest")
def ingest(payload: dict[str, Any]) -> dict[str, Any]:
    return {"received": payload, "prometheus": to_prometheus_payload(payload)}


@app.get("/ui", response_class=HTMLResponse)
def ui() -> str:
    return render_ui(load_assets())
