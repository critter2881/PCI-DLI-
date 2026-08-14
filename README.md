<div align="center">

# PCI-DLI

**Real-Time Liquidity Intelligence Engine**

[![CI](https://github.com/critter2881/PCI-DLI-/actions/workflows/ci.yml/badge.svg)](https://github.com/critter2881/PCI-DLI-/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776ab.svg?logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)](#docker)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

*A sovereign engine for real-time liquidity scoring, regime detection, predictive flow analysis, and Prometheus-aligned intelligence — built by [Positive Change Institute LLC](https://github.com/critter2881).*

</div>

---

## ✨ Highlights

| Capability | Description |
|---|---|
| **Liquidity Scoring** | Continuous, per-asset liquidity scores updated in real time |
| **Regime Detection** | Classify market conditions (bull / bear / unknown) on every ingested signal |
| **Prometheus Integration** | One-call conversion of signals to Prometheus-compatible metric payloads |
| **Plugin Architecture** | Decorator-based registry for custom signal processors |
| **i18n Ready** | Built-in internationalization string registry |
| **Container-Native** | Production `Dockerfile` included — deploy anywhere |

---

## 🚀 Quick Start

### Prerequisites

- Python **3.12+**
- (Optional) Docker **24+**

### Local Setup

```bash
# 1 — Install dependencies
pip install -r requirements.txt

# 2 — Initialize the local runtime (creates SQLite DB)
python install.py

# 3 — Start the API server (default: http://localhost:8000)
python start.py
```

### Docker

```bash
docker build -t pci-dli .
docker run -p 8000:8000 pci-dli
```

### Production Configuration

Override host and port via environment variables:

```bash
PCI_HOST=0.0.0.0 PCI_PORT=8080 python start.py
```

> **Security note:** Never expose the server to the public internet without an authentication proxy (e.g. nginx + API-key header) in front of it.

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health-check probe |
| `GET` | `/ui` | Live HTML dashboard |
| `POST` | `/ingest` | Ingest a raw market signal |
| `GET` | `/assets` | List all tracked assets |
| `GET` | `/score/{asset}` | Retrieve the liquidity score for a specific asset |

### Example — Ingest a signal

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{"asset": "BTC", "value": 0.87, "regime": "bull"}'
```

---

## 🏗️ Architecture

```
┌─────────────┐    JSON     ┌──────────────┐    Prometheus     ┌────────────┐
│  Data Source │ ──────────▶ │  PCI-DLI API │ ───────────────▶  │  Metrics   │
│  (signals)  │             │  (FastAPI)   │    payload         │  Backend   │
└─────────────┘             └──────┬───────┘                    └────────────┘
                                   │
                          ┌────────┴────────┐
                          │  Plugin Engine  │
                          │  i18n · UI · DB │
                          └─────────────────┘
```

---

## 📂 Project Structure

```
PCI-DLI/
├── .github/
│   ├── workflows/ci.yml        # CI pipeline
│   ├── ISSUE_TEMPLATE/         # Bug & feature request templates
│   └── PULL_REQUEST_TEMPLATE.md
├── data/
│   └── sample_assets.json      # Seed data
├── tests/
│   ├── conftest.py
│   └── test_api.py             # API smoke tests
├── pci_dli.py                  # Core domain models (Signal, Prediction)
├── pci_dli_api.py              # FastAPI application & routes
├── pci_dli_ui.py               # HTML dashboard builder
├── pci_dli_i18n.py             # Internationalization helpers
├── pci_dli_plugins.py          # Decorator-based plugin registry
├── prometheus_integration.py   # Signal → Prometheus converter
├── pci_dli_bootstrap.py        # Scaffold generator (safe, idempotent)
├── install.py                  # One-time local runtime setup
├── start.py                    # Server entry point
├── requirements.txt
├── Dockerfile
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
└── .gitignore
```

---

## 🔌 Extending PCI-DLI

### Custom Signal Processors

```python
from pci_dli_plugins import register

@register("my_processor")
def process(signal):
    # Your custom logic here
    return signal
```

### Scaffold Missing Files

```bash
python pci_dli_bootstrap.py
```

Existing files are **never overwritten**.

---

## 🛡️ Security

See [SECURITY.md](SECURITY.md) for the vulnerability disclosure policy.

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

## 📜 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

© 2026 Positive Change Institute LLC
