from __future__ import annotations

from typing import Any

import pandas as pd
import streamlit as st

from berlin_rent_prediction.data import LOCATIONS, generate_housing_data
from berlin_rent_prediction.models import (
    ClassificationResult,
    RegressionResult,
    predict_apartment,
    train_classification_model,
    train_regression_model,
)
from berlin_rent_prediction.plots import (
    plot_actual_vs_predicted,
    plot_class_distribution,
    plot_rent_distribution,
    plot_residuals,
)

APP_TITLE = "Berlin Rent Prediction ML"
APP_SUBTITLE = "Synthetic housing data · scikit-learn pipelines · Streamlit dashboard"

ApartmentInput = dict[str, Any]

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏠",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_data(n_samples: int, random_state: int) -> pd.DataFrame:
    """Load a reproducible synthetic dataset."""
    return generate_housing_data(n_samples=n_samples, random_state=random_state)


@st.cache_resource(show_spinner="Training models...")
def load_models(n_samples: int, random_state: int) -> tuple[RegressionResult, ClassificationResult]:
    """Train and cache both models for the selected dataset settings."""
    df = generate_housing_data(n_samples=n_samples, random_state=random_state)
    regression = train_regression_model(df, random_state=random_state)
    classification = train_classification_model(df, random_state=random_state)
    return regression, classification


def build_apartment_input() -> ApartmentInput:
    """Render sidebar controls and return one apartment payload."""
    with st.sidebar:
        st.header("Dataset")
        n_samples = st.slider("Synthetic samples", 300, 5_000, 1_000, step=100)
        random_state = st.number_input("Random seed", min_value=1, max_value=9999, value=42)

        st.header("Apartment Input")
        location = st.selectbox("Location", LOCATIONS)
        size_sqm = st.slider("Size (sqm)", 20.0, 150.0, 72.0, step=1.0)
        num_rooms = st.slider("Rooms", 1, 6, 3)
        distance_to_transport = st.slider(
            "Distance to transport (km)",
            0.1,
            5.0,
            0.8,
            step=0.1,
        )
        age_of_building = st.slider("Building age (years)", 1, 120, 35)

    st.session_state["n_samples"] = n_samples
    st.session_state["random_state"] = random_state

    return {
        "location": location,
        "size_sqm": size_sqm,
        "num_rooms": num_rooms,
        "distance_to_transport": distance_to_transport,
        "age_of_building": age_of_building,
    }


def render_header() -> None:
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    st.info(
        "This app uses synthetic data generated inside the project. It demonstrates a "
        "machine-learning workflow and should not be used for real rental valuation."
    )


def render_scope_summary(df: pd.DataFrame) -> None:
    """Render a compact project-specific summary above the model tabs."""
    with st.container(border=True):
        st.caption("Model scope")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Synthetic records", f"{len(df):,}")
        col_b.metric("Berlin areas", df["location"].nunique())
        col_c.metric("Data source", "Generated")


def render_prediction_metrics(
    apartment: ApartmentInput,
    regression_result: RegressionResult,
    classification_result: ClassificationResult,
) -> None:
    predicted_rent = predict_apartment(regression_result.model, apartment)
    input_df = pd.DataFrame([apartment])
    predicted_class = int(classification_result.model.predict(input_df)[0])
    class_probability = float(classification_result.model.predict_proba(input_df)[0][1])

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Predicted rent", f"€{predicted_rent:,.0f}")
    metric_2.metric("Apartment class", "Luxury" if predicted_class else "Standard")
    metric_3.metric("Luxury probability", f"{class_probability:.1%}")
    metric_4.metric("Regression R²", f"{regression_result.metrics['R2']:.3f}")


def render_tabs(
    df: pd.DataFrame,
    apartment: ApartmentInput,
    regression_result: RegressionResult,
    classification_result: ClassificationResult,
) -> None:
    tab_overview, tab_regression, tab_classification, tab_data = st.tabs(
        ["Overview", "Regression", "Classification", "Data"]
    )

    with tab_overview:
        left, right = st.columns([1, 1.2])
        with left:
            st.subheader("Selected apartment")
            st.json(apartment)
        with right:
            st.subheader("Dataset summary")
            summary_df = df.describe(include="all").fillna("").astype(str)
            st.dataframe(summary_df, width="stretch")

    with tab_regression:
        st.subheader("Rent prediction model")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("MAE", f"€{regression_result.metrics['MAE']:,.0f}")
        col_b.metric("RMSE", f"€{regression_result.metrics['RMSE']:,.0f}")
        col_c.metric("R²", f"{regression_result.metrics['R2']:.3f}")

        chart_a, chart_b = st.columns(2)
        chart_a.pyplot(plot_rent_distribution(df))
        chart_b.pyplot(plot_actual_vs_predicted(regression_result.y_test, regression_result.y_pred))
        st.pyplot(plot_residuals(regression_result.y_test, regression_result.y_pred))

    with tab_classification:
        st.subheader("Luxury apartment classification")
        st.metric("Accuracy", f"{classification_result.metrics['Accuracy']:.1%}")

        cm = classification_result.metrics["Confusion Matrix"]
        cm_df = pd.DataFrame(
            cm,
            index=["Actual standard", "Actual luxury"],
            columns=["Predicted standard", "Predicted luxury"],
        )
        col_a, col_b = st.columns(2)
        col_a.dataframe(cm_df, width="stretch")
        col_b.pyplot(plot_class_distribution(df))

    with tab_data:
        st.subheader("Synthetic dataset")
        st.dataframe(df.head(100), width="stretch")
        st.download_button(
            "Download dataset as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="berlin_rent_synthetic_data.csv",
            mime="text/csv",
        )


def main() -> None:
    render_header()
    apartment = build_apartment_input()
    n_samples = int(st.session_state["n_samples"])
    random_state = int(st.session_state["random_state"])

    df = load_data(n_samples, random_state)
    regression_result, classification_result = load_models(n_samples, random_state)

    render_prediction_metrics(apartment, regression_result, classification_result)
    render_scope_summary(df)
    st.divider()
    render_tabs(df, apartment, regression_result, classification_result)


if __name__ == "__main__":
    main()
