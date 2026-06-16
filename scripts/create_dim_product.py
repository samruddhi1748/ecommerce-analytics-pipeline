import pandas as pd

products = pd.read_csv(
    "s3://ecommerce-olist-dataset/cleaned/products_clean.csv"
)

dim_product = products[
    [
        'product_id',
        'product_category_name',
        'product_weight_g',
        'product_length_cm',
        'product_height_cm',
        'product_width_cm'
    ]
]

dim_product.to_csv(
    "s3://ecommerce-olist-dataset/output/dim_product.csv",
    index=False
)

print(dim_product.shape)