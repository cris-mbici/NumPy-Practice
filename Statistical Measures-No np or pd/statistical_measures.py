# -----------------------------------------------
# Implementing Statistics with Functions - Lab
# -----------------------------------------------

# Introduction:
# In this lab you'll calculate measures of central tendency and dispersion.
# You’ll implement them using Python functions — not just using NumPy or Pandas (yet).

# -----------------------------------------------
# Step 1: Load the Dataset
# -----------------------------------------------

import pandas as pd

# Load the dataset
df = pd.read_csv('nhis.csv')
height = list(df['height'])

# Display number of items
# Your Code Here:
num_records = len(height)
print("Number of records:", num_records)  # Expected: 4785

# Display first 10 items
# Your Code Here:
first_10 = height[:10]
print("First 10 records:", first_10)  # Expected: [74, 70, 61, 68, 66, 98, 99, 70, 65, 64]

# -----------------------------------------------
# Step 2: Plotting a Histogram
# -----------------------------------------------
import matplotlib.pyplot as plt
# %matplotlib inline  # (Only needed in Jupyter notebooks)

# Create histogram of `height` with 8 bins
plt.hist(height, bins=8)
plt.title("Histogram of Heights (Raw Data)")
plt.xlabel("Height (inches)")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------------------
# Step 3: Calculating the Mean
# -----------------------------------------------

def get_mean(data):
    mean = sum(data) / len(data)
    return round(mean, 2)

# Test the function
test1 = [5, 4, 1, 3, 2]
test2 = [4, 2, 3, 1]
print(get_mean(test1))  # Expected: 3.0

# Get mean of height data
mean = get_mean(height)
print("Sample Mean:", mean)  # Expected: 69.58

# -----------------------------------------------
# Step 4: Filter Outliers > 80 Inches
# -----------------------------------------------

'''(Isn't relevant to assignment, just having fun)
def filter_height_outliers(data):
    filtered_data = []
    data = sorted(data)
    Q1_index = round(0.25 * len(data))
    Q1 = data[Q1_index]
    Q3_index = round(0.75 * len(data))
    Q3 = data[Q3_index]

    IQR = Q3 - Q1

    upper = Q3 + 1.5 * IQR
    lower = Q1 - 1.5 * IQR

    for i in data:
        if lower <= i <= upper:
            filtered_data.append(i)
        else:
            continue

    return filtered_data
'''
def filter_height_outliers(data):
    filtered_data = []
    for i in data:
        if i < 80:
            filtered_data.append(i)
        else:
            continue
    
    return filtered_data


# Test the function
print(filter_height_outliers([60, 70, 80, 90]))  # Expected: [60, 70]

# Filter the height list
filtered_height = filter_height_outliers(height)
print("Filtered records:", len(filtered_height))  # Expected: 4347

# Plot histogram again
plt.hist(filtered_height, bins=8)  # Replace both Nones appropriately
plt.title("Histogram of Heights (Filtered)")
plt.xlabel("Height (inches)")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------------------
# Step 5: Recalculate Mean for Filtered Data
# -----------------------------------------------

new_mean = get_mean(filtered_height)
print("New Mean (Filtered):", new_mean)  # Expected: 66.85

# -----------------------------------------------
# Step 6: Calculating the Median
# -----------------------------------------------

def get_median(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2

    if n % 2 == 1:
        return data[mid]                # odd length → middle element
    else:
        return (data[mid - 1] + data[mid]) / 2  # even length → average two middles

    

# Test the function
print(get_median([5, 4, 1, 3, 2]))  # Expected: 3
print(get_median([4, 2, 3, 1]))    # Expected: 2.5

# Median for original height
median = get_median(filtered_height)
print("Median:", median)  # Expected: 67

# -----------------------------------------------
# Step 7: Calculating the Mode
# -----------------------------------------------

def get_mode(data):
    frequency_dict = {}
    for i in data:
        if i not in frequency_dict:
            frequency_dict[i] = 1
        else:
            frequency_dict[i] += 1

    max_count = max(frequency_dict.values())
    modes = []
    for i in frequency_dict:
        if frequency_dict[i] == max_count:
            modes.append(i)
        else:
            pass
    return modes

# Test the function
print(get_mode([1, 2, 3, 5, 5, 4]))  # Expected: [5]
print(get_mode([1, 1, 1, 2, 3, 4, 5, 5, 5]))  # Expected: [1, 5]

# Mode for height
mode = get_mode(height)
print("Mode:", mode)  # Expected: [64]

# -----------------------------------------------
# Step 8: Calculating the Variance
# -----------------------------------------------

def get_variance(sample):
    sample_mean = get_mean(sample)
    list_of_squares = []
    for i in sample:
        squared_diff = (i - sample_mean) ** 2
        list_of_squares.append(squared_diff)
    
    variance = sum(list_of_squares) / (len(list_of_squares) - 1)
    return round(variance, 2)

# Test the function
print(get_variance([1, 2, 3, 5, 5, 4]))  # Expected: 2.67

# Variance of height
variance = get_variance(height)
print("Variance:", variance)  # Expected: 87.74

# -----------------------------------------------
# Step 9: Calculating the Standard Deviation
# -----------------------------------------------

from math import sqrt

def get_stddev(sample):
    # Your Code Here
    stddev = sqrt(get_variance(sample))
    return round(stddev, 2)

# Test
print(get_stddev([120, 112, 131, 211, 312, 90]))  # Expected: ~84.03

# Standard Deviation for height
standard_deviation = get_stddev(height)
print("Standard Deviation:", standard_deviation)  # Expected: 9.37

# -----------------------------------------------
# Step 10: Visualize with Boxplot
# -----------------------------------------------

plt.boxplot(height)  # Replace None with height
plt.title("Boxplot of Heights")
plt.ylabel("Height (inches)")
plt.show()

# -----------------------------------------------
# Step 11: Validate With NumPy / SciPy
# -----------------------------------------------

import numpy as np
from scipy import stats

print("NumPy / SciPy Verification")
print("Mean:", round(np.mean(height), 2))
print("Median:", np.median(height))
print("Mode:", stats.mode(height, keepdims=True).mode)
print("Variance:", round(np.var(height, ddof=1), 2))
print("Standard Deviation:", round(np.std(height, ddof=1), 2))

# -----------------------------------------------
# Summary
# -----------------------------------------------
# In this lab, you:
# - Wrote custom functions for mean, median, mode, variance, and standard deviation
# - Handled outliers
# - Visualized distributions using histograms and boxplots
# - Compared your results with NumPy and SciPy implementations
