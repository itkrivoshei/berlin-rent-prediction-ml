from __future__ import annotations

import numpy as np
import pandas as pd

LOCATIONS = ["Mitte", "Friedrichshain", "Kreuzberg", "Neukölln", "Charlottenburg"]
FEATURE_COLUMNS = [
    "location",
    "size_sqm",
    "num_rooms",
    "distance_to_transport",
    "age_of_building",
]
TARGET_RENT = "rental_price"
TARGET_CLASS = "luxury"

LOCATION_PREMIUM = {
    "Mitte": 420,
    "Friedrichshain": 280,
    "Kreuzberg": 260,
    "Charlottenburg": 310,
    "Neukölln": 120,
}


def generate_housing_data(n_samples: int = 1_000, random_state: int = 42) -> pd.DataFrame:
    """Generate a reproducible synthetic Berlin apartment dataset.

    The dataset is intentionally synthetic. It is useful for demonstrating a full
    regression/classification workflow without depending on external APIs.
    """
    rng = np.random.default_rng(random_state)

    location = rng.choice(LOCATIONS, n_samples)
    size_sqm = rng.uniform(20, 150, n_samples).round(1)
    num_rooms = rng.integers(1, 6, n_samples)
    distance_to_transport = rng.uniform(0.1, 5.0, n_samples).round(2)
    age_of_building = rng.integers(1, 101, n_samples)

    df = pd.DataFrame(
        {
            "location": location,
            "size_sqm": size_sqm,
            "num_rooms": num_rooms,
            "distance_to_transport": distance_to_transport,
            "age_of_building": age_of_building,
        }
    )

    location_effect = df["location"].map(LOCATION_PREMIUM).astype(float)
    noise = rng.normal(0, 85, n_samples)

    df[TARGET_RENT] = (
        11.5 * df["size_sqm"]
        + 115 * df["num_rooms"]
        - 55 * df["distance_to_transport"]
        - 1.9 * df["age_of_building"]
        + location_effect
        + noise
    ).round(2)

    luxury_threshold = df[TARGET_RENT].quantile(0.70)
    df[TARGET_CLASS] = (df[TARGET_RENT] >= luxury_threshold).astype(int)

    return df
