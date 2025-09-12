import pandas as pd



def data_load(path):
    df = pd.read_csv(path)
    return df