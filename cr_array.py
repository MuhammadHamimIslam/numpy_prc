import numpy as np

# creating an array 
arr1 = np.array([1, 2, 3, 4, 5]) # simple array in numpy 
print(arr1)
print(type(arr1)) # returns the type -> ndarray

arr_0d = np.array(10) # 0 dimensional array 
print(arr_0d)
print(arr_0d.ndim) # get the dimension 

arr_1d = np.array([1, 2, 3, 4]) # 1 dimensional array 
print(arr_1d)
print(arr_1d.ndim) # get the dimension 

arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) # 2 dimensional array 
print(arr_2d)
print(arr_2d.ndim) # get the dimension 

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3 dimensional array 
print(arr_3d)
print(arr_3d.ndim) # get the dimension 

# higher dimension 
arr_higher_d = np.array([1, 2, 3, 4, 5], ndmin=5) # setting dimension manually 
print(arr_higher_d)
print(arr_higher_d.ndim) # get the dimension