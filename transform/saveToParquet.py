import pandas as pd

CSV_PATH = 'data/transformed_sales_data.csv'
PARQUET_PATH = 'data/sales_data.parquet'

df = pd.read_csv(CSV_PATH)
df.to_parquet(PARQUET_PATH, index=False)
print(f"Saved to {PARQUET_PATH}")