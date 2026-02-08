import pandas as pd
import os

# -----------------------------
# 1. PATH TO DATA FOLDER
# -----------------------------
data_folder = "../data"

# -----------------------------
# 2. LIST OF CSV FILES
# -----------------------------
files = {
    "c": "c_repos.csv",
    "c++": "c++_repos.csv",
    "python": "python_repos.csv",
    "java": "java_repos.csv",
    "go": "go_repos.csv",
    "rust": "rust_repos.csv",
    "php": "php_repos.csv",
    "javascript": "javascript_repos.csv",
    "typescript": "typescript_repos.csv",
    "c#": "c#_repos.csv"
}

# -----------------------------
# 3. READ & MERGE FILES
# -----------------------------
all_data = []

for language, filename in files.items():
    file_path = os.path.join(data_folder, filename)
    
    df = pd.read_csv(file_path)
    df["language_source"] = language   # NEW COLUMN
    
    all_data.append(df)

# -----------------------------
# 4. COMBINE INTO ONE DATAFRAME
# -----------------------------
merged_df = pd.concat(all_data, ignore_index=True)

# -----------------------------
# 5. SAVE FINAL FILE
# -----------------------------
output_path = os.path.join(data_folder, "all_github_repos.csv")
merged_df.to_csv(output_path, index=False)

print("All CSV files merged successfully!")
print(f"Final dataset shape: {merged_df.shape}")
