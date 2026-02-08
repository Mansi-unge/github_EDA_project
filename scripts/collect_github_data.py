import requests
import csv
import time
import os
from dotenv import load_dotenv
load_dotenv()

# ----------------------------------
# 1. YOUR GITHUB TOKEN
# ----------------------------------



TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# ----------------------------------
# 2. CONFIGURATION
# ----------------------------------
url = "https://api.github.com/search/repositories"

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

pages_per_language = 5    
repos_per_page = 100

# ----------------------------------
# 3. DATA COLLECTION
# ----------------------------------
for language in languages:
    print(f"\nCollecting data for: {language.upper()}")
    
    all_repos = []

    for page in range(1, pages_per_language + 1):
        params = {
            "q": f"language:{language}",
            "sort": "stars",
            "order": "desc",
            "per_page": repos_per_page,
            "page": page
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if "items" not in data:
            print("Error fetching data:", data)
            break

        all_repos.extend(data["items"])
        print(f"  Page {page} collected ({len(data['items'])} repos)")
        
        time.sleep(1)  # polite pause to avoid rate limits

    # ----------------------------------
    # 4. SAVE TO CSV
    # ----------------------------------
    file_path = f"../data/{language}_repos.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

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

print("\n✅ Data collection completed for all languages!")
