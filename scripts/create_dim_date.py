import pandas as pd

orders = pd.read_csv(
    "s3://ecommerce-olist-dataset/cleaned/orders_clean.csv"
)

orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp']
)

dim_date = pd.DataFrame()

dim_date['date'] = orders[
    'order_purchase_timestamp'
].dt.date

dim_date['year'] = orders[
    'order_purchase_timestamp'
].dt.year

dim_date['month'] = orders[
    'order_purchase_timestamp'
].dt.month

dim_date['day'] = orders[
    'order_purchase_timestamp'
].dt.day

dim_date = dim_date.drop_duplicates()

dim_date.to_csv(
    "s3://ecommerce-olist-dataset/output/dim_date.csv",
    index=False
)

print(dim_date.shape)