"""Plugin registry for PCI-DLI signal processors."""
from __future__ import annotations
from typing import Callable

_PLUGINS: dict[str, Callable] = {}


def register(name: str) -> Callable:
    def decorator(fn: Callable) -> Callable:
        _PLUGINS[name] = fn
        return fn
    return decorator


def get(name: str) -> Callable | None:
    return _PLUGINS.get(name)


def list_plugins() -> list[str]:
    return list(_PLUGINS.keys())
