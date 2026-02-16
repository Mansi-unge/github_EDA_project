import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------
# Config
# -------------------------
sns.set(style="whitegrid")
plots_dir = "../plots/"
os.makedirs(plots_dir, exist_ok=True)

# -------------------------
# Load data
# -------------------------
df = pd.read_csv("../data/processed/featured_github_repos.csv")

# Convert dates
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

# Year-month for trends
# Filter only PHP repositories
php_df = df[df["language"] == "PHP"]

# Sort and take top 10 by open issues
top_php = php_df.sort_values(
    by="open_issues_count",
    ascending=False
).head(10)

plt.figure(figsize=(10,6))
sns.barplot(
    x="open_issues_count",
    y="repo_name",
    data=top_php
)
plt.title("Top 10 PHP Repositories by Open Issues")
plt.xlabel("Open Issues")
plt.ylabel("Repository")
plt.savefig(f"{plots_dir}/05_php_maintenance.png")
plt.close()
