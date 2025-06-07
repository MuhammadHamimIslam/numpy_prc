import numpy as np 

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
arr3 = np.array([5, 4, 6])
com_arr = np.array([1+2j, 3+2j, 4-4j, 9-2j, -3j])

# Adding a Scalar to an Array
sc_arr = arr1 + 10
print(sc_arr)

# Adding Arrays of Different Shapes
add_arr = arr1 + arr2
print(add_arr)

# arithmetic operation

print(arr2 + arr3) # performs array addition 
print(arr2 - arr3) # perform array subtraction 
print(arr2 * arr3) # array multiplication 
print(arr2 / arr3) # array division 
print(arr2 ** arr3) # array power 
print(arr2 % arr3) # array modulo
print(arr2 // arr3) # floor division 
print(np.sum(arr2)) # array element's sum

# sum along 1 axis

sum_axis1 = np.sum(arr1, axis=0) # sum along axis 1 (column)
print(sum_axis1)
sum_axis2 = np.sum(arr1, axis=1) # sum along axis 1 (row)
print(sum_axis2)

print(np.mean(arr2)) # array element's mean 

# mean along 1 axis
mean_axis1 = np.mean(arr1, axis=0) # mean along axis 1 (column)
print(mean_axis1)
mean_axis2 = np.mean(arr1, axis=1) # mean along axis 1 (row)
print(mean_axis2)

# working with complex array 

print(np.real(com_arr)) # returns the real part 
print(np.imag(com_arr)) # returns the imaginary part 
print(np.conj(com_arr)) # returns the conjugate of the complex number 
print(np.angle(com_arr)) # returns the angle in radian
print(np.angle(com_arr, deg=True)) # return the angle in degree