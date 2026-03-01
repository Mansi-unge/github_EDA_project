import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------
# STEP 6: EXPLORATORY DATA ANALYSIS (EDA)
# --------------------------------------------------
# Objective:
# Perform exploratory data analysis on the feature-
# engineered GitHub repository dataset to uncover:
# - Popular programming languages
# - Distribution of stars and forks
# - Time-based trends
# - Repository activity patterns
# - Correlation between repository metrics
# --------------------------------------------------

# Create directory for plots
os.makedirs("../plots", exist_ok=True)

# Load dataset
df = pd.read_csv("../data/processed/featured_github_repos.csv")

# Convert dates
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

# Handle missing languages
df["language"] = df["language"].fillna("Unknown")

# Set theme
sns.set(style="whitegrid")

# ==================================================
# FIGURE 1: LANGUAGE POPULARITY & DISTRIBUTION
# ==================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Language Popularity and Repository Distribution", fontsize=16)

# Total Stars by Language
stars_by_language = (
    df.groupby("language")["stargazers_count"]
    .sum()
    .sort_values(ascending=False)
)
stars_by_language.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Total Stars by Language")
axes[0, 0].set_xlabel("Language")
axes[0, 0].set_ylabel("Total Stars")
axes[0, 0].tick_params(axis="x", rotation=45)

# Average Stars per Repo
avg_stars = (
    df.groupby("language")["stargazers_count"]
    .mean()
    .sort_values(ascending=False)
)
avg_stars.plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Average Stars per Repository")
axes[0, 1].set_xlabel("Language")
axes[0, 1].set_ylabel("Average Stars")
axes[0, 1].tick_params(axis="x", rotation=45)

# Log-Stars Distribution
axes[1, 0].hist(df["log_stars"], bins=30)
axes[1, 0].set_title("Distribution of Log(Stars)")
axes[1, 0].set_xlabel("Log(Stars)")
axes[1, 0].set_ylabel("Repository Count")

# Log Stars vs Log Forks
axes[1, 1].scatter(df["log_stars"], df["log_forks"], alpha=0.6)
axes[1, 1].set_title("Forks vs Stars (Log Scale)")
axes[1, 1].set_xlabel("Log(Stars)")
axes[1, 1].set_ylabel("Log(Forks)")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("../plots/figure_1_language_popularity.png", dpi=300)
plt.show()


# ==================================================
# FIGURE 2: TIME-BASED & ACTIVITY ANALYSIS
# ==================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Time-Based Trends and Repository Activity", fontsize=16)

# Repositories Created Per Year
df["created_year"] = df["created_at"].dt.year
repos_per_year = df["created_year"].value_counts().sort_index()
repos_per_year.plot(kind="line", marker="o", ax=axes[0, 0])
axes[0, 0].set_title("Repositories Created Per Year")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Number of Repositories")

# Average Days Since Last Update by Language
activity_trend = (
    df.groupby("language")["days_since_last_update"]
    .mean()
    .sort_values()
)
activity_trend.plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Average Days Since Last Update by Language")
axes[0, 1].set_xlabel("Language")
axes[0, 1].set_ylabel("Days Since Last Update")
axes[0, 1].tick_params(axis="x", rotation=45)

# Active vs Inactive
df["activity_status"] = df["days_since_last_update"].apply(
    lambda x: "Active" if x <= 180 else "Inactive"
)
activity_count = df["activity_status"].value_counts()
activity_count.plot(kind="bar", ax=axes[1, 0])
axes[1, 0].set_title("Active vs Inactive Repositories")
axes[1, 0].set_xlabel("Status")
axes[1, 0].set_ylabel("Count")

# Recently Updated Repos (Last 90 Days)
recent_repos = df[df["days_since_last_update"] <= 90]
recent_by_language = recent_repos["language"].value_counts()
recent_by_language.plot(kind="bar", ax=axes[1, 1])
axes[1, 1].set_title("Recently Updated Repositories by Language")
axes[1, 1].set_xlabel("Language")
axes[1, 1].set_ylabel("Repository Count")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("../plots/figure_2_time_activity_analysis.png", dpi=300)
plt.show()


# ==================================================
# FIGURE 3: DISTRIBUTION & CORRELATION
# ==================================================

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("Stars Distribution and Correlation Analysis", fontsize=16)

# Boxplot (Log Stars by Language)
sns.boxplot(
    x="language",
    y="log_stars",
    data=df,
    ax=axes[0]
)
axes[0].set_title("Log(Stars) Distribution by Language")
axes[0].set_xlabel("Language")
axes[0].set_ylabel("Log(Stars)")
axes[0].tick_params(axis="x", rotation=45)

# Correlation Heatmap (Using Log Features)
corr_cols = [
    "log_stars",
    "log_forks",
    "open_issues_count",
    "log_watchers",
    "popularity_score"
]

corr_matrix = df[corr_cols].corr()

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    ax=axes[1]
)
axes[1].set_title("Correlation Heatmap of Repository Metrics")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("../plots/figure_3_distribution_correlation.png", dpi=300)
plt.show()



































