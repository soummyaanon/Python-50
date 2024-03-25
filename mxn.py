import numpy as np

import matplotlib.pyplot as plt

# Create a 2x2 array with values from 1 to 4
d = np.arange(1, 5).reshape(2, 2)
print("2x2 array:\n", d)

# Print the attributes of d
print("Array Shape is:", d.shape, "Array dimensions are", d.ndim, "Length of each element of array in bytes is", d.itemsize)

# Visualize d
plt.imshow(d, origin='upper')  # Displays the array as an image with origin at the upper left corner
plt.colorbar(orientation='vertical')  # Adds a colorbar to the plot
plt.show()  # Shows the plot
