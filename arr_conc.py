import numpy as np 


arr1 = np.arange(5)
arr2 = np.arange(5, 11)
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])
arr5 = np.array([6, 8, 10])
# concatenating arrays
# np.concatenate((a1, a2, ...), axis=0, out=None)
conc_arr = np.concatenate((arr1, arr2))
print(conc_arr)

# Concatenating Arrays Along Rows
conc_rows = np.concatenate((arr3, arr4), axis=0)
print(conc_rows)

# Concatenating Arrays Along Columns
conc_col = np.concatenate((arr3, arr4), axis=1)
print(conc_col)

# Concatenating Arrays with Mixed Dimensions
exapnd_arr5 = np.expand_dims(arr5, axis=0)
concatenated_arr = np.concatenate((exapnd_arr5, arr3))
print(concatenated_arr)

# Concatenating Arrays Using stack()
# np.stack(arrays, axis=0)
stck_arr = np.stack((arr1, arr2)) # adds a new axis at the specified position to the arrays being stacked
print(stck_arr)