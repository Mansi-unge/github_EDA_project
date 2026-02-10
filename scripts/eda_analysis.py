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

# Create directory to store generated plots
# This ensures plots are saved inside the project repository
os.makedirs("../plots", exist_ok=True)

# Load the feature-engineered dataset
df = pd.read_csv("../data/featured_github_repos.csv")

# Convert date columns to datetime format for time-based analysis
df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

# Set a consistent visual theme for all plots
sns.set(style="whitegrid")

# ==================================================
# FIGURE 1: LANGUAGE POPULARITY & DISTRIBUTION
# ==================================================
# This figure analyzes language popularity and
# repository popularity using stars and forks.
# ==================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Language Popularity and Repository Distribution", fontsize=16)

# Plot 1: Total stars accumulated by each programming language
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

# Plot 2: Average stars per repository by language
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

# Plot 3: Distribution of stars across repositories
axes[1, 0].hist(df["stargazers_count"], bins=30)
axes[1, 0].set_title("Distribution of Stars")
axes[1, 0].set_xlabel("Stars")
axes[1, 0].set_ylabel("Repository Count")

# Plot 4: Relationship between stars and forks
axes[1, 1].scatter(df["stargazers_count"], df["forks_count"], alpha=0.6)
axes[1, 1].set_title("Forks vs Stars")
axes[1, 1].set_xlabel("Stars")
axes[1, 1].set_ylabel("Forks")

# Adjust layout and save figure
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("../plots/figure_1_language_popularity.png", dpi=300)
plt.show()

# ==================================================
# FIGURE 2: TIME-BASED & ACTIVITY ANALYSIS
# ==================================================
# This figure focuses on repository creation trends
# and recent activity levels across languages.
# ==================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Time-Based Trends and Repository Activity", fontsize=16)

# Plot 1: Number of repositories created per year
df["created_year"] = df["created_at"].dt.year
repos_per_year = df["created_year"].value_counts().sort_index()
repos_per_year.plot(kind="line", marker="o", ax=axes[0, 0])
axes[0, 0].set_title("Repositories Created Per Year")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Number of Repositories")

# Plot 2: Average inactivity duration by language
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

# Plot 3: Classification of repositories as active or inactive
df["activity_status"] = df["days_since_last_update"].apply(
    lambda x: "Active" if x <= 180 else "Inactive"
)
activity_count = df["activity_status"].value_counts()
activity_count.plot(kind="bar", ax=axes[1, 0])
axes[1, 0].set_title("Active vs Inactive Repositories")
axes[1, 0].set_xlabel("Status")
axes[1, 0].set_ylabel("Count")

# Plot 4: Recently updated repositories grouped by language
recent_repos = df[df["days_since_last_update"] <= 90]
recent_by_language = recent_repos["language"].value_counts()
recent_by_language.plot(kind="bar", ax=axes[1, 1])
axes[1, 1].set_title("Recently Updated Repositories by Language")
axes[1, 1].set_xlabel("Language")
axes[1, 1].set_ylabel("Repository Count")
axes[1, 1].tick_params(axis="x", rotation=45)

# Adjust layout and save figure
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("../plots/figure_2_time_activity_analysis.png", dpi=300)
plt.show()

# ==================================================
# FIGURE 3: DISTRIBUTION BY LANGUAGE & CORRELATION
# ==================================================
# This figure examines variation in stars by language
# and correlations between repository metrics.
# ==================================================

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("Stars Distribution and Correlation Analysis", fontsize=16)

# Plot 1: Box plot showing stars distribution for each language
sns.boxplot(
    x="language",
    y="stargazers_count",
    data=df,
    ax=axes[0]
)
axes[0].set_title("Stars Distribution by Language")
axes[0].set_xlabel("Language")
axes[0].set_ylabel("Stars")
axes[0].tick_params(axis="x", rotation=45)

# Plot 2: Heatmap showing correlations between key metrics
corr_cols = [
    "stargazers_count",
    "forks_count",
    "open_issues_count",
    "watchers_count",
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

# Adjust layout and save figure
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("../plots/figure_3_distribution_correlation.png", dpi=300)
plt.show()







































# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # --------------------------------------------------
# # STEP 6: EXPLORATORY DATA ANALYSIS (EDA)
# # --------------------------------------------------
# # Purpose:
# # This script performs exploratory data analysis on the
# # feature-engineered GitHub repository dataset. The goal
# # is to understand trends, distributions, correlations,
# # and activity patterns across repositories and languages.
# # --------------------------------------------------

# # Load the feature-engineered dataset created in Step 5
# df = pd.read_csv("../data/featured_github_repos.csv")

# # Convert date columns to datetime format to enable
# # time-based analysis and calculations
# df["created_at"] = pd.to_datetime(df["created_at"])
# df["updated_at"] = pd.to_datetime(df["updated_at"])

# # Apply a consistent visual style for all plots
# sns.set(style="whitegrid")

# # --------------------------------------------------
# # 1. LANGUAGE POPULARITY ANALYSIS
# # --------------------------------------------------
# # This section analyzes the popularity of programming
# # languages using star counts as a popularity indicator.

# # Compute total number of stars accumulated by repositories
# # belonging to each programming language
# stars_by_language = (
#     df.groupby("language")["stargazers_count"]
#     .sum()
#     .sort_values(ascending=False)
# )

# # Visualize total stars by programming language
# plt.figure(figsize=(10, 5))
# stars_by_language.plot(kind="bar")
# plt.title("Total Stars by Programming Language")
# plt.xlabel("Programming Language")
# plt.ylabel("Total Stars")
# plt.xticks(rotation=45)
# plt.show()

# # Compute average number of stars per repository
# # for each programming language
# avg_stars = (
#     df.groupby("language")["stargazers_count"]
#     .mean()
#     .sort_values(ascending=False)
# )

# # Visualize average stars per repository by language
# plt.figure(figsize=(10, 5))
# avg_stars.plot(kind="bar")
# plt.title("Average Stars per Repository by Language")
# plt.xlabel("Programming Language")
# plt.ylabel("Average Stars")
# plt.xticks(rotation=45)
# plt.show()

# # --------------------------------------------------
# # 2. DISTRIBUTION ANALYSIS
# # --------------------------------------------------
# # This section examines how stars and forks are distributed
# # across repositories and how they vary by language.

# # Plot a histogram to understand the distribution of stars
# # across all repositories
# plt.figure(figsize=(8, 5))
# plt.hist(df["stargazers_count"], bins=30)
# plt.title("Distribution of Stars Across Repositories")
# plt.xlabel("Number of Stars")
# plt.ylabel("Repository Count")
# plt.show()

# # Scatter plot to analyze the relationship between
# # stars and forks for repositories
# plt.figure(figsize=(8, 5))
# plt.scatter(df["stargazers_count"], df["forks_count"])
# plt.title("Relationship Between Stars and Forks")
# plt.xlabel("Stars")
# plt.ylabel("Forks")
# plt.show()

# # Box plot to compare the spread and variability of
# # star counts across different programming languages
# plt.figure(figsize=(12, 5))
# sns.boxplot(x="language", y="stargazers_count", data=df)
# plt.title("Stars Distribution by Programming Language")
# plt.xticks(rotation=45)
# plt.show()

# # --------------------------------------------------
# # 3. TIME-BASED ANALYSIS
# # --------------------------------------------------
# # This section analyzes repository creation trends and
# # recent activity patterns over time.

# # Extract the year from the repository creation date
# # to analyze yearly creation trends
# df["created_year"] = df["created_at"].dt.year

# # Count how many repositories were created each year
# repos_per_year = df["created_year"].value_counts().sort_index()

# # Line plot showing repository creation trend over time
# plt.figure(figsize=(8, 5))
# repos_per_year.plot(kind="line", marker="o")
# plt.title("Repositories Created Per Year")
# plt.xlabel("Year")
# plt.ylabel("Number of Repositories")
# plt.show()

# # Calculate the average number of days since the last
# # update for repositories in each programming language
# activity_trend = (
#     df.groupby("language")["days_since_last_update"]
#     .mean()
#     .sort_values()
# )

# # Bar chart showing average inactivity duration by language
# plt.figure(figsize=(10, 5))
# activity_trend.plot(kind="bar")
# plt.title("Average Days Since Last Update by Language")
# plt.xlabel("Programming Language")
# plt.ylabel("Days Since Last Update")
# plt.xticks(rotation=45)
# plt.show()

# # --------------------------------------------------
# # 4. CORRELATION ANALYSIS
# # --------------------------------------------------
# # This section identifies relationships between key
# # numerical metrics such as stars, forks, issues,
# # watchers, and popularity score.

# # Select numerical columns relevant for correlation analysis
# corr_cols = [
#     "stargazers_count",
#     "forks_count",
#     "open_issues_count",
#     "watchers_count",
#     "popularity_score"
# ]

# # Compute correlation matrix between selected metrics
# corr_matrix = df[corr_cols].corr()

# # Visualize correlations using a heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap of Repository Metrics")
# plt.show()

# # --------------------------------------------------
# # 5. ACTIVITY ANALYSIS
# # --------------------------------------------------
# # This section classifies repositories based on recent
# # activity and compares active versus inactive projects.

# # Define repository activity status based on the number
# # of days since the last update
# # Repositories updated within the last 180 days
# # are considered active
# df["activity_status"] = df["days_since_last_update"].apply(
#     lambda x: "Active" if x <= 180 else "Inactive"
# )

# # Count the number of active and inactive repositories
# activity_count = df["activity_status"].value_counts()

# # Visualize active versus inactive repositories
# plt.figure(figsize=(6, 4))
# activity_count.plot(kind="bar")
# plt.title("Active vs Inactive Repositories")
# plt.xlabel("Repository Status")
# plt.ylabel("Count")
# plt.show()

# # Filter repositories that were updated within the last
# # 90 days to analyze recently active projects
# recent_repos = df[df["days_since_last_update"] <= 90]

# # Count recently updated repositories by programming language
# recent_by_language = recent_repos["language"].value_counts()

# # Visualize recently updated repositories by language
# plt.figure(figsize=(10, 5))
# recent_by_language.plot(kind="bar")
# plt.title("Recently Updated Repositories by Language")
# plt.xlabel("Programming Language")
# plt.ylabel("Repository Count")
# plt.xticks(rotation=45)
# plt.show()



