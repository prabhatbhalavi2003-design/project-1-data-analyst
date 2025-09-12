import pandas as pd
import os


def data_load(path):
    
    # Load student performance data from CSV file

    try:
        if not os.path.exists(path):
            raise FileNotFoundError (f"Data file not found at: {path}")

        df = pd.read_csv(path)
        return df
    
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")
