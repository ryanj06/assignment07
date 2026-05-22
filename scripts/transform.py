import pandas as pd

df = pd.read_csv("data/clean/events.csv")

df["date"] = df["timestamp"].str[:10]

df.to_csv("data/transformed/events.csv", index=False)