import numpy as np

arr1 = np.array(["Welcome ", "Bye "])
arr2 = np.array(["to Numpy!", "for now!"])

# element wise string concatenation 
conc_arr = np.char.add(arr1, arr2)
print(conc_arr)

# centering string 
# np.char.center(a, width, fillchar=' ')
print(np.char.center(arr2, 20, fillchar=" "))
str_char = np.char.center(arr1, 20, fillchar="*")
print(str_char)

# capitalize the first letter 
# np.char.capitalize(a)
print(np.char.capitalize(arr2))

# set encoding 
encoded = np.char.encode(arr1, encoding="cp037", errors="replace")
print(encoded)

# lower case all characters 
print(np.char.lower(arr1))

# Repeat each string in the array a specified number of time
print(np.char.multiply(arr1, 5))

# replacing substring with new string 
# np.char.replace(a, old, new, count=-1)
rep_str = np.char.replace(arr1, "e", "u")
print(rep_str)

# remove leading and trailing whitespace characters
# np.char.strip(a, chars=None)
arr3 = np.array(["  Hi   ", "  Bye  "])
print(np.char.strip(arr3))
print(np.char.strip(str_char, chars="*"))

# split each string element of an array into a list of substrings based on a specified delimiter
# np.char.split(a, sep=None, maxsplit=-1)
splt = np.char.split(arr2, sep=" ")
print(splt)