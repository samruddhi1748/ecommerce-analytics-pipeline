import pandas as pd

# Customers
#customers = pd.read_csv("../data/raw/olist_customers_dataset.csv")

#print(customers.info())
#print(customers.isnull().sum())
#print(customers.duplicated().sum())

# Orders
orders = pd.read_csv("s3://ecommerce-olist-dataset/raw/olist_orders_dataset.csv")

#print(orders.info())
#print(orders.isnull().sum())
#print(orders.duplicated().sum())

# Products
#products = pd.read_csv("../data/raw/olist_products_dataset.csv")

#print(products.info())
#print(products.isnull().sum())
#print(products.duplicated().sum())

# Order Items
order_items = pd.read_csv("s3://ecommerce-olist-dataset/raw/olist_order_items_dataset.csv")

print(order_items.info())
print(order_items.isnull().sum())
print(order_items.duplicated().sum())

# Payments
payments = pd.read_csv("s3://ecommerce-olist-dataset/raw/olist_order_payments_dataset.csv")

print(payments.info())
print(payments.isnull().sum())
print(payments.duplicated().sum())