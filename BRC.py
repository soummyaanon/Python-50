import numpy as np
import matplotlib.pyplot as plt

# a) Array manipulation, Searching, Sorting and splitting
# Create a 1D numpy array
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

# Sort the array
arr = np.sort(arr)
print("Sorted Array:", arr)

# Search for a value in the array
index = np.where(arr == 5)
print("Index of 5 in the array:", index)

# Split the array into three
split_arr = np.array_split(arr, 3)
print("Split Array:", split_arr)

# b) Broadcasting and Plotting NumPy array
# Create two numpy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Broadcast the arrays
c = a * b
print("Broadcasted Array:", c)

# Plot the broadcasted array
plt.plot(c)
plt.show()