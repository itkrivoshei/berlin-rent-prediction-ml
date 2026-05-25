# Berlin Rent Prediction ML

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/berlin-rent-prediction-ml/ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/berlin-rent-prediction-ml/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/berlin-rent-prediction-ml?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)
[![Streamlit demo](https://img.shields.io/badge/demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://berlin-rent-prediction-ml.streamlit.app/)

Streamlit app for synthetic Berlin rent prediction with scikit-learn.

The project demonstrates a compact machine-learning workflow: synthetic data generation, regression, classification, model evaluation, Streamlit UI, automated tests, linting, formatting checks, and GitHub Actions CI.

## Live Demo

Streamlit app:

https://berlin-rent-prediction-ml.streamlit.app/

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
| Deployment | Streamlit Community Cloud |

## Dataset Scope

The dataset is synthetic and generated inside the project.

It is useful for demonstrating a machine-learning workflow, but it is not suitable for real rental valuation, financial decisions, legal advice, or Berlin housing market analysis.

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

~~~bash
git clone git@github.com:itkrivoshei/berlin-rent-prediction-ml.git
cd berlin-rent-prediction-ml
~~~

Create and activate a virtual environment:

~~~bash
python -m venv .venv
source .venv/bin/activate
~~~

On Windows PowerShell:

~~~powershell
.venv\Scripts\Activate.ps1
~~~

Install dependencies:

~~~bash
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
~~~

## Run

Run the Streamlit app:

~~~bash
streamlit run streamlit_app.py
~~~

The app runs locally at:

~~~text
http://localhost:8501
~~~

Run the CLI checks:

~~~bash
python regression_analysis.py
python classification_analysis.py
~~~

## Verify

Run the same checks used by CI:

~~~bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m compileall -q streamlit_app.py src tests
python -c "import streamlit_app"
~~~

## Project Structure

~~~text
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
~~~

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

## Deployment

Streamlit Community Cloud uses:

~~~text
Main file path: streamlit_app.py
Python version: runtime.txt
Dependencies: requirements.txt
~~~

`requirements.txt` installs the package with app dependencies:

~~~text
-e .[app]
~~~

## License

This project is licensed under the [MIT License](LICENSE).
