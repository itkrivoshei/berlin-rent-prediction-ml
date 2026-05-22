from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_rent_distribution(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(df["rental_price"], bins=30, edgecolor="black", alpha=0.75)
    ax.set_title("Synthetic Berlin Rent Distribution")
    ax.set_xlabel("Monthly Rent (€)")
    ax.set_ylabel("Apartments")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


def plot_actual_vs_predicted(y_test: pd.Series, y_pred):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.scatter(y_test, y_pred, alpha=0.7)
    min_value = min(float(y_test.min()), float(y_pred.min()))
    max_value = max(float(y_test.max()), float(y_pred.max()))
    ax.plot([min_value, max_value], [min_value, max_value], linestyle="--")
    ax.set_title("Actual vs Predicted Rent")
    ax.set_xlabel("Actual Rent (€)")
    ax.set_ylabel("Predicted Rent (€)")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


def plot_residuals(y_test: pd.Series, y_pred):
    residuals = y_test - y_pred
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.scatter(y_pred, residuals, alpha=0.7)
    ax.axhline(0, linestyle="--")
    ax.set_title("Regression Residuals")
    ax.set_xlabel("Predicted Rent (€)")
    ax.set_ylabel("Residual (€)")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


def plot_class_distribution(df: pd.DataFrame):
    counts = df["luxury"].value_counts().sort_index()
    labels = ["Standard", "Luxury"]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(labels, counts.values)
    ax.set_title("Apartment Class Distribution")
    ax.set_ylabel("Apartments")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    return fig
