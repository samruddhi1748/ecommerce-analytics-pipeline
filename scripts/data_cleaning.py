import pandas as pd

# Customers
customers = pd.read_csv("../data/raw/olist_customers_dataset.csv")

# Orders
orders = pd.read_csv("../data/raw/olist_orders_dataset.csv")

# Products
products = pd.read_csv("../data/raw/olist_products_dataset.csv")


# ------------------------
# Customers Cleaning
# ------------------------
customers.drop_duplicates(inplace=True)


# ------------------------
# Orders Cleaning
# ------------------------
orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp']
)

orders['order_approved_at'] = pd.to_datetime(
    orders['order_approved_at']
)

orders['order_delivered_carrier_date'] = pd.to_datetime(
    orders['order_delivered_carrier_date']
)

orders['order_delivered_customer_date'] = pd.to_datetime(
    orders['order_delivered_customer_date']
)


# ------------------------
# Products Cleaning
# ------------------------
products['product_category_name'] = products[
    'product_category_name'
].fillna('Unknown')

products['product_name_lenght'] = products[
    'product_name_lenght'
].fillna(0)

products['product_description_lenght'] = products[
    'product_description_lenght'
].fillna(0)

products['product_photos_qty'] = products[
    'product_photos_qty'
].fillna(0)

products.fillna(0, inplace=True)


# ------------------------
# Save Cleaned Files
# ------------------------
customers.to_csv(
    "../data/cleaned/customers_clean.csv",
    index=False
)

orders.to_csv(
    "../data/cleaned/orders_clean.csv",
    index=False
)

products.to_csv(
    "../data/cleaned/products_clean.csv",
    index=False
)

print("Data Cleaning Completed Successfully")