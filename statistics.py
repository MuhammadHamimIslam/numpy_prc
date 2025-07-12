import numpy as np

# NumPy amin() and amax()

a = np.array([[3, 4, 5],
              [1, 7, 3],
              [6, 9, 4]]
)

print(a)
print(np.amin(a, 0)) # returns the min along axis 0
print(np.amax(a, 0)) # returns the min along axis 0

# np.ptp() -> returns the range (maximum - minimum) of values along an axis
print(np.ptp(a, axis=0))

#  np.percentile(a, q, axis) -> computes the q-th percentile of the data along the specified axis
print(np.percentile(a,50))

# np.sum(), np.prod(), np.median()
print(np.sum(a, axis=0)) # sum of elements along axis 0
print(np.prod(a, axis=0)) # multiplication of elements along axis 0
print(np.median(a)) # finds the median
print(np.average(a)) # average of array elements
print(np.std(a)) # calculates the standard deviatio
print(np.var(a)) # returns the variance of elements in the array