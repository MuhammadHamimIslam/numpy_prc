import numpy as np

# NumPy loading arrays refers to the process of reading and loading data from external files or sources into NumPy arrays.

# np.loadtxt(file_name, dtype=<type>, delimiter=<delimiter>, comments=<char>, skiprows=<num>, usecols=<cols>)
arr1 = np.loadtxt("data/data.txt", dtype="int32", delimiter=",") # loads data from file delimiter=,

print(arr1)

# np.genfromtxt(fname, dtype=<type>, delimiter=<delimiter>, comments=<char>, skip_header=<num>, usecols=<cols>, filling_values=<value>, missing_values=<value>, converters=<dict>, encoding=<str>, names=<bool>)
arr2 = np.genfromtxt("data/data.txt", dtype="int32", delimiter=",")

print(arr2)

# load from binary file
# np.fromfile(file, dtype=<type>, count=-1, offset=0)

arr3 = np.fromfile("data/array_data.bin", dtype=np.int32)

print(arr3)

# load from .npy file
# np.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')

arr4 = np.load("data/array_data.npy")
print(arr4)