from __future__ import annotations

from src.berlin_rent_prediction.data import generate_housing_data
from src.berlin_rent_prediction.models import train_regression_model


def run_regression_analysis() -> None:
    """Run regression analysis from the command line."""
    df = generate_housing_data(n_samples=1_000, random_state=42)
    result = train_regression_model(df)

    print("Regression model performance")
    for name, value in result.metrics.items():
        print(f"{name}: {value:.3f}")


if __name__ == "__main__":
    run_regression_analysis()
