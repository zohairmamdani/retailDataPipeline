import pandas as pd
import os

STAGED_PATH = 'data/staged_sales_data.csv'
TRANSFORMED_PATH = 'data/transformed_sales_data.csv'

def transformData():
    print("Loading staged data...")
    df = pd.read_csv(STAGED_PATH)

    #standardize columns
    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

    #parse datetime
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])

    #create total_price column
    df['total_price'] = df['quantity'] * df['unitprice']

    #add day, month, year
    df['invoice_year'] = df['invoicedate'].dt.year
    df['invoice_month'] = df['invoicedate'].dt.month
    df['invoice_day'] = df['invoicedate'].dt.day

    #save data
    os.makedirs('data', exist_ok=True)
    df.to_csv(TRANSFORMED_PATH, index=False)
    print(f"Transformed data saved to: {TRANSFORMED_PATH}")

if __name__ == '__main__':
    transformData()