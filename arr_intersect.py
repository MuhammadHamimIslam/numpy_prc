import numpy as np
from functools import reduce

arr1 = np.array([1, 2, 3, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7, 5])
arr3 = np.array([1, 3, 5, 7, 9, 7])
# finding intersection 
# np.intersect1d(ar1, ar2, assume_unique=False, return_indices=False)
intersection1 = np.intersect1d(arr1, arr2)
print(intersection1)

# assuming unique for faster computation 
intersection2 = np.intersect1d(arr1, arr2, assume_unique=True)
print(intersection2)

# returning indexes 
intersect, index1, index2 = np.intersect1d(arr1, arr2, return_indices=True) # return intersection, indexes for array1 and array2

print(intersect)
print(index1)
print(index2)

# intersection for more than 2 arrays
# there's no built-in way to do this 
# using reduce to reduce the value with intersect1d function 
inters = reduce(np.intersect1d, (arr1, arr2, arr3))
print(inters)