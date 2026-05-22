from src.berlin_rent_prediction.data import FEATURE_COLUMNS, generate_housing_data
from src.berlin_rent_prediction.models import predict_apartment, train_classification_model, train_regression_model


def test_generate_housing_data_contains_expected_columns():
    df = generate_housing_data(n_samples=100, random_state=42)

    for column in [*FEATURE_COLUMNS, "rental_price", "luxury"]:
        assert column in df.columns

    assert len(df) == 100


def test_regression_model_can_predict_single_apartment():
    df = generate_housing_data(n_samples=200, random_state=42)
    result = train_regression_model(df)

    apartment = {
        "location": "Mitte",
        "size_sqm": 65,
        "num_rooms": 3,
        "distance_to_transport": 0.6,
        "age_of_building": 30,
    }

    prediction = predict_apartment(result.model, apartment)

    assert prediction > 0
    assert result.metrics["R2"] > 0.5


def test_classification_model_returns_valid_metrics():
    df = generate_housing_data(n_samples=300, random_state=42)
    result = train_classification_model(df)

    assert 0 <= result.metrics["Accuracy"] <= 1
    assert result.metrics["Confusion Matrix"].shape == (2, 2)
