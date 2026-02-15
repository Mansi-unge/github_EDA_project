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
df["year_month"] = df["updated_at"].dt.to_period("M")

# ==================================================
# 1. Average Stars per Language (Popularity)
# ==================================================
language_popularity = (
    df.groupby("language")["stargazers_count"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(x=language_popularity.index, y=language_popularity.values)
plt.title("Average Stars per Language")
plt.ylabel("Average Stars")
plt.xlabel("Language")
plt.xticks(rotation=45)
plt.savefig(f"{plots_dir}/01_language_popularity.png")
plt.close()

# ==================================================
# 2. Average Watchers per Language (Community Interest)
# ==================================================
watchers_per_language = (
    df.groupby("language")["watchers_count"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(x=watchers_per_language.index, y=watchers_per_language.values)
plt.title("Average Watchers per Language")
plt.ylabel("Average Watchers")
plt.xlabel("Language")
plt.xticks(rotation=45)
plt.savefig(f"{plots_dir}/02_watchers_comparison.png")
plt.close()

# ==================================================
# 3. Engagement Ratio per Language
# ==================================================
engagement_per_language = (
    df.groupby("language")["engagement_ratio"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(x=engagement_per_language.index, y=engagement_per_language.values)
plt.title("Average Engagement Ratio per Language")
plt.ylabel("Engagement Ratio")
plt.xlabel("Language")
plt.xticks(rotation=45)
plt.savefig(f"{plots_dir}/03_engagement_ratio.png")
plt.close()

# ==================================================
# 4. Rust: Stars per Day vs Forks (Focused Community)
# ==================================================
rust_df = df[df["language"] == "Rust"]

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=rust_df,
    x="stars_per_day",
    y="forks_count"
)
plt.title("Rust: Stars per Day vs Forks")
plt.xlabel("Stars per Day")
plt.ylabel("Forks")
plt.savefig(f"{plots_dir}/04_rust_focus.png")
plt.close()

# ==================================================
# 5. PHP Maintenance Pressure (Open Issues)
# ==================================================
php_df = df[df["language"] == "PHP"]

plt.figure(figsize=(8, 5))
sns.barplot(
    x="repo_name",
    y="open_issues_count",
    data=php_df
)
plt.title("PHP Repositories: Open Issues")
plt.xlabel("Repository")
plt.ylabel("Open Issues")
plt.xticks(rotation=90)
plt.savefig(f"{plots_dir}/05_php_maintenance.png")
plt.close()

# ==================================================
# 6. C & C++ Stability: Age vs Engagement
# ==================================================
c_df = df[df["language"].isin(["C", "C++"])]

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=c_df,
    x="repo_age_days",
    y="engagement_ratio",
    hue="language"
)
plt.title("C & C++: Repository Age vs Engagement")
plt.xlabel("Repository Age (Days)")
plt.ylabel("Engagement Ratio")
plt.savefig(f"{plots_dir}/06_c_cpp_stability.png")
plt.close()

# ==================================================
# 7. Popularity vs Maintenance
# ==================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="stargazers_count",
    y="open_issues_count",
    hue="language"
)
plt.title("Stars vs Open Issues")
plt.xlabel("Stars")
plt.ylabel("Open Issues")
plt.savefig(f"{plots_dir}/07_popularity_vs_issues.png")
plt.close()

# ==================================================
# 8. Star Growth per Language (Trending)
# ==================================================
stars_per_day_language = (
    df.groupby("language")["stars_per_day"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=stars_per_day_language.index,
    y=stars_per_day_language.values
)
plt.title("Average Stars per Day per Language")
plt.ylabel("Stars per Day")
plt.xlabel("Language")
plt.xticks(rotation=45)
plt.savefig(f"{plots_dir}/08_star_growth.png")
plt.close()

# ==================================================
# 9. Forks vs Stars (Collaboration Depth)
# ==================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="stargazers_count",
    y="forks_count",
    hue="language"
)
plt.title("Stars vs Forks")
plt.xlabel("Stars")
plt.ylabel("Forks")
plt.savefig(f"{plots_dir}/09_fork_behavior.png")
plt.close()

# ==================================================
# 10. Ecosystem Size vs Engagement
# ==================================================
repo_count = df["language"].value_counts()
engagement_avg = df.groupby("language")["engagement_ratio"].mean()

plt.figure(figsize=(12, 6))
sns.scatterplot(
    x=repo_count.index,
    y=engagement_avg.values,
    size=repo_count.values,
    sizes=(200, 1200),
    hue=repo_count.index,
    legend=False
)
plt.title("Ecosystem Size vs Engagement")
plt.xlabel("Language")
plt.ylabel("Average Engagement Ratio")
plt.savefig(f"{plots_dir}/10_ecosystem_size_vs_quality.png")
plt.close()

# ==================================================
# 11. Repository Age vs Popularity
# ==================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="repo_age_years",
    y="stargazers_count",
    hue="language"
)
plt.title("Repository Age vs Stars")
plt.xlabel("Repository Age (Years)")
plt.ylabel("Stars")
plt.savefig(f"{plots_dir}/11_age_vs_popularity.png")
plt.close()

# ==================================================
# 12. Activity Load (Issues vs Days Since Update)
# ==================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="days_since_last_update",
    y="open_issues_count",
    hue="language"
)
plt.title("Days Since Last Update vs Open Issues")
plt.xlabel("Days Since Last Update")
plt.ylabel("Open Issues")
plt.savefig(f"{plots_dir}/12_activity_load.png")
plt.close()

plt.tight_layout()

print("All 12 insight visualizations generated successfully!")
