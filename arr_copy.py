import numpy as np 

or_arr = np.array([1, 2, 3, 4])

# copying an array 
shallow_copy = or_arr.copy() # creates a shallow copy that mean if data is changed the main array won't be changed 
print(shallow_copy)

shallow_copy[0] = 10
print(or_arr)
print(shallow_copy)

# creating deep copy

deep_copy = or_arr.view() # # creates a deep copy that mean if data is changed the main array will be changed too
print(deep_copy)

deep_copy[0] = 10
print(or_arr)
print(deep_copy)

# base array 
print(or_arr.base) # returns the base array of it -> None
print(deep_copy.base) # returns the base original array 
print(shallow_copy.base) # None for shallow copy