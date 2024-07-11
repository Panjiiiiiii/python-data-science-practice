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

#EDA DATA CUSTOMER AND ORDERS
customers_df.describe(include="all")
orders_df.describe(include="all")

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

#EDA DATA PRODUCT AND SALES
product_df.describe(include='all')
sales_df.describe(include='all')

#EDA sort price product
price_product = product_df.sort_values(by="price", ascending=False)
# print(price_product)

#EDA product and type
product_type = product_df.groupby(by="product_type").agg({
    "product_id" : "nunique",
    "quantity" : "sum",
    "price" : ["min", "max"]
})

product_name = product_df.groupby(by="product_name").agg({
    "product_id" : "nunique",
    "quantity" : "sum",
    "price" : ["min", "max"]
})
# print(product_type)
# print(product_name)

#EDA best selling product
sales_product_df = pd.merge(
    left=sales_df,
    right=product_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)
# print(sales_product_df.head())

#EDA sales basic on product
sales_product_type = sales_product_df.groupby(by="product_type").agg({
    'sales_id' : 'nunique',
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(sales_product_type)
sales_product_name = sales_product_df.groupby(by="product_name").agg({
    'sales_id' : 'nunique',
    "quantity_x" : "sum",
    "total_price" : "sum"
}).sort_values(by="total_price", ascending=False).reset_index().head(6)
# print(sales_product_name)

#EDA all data
all_df = pd.merge(
    left=sales_product_df,
    right=order_customer_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
# print(all_df.head())

#EDA preference by state
preference_state = all_df.groupby(by=["state", "product_type"]).agg({
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(preference_state)

#EDA preference by gender
preference_gender = all_df.groupby(by=["gender", "product_type"]).agg({
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(preference_gender)

#EDA preference by age
preference_age = all_df.groupby(by=["age_group", "product_type"]).agg({
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(preference_age)