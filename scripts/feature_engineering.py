import pandas as pd

# --------------------------------------------------
# STEP 5: FEATURE ENGINEERING
# --------------------------------------------------
# This step creates new meaningful features that help
# uncover deeper insights from the dataset.
# --------------------------------------------------

# 1. Load cleaned dataset
df = pd.read_csv("../data/cleaned_github_repos.csv")

print("Dataset Loaded for Feature Engineering")
print("Current Shape:", df.shape)
print("-" * 50)

# --------------------------------------------------
# 2. Convert date columns to datetime (safety check)
# --------------------------------------------------
df["created_at"] = pd.to_datetime(df["created_at"], utc=True)
df["updated_at"] = pd.to_datetime(df["updated_at"], utc=True)

# --------------------------------------------------
# 3. Repository Age (in Years)
# --------------------------------------------------
# Shows how old the repository is
df["repo_age_years"] = (
    (pd.Timestamp.now(tz="UTC") - df["created_at"]).dt.days / 365
).round(2)

print("Feature Created: repo_age_years")
print("-" * 50)

# --------------------------------------------------
# 4. Days Since Last Update
# --------------------------------------------------
# Indicates how recently the repository was active
df["days_since_last_update"] = (
    pd.Timestamp.now(tz="UTC") - df["updated_at"]
).dt.days

print("Feature Created: days_since_last_update")
print("-" * 50)

# --------------------------------------------------
# 5. Popularity Score
# --------------------------------------------------
# Combined popularity based on stars, forks, and watchers
df["popularity_score"] = (
    df["stargazers_count"]
    + df["forks_count"]
    + df["watchers_count"]
)

print("Feature Created: popularity_score")
print("-" * 50)

# --------------------------------------------------
# 6. Engagement Ratio
# --------------------------------------------------
# Measures active contribution compared to popularity
# Division by zero is avoided
df["engagement_ratio"] = (
    df["forks_count"] / df["stargazers_count"].replace(0, 1)
).round(3)

print("Feature Created: engagement_ratio")
print("-" * 50)

# --------------------------------------------------
# 7. Final Validation
# --------------------------------------------------
print("Final Missing Values Check:")
print(df.isnull().sum())
print("-" * 50)

# --------------------------------------------------
# 8. Save Feature-Engineered Dataset
# --------------------------------------------------
df.to_csv("../data/featured_github_repos.csv", index=False)

print("Feature-engineered dataset saved as 'featured_github_repos.csv'")
print("Final Dataset Shape:", df.shape)
print("-" * 50)
