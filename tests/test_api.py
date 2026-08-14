"""API smoke tests for PCI-DLI."""
import pytest
from fastapi.testclient import TestClient
from pci_dli_api import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_ingest_and_score():
    resp = client.post("/ingest", json={"asset": "BTC", "value": 0.87, "regime": "bull"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["accepted"] is True
    assert body["prometheus"]["metric"] == "pci_dli_liquidity_score"
    assert body["prometheus"]["labels"]["asset"] == "BTC"

    resp2 = client.get("/score/BTC")
    assert resp2.status_code == 200
    data = resp2.json()
    assert data["asset"] == "BTC"
    assert data["score"] == pytest.approx(0.87)


def test_assets_list():
    client.post("/ingest", json={"asset": "ETH", "value": 0.65})
    resp = client.get("/assets")
    assert resp.status_code == 200
    assert "ETH" in resp.json()["assets"]


def test_score_missing_asset():
    resp = client.get("/score/UNKNOWN_ASSET_XYZ")
    assert resp.status_code == 200
    assert resp.json()["score"] is None


def test_ui_returns_html():
    resp = client.get("/ui")
    assert resp.status_code == 200
    assert "PCI-DLI" in resp.text
