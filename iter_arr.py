import numpy as np 

array1 = np.array([1, 3, 2, 5, 7, 4])
array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# iterating using for loop 
for i in array1: 
    print(f"arr[{i}] = {i}")

# iterating with indices 
rows, cols = array2.shape
for i in range(rows): 
    for j in range(cols): 
        print(f"array2[{i}, {j}] = {array2[i, j]}")

# iterating using np.nditer()
for i in np.nditer(array2):
    print(i)

# broadcasting iteration 
arr1 = np.array([1, 3, 2])
arr2 = np.array([2, 3, 4])

for i, j in np.nditer([arr1, arr2]): 
    print(i, j)
    print(i + j) # performs matrix addition 

# external loop 
for row in np.nditer(array2, flags=["external_loop"]): # runs a loop and convert the 2d array to 1d
    print(row)

# modifying array value 
print(f"before modifying: {arr1 = }")
with np.nditer(arr1, flags=["buffered"], op_flags=["readwrite"]) as itr: 
    for i in itr: 
        i[...] = i ** 2 # squaring all value 

print(f"after modifying: {arr1 = }")