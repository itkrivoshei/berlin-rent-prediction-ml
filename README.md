# Berlin Rent Prediction ML

Interactive machine-learning app for predicting Berlin apartment rent and classifying apartments as standard or luxury with synthetic housing data.

The project is structured as a small Python ML application: reusable data generation, reusable model training functions, automated tests, linting, and a Streamlit dashboard.

## Features

- Synthetic Berlin apartment dataset generation
- Rent prediction with a scikit-learn regression pipeline
- Luxury apartment classification with a scikit-learn classification pipeline
- Shared preprocessing for categorical and numerical features
- Streamlit dashboard with sidebar inputs, metrics, plots, and CSV export
- Regression metrics: MAE, RMSE, and R²
- Classification metrics: accuracy and confusion matrix
- GitHub Actions workflow for linting, formatting checks, tests, and module validation
- Streamlit Community Cloud and Replit deployment configuration

## Tech Stack

- Python 3.12
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
├── classification_analysis.py
├── regression_analysis.py
├── streamlit_app.py
├── requirements.txt
├── runtime.txt
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

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Then open:

```txt
http://localhost:8501
```

## Command-Line Analysis

Run the regression workflow:

```bash
python regression_analysis.py
```

Run the classification workflow:

```bash
python classification_analysis.py
```

## Quality Checks

Run linting:

```bash
ruff check .
```

Run formatting validation:

```bash
ruff format --check .
```

Run tests:

```bash
pytest -q
```

Validate Python modules:

```bash
python -m compileall -q streamlit_app.py src tests
```

## Deployment

### Streamlit Community Cloud

1. Connect this GitHub repository.
2. Select branch: `main`.
3. Set the main file path to `streamlit_app.py`.
4. Use Python 3.12. The repository includes `runtime.txt` for this.
5. Deploy or reboot the app after dependency changes.

### Replit

The repository also includes `.replit` and `replit.nix` for running the same Streamlit app on Replit.

## Data Note

The dataset is synthetic and generated inside the project. It is useful for demonstrating a machine-learning workflow, but it should not be used for real estate valuation, legal advice, financial decisions, or rental market analysis.

## License

This project is open-source. See the repository license for details.
