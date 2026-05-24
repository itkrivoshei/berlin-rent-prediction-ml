# Berlin Rent Prediction ML

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://berlin-rent-prediction-ml.streamlit.app/)
[![CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/berlin-rent-prediction-ml/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/itkrivoshei/berlin-rent-prediction-ml/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

Streamlit app for predicting synthetic Berlin apartment rent and classifying apartments as standard or luxury.

## Tech stack

- Python 3.12
- Streamlit
- pandas / NumPy
- scikit-learn
- Matplotlib
- pytest
- Ruff
- GitHub Actions

## Scope

- Generates a reproducible synthetic Berlin housing dataset
- Trains a linear regression model for rent prediction
- Trains a logistic regression model for luxury apartment classification
- Displays metrics, plots, sample data, and CSV export in Streamlit
- Includes CLI scripts for separate regression and classification checks

The dataset is synthetic and generated inside the project. It is not suitable for real rental valuation, financial decisions, legal advice, or market analysis.

## Live demo

```txt
https://berlin-rent-prediction-ml.streamlit.app/
```

## Install

```bash
git clone https://github.com/itkrivoshei/berlin-rent-prediction-ml.git
cd berlin-rent-prediction-ml
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Windows PowerShell activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Run

```bash
streamlit run streamlit_app.py
```

The app runs locally at:

```txt
http://localhost:8501
```

## CLI checks

```bash
python regression_analysis.py
python classification_analysis.py
```

## Quality checks

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m compileall -q streamlit_app.py src tests
python -c "import streamlit_app"
```

## Project structure

```txt
.
├── .devcontainer/devcontainer.json
├── .github/workflows/ci.yml
├── .streamlit/config.toml
├── src/berlin_rent_prediction/
│   ├── __init__.py
│   ├── data.py
│   ├── models.py
│   └── plots.py
├── tests/test_models.py
├── classification_analysis.py
├── regression_analysis.py
├── streamlit_app.py
├── requirements.txt
├── runtime.txt
├── pyproject.toml
├── LICENSE
└── README.md
```

## Deployment

The live app is deployed on Streamlit Community Cloud.

Repository deployment settings:

```txt
Branch: main
Main file: streamlit_app.py
Python runtime: runtime.txt
```

The repository also contains Replit configuration files for running the same Streamlit app in Replit.

## License

MIT License. See [LICENSE](LICENSE).
