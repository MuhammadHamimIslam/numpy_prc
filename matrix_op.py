import numpy as np 

matrix1 = np.arange(1, 10).reshape(3, 3)
matrix2 = np.arange(0, 18, 2).reshape(3, 3)

# creating matrix from string 
mt1 = np.matrix("3 0 0; 0 2 0; 0 0 5")
print(mt1)

# creating matrix from array 
# np.matrix(array)
mt2 = np.matrix(matrix1)
print(mt2)

# np.asmatrix(array)
mt3 = np.asmatrix(matrix2)
print(mt3)

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

# inverse matrix 
print(np.linalg.inv(mt1))

# matrix transpose 
print(matrix1.T)

# finding determinet
print(np.linalg.det(matrix1))

# finding eigenvalue, eigenvector
eigenvalues, eigenvector = np.linalg.eig(mt1)
print(f"{eigenvalues = }")
print(f"{eigenvector = }")

# finding svd
S, V, D = np.linalg.svd(matrix1)
print(S)
print(V)
print(D)

# value of a vector 
vector = np.array([5, 12])
norm = np.linalg.norm(vector) # returns the norm of the vector 
print(norm)

# solving linear equations 
B = np.array([6, 4, 15])
X = np.linalg.solve(mt1, B) # solve X for AX=B
print(X)

# computing condition 
cond = np.linalg.cond(mt1)
print(cond)

# solving linear equations 
# 3x + 2y = 5
# x + 2y = 5
# matrix representation -> [5, 5]
# [3  2]
# [1  2] x, y = ?

a = np.array([[3, 2], [1, 2]], dtype=np.int32)
b = np.array([5, 5])

x, y = np.linalg.solve(a, b)
print(x, y) # x and y value 