# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Community files: CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md
- GitHub issue templates (bug report, feature request)
- Pull request template
- Polished, enterprise-grade README with architecture diagram, badges, and examples

## [0.1.0] — 2026-08-14

### Added
- Core domain models: `Signal` and `Prediction` dataclasses
- FastAPI-based REST API with `/health`, `/ingest`, `/assets`, `/score/{asset}`, and `/ui` endpoints
- Prometheus integration bridge (`to_prometheus_payload`)
- Minimal HTML dashboard
- Decorator-based plugin registry for custom signal processors
- Internationalization (i18n) string registry
- Idempotent bootstrap scaffold generator
- One-time local setup script with SQLite database initialization
- Dockerfile for containerized deployments
- CI pipeline via GitHub Actions
- Security disclosure policy (SECURITY.md)
- MIT License
