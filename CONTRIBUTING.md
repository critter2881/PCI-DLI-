# Contributing to PCI-DLI

Thank you for your interest in contributing! We welcome pull requests, bug reports, and feature suggestions from the community.

---

## Getting Started

1. **Fork** this repository and clone your fork locally.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the existing tests to make sure everything passes:
   ```bash
   pytest tests/ -v
   ```

## Making Changes

- Create a new branch from `main` for your work: `git checkout -b feature/my-feature`
- Keep commits small, focused, and well-described.
- Add or update tests for any new functionality.
- Make sure all tests pass before submitting.

## Pull Request Process

1. Push your branch and open a pull request against `main`.
2. Fill out the pull request template — describe *what* changed and *why*.
3. A maintainer will review your PR. Please be responsive to feedback.
4. Once approved, a maintainer will merge your contribution.

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Use type hints wherever practical.
- Keep functions small and focused.

## Reporting Bugs

Open a [GitHub Issue](../../issues/new?template=bug_report.md) with:
- A clear title and description
- Steps to reproduce
- Expected vs. actual behavior

## Suggesting Features

Open a [GitHub Issue](../../issues/new?template=feature_request.md) describing the feature and the problem it solves.

## Code of Conduct

All participants are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

Thank you for helping make PCI-DLI better! 🚀
