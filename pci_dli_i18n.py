"""Simple i18n string registry for PCI-DLI."""
from __future__ import annotations

_STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "welcome": "Welcome to PCI-DLI",
        "health_ok": "System is healthy",
        "no_data": "No data available",
    }
}


def t(key: str, lang: str = "en") -> str:
    return _STRINGS.get(lang, _STRINGS["en"]).get(key, key)
