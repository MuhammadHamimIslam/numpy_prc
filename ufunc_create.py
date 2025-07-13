import numpy as np

# Ufuncs, or universal functions, are functions in NumPy that apply operations element-wise on ndarrays
# NumPy provides a complete set of built-in ufuncs for performing various operations
#   Arithmetic ufuncs: np.add(), np.subtract(), np.multiply(), np.divide()
#   Trigonometric ufuncs: np.sin(), np.cos(), np.tan(), np.arcsin(), np.arccos(), np.arctan()
#   Exponential and logarithmic ufuncs: np.exp(), np.log(), np.log10(), np.log2()
#   Comparison ufuncs: np.greater(), np.less(), np.equal(), np.not_equal()

array1 = np.array([2, 4, 6, 8])
array2 = np.array([1, 3, 5, 7])

# built in ufunction
print(np.add(array1, array2))
print(np.sin(array1))
print(np.greater(array1, array2))

# creating custom ufunction

def multiply(x, y):
    "Simple x and y multiply function"
    return x * y
# create unfunction from python function
# np.frompyfunc(function, numbers_of_argument, numbers_of_return_value)
multiply_func = np.frompyfunc(multiply, 2, 1) # makes ufunction
print(multiply_func(array1, array2)) # multiplies 2 array elements