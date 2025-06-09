import numpy as np 

arr = np.array([13, 54, 25, 34, 89, 27, 18])

# filtering 
condition = arr % 2 == 0 # even 
print(arr[condition]) # get the even

# multiple condition 
cond = (20 < arr) & (arr < 40) # filter elements greater than 20 and less than 40
print(arr[cond])

# condition with np.where(condition)
filtered_index = np.where(cond)
filtered_arr = arr[filtered_index]
print(filtered_arr)

# filtering with custom function 
def is_prime(num):
    "Return True if number is prime else return False"
    if num <= 1: 
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0: 
            return False
    return True

filtered_indices = np.array([is_prime(x) for x in arr])
filtered_prime_arr = arr[filtered_indices]
print(filtered_prime_arr)