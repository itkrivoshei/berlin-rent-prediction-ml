# Berlin Rent Prediction ML

Interactive machine-learning demo for predicting Berlin apartment rent and classifying apartments as standard or luxury using synthetic housing data.

The app uses a shared synthetic dataset, scikit-learn preprocessing pipelines, regression, classification, and a Streamlit interface for model interaction and visual analysis.

## Features

- Synthetic Berlin apartment dataset generation
- Rent prediction with linear regression
- Luxury apartment classification with logistic regression
- Reusable scikit-learn preprocessing pipeline
- Interactive Streamlit UI with sidebar controls
- Regression metrics: MAE, RMSE, R²
- Classification metrics: accuracy and confusion matrix
- Dataset preview and CSV download
- GitHub Actions workflow for linting, tests, and import validation

## Tech Stack

- Python
- Streamlit
- pandas
- NumPy
- scikit-learn
- Matplotlib
- pytest
- Ruff
- GitHub Actions

## Project Structure

```txt
.
├── .github/workflows/ci.yml
├── src/
│   └── berlin_rent_prediction/
│       ├── __init__.py
│       ├── data.py
│       ├── models.py
│       └── plots.py
├── tests/
│   └── test_models.py
├── streamlit_app.py
├── requirements.txt
├── pyproject.toml
├── .replit
├── replit.nix
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/itkrivoshei/berlin-rent-prediction-ml.git
cd berlin-rent-prediction-ml
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Then open:

```txt
http://localhost:8501
```

## Quality Checks

Run linting:

```bash
ruff check .
```

Run tests:

```bash
pytest -q
```

Validate Python imports:

```bash
python -m py_compile streamlit_app.py src/berlin_rent_prediction/*.py
```

## Deployment

This project is prepared for Streamlit Community Cloud or Replit deployment.

For Streamlit Community Cloud:

1. Connect the GitHub repository.
2. Select branch: `main`.
3. Set main file path: `streamlit_app.py`.
4. Deploy.

## Notes

The dataset is synthetic and generated inside the project. It is designed for demonstrating a machine-learning workflow, not for real estate valuation or financial decision-making.

## License

This project is open-source. See the repository license for details.
