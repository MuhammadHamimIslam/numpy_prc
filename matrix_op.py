import numpy as np 

matrix1 = np.arange(1, 10).reshape(3, 3)
matrix2 = np.arange(0, 18, 2).reshape(3, 3)

# matrix addition 
print(matrix1 + matrix2)

# matrix subtraction 
print(matrix1 - matrix2)

# matrix multiplication 
print(np.dot(matrix1, matrix2)) # A × B
print(matrix1 @ matrix2) # A × B
print(np.matmul(matrix1, matrix2)) # A × B
print(np.dot(matrix2, matrix1)) # B × A
print(matrix2 @ matrix1) # B × A
print(np.matmul(matrix2, matrix1)) # B × A

# scalar multiplication 
print(matrix1 * 2)

# element wise multiplication 
print(matrix1 * matrix2)

# materix division 