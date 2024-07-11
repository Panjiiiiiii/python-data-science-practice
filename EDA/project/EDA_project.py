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

customers_df.describe(include="all")

#EDA group by gender
group_by_gender = customers_df.groupby(by="gender").agg({
    "customer_id" : "nunique",
    "age" : ["max", "min", "mean", "std"]
})
# print(group_by_gender)

#EDA by group by city and state
group_by_city = customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False)
group_by_state = customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=True)
# print(group_by_city)
# print(group_by_state)

#EDA by delivery time
# delivery_time = orders_df['delivery_date'] - orders_df['order_date']
# delivery_time = delivery_time.apply(lambda x: x.total_seconds())
# orders_df["delivery_time"] = round(delivery_time/86400)

#EDA by active user
customers_id_in_orders_df = orders_df.customer_id.tolist()
customers_df["status"] = customers_df["customer_id"].apply(lambda x: "Active" if x in customers_id_in_orders_df else "Non Active")
active_pivot_table = customers_df.groupby("status").customer_id.count()
# print(active_pivot_table)

#EDA JOIN ORDER_DF AND CUSTOMER_DF
order_customer_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
# print(order_customer_df.head())

#EDA COUNT DATA ORDER BY CITY
group_by_city = order_customer_df.groupby(by="city").order_id.nunique().sort_values(ascending=False).reset_index().head(10)
#print(group_by_city)

#EDA COUNT DATA ORDER BY STATE
group_by_state = order_customer_df.groupby(by="state").order_id.nunique().sort_values(ascending=False)
# print(group_by_state)

#EDA COUNT DATA ORDER BY GENDER
group_by_gender = order_customer_df.groupby(by="gender").order_id.nunique().sort_values(ascending=False)
# print(group_by_gender)

#EDA COUNT DATA ORDER BY AGE
order_customer_df["age_group"] = order_customer_df.age.apply(lambda x: "Youth" if x <= 24 else ("Seniors" if x > 64 else "Adults"))
group_by_age = order_customer_df.groupby(by="age_group").order_id.nunique().sort_values(ascending=False)
# print(group_by_age)