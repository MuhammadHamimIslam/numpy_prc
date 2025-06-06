import numpy as np 

arr1 = np.arange(10)
arr2 = np.arange(1, 10).reshape(3, 3)


# splitting an array 
# nup.split(array, indices_or_sections, axis=0)
split_arr = np.split(arr1, 2) # splits into 2 equal sub arrays 
print(split_arr)

# Splitting Arrays Using array_split() which allows unequal split 
# np.array_split(array, indices_or_sections, axis=0)
sp_arr = np.array_split(arr1, 3)
print(sp_arr)

#Horizontal Splitting
# np.hsplit(array, indices_or_sections)
h_split = np.hsplit(arr2, 3)
print(h_split)

# Vertical Splitting
# np.vsplit(array, indices_or_sections)
v_split = np.vsplit(arr2, 3)
print(v_split)