"""Starter ETL pipeline for NST DVA Capstone 2.

Adapted for the Zomato Delivery Operations Analytics dataset.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd
import numpy as np

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to a clean snake_case format."""
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    result = df.copy()
    result.columns = cleaned
    return result

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply a few safe default cleaning steps."""
    result = normalize_columns(df)
    result = result.drop_duplicates().reset_index(drop=True)

    for column in result.select_dtypes(include="object").columns:
        result[column] = result[column].astype("string").str.strip()

    return result

def custom_zomato_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply Zomato-specific cleaning and feature engineering."""
    
    # 1. Fix typos (using new snake_case column names)
    df.rename(columns={'time_orderd': 'time_ordered'}, inplace=True)
    df['city'] = df['city'].str.replace('Metropolitian', 'Metropolitan')

    # 2. Fill missing values (Numerical)
    num_cols = ['delivery_person_age', 'delivery_person_ratings', 'multiple_deliveries']
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    # 3. Fill missing values (Categorical)
    cat_cols = ['weather_conditions', 'road_traffic_density', 'festival', 'city', 'time_ordered']
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # 4. Datetime & Type conversions
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
    df['time_ordered'] = df['time_ordered'].astype(str)
    df['time_order_picked'] = df['time_order_picked'].astype(str)

    # 5. Feature Engineering
    df['order_day'] = df['order_date'].dt.day
    df['order_month'] = df['order_date'].dt.month
    df['order_year'] = df['order_date'].dt.year
    df['day_of_week'] = df['order_date'].dt.day_name()

    # Extract order hour and handle the resulting NaNs
    df['order_hour'] = pd.to_datetime(df['time_ordered'], format='%H:%M', errors='coerce').dt.hour
    df['order_hour'] = df['order_hour'].fillna(df['order_hour'].median())

    return df

def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Read a raw CSV file and return a cleaned dataframe."""
    df = pd.read_csv(input_path)
    df = basic_clean(df)
    df = custom_zomato_clean(df)
    return df

def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Write the cleaned dataframe to disk, creating the parent folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Capstone 2 starter ETL pipeline.")
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the raw CSV file in data/raw/.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to the cleaned CSV file in data/processed/.",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    cleaned_df = build_clean_dataset(args.input)
    save_processed(cleaned_df, args.output)
    print(f"Processed dataset saved to: {args.output}")
    print(f"Rows: {len(cleaned_df)} | Columns: {len(cleaned_df.columns)}")
    print(f"Remaining Missing Values:\n{cleaned_df.isnull().sum()[cleaned_df.isnull().sum() > 0]}")

if __name__ == "__main__":
    main()