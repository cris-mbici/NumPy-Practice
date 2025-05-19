# ============================================
# Getting Started with NumPy - Lab
# ============================================

# --------------------------------------------
# Step 1: Import numpy using the standard alias
# --------------------------------------------

# Your Code Here
import numpy as np


# --------------------------------------------
# Step 2: Generate mock data using list and range
# --------------------------------------------

# Create a Python list with 5 elements
# Your Code Here
py_list = list(range(5))

# Create a Python range with 5 elements
# Your Code Here
py_range = range(5)

# Convert list to NumPy array
# Your Code Here
array_from_list = np.array(py_list)

# Convert range to NumPy array
# Your Code Here
array_from_range = np.array(py_range)


# --------------------------------------------
# Step 3: Convert height from inches to meters
# --------------------------------------------

# 1.0 inch = 0.0254 meters
list_height_inches = [65, 68, 73, 75, 78]

# Convert list to NumPy array
# Your Code Here
array_height_inches = np.array(list_height_inches)

# Convert inches to meters using broadcasting
# Your Code Here
array_height_meters = array_height_inches * 0.0254


# --------------------------------------------
# Step 4: Convert weight from pounds to kilograms
# --------------------------------------------

# 2.2046 pounds = 1 kilogram
list_weight_pounds = [150, 140, 220, 205, 265]

# Convert list to NumPy array
# Your Code Here
array_weight_pounds = np.array(list_weight_pounds) 

# Convert pounds to kilograms using broadcasting
# Your Code Here
array_weight_kg = array_weight_pounds / 2.2046


# --------------------------------------------
# Step 5: Calculate BMI
# Formula: BMI = weight (kg) / height (m)^2
# --------------------------------------------

# Your Code Here
BMI_array = array_weight_kg / pow(array_height_meters, 2)

# --------------------------------------------
# Step 6: Create a vector of ones (same size as BMI_array)
# --------------------------------------------

# Your Code Here
identity = np.ones(BMI_array)


# --------------------------------------------
# Step 7: Multiply BMI_array by vector of ones
# Result should be the same as the original BMI_array
# --------------------------------------------

# Your Code Here
BMI_times_ones = BMI_array * identity


# --------------------------------------------
# TODO Step 8: BONUS - Parse a tab-delimited file using NumPy
# --------------------------------------------

# This simulates how pandas.read_csv works under the hood

# Open and read the file
f = open('bp.txt')
n_rows = len(f.readlines())
print('The file has {} lines.'.format(n_rows))

# Reopen the file and get number of columns
f = open('bp.txt')
n_cols = len(f.readline().split('\t'))

# Reopen again to start processing
f = open('bp.txt')

# Create a NumPy matrix of zeros with dimensions (n_rows - 1, n_cols)
# Skipping the header row
# Your Code Here
data_matrix = None

# Iterate through file using enumerate
# Skip the first line (headers)
# For each subsequent line, split the line by tab and convert to float
# Fill in each row of the matrix
# Your Code Here
for i, line in enumerate(f):
    if i == 0:
        continue  # skip header
    # Your Code Here
    pass  # replace this with logic to update data_matrix[i - 1]

# Optional: Print or preview the final matrix
# print(data_matrix)


# ============================================
# Summary
# ============================================

# In this lab, you practiced:
# - Creating arrays from lists and ranges
# - Performing element-wise operations with NumPy
# - Converting units (inches → meters, pounds → kilograms)
# - Calculating BMI
# - Creating identity-like arrays
# - Reading and parsing data from a tab-delimited file

