import numpy as np
import matplotlib.pyplot as plt

d = np.arange(1, 15).reshape(2, 7)
print(d)   # 2x7 array
plt.imshow(d)
plt.colorbar(orientation='vertical')
plt.show()

print("Printing numpy array Attributes")
print("1> Array Shape is: ", d.shape)
print("2>. Array dimensions are ", d.ndim)
print("3>. Length of each element of array in bytes is ", d.itemsize)