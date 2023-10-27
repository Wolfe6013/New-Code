import matplotlib.pyplot as plt

# Initial data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 12]

# Create a line chart
plt.plot(x, y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line Chart")

# Display the plot
plt.show()

# Update the data
new_y = [5, 12, 10, 15, 8]

# Clear the previous plot
plt.clf()

# Update the plot with new data
plt.plot(x, new_y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Updated Line Chart")

# Display the updated plot
plt.show()