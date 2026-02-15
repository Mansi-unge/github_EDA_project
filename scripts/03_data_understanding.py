import pandas as pd

# -------------------------------------------------------
# STEP 3: Data Understanding & Sanity Check
# This script is used to understand the structure, quality,
# and basic characteristics of the merged dataset before
# performing data cleaning or exploratory analysis.
# -------------------------------------------------------

# Load the merged GitHub repository dataset from the data folder
df = pd.read_csv("../data/raw/all_github_repos.csv")

# -------------------------------------------------------
# 1. Check the shape of the dataset
# This shows the total number of rows (repositories)
# and columns (features) present in the dataset
# -------------------------------------------------------
print("Dataset Shape (Rows, Columns):")
print(df.shape)
print("-" * 50)

# -------------------------------------------------------
# 2. Display column names
# This helps in understanding what attributes are
# available in the dataset
# -------------------------------------------------------
print("Column Names:")
print(df.columns)
print("-" * 50)

# -------------------------------------------------------
# 3. Inspect data types and non-null values
# This provides information about each column,
# including data type and presence of missing values
# -------------------------------------------------------
print("Dataset Info:")
df.info()
print("-" * 50)

# -------------------------------------------------------
# 4. Generate statistical summary for numerical columns
# This includes count, mean, standard deviation,
# minimum, maximum, and percentile values
# -------------------------------------------------------
print("Statistical Summary:")
print(df.describe())
print("-" * 50)

# -------------------------------------------------------
# 5. Check for missing values in each column
# This helps identify columns that may require
# cleaning or special handling
# -------------------------------------------------------
print("Missing Values per Column:")
print(df.isnull().sum())
print("-" * 50)

# -------------------------------------------------------
# 6. Check for duplicate records
# Duplicate rows can lead to biased analysis,
# so it is important to detect them early
# -------------------------------------------------------
print("Duplicate Rows Count:")
print(df.duplicated().sum())
print("-" * 50)

# -------------------------------------------------------
# 7. Count unique programming languages
# This provides an overview of the diversity of
# programming languages in the dataset
# -------------------------------------------------------
if "language" in df.columns:
    print("Total Unique Programming Languages:")
    print(df["language"].nunique())
