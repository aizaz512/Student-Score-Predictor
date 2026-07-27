import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/student_scores.csv")

# Show first 5 rows
print("First 5 Rows")
print(df.head())

print("\n")

# Dataset information
print("Dataset Information")
print(df.info())

print("\n")

# Statistics
print("Statistics")
print(df.describe())

print("\n")

# Check missing values
print("Missing Values")
print(df.isnull().sum())