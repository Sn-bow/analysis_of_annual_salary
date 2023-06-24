import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
URL = os.environ.get("START_URL")
print("====" * 30)
print("\n\n\n\n")
print(URL)

print("\n\n\n\n")
df = pd.read_csv("./static/data/major_early_data.csv", thousands = ',')
print(df)
print("\n\n\n\n")
print("====" * 30)

print(df.isna())
# print(df.dropna())
print(df)
df["High Meaning %"] = df['High Meaning %'].fillna(0)
print(df)

# a = df[["Major","id","Early Career Pay", "Mid-Career Pay", "High Meaning %"]].groupby(by="Major").mean()
# print(a)
