import numpy as np 
from functools import reduce

a = np.array([1, 2, 3, 4, 3, 5])
b = np.array([3, 4, 3, 5, 7, 6])
c = np.array([3, 4, 6, 7, 3, 5])

# finding difference (a - b)
# np.setdiff1d(ar1, ar2)
differ = np.setdiff1d(a, b) # set operation (a - b)
print(differ)

# difference of multiple array 
diff_mul = reduce(np.setdiff1d, (a, b, c))
print(diff_mul)