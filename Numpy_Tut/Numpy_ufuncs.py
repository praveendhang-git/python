# numpy ufuncs are universal functions that operate element-wise on arrays.
# ufuncs are used for the vectorized operations in numpy, which is faster than using loops in Python.
# This script demonstrates how to use numpy ufuncs to perform element-wise operations.
import numpy as np
# Create two arrays
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
# Perform element-wise addition
c = np.add(a, b)
print("Element-wise addition:", c)
# normal python addition of arrays by iteration
d = []
for i, j in zip(a, b):
    d.append(i + j)
print("Element-wise addition using loop:", d)
