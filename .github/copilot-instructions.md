# Copilot instructions for webhook-test

## Quick: build / test / lint
- Python: requires Python 3.x (no virtualenv script provided; use venv/poetry as desired).
- Run full test suites:
  - Unittest (existing tests): python -m unittest
  - Pytest (examples included): pytest
- Run a single test:
  - Unittest: python -m unittest test_yanghui.YanghuiTests.test_print_yanghui
  - Pytest: pytest test_random.py::test_addition  OR pytest -k test_addition
- Lint: No linter configured in repo. Recommend adding flake8/ruff and a pre-commit hook.

## High-level architecture
- Tiny demo repository focused on examples and webhook demo pages.
- Core module: `yanghui.py` — generates and prints Pascal's (Yanghui) triangle. Provides:
  - yanghui(n) -> list[list[int]]
  - print_yanghui(n) -> prints centered lines
- Tests:
  - `test_yanghui.py` — unittest.TestCase based tests for yanghui.py
  - `test_random.py` — pytest-style sample tests (auto-generated)
- Static demo: `index.html` (Vercel demo output)
- Deployment notes: `DEPLOY.md` (placeholder steps)

## Key conventions & repository-specific notes
- Mixed test frameworks present (unittest + pytest). When adding tests, prefer one framework for consistency.
- Tests live at repository root and target module-level functions. Use module-qualified names to run single unittest tests.
- Scripts in modules use interactive input (if __name__ == "__main__"); CI should avoid running those directly.
- No packaging (setup.cfg/pyproject.toml) — treat this as a demo repo unless packaging is added.

## Existing docs scanned
- README.md / README_en.md: basic usage and file map. Incorporated above.
- DEPLOY.md: placeholder. Consider adding concrete deploy steps if used in CI/CD.

## Assistant / AI config files
- No special AI assistant configuration files found (CLAUDE.md, AGENTS.md, .cursorrules, etc.).

## Suggested improvements for future Copilot sessions
- Consolidate tests to one framework (recommend pytest).
- Add pyproject.toml or requirements.txt with pinned Python version and test deps.
- Add a linter config and pre-commit to enforce consistency.
- Expand DEPLOY.md with exact commands if deploying (Vercel/GitHub Pages).

---

If you'd like, configure an MCP server for web testing (Playwright) or another server for this project—should I set one up?

Summary: created .github/copilot-instructions.md with build/test commands, architecture, and repo-specific conventions.
