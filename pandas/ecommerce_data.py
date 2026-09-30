import pandas as pd
df= pd.read_csv("ecommerce_dataset.csv")
print(df)
#most expensive product
exp= df.loc[df["price"].idxmax()]
print(exp["product"], exp["price"])
#cheapest product
cheap= df.loc[df["price"].idxmin()]
print(cheap["product"], cheap["price"])
#average rating
avg= df["rating"].mean()
print("average rating:", avg)
#category wise products
for cat, pro in df.groupby("category"):
    print(cat)
    print(pro)
#total inventory value
te_value= (df["price"]*df["quantity"].sum())
print(te_value)