import pandas as pd

df = pd.read_csv('data/ecommerce_data.csv', encoding = 'ISO-8859-1')

print(f"Rows: {len(df)}")
print("Columns:", df.columns.tolist())
print(df.head())