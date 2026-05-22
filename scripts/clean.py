import pandas as pd

VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}

df = pd.read_csv("data/raw/events.csv")

df = df.dropna()

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df.dropna()
df = df[df["duration_seconds"] > 0]
df["duration_seconds"] = df["duration_seconds"].astype(int)

df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna()

df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

df.to_csv("data/clean/events.csv", index=False)