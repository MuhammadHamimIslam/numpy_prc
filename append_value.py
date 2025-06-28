import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
arr3 = np.array([[1, 2], [4, 5], [7, 8]])

# "numpy array has a fixed size so adding value to an existing array isn't possible. We can add value by creating new array" 

# adding value to 1D array 
# np.append(arr, values, axis=None)
new_arr1 = np.append(arr1, [6, 8, 7, 9])
print(new_arr1)

# appending row to 2D array 
# np.vstack(tup)
rows = np.array([[7, 8], [9, 10]])
new_arr2 = np.vstack((arr2, rows))
print(new_arr2)

# adding column to 2D array 
# np.hstack(tup)
cols = np.array([[3], [6], [9]])
new_arr3 = np.hstack((arr3, cols))
print(new_arr3)