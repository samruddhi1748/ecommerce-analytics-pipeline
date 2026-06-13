import pandas as pd

customers = pd.read_csv(
    "../data/cleaned/customers_clean.csv"
)

dim_customer = customers[
    [
        'customer_id',
        'customer_unique_id',
        'customer_city',
        'customer_state'
    ]
]

dim_customer.to_csv(
    "../data/cleaned/dim_customer.csv",
    index=False
)

print(dim_customer.shape)