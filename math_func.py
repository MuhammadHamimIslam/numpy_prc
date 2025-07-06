import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 3, 5, 7, 9])
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi])
values = np.array([0, 0.5, 1])
h_value = np.array([0, 1, 2])

# arithmetic operation

print(arr1 + arr2) # addition element wise
print(arr1 - arr2) # substraction element wise
print(arr1 * arr2) # multiplication element wise
print(arr1 / arr2) # division element wise

# trigonometric operation

sine = np.sin(angles) # sine of the angles 
print(sine)
cosine = np.cos(angles) # cos of the angles 
print(cosine)
tangent = np.tan(angles) # tan of the angles 
print(tangent)

# inverse trigonometric operation
sine_inverse = np.arcsin(values) # sin^-1 of the values
print(sine_inverse)
cosine_inverse = np.arccos(values) # cos^-1 of the values
print(cosine_inverse)
tan_inverse = np.arctan(values) # tan^-1 of the values
print(tan_inverse)

# hyperabolic trigonometric operation
sinh = np.sinh(h_value)
print(sinh)
cosh = np.cosh(h_value)
print(cosh)
tanh = np.tanh(h_value)
print(tanh)

# convert radian to degree
degrees = np.rad2deg(angles)
print(degrees)
 
# convert degree to radian
radians = np.deg2rad(degrees)
print(radians)

# logarithimic operatuon
