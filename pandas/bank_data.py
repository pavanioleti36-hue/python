import pandas as pd
df= pd.read_csv("bank_dataset.csv")
print(df) 
#highest balance
high_bal= df["Balance"].max()
print(high_bal)
#lowest balance
low_bal= df["Balance"].min()
print(low_bal)
#customers with loan > 5lakh
cus= df[df["Loan"]>500000]
print(cus)
#city wise custo,ers
city= df.groupby("City")
for c, cus in city:
    print(c)
    print(cus)
#total balance
total= df["Balance"].sum()
print(total)     