import pandas as pd

def read_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(0)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

def insert_into_mongo(df, collection):
    records = df.to_dict(orient="records")
    if records:
        collection.insert_many(records)
