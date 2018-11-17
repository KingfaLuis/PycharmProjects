import scipy
import numpy as np
from scipy.optimize import minimize
import sympy
import math

'''
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.newton.html
scipy.optimize.newton(func, x0, fprime=None, args=(), tol=1.48e-08, maxiter=50, fprime2=None)[source]¶
AttributeError: module 'scipy' has no attribute 'optimize'
'''
func = np.sqrt(115)
# func = x*exp(x)-1
x0 = 10
maxi = 8

# x = symbols("x") # 设为变量
#
# func = x*exp(x)-1
# ffunc = diff(func, x)

result = scipy.optimize.newton(func,x0=1,fprime=None)
print(result)