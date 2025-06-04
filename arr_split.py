import numpy as np 

arr1 = np.arange(10)

# splitting an array 
# nup.split(array, indices_or_sections, axis=0)
split_arr = np.split(arr1, 2) # splits into 2 equal sub arrays 
print(split_arr)

