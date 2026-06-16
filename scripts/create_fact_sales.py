import pandas as pd

orders = pd.read_csv("s3://ecommerce-olist-dataset/cleaned/orders_clean.csv")

order_items = pd.read_csv(
    "s3://ecommerce-olist-dataset/raw/olist_order_items_dataset.csv"
)

payments = pd.read_csv(
    "s3://ecommerce-olist-dataset/raw/olist_order_payments_dataset.csv"
)

# Orders + Order Items
fact_sales = pd.merge(
    orders,
    order_items,
    on="order_id",
    how="inner"
)

# Add Payments
fact_sales = pd.merge(
    fact_sales,
    payments,
    on="order_id",
    how="inner"
)

print(fact_sales.head())

print(fact_sales.shape)

fact_sales.to_csv(
    "s3://ecommerce-olist-dataset/output/fact_sales.csv",
    index=False
)