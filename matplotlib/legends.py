import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5]
y1=[10, 20, 30, 40, 50]
y2=[15, 25, 35, 45, 55]
plt.plot(x,y1, label="product A")
plt.plot(x,y2, label="product B")
plt.legend()
plt.show()