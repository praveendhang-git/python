# numpy are mainly used for array operations and numerical computations in Python.
# Python provide the list data structure, but it is not efficient for numerical computations.
# NumPy provides a powerful N-dimensional array object, which is more efficient for numerical operations than lists.
# numpy arrays are stored in contiguous memory locations unlike list, which makes them more efficient & faster.
# Array objects in NumPy are called ndarray (N-dimensional array).
import numpy as np
print("NumPy version:", np.__version__)
arr = np.array([1, 2, 3, 'p', 4, 5])  # Create a NumPy array
print("NumPy array:", arr, "Array type :", type(arr))  # Output: [1 2 3
oneD = np.array([1, 2, 3, 4, 5])  # Create a one-dimensional NumPy array
print("One-dimensional array:", oneD, "Array Dimension : ", oneD.ndim)
twoD = np.array([[1, 2, 3], [4, 5, 6]])  # Create a two-dimensional NumPy array
print("Two-dimensional array:\n", twoD, "\nArray Dimension : ", twoD.ndim)
# Create a three-dimensional NumPy array
threeD = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Three-dimensional array:\n", threeD,
      "\nArray Dimension : ", threeD.ndim)
arr5 = np.array([1, 2, 3, 4], ndmin=5)
# Create a NumPy array with a specified minimum number of dimensions
print("Array with minimum 5 dimensions:\n",
      arr5, "\nArray Dimension : ", arr5.ndim)
print(arr5)
# array elements accessing
print("Accessing elements in one-dimensional array:", oneD[0])  # Output: 1
print("Accessing elements in two-dimensional array:", twoD[1, 1])  # Output: 2
