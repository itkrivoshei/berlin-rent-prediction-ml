from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .data import FEATURE_COLUMNS, TARGET_CLASS, TARGET_RENT

CATEGORICAL_FEATURES = ["location"]
NUMERICAL_FEATURES = ["size_sqm", "num_rooms", "distance_to_transport", "age_of_building"]


@dataclass(frozen=True)
class RegressionResult:
    model: Pipeline
    y_test: pd.Series
    y_pred: np.ndarray
    metrics: dict[str, float]


@dataclass(frozen=True)
class ClassificationResult:
    model: Pipeline
    y_test: pd.Series
    y_pred: np.ndarray
    metrics: dict[str, Any]


def build_preprocessor() -> ColumnTransformer:
    """Create a preprocessing pipeline for categorical and numerical features."""
    return ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
            ("num", StandardScaler(), NUMERICAL_FEATURES),
        ]
    )


def train_regression_model(df: pd.DataFrame, random_state: int = 42) -> RegressionResult:
    """Train a linear regression model to predict monthly rent."""
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_RENT]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state
    )

    model = Pipeline(
        steps=[
            ("preprocessor", build_preprocessor()),
            ("regressor", LinearRegression()),
        ]
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "RMSE": float(np.sqrt(mean_squared_error(y_test, y_pred))),
        "R2": r2_score(y_test, y_pred),
    }

    return RegressionResult(model=model, y_test=y_test, y_pred=y_pred, metrics=metrics)


def train_classification_model(df: pd.DataFrame, random_state: int = 42) -> ClassificationResult:
    """Train a logistic regression model to classify luxury apartments."""
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_CLASS]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=random_state,
        stratify=y,
    )

    model = Pipeline(
        steps=[
            ("preprocessor", build_preprocessor()),
            (
                "classifier",
                LogisticRegression(max_iter=1_000, class_weight="balanced"),
            ),
        ]
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Confusion Matrix": confusion_matrix(y_test, y_pred),
    }

    return ClassificationResult(model=model, y_test=y_test, y_pred=y_pred, metrics=metrics)


def predict_apartment(model: Pipeline, apartment: dict[str, Any]) -> float:
    """Run a prediction for one apartment input."""
    input_df = pd.DataFrame([apartment], columns=FEATURE_COLUMNS)
    prediction = model.predict(input_df)[0]
    return float(prediction)
