import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({"Department":["IT","HR","IT","Finance","HR"],"Salary":[50000,40000,60000,55000,45000]})
summary = df.groupby("Department")["Salary"].mean()
plt.bar(summary.index, summary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()