import numpy as np


# creating array with all zeroes 
# works like np.zeros(shape, dtype, order)
arr1 = np.zeros((3, 3), dtype="int8")
print(arr1)

# creating array with all 1
# np.ones(shape, dtype, order)
arr2 = np.ones((3, 3), dtype="int8")
print(arr2)

# generating a sequence of numbers
# np.arange(start, end, step)
arr3 = np.arange(10, 20, 1)
print(arr3)

# create an array by specifying the start, stop, and the number of elements we want
# np.linspace(start, stop, num, endpoint=True, retstep=False, dtype, axis=0)
arr4 = np.linspace(1, 10, num=5, dtype="int8")
print(arr4)

# generating array with random numbers
# np.random.rand(size) // size isn't as tuple
arr5 = np.random.rand(2, 3) # generates items as float 
print(arr5)

# creating array with random numbers within range
# np.random.randit(start, end)
rand_arr = np.random.randint(1, 10)
print(rand_arr)

# creating array from choosing elements from another array 
# np.random.choice(array, size, replace=True)
rand_choice = np.random.choice(arr3, (2, 3))
print(rand_choice)

# creating an empty array 
# np empty(size, dtype, order="C")
arr6 = np.empty((3, 3), dtype="int8")
print(arr6)

# filling an array with an item 
# np.full(size, fill_item, order="C")
arr7 = np.full((3, 3), 10)
print(arr7)

# creating identity matrix 
# np.identity(len, dtype)
arr8 = np.identity(3, dtype="int8")
print(arr8)

# converting list, tuple or this like object to numpy array
# numpy.asarray(arr, dtype=None, order=None, device=None, copy=None, like=None)
tpl = (1, 2, 3)
arr8 = np.asarray(tpl)
print(arr8)

# creating a new numpy array of the same shape filled with zeros
# numpy.zeros_like(arr, dtype=None, order='K', subok=True, shape=None)
zeroes = np.zeros_like(arr7)
print(zeroes)

# creating a new numpy array of the same shape filled with ones
# numpy.ones_like(arr, dtype=None, order='K', subok=True, shape=None)
ones = np.ones_like(arr7)
print(ones)

# creating a new numpy array of the same shape but empty 
# numpy.empty_like(arr, dtype=None, order='K', subok=True, shape=None)
empty = np.empty_like(arr7)
print(empty)

# creating a new numpy array of the same shape filled with num
# numpy.zeros_like(arr, num, order='K', subok=True, shape=None)
fill = np.full_like(arr7, 14)
print(fill)

# creating array from iterable
# np.fromiter(Iterable, dtype)
def gen(n): 
    for i in range(n): 
        yield i

arr9 = np.fromiter(gen(5), dtype="int8")
print(arr9)

# generating an array with values that are evenly spaced on a log scale
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
arr10 = np.logspace(1, 10, num=5)
print(arr10)

# generating coordinate matrices from coordinate vectors
# np.meshgrid(*xi, copy=True, sparse=False, indexing='xy')
x = np.arange(1, 4)
y = np.arange(2, 6)

X, Y = np.meshgrid(x, y)
print("X coordinate: ", X)
print("Y coordinate: ", Y)