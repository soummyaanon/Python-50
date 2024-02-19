import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 0, 1, 5, 8, 9, 3, 4, 5])

# Reshape b to be a 3x3 array
b = b.reshape(3, 3)

print ("\nPrinting array a:")
print (a)
print ("\nPrinting array b:")
print(b)
print ("\nPrinting array a+b:")
c = a+b
print (c)