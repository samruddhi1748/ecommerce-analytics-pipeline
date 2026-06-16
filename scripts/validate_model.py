import pandas as pd

fact = pd.read_csv("s3://ecommerce-olist-dataset/output/fact_sales.csv")
customer = pd.read_csv("s3://ecommerce-olist-dataset/output/dim_customer.csv")
product = pd.read_csv("s3://ecommerce-olist-dataset/output/dim_product.csv")

print("FactSales Rows :", len(fact))
print("DimCustomer Rows :", len(customer))
print("DimProduct Rows :", len(product))

print("Unique Customers in FactSales:",
      fact['customer_id'].nunique())

print("Unique Products in FactSales:",
      fact['product_id'].nunique())