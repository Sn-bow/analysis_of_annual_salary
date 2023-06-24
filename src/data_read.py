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
