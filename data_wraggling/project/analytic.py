import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
customers_df.head()

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
orders_df.head()

product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
product_df.head()

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
sales_df.head()

#gathering data
print(customers_df.info())
print(customers_df.isna().sum())
print("Jumlah diplikasi data: ", customers_df.duplicated().sum())
print(customers_df.describe())

print(orders_df.info())
print("Jumlah diplikasi data: ", orders_df.duplicated().sum())
print(orders_df.describe())

print(product_df.info())
print("Jumlah diplikasi data: ", product_df.duplicated().sum())


print(sales_df.info())
print(sales_df.isna().sum())
print("Jumlah diplikasi data: ", sales_df.duplicated().sum())
print(sales_df.describe())

#cleaning data
customers_df.drop_duplicates(inplace=True)
print("Jumlah duplikasi setelah cleaning: ", customers_df.duplicated().sum())
customers_df[customers_df.gender.isna()]
print(customers_df.gender.value_counts())
customers_df[customers_df.age == customers_df.age.max()]
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)
customers_df[customers_df.age == customers_df.age.max()]
customers_df.age.replace(customers_df.age.max(), 50, inplace=True)
print(customers_df.describe())

datetime_columns = ["order_date", "delivery_date"]
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column])
print(orders_df.info())
product_df.drop_duplicates(inplace=True)
print("Jumlah duplikasi setelah cleaning", product_df.duplicated().sum())

print(sales_df[sales_df.total_price.isna()])
sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"]
print(sales_df.isna().sum())