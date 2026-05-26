# QA_Playwright_project 
This is a showcase project built to demonstrate automation testing functionalities using Python, Selenium, and PyTest. The project is based on SauceDemo, a demo website designed for practicing and learning test automation workflows. It includes basic UI and API testing concepts along with report generation and reusable framework structuree.

## Tech Stack
- Python 3.11
- Playwright (UI)
- Requests for API
- PyTest 

## Core Architecture
- Page Object Model (POM): UI locators and actions are strictly separated from test logic.
- Parallel Execution: Used `pytest-xdist` to run multiple browser workers simultaneously.
- CI/CD: GitHub Actions pipeline configured to run tests on push and generate HTML reports.


### Directory Structure
QA_Playright_Project
├── .github/workflows/   # CI/CD pipeline configuration (YAML)
├── pages/               # Page Object Model (POM) classes (e.g., checkout_page.py)
├── tests/               # PyTest execution files (e.g., test_checkout.py, test_api.py)
├── .gitignore           # Ignored system and cache files
├── requirements.txt     # Python dependencies list
├── Dockerfile           # Containerization blueprint
└── README.md            # Project documentation

## Local Setup

1. Install requirements:
    pip install pytest pytest-playwright pytest-html pytest-xdist requests
    playwright install chromium

2. Run tests and generate HTML reports :
    pytest -n 3 --html=report.html --self-contained-html