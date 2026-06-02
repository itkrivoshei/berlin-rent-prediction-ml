<div align="center">

# Berlin Rent Prediction ML

Streamlit app for synthetic Berlin rent prediction using scikit-learn regression and classification pipelines.

[![Live app](https://img.shields.io/badge/live-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=0f172a)](https://berlin-rent-prediction-ml.streamlit.app/)
[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/berlin-rent-prediction-ml/ci.yml?branch=main&style=for-the-badge&label=ci&logo=githubactions&logoColor=white&labelColor=0f172a)](https://github.com/itkrivoshei/berlin-rent-prediction-ml/actions/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/itkrivoshei/berlin-rent-prediction-ml/codeql.yml?branch=main&style=for-the-badge&label=codeql&logo=github&logoColor=white&labelColor=0f172a)](https://github.com/itkrivoshei/berlin-rent-prediction-ml/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/Python-3.12-3776ab?style=for-the-badge&logo=python&logoColor=white&labelColor=0f172a)](pyproject.toml)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7-f7931e?style=for-the-badge&logo=scikitlearn&logoColor=white&labelColor=0f172a)](pyproject.toml)
[![License](https://img.shields.io/github/license/itkrivoshei/berlin-rent-prediction-ml?style=for-the-badge&labelColor=0f172a)](LICENSE)

</div>

## Model Boundary

This repository generates its own synthetic housing dataset. It does not scrape listings, query external real-estate APIs, or represent the live Berlin rental market.

The project is intended as a compact ML workflow demo covering data generation, preprocessing, model training, metrics, prediction controls, charts, tests, and CI.

| Task          | Model                        | Output                       |
| ------------- | ---------------------------- | ---------------------------- |
| Rent estimate | Linear regression pipeline   | Predicted monthly rent       |
| Segment label | Logistic regression pipeline | Standard or luxury apartment |

## Input Signals

- Berlin area: Mitte, Friedrichshain, Kreuzberg, Neukolln, Charlottenburg
- Apartment size in square meters
- Number of rooms
- Distance to public transport
- Building age
- Synthetic sample count and random seed

## Tech Stack

| Area          | Tools                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| App           | [Streamlit](https://streamlit.io/)                                                                                       |
| Language      | [Python 3.12](https://www.python.org/)                                                                                   |
| ML            | [scikit-learn](https://scikit-learn.org/)                                                                                |
| Data / charts | [pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/)                                              |
| Quality       | [Ruff](https://docs.astral.sh/ruff/), [pytest](https://docs.pytest.org/)                                                 |
| CI / security | [GitHub Actions](https://github.com/itkrivoshei/berlin-rent-prediction-ml/actions), [CodeQL](https://codeql.github.com/) |
| Hosting       | [Streamlit Community Cloud](https://streamlit.io/cloud)                                                                  |

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

## Quality Gates

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m compileall -q streamlit_app.py src tests
python -c "import streamlit_app"
python regression_analysis.py
python classification_analysis.py
```

These checks are also covered by the [Python CI workflow](.github/workflows/ci.yml).

## Project Files

| Path                                                                           | Role                                               |
| ------------------------------------------------------------------------------ | -------------------------------------------------- |
| [`streamlit_app.py`](streamlit_app.py)                                         | Streamlit UI, controls, tabs, charts               |
| [`src/berlin_rent_prediction/data.py`](src/berlin_rent_prediction/data.py)     | Synthetic dataset generator                        |
| [`src/berlin_rent_prediction/models.py`](src/berlin_rent_prediction/models.py) | Preprocessing, regression, classification          |
| [`src/berlin_rent_prediction/plots.py`](src/berlin_rent_prediction/plots.py)   | Matplotlib chart helpers                           |
| [`regression_analysis.py`](regression_analysis.py)                             | CLI regression run                                 |
| [`classification_analysis.py`](classification_analysis.py)                     | CLI classification run                             |
| [`tests/test_models.py`](tests/test_models.py)                                 | Unit coverage for model behavior                   |
| [`pyproject.toml`](pyproject.toml)                                             | Python package metadata, dependencies, and tooling |
| [`requirements.txt`](requirements.txt)                                         | Streamlit deployment dependencies                  |
| [`runtime.txt`](runtime.txt)                                                   | Streamlit Python runtime                           |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml)                         | Ruff, pytest, compile, import, and analysis checks |
| [`.github/workflows/codeql.yml`](.github/workflows/codeql.yml)                 | GitHub CodeQL analysis                             |

## Deployment

Streamlit Community Cloud runs [`streamlit_app.py`](streamlit_app.py) with dependencies from [`requirements.txt`](requirements.txt) and Python from [`runtime.txt`](runtime.txt).

Live app: [berlin-rent-prediction-ml.streamlit.app](https://berlin-rent-prediction-ml.streamlit.app/)

## License

[MIT](LICENSE)
