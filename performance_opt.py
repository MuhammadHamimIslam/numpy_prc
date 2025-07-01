import numpy as np 
import time

# Utilizing Efficient Data Types
arr_db = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0], dtype=np.float64)
print(arr_db)

arr_single = arr_db.astype(dtype=np.float32) # convert to float32 for memory efficiency 
print(arr_single)

# avoid using loop. using built in function of numpy 

# using built in function to find mean
st1 = time.perf_counter()
print(np.mean(arr_single))
end1 = time.perf_counter()

print(end1 - st1)

# using for loop
st2 = time.perf_counter()
total = 0
for elm in arr_single: 
    total += elm
print(total / len(arr_single))
end2 = time.perf_counter()

print(end2 - st2)

# In-place Operations for Vectorization
# avoid creating new array. use in place operation 
arr_single += 20 # adds 20 to every element 
print(arr_single)