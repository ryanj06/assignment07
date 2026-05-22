import os
import pandas as pd

os.makedirs("data/transformed", exist_ok=True)

df = pd.read_csv("data/clean/events.csv")

df["date"] = df["timestamp"].str[:10]

df.to_csv(
    "data/transformed/events.csv",
    index=False
)