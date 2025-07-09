import numpy as np
from numpy.polynomial import Polynomial # to work with polynomial we need this library

# creatind a polynomial

# cofficient of the polynomial
cofficient = (-5, 1, 3, 2) # 2x³+3x²+x-5
p = Polynomial(cofficient)
print(p)

# evaluating a polynomial
value_call = p(2) # calls the polynomial where x = 2
print(value_call)

value_evaluate = np.polyval(p.coef, 2)
print(value_evaluate)

p1 = Polynomial([1, 2]) # 2x + 1
p2 = Polynomial([3, 1]) # x + 3
poly1 = np.array([1, 2, 3]) # x²+2x+3
poly2 = np.array([2, 0, 4]) # 2x²+4

# adding polynomial
result_add = p1 + p2
print(result_add)
print(np.polyadd(poly1, poly2)) # adds 2 polynomials

# polynomial multiplication
result_multiplication = p1 * p2
print(result_multiplication)
print(np.polymul(poly1, poly2)) # substracts 2 polunomials

# polynomial substraction
substraction = np.polysub(poly1, poly2)
print(substraction)

# polynomial differentiation
differentiation = p.deriv()
print(differentiation)
print(np.polyder(poly1)) # dfferentuation of polynomial

# polynomial intigration
intigration = np.polyint(poly2)
print(intigration)

# finding root of polynomial
root_value = np.roots(poly1)
print(root_value)

verification = np.polyval(poly1, root_value) # verification of root
print(verification)