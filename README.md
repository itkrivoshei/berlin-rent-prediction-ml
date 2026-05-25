# Berlin Rent Prediction ML

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/berlin-rent-prediction-ml/ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/berlin-rent-prediction-ml/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/berlin-rent-prediction-ml?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)

Streamlit app for synthetic Berlin rent prediction with scikit-learn.

The project demonstrates a compact machine-learning workflow: synthetic data generation, regression and classification pipelines, model evaluation, Streamlit UI, automated tests, linting, formatting checks, and GitHub Actions CI.

## Project Status

This is a small educational ML project. The dataset is generated inside the repository and does not use external APIs, scraped listings, or real rental-market data.

It is suitable for demonstrating a Python ML workflow, but not for real rental valuation, financial decisions, legal advice, or Berlin housing-market analysis.

## Features

- Generate a reproducible synthetic Berlin apartment dataset
- Predict monthly rent with a linear regression pipeline
- Classify apartments as standard or luxury with logistic regression
- Display metrics, charts, sample data, and CSV export in Streamlit
- Run separate CLI checks for regression and classification
- Validate code quality with Ruff, Pytest, and GitHub Actions

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.12 |
| UI | Streamlit |
| Data | pandas, NumPy |
| Machine learning | scikit-learn |
| Visualization | Matplotlib |
| Testing | Pytest |
| Linting / formatting | Ruff |
| CI | GitHub Actions |
| Dependency checks | Dependabot |
| Dev environment | Dev Container / Codespaces |

## Models

| Task | Model | Target |
|---|---|---|
| Regression | Linear Regression | Monthly rent |
| Classification | Logistic Regression | Standard or luxury apartment |

Input features:

- location
- size in square meters
- number of rooms
- distance to transport
- building age

## Install

Clone the repository:

```bash
git clone git@github.com:itkrivoshei/berlin-rent-prediction-ml.git
cd berlin-rent-prediction-ml
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
```

## Run

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

The app runs locally at:

```text
http://localhost:8501
```

Run the CLI checks:

```bash
python regression_analysis.py
python classification_analysis.py
```

## Verify

Run the same checks used by CI:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m compileall -q streamlit_app.py src tests
python -c "import streamlit_app"
python regression_analysis.py
python classification_analysis.py
```

## CI/CD

The GitHub Actions workflow runs on pushes and pull requests to `main`.

It checks:

- dependency installation
- Ruff linting
- Ruff formatting
- Pytest tests
- Python module compilation
- Streamlit app import
- regression and classification scripts

Dependabot checks Python and GitHub Actions dependencies weekly. Major version updates are ignored by default and should be reviewed manually.

## Project Structure

```text
.
├── .devcontainer/
│   └── devcontainer.json
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       └── ci.yml
├── .streamlit/
│   └── config.toml
├── src/
│   └── berlin_rent_prediction/
│       ├── __init__.py
│       ├── data.py
│       ├── models.py
│       └── plots.py
├── tests/
│   └── test_models.py
├── classification_analysis.py
├── regression_analysis.py
├── streamlit_app.py
├── requirements.txt
├── runtime.txt
├── pyproject.toml
└── README.md
```

## Key Files

| File | Purpose |
|---|---|
| `streamlit_app.py` | Streamlit dashboard |
| `src/berlin_rent_prediction/data.py` | Synthetic dataset generation |
| `src/berlin_rent_prediction/models.py` | Regression and classification pipelines |
| `src/berlin_rent_prediction/plots.py` | Matplotlib chart helpers |
| `regression_analysis.py` | CLI regression check |
| `classification_analysis.py` | CLI classification check |
| `tests/` | Unit tests |
| `.github/workflows/ci.yml` | CI validation |
| `.github/dependabot.yml` | Weekly dependency update checks |
| `.devcontainer/devcontainer.json` | Codespaces / Dev Container setup |

## Streamlit Cloud Setup

Use these settings if deploying the app to Streamlit Community Cloud:

```text
Main file path: streamlit_app.py
Python version: runtime.txt
Dependencies: requirements.txt
```

`requirements.txt` installs the package with app dependencies:

```text
-e .[app]
```

## License

This project is licensed under the [MIT License](LICENSE).
