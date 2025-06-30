import numpy as np

arr1 = np.array([1, 2, 3, np.nan, 5, np.nan])

# finding NaN value 
ind = np.isnan(arr1)
print(ind)

# counting missing values
count_nan = np.sum(ind)
print(count_nan)

# removing missing data
new_arr1 = arr1[~ind]
print(new_arr1)

# replacing missing data
# np.nan_to_num(x, copy=True, nan=0.0, posinf=None, neginf=None)
filtered_arr = np.nan_to_num(arr1, nan=1) # replace all NaN with 1
print(filtered_arr)