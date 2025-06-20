import numpy as np 

arr1 = np.array([2, 1, 0, 3, 0, 8, 3, 7, 4])

dt = np.dtype([("name", "S10"), ("age", int)])
arr2 = np.array([("john", 29), ("jane", 34), ("Alex", 28), ("Steve", 31)], dtype=dt)


# sorting an array 
# np.sort(a, axis, kind, order) -> a: array, kind -> sorting algorithm, order -> order of fields to be sorted
sorted_arr = np.sort(arr1)
print(sorted_arr)

# sorting by name
sorted_by_name = np.sort(arr2, order="name")
print(sorted_by_name)

# sorting with np.argsort()
arg_sort = np.argsort(arr1)
print(arg_sort) # returns the indexes sorting
print(arr1[arg_sort])

# sorting with np.lexsort()
names = np.array(["John", "Steve", "Alex", "Jane"])
ages = np.array([29, 31, 28, 34])

indices = np.lexsort((names, ages)) # sort by name then sort by age
print(names[indices])
print(ages[indices])

# partial sorting 
# np.partition(array, kth) sorts the array so that kth element becomes the kth smallest element 
np.partition(arr1, 4) # sorts the array as 4th element becomes the 4th smallest 
print(arr1)