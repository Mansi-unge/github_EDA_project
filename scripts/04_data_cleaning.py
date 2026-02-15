import pandas as pd

# ==================================================
# STEP 4: DATA CLEANING
# Purpose:
# Clean and prepare GitHub repository data for
# Exploratory Data Analysis (EDA)
# ==================================================

# --------------------------------------------------
# 1. Load the raw dataset
# --------------------------------------------------
# Reading the merged GitHub repository dataset
df = pd.read_csv("../data/raw/all_github_repos.csv")

# Display original shape of the dataset
print("Original Dataset Shape:", df.shape)
print("-" * 50)

# --------------------------------------------------
# 2. Handle Missing Values
# (Mandatory step even if data appears clean)
# --------------------------------------------------

# Fill missing programming language values with 'Unknown'
# This avoids issues during grouping and visualization
df["language"] = df["language"].fillna("Unknown")

# Fill missing numeric values with 0
# These columns represent counts and size, so 0 is reasonable
numeric_cols = ["stargazers_count", "forks_count", "size"]
df[numeric_cols] = df[numeric_cols].fillna(0)

# Verify missing values after handling
print("Missing Values After Handling:")
print(df.isnull().sum())
print("-" * 50)

# --------------------------------------------------
# 3. Remove Duplicate Repositories
# --------------------------------------------------
# Removing duplicate repositories based on
# combination of repository name and language
df = df.drop_duplicates(subset=["repo_name", "language"])

print("Dataset Shape After Removing Duplicates:", df.shape)
print("-" * 50)

# --------------------------------------------------
# 4. Convert Date Columns to Datetime Format
# --------------------------------------------------
# Convert GitHub timestamp strings to datetime objects
# UTC timezone is used to maintain consistency
df["created_at"] = pd.to_datetime(df["created_at"], utc=True)
df["updated_at"] = pd.to_datetime(df["updated_at"], utc=True)

print("Date Columns Converted to Datetime")
print("-" * 50)

# --------------------------------------------------
# 5. Handle Outliers
# --------------------------------------------------
# Capping extreme values at the 99th percentile
# This prevents highly popular repositories from
# skewing analysis and visualizations
for col in ["stargazers_count", "forks_count", "size"]:
    upper_limit = df[col].quantile(0.99)
    df[col] = df[col].clip(upper=upper_limit)

print("Outliers Capped at 99th Percentile")
print("-" * 50)

# --------------------------------------------------
# 6. Standardize Column Names
# --------------------------------------------------
# Convert all column names to lowercase and remove spaces
# This improves consistency and avoids coding errors
df.columns = df.columns.str.lower().str.strip()

print("Column Names Standardized")
print("-" * 50)

# --------------------------------------------------
# 7. Feature Engineering
# --------------------------------------------------
# Creating new features to support deeper analysis

# Calculate repository age in days
df["repo_age_days"] = (
    pd.Timestamp.now(tz="UTC") - df["created_at"]
).dt.days

# Calculate average stars gained per day
# This measures repository popularity growth
df["stars_per_day"] = df["stargazers_count"] / df["repo_age_days"]

print("New Features Created: repo_age_days, stars_per_day")
print("-" * 50)

# --------------------------------------------------
# 8. Final Validation Checks
# --------------------------------------------------

# Final missing values check
print("Final Missing Values Check:")
print(df.isnull().sum())
print("-" * 50)

# Final duplicate check
print("Final Duplicate Check:")
print(df.duplicated(subset=["repo_name", "language"]).sum())
print("-" * 50)

# --------------------------------------------------
# 9. Save Cleaned Dataset
# --------------------------------------------------
# Saving cleaned dataset for EDA and visualization
df.to_csv("../data/processed/cleaned_github_repos.csv", index=False)

print("Cleaned dataset saved as 'cleaned_github_repos.csv'")
print("Final Dataset Shape:", df.shape)
