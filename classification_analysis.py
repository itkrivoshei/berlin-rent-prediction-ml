from __future__ import annotations

from src.berlin_rent_prediction.data import generate_housing_data
from src.berlin_rent_prediction.models import train_classification_model


def run_classification_analysis() -> None:
    """Run classification analysis from the command line."""
    df = generate_housing_data(n_samples=1_000, random_state=42)
    result = train_classification_model(df)

    print("Classification model performance")
    print(f"Accuracy: {result.metrics['Accuracy']:.3f}")
    print("Confusion Matrix:")
    print(result.metrics["Confusion Matrix"])


if __name__ == "__main__":
    run_classification_analysis()
