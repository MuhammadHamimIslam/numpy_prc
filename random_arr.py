import numpy as np

# Seeding the Random Generator -> generate the same random numbers every time run the program
np.random.seed(100) # setting seed to 100
rand1 = np.random.randint(1, 10, (3,))
print(rand1)

np.random.seed(100)
rand2 = np.random.randint(1, 10, (3,))
print(rand2) 
print(rand1 == rand2) # same seed so same array

# random numbers from a normal (Gaussian) distribution with a specified mean and standard deviation
# np.random.normal()
np.random.seed()
print(np.random.normal(1, 3, 4))

# randomly choosing element(s) from an array
arr = np.array([1, 3, 5, 7, 9])

rand_choice = np.random.choice(arr, 3) # chooses 5 elements randomly 
print(rand_choice)

# permutation 
permutation = np.random.permutation(arr) # shuffles the order of the array (doesn't change the original array )
print(permutation)

# shuffling the order
np.random.shuffle(arr) # shuffles the order of the array (changes the original array )
print(arr)

# Random Permutations of Integers
print(np.random.permutation(10)) # Generate a random permutation of integers from 0 to 9