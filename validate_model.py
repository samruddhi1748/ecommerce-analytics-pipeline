import pandas as pd

fact = pd.read_csv("../data/cleaned/fact_sales.csv")
customer = pd.read_csv("../data/cleaned/dim_customer.csv")
product = pd.read_csv("../data/cleaned/dim_product.csv")

print("FactSales Rows :", len(fact))
print("DimCustomer Rows :", len(customer))
print("DimProduct Rows :", len(product))

print("Unique Customers in FactSales:",
      fact['customer_id'].nunique())

print("Unique Products in FactSales:",
      fact['product_id'].nunique())