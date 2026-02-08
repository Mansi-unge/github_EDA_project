import requests
import csv
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This is used to securely read the GitHub token
load_dotenv()

# ----------------------------------
# 1. GITHUB AUTHENTICATION
# ----------------------------------

# Read GitHub Personal Access Token from environment variable
# The token is not hardcoded for security reasons
TOKEN = os.getenv("GITHUB_TOKEN")

# Request headers including authorization
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# ----------------------------------
# 2. API CONFIGURATION
# ----------------------------------

# GitHub Search Repositories API endpoint
url = "https://api.github.com/search/repositories"

# List of programming languages to be analyzed
languages = [
    "c",
    "c++",
    "python",
    "java",
    "go",
    "rust",
    "php",
    "javascript",
    "typescript",
    "c#"
]

# Number of pages to fetch per language
# Each page contains up to 100 repositories
pages_per_language = 5
repos_per_page = 100

# ----------------------------------
# 3. DATA COLLECTION PROCESS
# ----------------------------------

# Loop through each programming language
for language in languages:
    print(f"\nCollecting data for: {language.upper()}")

    # List to store all repositories for the current language
    all_repos = []

    # Loop through paginated API results
    for page in range(1, pages_per_language + 1):
        # Query parameters for the API request
        params = {
            "q": f"language:{language}",   # Filter repositories by language
            "sort": "stars",              # Sort repositories by star count
            "order": "desc",              # Highest stars first
            "per_page": repos_per_page,   # Number of repositories per page
            "page": page                  # Page number
        }

        # Send GET request to GitHub API
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # Check if valid repository data is returned
        if "items" not in data:
            print("Error fetching data:", data)
            break

        # Add repositories from the current page to the main list
        all_repos.extend(data["items"])
        print(f"  Page {page} collected ({len(data['items'])} repos)")

        # Pause between requests to avoid hitting API rate limits
        time.sleep(1)

    # ----------------------------------
    # 4. SAVE COLLECTED DATA TO CSV
    # ----------------------------------

    # File path for saving language-specific data
    file_path = f"../data/{language}_repos.csv"

    # Open CSV file in write mode
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow([
            "repo_name",
            "language",
            "created_at",
            "updated_at",
            "stargazers_count",
            "forks_count",
            "open_issues_count",
            "watchers_count",
            "size"
        ])

        # Write repository data rows
        for repo in all_repos:
            writer.writerow([
                repo.get("name"),
                repo.get("language"),
                repo.get("created_at"),
                repo.get("updated_at"),
                repo.get("stargazers_count"),
                repo.get("forks_count"),
                repo.get("open_issues_count"),
                repo.get("watchers_count"),
                repo.get("size")
            ])

    print(f"Saved {len(all_repos)} repositories to {file_path}")

# ----------------------------------
# 5. COMPLETION MESSAGE
# ----------------------------------

print("\nData collection completed for all languages.")
