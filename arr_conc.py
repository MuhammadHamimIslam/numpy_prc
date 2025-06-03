import numpy as np 


arr1 = np.arange(5)
arr2 = np.arange(5, 11)
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])

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