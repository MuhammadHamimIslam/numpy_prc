import numpy as np

arr1 = np.array([1, 2, 3], dtype="int16") # string data type array 
arr2 = np.array([1, 2, 3, 4, 10, 20], dtype="int32")
arr3 = np.array([1+2j, 1+3j, 2j])
arr4 = np.array([1+2j, 1+3j, 2j], dtype="complex64")

print(arr1.dtype) # get the data type
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)

# converting data type

a_int = np.array([1, 2, 3, 4])

a_float = a_int.astype(np.float32) # type casting 
print(a_float)
print(a_float.dtype)

b_float = np.array([1.1, 2.2, 3.4, 5.1])
b_int = np.int32(b_float)
print(b_int)
print(b_int.dtype)