import pandas as pd
import os

# ----------------------------------
# 1. DATA FOLDER PATH
# ----------------------------------

# Path where all language-wise CSV files are stored
data_folder = "../data"

# ----------------------------------
# 2. CSV FILE MAPPING
# ----------------------------------

# Dictionary mapping programming languages to their CSV file names
# Each file contains repository data collected from GitHub API
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

# ----------------------------------
# 3. READ AND STORE DATA
# ----------------------------------

# List to store DataFrames from all CSV files
all_data = []

# Loop through each language and its corresponding CSV file
for language, filename in files.items():
    # Construct full file path
    file_path = os.path.join(data_folder, filename)
    
    # Read CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Add a new column to identify the language source
    # This is important after merging all datasets
    df["language_source"] = language
    
    # Append DataFrame to the list
    all_data.append(df)

# ----------------------------------
# 4. MERGE ALL DATAFRAMES
# ----------------------------------

# Combine all DataFrames into a single DataFrame
# ignore_index=True resets the index after merging
merged_df = pd.concat(all_data, ignore_index=True)

# ----------------------------------
# 5. SAVE MERGED DATASET
# ----------------------------------

# Path for the final merged CSV file
output_path = os.path.join(data_folder, "all_github_repos.csv")

# Save the merged DataFrame to a CSV file
merged_df.to_csv(output_path, index=False)

# ----------------------------------
# 6. CONFIRMATION OUTPUT
# ----------------------------------

print("All CSV files merged successfully!")
print(f"Final dataset shape: {merged_df.shape}")
