# Covariance and Correlation - Lab

# In this lab, you'll calculate covariance and correlation using Python.
# You'll also practice writing functions and performing statistical analysis on two variables: height and weight.

# ------------------------------------------------------------------------------
# Step 1: Load the Data
# ------------------------------------------------------------------------------

height = [68, 71, 61, 69, 71, 58, 72, 73, 58, 74,
          61, 59, 69, 68, 64, 69, 72, 66, 65, 69]
weight = [165, 201, 140, 170, 192, 125, 195, 205,
          115, 210, 135, 125, 172, 175, 145, 170,
          200, 155, 150, 171]

# ------------------------------------------------------------------------------
# Step 2: Mean Normalization
# ------------------------------------------------------------------------------

# Create a function to mean normalize a list of values

def mean_normalize(var): 
    # Your Code Here
    arithmetic_mean = sum(var) / len(var)
    data_range = 1 # Dividing by the range gives the version used in machine learning
    norm_mean_list = []

    for i in var:
        normalized_mean = (i - arithmetic_mean) / data_range
        norm_mean_list.append(normalized_mean)

    return norm_mean_list


# Example test
print(mean_normalize([1, 2, 3, 4, 5]))
print(mean_normalize([11, 22, 33, 44, 55]))

# ------------------------------------------------------------------------------
# Step 3: Normalize height and visualize
# ------------------------------------------------------------------------------

# Mean normalize the height data
height_normalized = mean_normalize(height)
print(height_normalized)

# TODO Visualization (Optional, requires matplotlib)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(height_normalized, label="normalized data", bins=6)
ax.hist(height, label="original data", bins=6)

ax.set_title("Distribution of Height Data Before and After Normalization")
ax.set_xlabel("Height")
ax.set_ylabel("Count")
ax.legend(loc="center")
#plt.show()

# ------------------------------------------------------------------------------
# Step 4: Define Dot Product Function
# ------------------------------------------------------------------------------

# Write a function that takes two lists and returns the dot product

def dot_product(x, y):
    list_of_products = []

    for a, b in zip(x, y): # zip takes values in a list of the same index and pairs them
        product = a * b
        list_of_products.append(product)

    return sum(list_of_products)

# Test the function
a = [1, 2, 3]
b = [4, 5, 6]
print(dot_product(a, b))  # Should print 32

# ------------------------------------------------------------------------------
# Step 5: Calculate Covariance
# ------------------------------------------------------------------------------

# Use the mean_normalize and dot_product functions to calculate covariance

def covariance(x, y):
    centered_x = mean_normalize(x)
    centered_y = mean_normalize(y)

    centered_combined = dot_product(centered_x, centered_y)
    cov = centered_combined / (len(x) - 1)

    return cov

print(f"Hard math covariance: {covariance(height, weight)}")  # Expected: 144.75789473684208

# ------------------------------------------------------------------------------
# Step 6: Calculate Standard Deviation (provided helper function)
# ------------------------------------------------------------------------------

from math import sqrt

def stddev(var):
    mean = sum(var) / len(var)
    sum_of_squares = sum((i - mean) ** 2 for i in var)
    variance = sum_of_squares / (len(var) - 1)
    return sqrt(variance)

print(f"Hard math standard deviation: {stddev(height)}")  # Expected: ~5.11

# ------------------------------------------------------------------------------
# Step 7: Calculate Correlation
# ------------------------------------------------------------------------------

# Use covariance and standard deviation to compute correlation

def correlation(x, y):
    standard_deviation_x = stddev(x)
    standard_deviation_y = stddev(y)
    covariance_xy = covariance(x, y)
    
    pearson_corr = (covariance_xy) / (standard_deviation_x * standard_deviation_y)
    return pearson_corr

print(f"Hard math correlation: {correlation(height, weight)}")  # Expected: ~0.9774

# ------------------------------------------------------------------------------
# Step 8: Visualize Height vs Weight (Optional) # TODO because I haven't learnt visualization yet
# ------------------------------------------------------------------------------

fig, ax = plt.subplots()
ax.scatter(height, weight, label="actual data")

x_bounds = [min(height), max(height)]
y_bounds = [min(weight), max(weight)]

ax.plot(x_bounds, y_bounds, "--", label="perfect correlation")
ax.set_title("Height vs. Weight for a Sample of Individuals")
ax.set_xlabel("Height (inches)")
ax.set_ylabel("Weight (pounds)")
ax.legend()
plt.show()

# ------------------------------------------------------------------------------
# Step 9: Using NumPy (for comparison)
# ------------------------------------------------------------------------------

import numpy as np

# Covariance using NumPy
covariance_matrix = np.cov(height, weight)
print("NumPy Covariance:", covariance_matrix[0][1])

# Correlation using NumPy
correlation_matrix = np.corrcoef(height, weight)
print("NumPy Correlation:", correlation_matrix[0][1])
