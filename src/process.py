
import pandas as pd

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("data/dados.csv", index=False)


def analyze_data():
    df = pd.read_csv("data/dados.csv")

    top = df.sort_values(by="current_price", ascending=False).head(5)

    return top[["name", "current_price"]]