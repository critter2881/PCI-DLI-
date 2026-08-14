# PCI-DLI-

PCI-DLI (Prometheus-CI Distributed Liquidity Intelligence) is a lightweight starter repository for liquidity scoring, regime detection, predictive flow analysis, and Prometheus-friendly signal export.

## What this repo includes
- A minimal FastAPI service
- A simple HTML UI
- A bootstrapper that creates the expected project structure without overwriting existing files
- A Prometheus integration helper
- A small sample asset dataset

## Quick start
```bash
python install.py
python start.py
```

Then open:
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/ui`
- `http://127.0.0.1:8000/docs`

## Endpoints
- `GET /health` — health check
- `GET /assets` — list sample assets
- `GET /score/{asset}` — score an asset
- `POST /ingest` — ingest signal data
- `GET /ui` — simple HTML dashboard

## Notes
This is a safe starter scaffold. It is designed to be easy to extend and to avoid overwriting any existing files.
