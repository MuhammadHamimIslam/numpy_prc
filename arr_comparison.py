import numpy as np 

arr1 = np.array([10, 23, 18, 34, 29, 34, 90])
arr2 = np.array([20, 34, 56, 78, 25, 34, 91])

# element wise comparison 
equality = arr1 == arr2
inequality = arr1 != arr2
greater_than = arr1 > arr2
less_than = arr1 < arr2

print(equality) # returns True or False for element comparison 
print(inequality)
print(greater_than)
print(less_than)

even = arr1 % 2 == 0
print(even)

# comparison with scalar 
greater_than_40 = arr2 > 40
print(greater_than_40)

# finding minimum and maximum values
max_arr = np.maximum(arr1, arr2) 
min_arr = np.minimum(arr1, arr2)

print(max_arr)
print(min_arr)