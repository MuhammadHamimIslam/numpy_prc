import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.random.randint(1, 20, (3, 3), dtype=np.int32)
arr3 = np.identity(3)

# saving array to a text file
# np.savetxt(fname, data, fmt=<format>, delimiter=<delimiter>, header=<header>, footer=<footer>, comments=<char>)

np.savetxt("data/arr1.txt", arr1)

# saving to a binary file
# np.save(file, arr, allow_pickle=False, fix_imports=True)
np.save("data/arr_bin.bin", arr1)

# saving as .npz file
# np.savez(file, *args, **kwargs)
np.savez("data/mul_arr.npz", array1=arr1, array2=arr2)

# saving as .npz by compressing 
# numpy.savez_compressed(file, *args, **kwargs)
np.savez_compressed("arrays_data.npz", array1=arr1, array2=arr2, array3=arr3)