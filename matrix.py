import numpy as np

# Create a 2x2 matrix
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7,8], [9,10], [11,12]])


result_matrix = matrix_a @ matrix_b

print("Matrix A:")
print(matrix_a)

print("matrix B:")
print(matrix_b)

print("\nresult of Matrix Multiplivcation (A * B):") #
print(result_matrix )


