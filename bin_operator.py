import numpy as np 

a = 5
b = 6

# bitwise and operation 
# and operation 
# 5 -> 101
# 6 -> 110
#and-> 100 = 4
print("bitwise and: ", a & b) # using build in operator 
print("bitwise and", np.bitwise_and(a, b)) # using numpy bitwise and function 

# bitwise or operation 
# or operation 
# 5 -> 101
# 6 -> 110
# or-> 111 = 7
print("bitwise or: ", a | b) # using build in operator 
print("bitwise or", np.bitwise_or(a, b)) # using numpy bitwise or function 

# bitwise exclusive or (xor)
# xor operation 
# 5 -> 101
# 6 -> 110
#xor-> 011 = 3 
print("bitwise xor: ", a ^ b) # using build in operator 
print("bitwise xor", np.bitwise_xor(a, b)) # using numpy bitwise xor function 

# bitwise right shift operation 
rshift_value = 1
# right shift operation 
# 5 -> 101
#right shift(1) -> 010 = 2
print("bitwise right shift: ", a >> rshift_value) # using build in operator 
print("bitwise right shift", np.right_shift(a, rshift_value)) # using numpy right shift function

# bitwise left shift operation 
lshift_value = 1
# left shift operation 
# 6 -> 110
#left shift(1) -> 1100 = 12
print("bitwise left shift: ", b << lshift_value) # using build in operator 
print("bitwise left shift", np.left_shift(b, lshift_value)) # using numpy left shift function

# binary represantion of integer 
print("binary represantion: ", bin(a)) # using build in function 
print("binary represantion: ", bin(b)) 

print("binary represantion: ", np.binary_repr(a)) # using numpy function 
print("binary represantion: ", np.binary_repr(b, width=8))

# bitwise not operation 
# not operation 
# 5 -> 00000000...(32)101 // 32 bit
#invert -> 111111...(32)010 = -6
print("bitwise not: ", ~a) # using build in operator 
print("bitwise not", np.invert(a)) # using numpy invert function