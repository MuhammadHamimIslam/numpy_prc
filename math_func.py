import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 3, 5, 7, 9])
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi])
values = np.array([0, 0.5, 1])
h_value = np.array([0, 1, 2])
expontents = np.array([0, 1, 2, 3])
base10 = np.array([1, 10, 100, 1000])
base2 = np.array([1, 2, 4, 8, 16])
base5 = np.array([1, 5, 25, 125])
dec_values = np.array([3.141592, 6.626, 6.673, 1.67262158])

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

# expontential operation
exp_values = np.exp(expontents) # finds exponent
print(exp_values)

# logarithimic operatuon
natural_log = np.log(exp_values) # finds loge
print(natural_log)

log10 = np.log10(base10) # finds log10
print(log10)

log2 = np.log2(base2) # logarithm for base2
print(log2)

# custom base logarithm
# log_base(x) = loge(x) / loge(base)
log_5 = np.log(base5) / np.log(5)
print(log_5)

# rounding decimal values
# np.round(values, place) : place = rounded to decimal places
rounded = np.round(dec_values, 3)
print(rounded)

# flooring decimal values to the nearest integer
floored = np.floor(dec_values)
print(floored)

# ceiling decimal values to the largest nearer integer
ceiled = np.ceil(dec_values)
print(ceiled)

# truncating decimal by removing the decimal parts
trunced = np.trunc(dec_values)
print(trunced)