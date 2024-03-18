import matplotlib.pyplot as plt
import numpy as np

# Create simple data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])  # y is the square of x

# Line plot
plt.figure(figsize=(15, 3))
plt.subplot(151)
plt.plot(x, y)
plt.title('Line plot')

# Bar plot
plt.subplot(154)
plt.bar(x, y)
plt.title('Bar plot')

# Pie chart
plt.subplot(155)
labels = ['1', '2', '3', '4', '5']
plt.pie(y, labels=labels, autopct='%1.1f%%')
plt.title('Pie chart')
plt.show()