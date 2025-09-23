import numpy as np
#58 quetions
# -----------------------------
# 1. Basics of Arrays
# -----------------------------
# Create an empty and a full NumPy array
#full
full_array = np.full((3, 4), 7)
print("Full Array:\n", full_array)

#empty
empty_array = np.empty((3, 4))
print("Empty Array:\n", empty_array)

# Create a NumPy array filled with zeros
zeros_array = np.zeros((3, 4))
print("Zeros Array:\n", zeros_array)

# Create a NumPy array filled with ones
ones_array = np.ones((3, 4))
print("Ones Array:\n", ones_array)

# Flatten a 2D numpy array into 1D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
flattened_array = array_2d.flatten()
print("Flattened Array:\n", flattened_array)

# Reverse a numpy array
reversed_array = np.flip(array_2d)
print("Reversed Array:\n", reversed_array)


# Change data type of given numpy array
array_int = np.array([1, 2, 3, 4])
array_float = array_int.astype(float)
print("Array with float data type:\n", array_float)


# How to make a NumPy array read-only?
read_only_array = np.array([1, 2, 3])
read_only_array.flags.writeable = False
print("Read-only Array:\n", read_only_array)


# -----------------------------
# 2. Indexing & Selection
# -----------------------------
# Replace NumPy array elements that don’t satisfy a given condition
array = np.array([1, 2, 3, 4, 5, 6])
array[array < 3] = 0
print("Modified Array:\n", array)

# Return the indices of elements where the condition is satisfied
indices = np.where(array > 3)
print("Indices where condition is satisfied:\n", indices)

# Replace NaN values with average of columns
array_with_nan = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
col_mean = np.nanmean(array_with_nan, axis=0)
inds = np.where(np.isnan(array_with_nan))
array_with_nan[inds] = np.take(col_mean, inds[1])
print("Array after replacing NaN with column mean:\n", array_with_nan)

# Replace negative values with zero in NumPy array
array_with_neg = np.array([-1, 2, -3, 4, -5])
array_with_neg[array_with_neg < 0] = 0
print("Array after replacing negative values with zero:\n", array_with_neg)

# How to get values of a NumPy array at certain index positions?
array = np.array([10, 20, 30, 40, 50])
indices = [1, 3]
values = array[indices]
print("Values at certain index positions:\n", values)

# Find indices of elements equal to zero in a NumPy array
array_with_zeros = np.array([0, 1, 2, 0, 3, 0])
zero_indices = np.where(array_with_zeros == 0)[0]
print("Indices of elements equal to zero:\n", zero_indices)


# Access different rows of a multidimensional NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_row = array_2d[1, :]
print("Second row of the array:\n", second_row)

# Get row numbers of NumPy array having element larger than X
row_indices = np.where(array_2d > 5)[0]
print("Row numbers with elements larger than 5:\n", row_indices)

# -----------------------------
# 3. Array Operations
# -----------------------------
# Remove single-dimensional entries (squeeze)
# Move axes of an array to new positions
# Interchange two axes of an array
# Counts the number of non-zero values in the array
# Count the number of elements along a given axis
# Trim leading/trailing zeros from a 1D array
# Compute element-wise true division
# Calculate element-wise absolute value
# Multiply 2D numpy array corresponding to 1D array
# Round, floor, ceiling of elements

# -----------------------------
# 4. Statistics & Probability
# -----------------------------
# Compute the median of a flattened NumPy array
# Find Mean of a List of NumPy Array
# Calculate mean ignoring NaN values
# Compute variance of NumPy array
# Compute standard deviation of NumPy array
# Compute Pearson correlation of two arrays
# Calculate average, variance, and std dev in Python using NumPy

# -----------------------------
# 5. Linear Algebra
# -----------------------------
# Matrix Multiplication in NumPy
# Add and subtract matrices
# Calculate determinant of a matrix
# Inverse of a matrix
# Eigenvalues and eigenvectors
# Norm of a matrix or vector
# QR decomposition of a matrix
# Covariance matrix of two arrays
# Convert covariance to correlation matrix

# -----------------------------
# 6. Random & Distributions
# -----------------------------
# Create a NumPy array with random values
# Choose elements with different probability
# Weighted random choice
# Uniform distribution random values
# Gaussian distribution random values

# -----------------------------
# 7. Advanced Array Manipulation
# -----------------------------
# Build an array of all combinations of two arrays
# Add a border around a NumPy array
# Get all 2D diagonals of a 3D NumPy array
# Einstein summation convention
# Kronecker product of two arrays
# Outer product of two vectors
# Cross product of matrices/vectors

# -----------------------------
# 8. File Handling & Visualization
# -----------------------------
# Convert list/tuple to NumPy arrays
# Convert NumPy array to CSV file
# Load data from text/CSV file
# Convert image to NumPy array
# Plot line graph from NumPy array
# Create histogram using NumPy
