import numpy as np

arr = np.array([1, 2, 4, 8, 16])

# Difference Universal Function
diff = np.diff(arr) # finds the difference between each elements
print(diff)

# Higher order difference
sec_diff = np.diff(arr, n=2) # By specifying the n parameter, we can calculate the difference between elements multiple times
print(sec_diff)

# finding gradient
gradient = np.gradient(arr) # finds gradient
print(gradient)

# Compute the element-wise differences
elm_diff = np.ediff1d(arr) # same as np.diff()
print(elm_diff)

# finding LCM (Least Common Multiple)
a = np.array([4, 6, 8, 12])
b = np.array([6, 8, 10, 12])

lcm = np.lcm(a, b) # element wise lcm
print(lcm)

# lcm of an array elements
lcm_arr = np.lcm.reduce(a)
print(lcm_arr)

# finding GCD (Greatest Common Divisor)
gcd = np.gcd(a, b) # element wise gcd
print(gcd)

# gcd of an array elements
gcd_arr = np.gcd.reduce(a)
print(gcd_arr)