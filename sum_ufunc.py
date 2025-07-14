import numpy as np

arr = np.array([[1, 3, 5], [7, 9, 11]])
#arr2 = np.array([2, 4, 6, 8, 10])

# numpy summation : np.sum()
summation = np.sum(arr) # sum of array elements
sum_col = np.sum(arr, axis=0) # sum of columns
sum_row = np.sum(arr, axis=1) # sum of rows
print(summation)
print(sum_col)
print(sum_row)

# cumlarive sum
cum_sum = np.cumsum(arr) # cumlative sum
print(cum_sum)

# cumlative product
cum_prod = np.cumprod(arr) # cumlative product
print(cum_prod)

# sum with condition
sum_gt_4 = np.sum(arr[arr > 4]) # sum of array elements greater than 4
print(sum_gt_4)

# finding product
product = np.prod(arr) # returns the product
print(product)