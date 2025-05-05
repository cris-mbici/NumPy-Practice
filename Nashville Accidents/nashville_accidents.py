import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("Nashville Accidents Jan 2018 - Apl 2025.csv")

# 1. Display the first 5 rows of the DataFrame
# Your Code Here
print(df.head())

# 2. Print the column names of the dataset
# Your Code Here
print(df.columns)

# 3. Get a summary (info) of the dataset including number of non-null values and data types
# Your Code Here
print(df.info())

# 4. Show basic statistics (mean, std, min, max) for one numeric column
# Your Code Here
print(df["Number of Fatalities"].mean())
print(df["Number of Fatalities"].std())
print(df["Number of Fatalities"].max())
print(df["Number of Fatalities"].min())


# 5. Select only the column with the Weather Description (or a similar measure if present) and display the first 10 values
# Your Code Here
print(df["Weather Description"].head(10))

# 6. Filter the dataset to show rows where the number of fatalities index is above 2
# Your Code Here
print(df[df["Number of Fatalities"] > 2])

# 7. Count how many unique values are in a column (e.g., city or station name, if available)
# Your Code Here
print(df["Weather Description"].nunique())

# 8. Group the data by a column like city or station and calculate the mean air quality index for each group
# Your Code Here
print(df.groupby("Weather Description")["Number of Motor Vehicles"].sum().sort_values(ascending=False))

# 9. Create a new column that classifies the accident into categories like "No Casualty", "Moderate", "Fatal"
# Your Code Here
def accident_lvl(fatalities):
    if fatalities == 0:
        return "No Casualty"
    elif fatalities == 1 or 2:
        return "Moderate"
    else:
        return "Fatal"

df ["accident_category"] = df["Number of Fatalities"].apply(accident_lvl)
print(df[["accident_category", "Weather Description"]].head(50))

# 10. Sort the dataset by Number of Motor Vehicles in descending order
# Your Code Here
print(df["Number of Motor Vehicles"].sort_values(ascending= False))


# 11. Fill any missing values in the dataset with the column mean (for numerical columns)
# Your Code Here

# 12. Drop any rows where important values (e.g., timestamp, AQI) are missing
# Your Code Here

# 13. Convert the date/time column to datetime format and extract the month from it
# Your Code Here

# 14. Plot a line graph showing how air quality index changed over time (use matplotlib or pandas built-in plotting)
# Your Code Here

# 15. Export the cleaned and processed DataFrame to a new CSV file named "cleaned_air_quality.csv"
# Your Code Here
