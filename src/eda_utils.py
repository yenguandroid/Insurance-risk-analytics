import pandas as pd

def missing_summary(df):
    return (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )