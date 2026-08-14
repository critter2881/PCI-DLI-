# PCI-DLI

[![CI](https://github.com/critter2881/PCI-DLI-/actions/workflows/ci.yml/badge.svg)](https://github.com/critter2881/PCI-DLI-/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

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

#### Production configuration

Override host and port via environment variables before starting:

```bash
PCI_HOST=0.0.0.0 PCI_PORT=8080 python start.py
```

In a containerized environment (Docker / Kubernetes) set these in your `env:` block or
pass `--env` flags. Never expose the server to the public internet without an auth proxy
(e.g. nginx + API key header) in front of it.

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
├── .github/workflows/ci.yml  # GitHub Actions CI
├── data/
│   └── sample_assets.json
├── tests/
│   └── test_api.py
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
├── LICENSE
├── SECURITY.md
└── .gitignore
```

## Security

See [SECURITY.md](SECURITY.md) for the vulnerability disclosure policy.


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
