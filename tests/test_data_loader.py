import pandas as pd

# Define dataset path
file_path = "data/MachineLearningRating_v3_cleaned.csv"

def test_load_data():
    # Load dataset
    df = pd.read_csv(file_path)

    # Ensure dataset is not empty
    assert not df.empty

    # Ensure dataframe exists
    assert df is not None