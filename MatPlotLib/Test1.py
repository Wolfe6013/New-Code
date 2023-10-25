import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data with customizations
ax.plot(x, y, color='red', linestyle='-', label='Sine Curve')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Customized Sine Curve Plot')
ax.legend()

# Display the plot
plt.show()