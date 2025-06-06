import numpy as np 

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape) # returns array shape -> (column, row)
print(arr.ndim) # returns the dimensions 
print(arr.size) # returns the total number of elements 
print(arr.itemsize) # returns the byte size of the elements 
# calculating total memory 
mem = arr.size * arr.itemsize
print(mem)

# array strides.strides are tuples of integers representing the number of bytes to step in each dimension when traversing an array
print(arr.strides)