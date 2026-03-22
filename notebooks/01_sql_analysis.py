import pandas as pd
import sqlite3

# Load data
df = pd.read_csv('data/marketing_data.csv')
print("=== DATASET OVERVIEW ===")
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")
print(f"\nDate range: {df['date'].min()} to {df['date'].max()}")
print(f"Channels: {df['channel'].unique()}")
print(f"Campaign types: {df['campaign_type'].unique()}")
print(f"\nMissing values:\n{df.isnull().sum()}")