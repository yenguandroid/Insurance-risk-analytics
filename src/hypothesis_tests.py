# Create Reusable Statistical Functions

from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
import pandas as pd


def run_ttest(group_a, group_b):
    """
    Perform independent t-test between two groups.
    """

    stat, p_value = ttest_ind(
        group_a,
        group_b,
        nan_policy='omit'
    )

    return {
        "test": "Independent T-Test",
        "p_value": p_value,
        "decision": (
            "Reject H0"
            if p_value < 0.05
            else "Fail to Reject H0"
        )
    }


def run_chi_square(contingency_table):
    """
    Perform Chi-Square test.
    """

    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    return {
        "test": "Chi-Square",
        "p_value": p_value,
        "decision": (
            "Reject H0"
            if p_value < 0.05
            else "Fail to Reject H0"
        )
    }


def calculate_margin(df):
    """
    Calculate insurance margin.
    """

    df["Margin"] = (
        df["TotalPremium"] - df["TotalClaims"]
    )

    return df


def create_claim_indicator(df):
    """
    Create binary claim indicator.
    """

    df["HasClaim"] = (
        df["TotalClaims"] > 0
    ).astype(int)

    return df