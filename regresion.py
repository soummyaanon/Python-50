import numpy as np 
import matplotlib.pyplot as plt

x = np.random.rand(100, 1)
y = 2+3 * np.random.rand(100,1)
slope = np.sum((x-np.mean(x)) * (y-np.mean(y))) /np.sum((x-np.mean(x))**2)

intercept = np.mean(y) - slope * np.mean(x)

plt.scatter(x, y)
plt.plot(x, slope* x + intercept ,color = 'red')
plt.show()