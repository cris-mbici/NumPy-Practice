import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("air_quality_dataset.csv")

# 1. Display the first 5 rows of the DataFrame
# Your Code Here

#print(df)

# 2. Print the column names of the dataset
# Your Code Here
#print(df.columns)

# 3. Get a summary (info) of the dataset including number of non-null values and data types
# Your Code Here
#print(df.info())

# 4. Show basic statistics (mean, std, min, max) for all numeric columns
# Your Code Here
#num_df = df.select_dtypes(include='number')

#print(num_df.mean())
#print(num_df.std())
#print(num_df.min())
#print(num_df.max())

# 5. Select only the column with the air quality index (or a similar measure if present) and display the first 10 values
# Your Code Here
#print(df['PM2.5'].head(10))

# 6. Filter the dataset to show rows where the air quality index is above 100
# Your Code Here
#print(df[df['PM2.5'] > 100])

# 7. Count how many unique values are in a column (e.g., city or station name, if available)
# Your Code Here
#print(df["Location_Type"].nunique())

# 8. Group the data by a column like city or station and calculate the mean air quality index for each group
# Your Code Here
#print(df.groupby("Location_Type")["NO2"].mean())

# 9. Create a new column that classifies the air quality index into categories like "Good", "Moderate", "Unhealthy"
# Your Code Here
#def classify_aqi(value):
#    if value <= 50:
#        return "Good"
#    elif value <= 100:
#        return "Moderate"
#    else:
#        return "Unhealthy"
    
#df["AQI_Category"] = df["PM2.5"].apply(classify_aqi)
#print(df[["PM2.5", "AQI_Category"]].head(10))

# 10. Sort the dataset by air quality index in descending order
# Your Code Here
print(df.sort_values(by="PM2.5", ascending=False))

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
