import matplotlib.pyplot as plt
months = ["January", "February", "March", "April", "May", "June"]
sales2025 = [100, 150, 200, 250, 300, 350]
sales2026 = [120, 180, 220, 280, 320, 400]
plt.plot(months, sales2025, label="Sales 2025", marker='o')
plt.plot(months, sales2026, label="Sales 2026", marker='s')
plt.title("Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()