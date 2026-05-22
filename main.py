from __future__ import annotations

from src.berlin_rent_prediction.data import generate_housing_data
from src.berlin_rent_prediction.models import train_classification_model, train_regression_model


def main() -> None:
    """Run a local model smoke check from the command line."""
    df = generate_housing_data(n_samples=1_000, random_state=42)
    regression = train_regression_model(df)
    classification = train_classification_model(df)

    print("Berlin Rent Prediction ML")
    print(f"Rows: {len(df)}")
    print("Regression metrics:")
    for name, value in regression.metrics.items():
        print(f"  {name}: {value:.3f}")

    print("Classification metrics:")
    print(f"  Accuracy: {classification.metrics['Accuracy']:.3f}")


if __name__ == "__main__":
    main()
