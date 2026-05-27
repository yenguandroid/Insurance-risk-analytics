# src/feature_engineering.py

import pandas as pd


def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract date-based features from TransactionMonth.
    """

    df = df.copy()

    df["TransactionMonth"] = pd.to_datetime(df["TransactionMonth"])

    df["PolicyYear"] = df["TransactionMonth"].dt.year
    df["PolicyMonth"] = df["TransactionMonth"].dt.month

    return df


def create_vehicle_age(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create vehicle age feature.
    """

    df = df.copy()

    if "VehicleIntroDate" in df.columns:
        df["VehicleIntroDate"] = pd.to_datetime(df["VehicleIntroDate"])
        df["VehicleIntroYear"] = df["VehicleIntroDate"].dt.year
        df["VehicleAge"] = 2026 - df["VehicleIntroYear"]

    return df


def create_target_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create ML targets and financial KPIs.
    """

    df = df.copy()

    # Claim indicator (classification target)
    df["HasClaim"] = (df["TotalClaims"] > 0).astype(int)

    # Margin
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    return df


def run_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Master function to run all feature engineering steps.
    """

    df = create_time_features(df)
    df = create_vehicle_age(df)
    df = create_target_features(df)

    return df