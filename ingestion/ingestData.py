import pandas as pd
import os
RAW_DATA_PATH = 'data/ecommerce_data.csv'
STAGED_DATA_PATH = 'data/staged_sales_data.csv'

def ingestData():
    print("Reading raw data:")

    df = pd.read_csv(RAW_DATA_PATH, encoding='ISO-8859-1')
    
    os.makedirs('data', exist_ok=True)
    df.to_csv(STAGED_DATA_PATH, index=False)
    print(f"Staged data saved to: {STAGED_DATA_PATH}")

if __name__ == '__main__':
    ingestData()