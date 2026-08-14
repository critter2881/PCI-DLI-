# PCI-DLI

**PCI-DLI** is a sovereign engine for real-time liquidity scoring, regime detection,
predictive flow analysis, and Prometheus-aligned intelligence across PCI's
multi-surface ecosystem.

---

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Initialize local runtime
```bash
python install.py
```

### 3. Start the API server
```bash
python start.py
```

The server starts at **http://localhost:8000**.

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/ui` | Minimal HTML dashboard |
| POST | `/ingest` | Ingest a raw signal |
| GET | `/assets` | List tracked assets |
| GET | `/score/{asset}` | Get liquidity score for an asset |

---

## Bootstrap / Scaffold

Run `python pci_dli_bootstrap.py` to create any missing files or directories.
Existing files are **never overwritten**.

---

## Prometheus Integration

`prometheus_integration.py` exposes a `to_prometheus_payload(signal)` helper that
converts a `Signal` dataclass into a Prometheus-compatible metrics payload.

---

## Directory Structure

```
PCI-DLI/
├── data/
│   └── sample_assets.json
├── pci_dli.py              # Core dataclasses
├── pci_dli_api.py          # FastAPI application
├── pci_dli_ui.py           # HTML UI builder
├── pci_dli_i18n.py         # Internationalization helpers
├── pci_dli_plugins.py      # Plugin registry
├── prometheus_integration.py
├── pci_dli_bootstrap.py    # Scaffold generator
├── install.py              # One-time local setup
├── start.py                # Entry point
├── requirements.txt
├── Dockerfile
└── .gitignore
```
