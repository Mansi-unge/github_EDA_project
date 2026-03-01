import pandas as pd
import numpy as np

# --------------------------------------------------
# STEP 5: FEATURE ENGINEERING
# --------------------------------------------------
# This step creates new meaningful features that help
# uncover deeper insights from the dataset.
# --------------------------------------------------

# 1. Load cleaned dataset
df = pd.read_csv("../data/processed/cleaned_github_repos.csv")

print("Dataset Loaded for Feature Engineering")
print("Current Shape:", df.shape)
print("-" * 50)

# --------------------------------------------------
# 2. Convert date columns to datetime (safety check)
# --------------------------------------------------
df["created_at"] = pd.to_datetime(df["created_at"], utc=True)
df["updated_at"] = pd.to_datetime(df["updated_at"], utc=True)

print("Date Columns Verified")
print("-" * 50)

# --------------------------------------------------
# 3. Log Transformation (Reduce Skewness)
# --------------------------------------------------
# GitHub popularity metrics are highly right-skewed.
# Log transformation stabilizes variance and improves analysis.

df["log_stars"] = np.log1p(df["stargazers_count"])
df["log_forks"] = np.log1p(df["forks_count"])
df["log_watchers"] = np.log1p(df["watchers_count"])

print("Log Features Created: log_stars, log_forks, log_watchers")
print("-" * 50)

# --------------------------------------------------
# 4. Repository Age (in Years)
# --------------------------------------------------
# Shows how old the repository is
df["repo_age_years"] = (
    (pd.Timestamp.now(tz="UTC") - df["created_at"]).dt.days / 365
).round(2)

print("Feature Created: repo_age_years")
print("-" * 50)

# --------------------------------------------------
# 5. Days Since Last Update
# --------------------------------------------------
# Indicates how recently the repository was active
df["days_since_last_update"] = (
    pd.Timestamp.now(tz="UTC") - df["updated_at"]
).dt.days

print("Feature Created: days_since_last_update")
print("-" * 50)

# --------------------------------------------------
# 6. Popularity Score (Log-Based)
# --------------------------------------------------
# Combined popularity using log-transformed metrics
# Prevents extreme repositories from dominating analysis

df["popularity_score"] = (
    df["log_stars"]
    + df["log_forks"]
    + df["log_watchers"]
).round(3)

print("Feature Created: popularity_score (log-based)")
print("-" * 50)

# --------------------------------------------------
# 7. Engagement Ratio
# --------------------------------------------------
# Measures contributor activity relative to popularity
# +1 avoids division-by-zero errors

df["engagement_ratio"] = (
    df["forks_count"] / (df["stargazers_count"] + 1)
).round(3)

print("Feature Created: engagement_ratio")
print("-" * 50)

# --------------------------------------------------
# 8. Final Validation
# --------------------------------------------------
print("Final Missing Values Check:")
print(df.isnull().sum())
print("-" * 50)

# --------------------------------------------------
# 9. Save Feature-Engineered Dataset
# --------------------------------------------------
df.to_csv("../data/processed/featured_github_repos.csv", index=False)

print("Feature-engineered dataset saved as 'featured_github_repos.csv'")
print("Final Dataset Shape:", df.shape)
print("-" * 50)