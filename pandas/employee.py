import pandas as pd
df= pd.read_csv("emp_data.csv")
print(df)
print(df.head())
print(df.tail())
print(df.columns)
print("shapes:",df.shape)
print(df.info())
print(df.describe())
print(df["Name"])
print(df.iloc[0])
print(df[0:3])
sal= df[df["salary"] > "50000"]
print(sal)