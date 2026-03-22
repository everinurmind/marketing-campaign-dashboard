import pandas as pd
import sqlite3

# Load data
df = pd.read_csv('data/marketing_data.csv')
print("=== DATASET OVERVIEW ===")
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")
print(f"\nFirst row:\n{df.head(1)}")