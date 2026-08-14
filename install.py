"""One-time local setup for PCI-DLI."""
from __future__ import annotations
import os

RUNTIME_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runtime")


def install() -> None:
    os.makedirs(RUNTIME_DIR, exist_ok=True)
    print(f"Runtime directory ready: {RUNTIME_DIR}")

    db_path = os.path.join(RUNTIME_DIR, "pci_dli.db")
    if not os.path.exists(db_path):
        import sqlite3
        conn = sqlite3.connect(db_path)
        conn.execute(
            "CREATE TABLE IF NOT EXISTS signals "
            "(id INTEGER PRIMARY KEY, asset TEXT, value REAL, regime TEXT, ts TEXT)"
        )
        conn.commit()
        conn.close()
        print(f"Database initialized: {db_path}")
    else:
        print(f"Database already exists: {db_path}")

    print("Install complete.")


if __name__ == "__main__":
    install()
