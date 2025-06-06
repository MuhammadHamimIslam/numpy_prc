import numpy as np


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2], [3, 4]])
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr4 = np.array([1, 3, 3+2j, 2j, 3-2j, 9+4j])
srch = np.array([1, 0])


print(arr1[0]) # getting the element of 1st index 

print(arr2[1][1]) # accessing 2D array 
print(arr2[1, 1]) # does the same as previous 

print(arr3[0][1][0]) # accessing 3D array 
print(arr3[0, 1, 0]) # does the same as previous 

print(arr1[0:3]) # slicing elements from 0 to 3(exclusive)

print(arr1[0:5:2]) # slicing elements from 0 to 3(exclusive) step 2

print(arr1[::2]) # returns every other element from the entire array

print(arr1[::-1]) # reverse the array 

# slicing an array 
s = slice(1, 2)
slc_arr = arr3[s]
print(slc_arr)

# Ellipsis
print(arr3[..., 1]) # returns the items in the 2nd column 
print(arr3[1, ...]) # returns the items in 2nd row

# boolean indexing 
print(arr2[(arr2 % 2) != 0]) # returns only the odd elements 

# filtering complex number 
print(arr4[np.iscomplex(arr4)]) # returns only the complex numbers 

# fancy indexing 
print(arr3[srch])

