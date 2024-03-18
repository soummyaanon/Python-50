import numpy as np

import matplotlib.pyplot as plt

# Create a 2x2 array with values from 1 to 4
d = np.arange(1, 5).reshape(2, 2)
print("2x2 array:\n", d)

# Print the attributes of d
print("Array Shape is: ", d.shape)  # Prints the shape of the array (2, 2)
print("Array dimensions are ", d.ndim)  # Prints the number of dimensions of the array (2)
print("Length of each element of array in bytes is ", d.itemsize)  # Prints the size of each element in bytes (4)

# Visualize d
plt.imshow(d)  # Displays the array as an image
plt.colorbar(orientation='vertical')  # Adds a colorbar to the plot
plt.show()  # Shows the plot
