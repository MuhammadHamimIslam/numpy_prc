import numpy as np 

arr1 = np.array([1, 3, 4, 5])
arr2 = np.array([2, 4, 5, 6])
arr3 = np.array([1, 6, 7, 8, 9])

arr4 = np.array(([1, 2], [3, 5]))
arr5 = np.array(([3, 4], [5, 6]))

# union of two 1d array 
# np.union1d(arr1, arr2)
union1d = np.union1d(arr1, arr2)
print(union1d)

# union of multiple arrays using temporary union
union_mul1 = np.union1d(union1d, arr3) # used union1d because it's the union of 2 arrays 
print(union_mul1)

# union of multiple arrays using np.concatenate()
all_arr = np.concatenate((arr1, arr2, arr3)) # concatenate all arrays
union_mul2 = np.unique(all_arr) # find out the unique elements to compute union
print(union_mul2)

# handling union of multiple dimensions 
# first flatten 2 arrays 
flatten_arr4 = arr4.flatten()
flatten_arr5 = arr5.flatten()

union_result = np.union1d(flatten_arr4, flatten_arr5) # now perform union to tje flatten arrays 
print(union_result)