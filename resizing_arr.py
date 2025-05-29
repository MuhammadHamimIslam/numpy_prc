import numpy as np

arr1 = np.array([[1, 2, 3],  [4, 5, 6]])

# reshaping array with same data
# np.reshape(array, newsize, order="C")
arr2 = np.reshape(arr1, (3, 2))
print(arr2)

# flating array (2d, 3d -> 1d)
flat = arr1.flat # returns an flaten iterator
for elm in flat:
    print(elm)

# new flatten array 
# array.flatten(order="C")
flatten_arr = arr1.flatten()
print(flatten_arr)

# np.ravel(array, order="C")
raveled = np.ravel(arr1)
print(raveled)

# making transpose array 
# np.transpose(array, axes=None)
transpose1 = np.transpose(arr1)
print(transpose1)

# array.T
transpose2 = arr1.T
print(transpose2)