# Exercise 2: Access elements in a 1D NumPy array.
# - Use indexing to print the second element of the array you created in the previous exercise.
# - Additionally, print the last element using negative indexing.

# Your code here
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[1])
print(arr[-1])

# Exercise 3: Array Slicing.
# - Using slicing, extract the sub-array consisting of the 3rd, 4th, and 5th elements from the original array.
# - Print the sliced sub-array.

# Your code here
subarr = arr[2:5]
print(subarr)

# Exercise 4: Modify Array Elements.
# - Change the 3rd element of the array you created in Exercise 1 to 10.
# - Print the updated array to confirm the change.

# Your code here
arr[2] = 10
print(arr)

# Exercise 5: Create a 2D NumPy Array.
# - Create a 2D NumPy array with 3 rows and 3 columns, filled with numbers 1 to 9.
# - Print the array.

# Your code here
complex_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(complex_arr)

# Exercise 6: Accessing Elements in a 2D NumPy Array.
# - Access and print the element located in the second row, third column of the array you created in Exercise 5.
# - Additionally, access and print the entire second row.

# Your code here
print(complex_arr[1, 2])
print(complex_arr[1])

# Exercise 7: Array Slicing in 2D.
# - Slice and print the sub-array consisting of the first two rows and first two columns from the array you created in Exercise 5.

# Your code here
print(complex_arr[0:2, 0:2])

# Exercise 8: Array Reshaping.
# - Reshape the 1D array from Exercise 1 (with elements 1 to 6) into a 2D array with 2 rows and 3 columns.
# - Print the reshaped array.

# Your code here
arr = arr.reshape(2, 3)
print(arr)

# Exercise 9: NumPy Data Types.
# - Check the data type (`dtype`) of the reshaped array from Exercise 8.
# - Then, create a new NumPy array with three floating-point numbers (e.g., 1.1, 2.2, 3.3).
# - Print the array and its data type.

# Your code here
print(arr.dtype)

float_arr = np.array([1.1, 2.2, 3.3])
print(float_arr.dtype)

# Exercise 10: Basic Array Operations.
# - Create a new NumPy array: np.array([10, 20, 30])
# - Add 5 to every element and print the result.
# - Multiply the result by 2 and print it.
# - Finally, calculate and print the mean of the final array.

# Your code here
new_arr = np.array([10, 20, 30])

new_arr = new_arr + 5
print(new_arr)

new_arr = new_arr * 2
print(new_arr)

print(new_arr.mean())