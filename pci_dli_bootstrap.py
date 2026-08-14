"""Bootstrap scaffold – creates missing files/directories only."""
from __future__ import annotations
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "data/sample_assets.json": '[\n  {"asset": "BTC", "label": "Bitcoin"},\n  {"asset": "ETH", "label": "Ethereum"}\n]\n',
    "runtime/.keep": "",
}

DIRS = ["data", "runtime"]


def bootstrap() -> None:
    for d in DIRS:
        path = os.path.join(ROOT, d)
        if not os.path.isdir(path):
            os.makedirs(path)
            print(f"[created] dir  {d}/")
        else:
            print(f"[exists]  dir  {d}/")

    for rel, content in FILES.items():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(content)
            print(f"[created] file {rel}")
        else:
            print(f"[exists]  file {rel}")

    print("Bootstrap complete.")


if __name__ == "__main__":
    bootstrap()
