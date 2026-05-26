# Berlin Rent Prediction ML

[![Live app](https://img.shields.io/badge/live-Streamlit-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)](https://berlin-rent-prediction-ml.streamlit.app/)
[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/berlin-rent-prediction-ml/ci.yml?branch=main&style=flat-square&label=python%20ci&logo=githubactions&logoColor=white)](https://github.com/itkrivoshei/berlin-rent-prediction-ml/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12-3776ab?style=flat-square&logo=python&logoColor=white)](pyproject.toml)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7-f7931e?style=flat-square&logo=scikitlearn&logoColor=white)](pyproject.toml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/berlin-rent-prediction-ml?style=flat-square)](LICENSE)

## [Open Streamlit App ->](https://berlin-rent-prediction-ml.streamlit.app/)

Streamlit app for synthetic Berlin rent prediction using scikit-learn regression and classification pipelines.

## Model Boundary

This repository generates its own synthetic housing dataset. It does not scrape listings, query external real-estate APIs, or represent the live Berlin rental market.

| Task | Model | Output |
| --- | --- | --- |
| Rent estimate | Linear regression pipeline | Predicted monthly rent |
| Segment label | Logistic regression pipeline | Standard or luxury apartment |

The app is useful for inspecting a full ML workflow: data generation, preprocessing, model training, metrics, prediction controls, charts, tests, and CI.

## Input Signals

- Berlin area: Mitte, Friedrichshain, Kreuzberg, Neukolln, Charlottenburg
- Size in square meters
- Number of rooms
- Distance to transport
- Building age
- Synthetic sample count and random seed

## Run Locally

```bash
git clone https://github.com/itkrivoshei/berlin-rent-prediction-ml.git
cd berlin-rent-prediction-ml
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
streamlit run streamlit_app.py
```

Open `http://localhost:8501`.

## Checks

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m compileall -q streamlit_app.py src tests
python -c "import streamlit_app"
python regression_analysis.py
python classification_analysis.py
```

## Project Files

| Path | Role |
| --- | --- |
| `streamlit_app.py` | Streamlit UI, controls, tabs, charts |
| `src/berlin_rent_prediction/data.py` | Synthetic dataset generator |
| `src/berlin_rent_prediction/models.py` | Preprocessing, regression, classification |
| `src/berlin_rent_prediction/plots.py` | Matplotlib chart helpers |
| `regression_analysis.py` | CLI regression run |
| `classification_analysis.py` | CLI classification run |
| `tests/test_models.py` | Unit coverage for model behavior |
| `.github/workflows/ci.yml` | Ruff, Pytest, compile, import, analysis scripts |

## Deployment

Streamlit Community Cloud runs `streamlit_app.py` with dependencies from `requirements.txt` and Python from `runtime.txt`.

Live app: https://berlin-rent-prediction-ml.streamlit.app/

## License

[MIT](LICENSE)
