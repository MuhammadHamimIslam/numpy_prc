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

# swapping an axis
# np.swapaxes(a, axis1, axis2)
arr3 = np.swapaxes(arr1, 0, 1)
print(arr3)

# moving an axis 
# np.moveaxis(array, source, destination)
arr4 = np. moveaxis(arr2, 0, 1)
print(arr4)

# array broadcast 
# np.broadcast(*array)
broadcast_obj = np.broadcast(2, arr1)
for i, j in broadcast_obj:
    print(i, j) # 2 is printed with every item in the array 

# broadcasting an array to a new shape
# np.broadcast_to(array, shape, subok=False)
broadcast_arr = np.broadcast_to(flatten_arr, (3, 6))
print(broadcast_arr)

# adding a new axis or dimension to an array
# np.expand_dims(array, axis)
expanded = np.expand_dims(arr1, axis=1)
print(expanded)