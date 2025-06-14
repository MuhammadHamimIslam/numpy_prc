import numpy as np

arr1 = np.array(["Welcome ", "Bye "])
arr2 = np.array(["to Numpy!", "for now!"])

# element wise string concatenation 
conc_arr = np.char.add(arr1, arr2)
print(conc_arr)

# centering string 
# np.char.center(a, width, fillchar=' ')
print(np.char.center(arr2, 20, fillchar=" "))
print(np.char.center(arr1, 20, fillchar="*"))

# capitalize the first letter 
# np.char.capitalize(a)
print(np.char.capitalize(arr2))