import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------
# Configuration
# -------------------------
sns.set(style="whitegrid")
plots_dir = "../plots/"
os.makedirs(plots_dir, exist_ok=True)

# -------------------------
# Load Data
# -------------------------
df = pd.read_csv("../data/processed/featured_github_repos.csv")

# Handle missing languages
df["language"] = df["language"].fillna("Unknown")

# Convert dates
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

# ==================================================
# 1. Average Stars per Language
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
# 2. Average Watchers per Language
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
# 4. Rust: Stars per Day vs Forks
# ==================================================
rust_df = df[df["language"] == "Rust"]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=rust_df, x="stars_per_day", y="forks_count")
plt.title("Rust: Stars per Day vs Forks")
plt.xlabel("Stars per Day")
plt.ylabel("Forks")
plt.savefig(f"{plots_dir}/04_rust_focus.png")
plt.close()

# ==================================================
# 5. PHP Maintenance Pressure
# ==================================================
php_df = df[df["language"] == "PHP"]

top_php = php_df.sort_values(
    by="open_issues_count",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x="open_issues_count", y="repo_name", data=top_php)
plt.title("Top 10 PHP Repositories by Open Issues")
plt.xlabel("Open Issues")
plt.ylabel("Repository")
plt.savefig(f"{plots_dir}/05_php_maintenance.png")
plt.close()

# ==================================================
# 6. C & C++ Stability
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
# 7. Popularity vs Maintenance (Log Scale)
# ==================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="log_stars",
    y="open_issues_count",
    hue="language"
)
plt.title("Log(Stars) vs Open Issues")
plt.xlabel("Log(Stars)")
plt.ylabel("Open Issues")
plt.savefig(f"{plots_dir}/07_popularity_vs_issues.png")
plt.close()

# ==================================================
# 8. Star Growth per Language
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
# 9. Forks vs Stars (Log Scale)
# ==================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="log_stars",
    y="log_forks",
    hue="language"
)
plt.title("Log(Stars) vs Log(Forks)")
plt.xlabel("Log(Stars)")
plt.ylabel("Log(Forks)")
plt.savefig(f"{plots_dir}/09_fork_behavior.png")
plt.close()

# ==================================================
# 10. Ecosystem Size vs Engagement
# ==================================================
repo_count = df["language"].value_counts()
engagement_avg = df.groupby("language")["engagement_ratio"].mean()

eco_df = pd.DataFrame({
    "language": repo_count.index,
    "repo_count": repo_count.values,
    "engagement": engagement_avg.values
})

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=eco_df,
    x="repo_count",
    y="engagement",
    size="repo_count",
    sizes=(200, 1200),
    hue="language"
)
plt.title("Ecosystem Size vs Engagement")
plt.xlabel("Number of Repositories")
plt.ylabel("Average Engagement Ratio")
plt.savefig(f"{plots_dir}/10_ecosystem_size_vs_quality.png")
plt.close()

# ==================================================
# 11. Repository Age vs Popularity (Log Scale)
# ==================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="repo_age_years",
    y="log_stars",
    hue="language"
)
plt.title("Repository Age vs Log(Stars)")
plt.xlabel("Repository Age (Years)")
plt.ylabel("Log(Stars)")
plt.savefig(f"{plots_dir}/11_age_vs_popularity.png")
plt.close()

# ==================================================
# 12. Activity Load
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

print("All 12 final insight visualizations generated successfully!")