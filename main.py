import matplotlib.pyplot as plt

x = int(input())

plt.plot([1,2,3,4])
x_vals = [1,2,3,4]
plt.plot(x_vals, label="An awesome line")
plt.ylabel('The y-axis label!')
plt.xlabel('The x-axis label!')
plt.title("The title of the graph!")
plt.legend()
x_vals = [1,2,3,4]
y_vals = [1, 4, 9, 16]
plt.plot(x_vals, y_vals)
plt.show()