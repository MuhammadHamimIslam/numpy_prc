import numpy as np 

arr1 = np.array([1, 3, 2, 5, 7, 2, 4, 4, 6, 9, 8, 5])
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [1, 2, 3],
                [7, 1, 9]])
                
# finding unique elements in 1d array using np.unique()
unique_elm1d = np.unique(arr1)
print(unique_elm1d)

# finding unique elements in 2d array using np.unique()
unique_elm2d = np.unique(arr2, axis=0)
print(unique_elm2d)

# Finding Unique Rows with Indexes

unique_rows, index= np.unique(arr2, axis=0, return_index=True)
print(unique_rows)
print(index)