import numpy as np
import matplotlib.pyplot as plt

# Create a 3x5 array with values from 1 to 15
d1 = np.arange(1, 16).reshape(3, 5)
print("3x5 array:\n", d1)

# Create a 5x3 array with values from 16 to 31
d2 = np.arange(16, 31).reshape(5, 3)
print("\n5x3 array:\n", d2)

# Create a 4x4 array with values from 32 to 48
d3 = np.arange(32, 48).reshape(4, 4)
print("\n4x4 array:\n", d3)

# Visualize and print the attributes of d1
print("\nVisualizing and printing the attributes of d1:")
plt.imshow(d1)
plt.colorbar(orientation='vertical')
plt.show()
print("1> Array Shape is: ", d1.shape)
print("2>. Array dimensions are ", d1.ndim)
print("3>. Length of each element of array in bytes is ", d1.itemsize)

# Visualize and print the attributes of d2
print("\nVisualizing and printing the attributes of d2:")
plt.imshow(d2)
plt.colorbar(orientation='vertical')
plt.show()
print("1> Array Shape is: ", d2.shape)
print("2>. Array dimensions are ", d2.ndim)
print("3>. Length of each element of array in bytes is ", d2.itemsize)

# Visualize and print the attributes of d3
print("\nVisualizing and printing the attributes of d3:")
plt.imshow(d3)
plt.colorbar(orientation='vertical')
plt.show()
print("1> Array Shape is: ", d3.shape)
print("2>. Array dimensions are ", d3.ndim)
print("3>. Length of each element of array in bytes is ", d3.itemsize)