import pandas as pd
import streamlit as st

DATA_PATH = 'data/transformed_sales_data.csv'

# Load Data

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()
    
# Visual

def revenueByCountry(df):
    st.subheader("Revenue by Country")
    revenue = df.groupby('country')['total_price'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(revenue)

def monthlySalesTrend(df):
    st.subheader("Monthly Sales Trend")
    df['period'] = df['invoice_year'].astype(str) + '-' + df['invoice_month'].astype(str).str.zfill(2)
    monthly_sales = df.groupby('period')['total_price'].sum()
    st.line_chart(monthly_sales)

def topCustomers(df):
    st.subheader("Top Customers by Revenue")
    if 'customerid' in df.columns:
        customers = df.groupby('customerid')['total_price'].sum().sort_values(ascending=False).head(10)
        st.bar_chart(customers)
    else:
        st.warning("Column 'customerid' not found in dataset.")



# Main

def main():
    st.set_page_config(page_title="Retail Dashboard", layout="wide")
    st.title("Retail Sales Dashboard")
    st.write("Explore cleaned and transformed retail sales data.")

    df = load_data(DATA_PATH)
    if df.empty:
        return
    
    with st.sidebar:
        st.header("Filters")
        countries = df['country'].dropna().unique()
        selected = st.multiselect("Filter by Country", options=sorted(countries), default=sorted(countries))
        df = df[df['country'].isin(selected)]
    
    # KPIs

    st.markdown("## Key Metrics")

    total_revenue = df['total_price'].sum()
    total_orders = df['invoiceno'].nunique()
    unique_customer = df['customerid'].nunique()
    avgOrderValue = total_revenue / total_orders

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", f"${total_revenue:.2f}")
    col2.metric("Total Orders", f"{total_orders}")
    col3.metric("Unique Customers", f"{unique_customer}")
    col4.metric("Avg Order Value", f"${avgOrderValue:,.2f}")
    # Tabs

    tab1, tab2, tab3 = st.tabs(["Revenue by Country", "Monthly Sales", "Top Customers"])
    
    with tab1:
        revenueByCountry(df)
    with tab2:
        monthlySalesTrend(df)
    with tab3:
        topCustomers(df)

if __name__ == '__main__':
    main()