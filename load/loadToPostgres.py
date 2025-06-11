import pandas as pd
import psycopg2

DB_NAME = "retail"
DB_USER = "zohair"
DB_PASSWORD = "bhaiarox"
DB_HOST = "localhost"
DB_PORT = "5432"

def load_to_postgres():
    df = pd.read_csv('data/transformed_sales_data.csv')

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
                invoice_no TEXT,
                stock_code TEXT,
                description TEXT,
                quantity INTEGER,
                invoice_date TIMESTAMP,
                unit_price NUMERIC,
                customer_id TEXT,
                country TEXT,
                total_price NUMERIC, 
                invoice_year INTEGER,
                invoice_month INTEGER,
                invoice_day INTEGER
            );
    """)
    conn.commit()

    for _, row in df.iterrows():
        cur.execute("""INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tuple(row))

    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded into postgres")

if __name__ == "__main__":
    load_to_postgres()