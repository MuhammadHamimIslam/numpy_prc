import numpy as np 

arr1 = np.array([2, 1, 0, 3, 0, 8, 3, 7, 4])


# np.argmax() to find out the max element's index
max_ind = np.argmax(arr1) # returns the max element's index
print(arr1[max_ind])

# np.argin() to find out the min element's index
min_ind = np.argmin(arr1) # returns the min element's index
print(arr1[min_ind])

# np.nonzero() to find out the non zero element's index
non_zero = np.nonzero(arr1)
print(arr1[non_zero])

# np.extract() to return the elements satisfying any condition
cond = np.mod(arr1, 2) == 0
print(np.extract(cond, arr1)) # returns the even elements that satisfies the condition 

# np.where() to find elements with specific condition
less_than5= np.where(arr1 <= 5)
print(arr1[less_than5])

# search elements sorting using np.searchsorted()
# np.searchsorted(sorted_array, values, side='left')
sorted_array = np.array([1, 3, 4, 5, 8, 9])
values = np.array([2, 6, 7])

indices = np.searchsorted(sorted_array, values) # returns the indices where elements will be added 
new_sorted_arr = np.insert(sorted_array, indices, values) # adds new elements by sorting 
print(indices)
print(new_sorted_arr)