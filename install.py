from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
LOGS_DIR = ROOT / "logs"
ASSETS_FILE = DATA_DIR / "sample_assets.json"


def ensure_file(path: Path, content: str) -> None:
    if path.exists():
        print(f"skip existing: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"created: {path}")


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)

    if not ASSETS_FILE.exists():
        ASSETS_FILE.write_text(
            json.dumps(
                [
                    {"symbol": "BTC", "liquidity": 0.82, "regime": "expansion"},
                    {"symbol": "ETH", "liquidity": 0.76, "regime": "balanced"},
                    {"symbol": "SOL", "liquidity": 0.64, "regime": "volatile"},
                ],
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"created: {ASSETS_FILE}")
    else:
        print(f"skip existing: {ASSETS_FILE}")

    ensure_file(ROOT / "repo_structure.txt", "PCI-DLI-\n├── README.md\n├── start.py\n├── install.py\n├── pci_dli.py\n├── pci_dli_api.py\n├── pci_dli_ui.py\n├── prometheus_integration.py\n└── data/sample_assets.json\n")


if __name__ == "__main__":
    main()
