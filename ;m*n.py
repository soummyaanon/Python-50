import numpy as np
import matplotlib.pyplot as plt

# Create an m x n integer array
m, n = 5, 10  # Replace with your desired dimensions
arr = np.random.randint(0, 100, size=(m, n))

# Print the array's attributes
print("Array Shape:", arr.shape)
print("Array Dimensions:", arr.ndim)
print("Array Size:", arr.size)
print("Array Data Type:", arr.dtype)

# Visualize the array
plt.imshow(arr, cmap='viridis')
plt.colorbar(label='Value')
plt.title('Array Visualization')
plt.show()