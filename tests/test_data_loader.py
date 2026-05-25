
import pandas as pd
def test_load_data():
    # Load dataset
    df = pd.read_csv(file_path)
    df = load_data("data/machine_learning_data.csv")
    missing = df.isnull().sum().sort_values(ascending=False)
    missing[missing > 0]