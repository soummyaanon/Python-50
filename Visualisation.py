import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.plot(x, y)
plt.title('Line plot')

# Scatter plot
plt.subplot(132)
plt.scatter(x, y)
plt.title('Scatter plot')

# Histogram
plt.subplot(133)
plt.hist(y, bins=20)
plt.title('Histogram')

# Show the plot
plt.tight_layout()
plt.show()