import pandas as pd

def load_dataset():
    dataset_path = "data/Dataset.csv"
    return pd.read_csv(dataset_path)

def load_users():
    users_path = "data/users.xlsx"
    try:
        return pd.read_excel(users_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["username", "hashed_password"])
