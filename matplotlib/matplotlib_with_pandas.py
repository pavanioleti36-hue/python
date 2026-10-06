import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.DataFrame({    
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [10000, 15000, 12000, 18000] }) 
plt.plot(df["Month"], df["Sales"]) 
plt.title("Monthly Sales") 
plt.xlabel("Month") 
plt.ylabel("Sales") 
plt.show()