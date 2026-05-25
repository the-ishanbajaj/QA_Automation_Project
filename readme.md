# QA E-Com_project (Playwright + PyTest)

## Tech Stack
- Python 3.11
- Playwright (UI)
- Requests (API)
- PyTest (Execution & Data-Driven Testing)

## Core Architecture
- Page Object Model (POM): UI locators and actions are strictly separated from test logic.
- API State Injection:** UI tests bypass the login screen by injecting authentication cookies directly via API, cutting execution time significantly.
- Parallel Execution:** Configured with `pytest-xdist` to run multiple browser workers concurrently.
- CI/CD:** GitHub Actions pipeline configured to run tests on push and generate HTML reports.

## Local Setup

1. Install requirements:
```bash
pip install pytest pytest-playwright pytest-html pytest-xdist requests
playwright install chromium