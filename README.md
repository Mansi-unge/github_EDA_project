# GitHub Repository Exploratory Data Analysis (EDA)

## Project Overview
Open-source software development plays a critical role in modern technology, and GitHub is the largest platform hosting millions of repositories across diverse programming languages.

This project performs **Exploratory Data Analysis (EDA)** on GitHub repository data to uncover trends related to:
- Programming language popularity  
- Repository activity and maintenance  
- Community engagement  
- Relationships between key repository metrics  

The analysis is based on real-world data collected using the **GitHub REST API** and focuses on understanding how different programming languages perform across important repository indicators.

---

## Problem Statement
With the rapid growth of open-source projects on GitHub, it becomes difficult to understand development trends, language popularity, and repository health using raw data alone.

This project aims to analyze GitHub repositories using data-driven techniques to extract meaningful insights and patterns that help in understanding the open-source ecosystem.

---

## Objectives
- To collect GitHub repository data using the GitHub REST API  
- To analyze popularity and engagement metrics across programming languages  
- To study repository activity and maintenance behavior  
- To visualize trends and correlations among repository features  
- To derive actionable insights using exploratory data analysis  

---

## Dataset Description
The dataset was collected using the GitHub REST API and consists of popular public repositories across multiple programming languages.

- **Number of repositories:** ~5,000  
- **Programming languages analyzed:**  
  C, C++, Python, Java, Go, Rust, PHP, JavaScript, TypeScript, C#  
- **Data format:** CSV  

### Key Attributes
- Repository name  
- Programming language  
- Stargazers count  
- Forks count  
- Watchers count  
- Open issues count  
- Created date  
- Last updated date
- size

---

## Data Cleaning & Feature Engineering

### Data Cleaning
- Converted date columns to datetime format  
- Handled missing values where necessary  
- Ensured numerical consistency across all metrics  

### Feature Engineering
The following derived features were created to enhance analysis:

- **Repository Age (years):** Time since repository creation  
- **Days Since Last Update:** Indicator of repository activity  
- **Popularity Score:** Combined metric using stars, forks, and watchers  
- **Engagement Ratio:** Forks-to-stars ratio  

These features helped uncover deeper insights into repository popularity and engagement patterns.

---

## Exploratory Data Analysis (EDA)
EDA was performed using statistical summaries and visualizations to explore trends, distributions, and relationships within the dataset.

### Analyses Performed
- Programming language popularity analysis  
- Distribution analysis of stars and forks  
- Time-based analysis of repository creation and updates  
- Correlation analysis between repository metrics  
- Activity-based analysis of repositories  

Visualizations were created using **Matplotlib** and **Seaborn**.

---

## Key Insights
- A small number of repositories account for a large proportion of total stars, indicating a highly skewed popularity distribution  
- Some programming languages exhibit higher engagement ratios, suggesting deeper contributor involvement  
- Actively maintained repositories tend to have higher popularity and community engagement  
- Stars and forks show a strong positive correlation, indicating that popular repositories are more likely to attract contributions  

---

## Tools & Technologies Used
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- GitHub REST API  

---

## Project Structure

```text
GITHUB_EDA_PROJECT/
│
├── data/
│   ├── raw/
│   │   ├── all_github_repos.csv
│   │   ├── c_repos.csv
│   │   ├── c#_repos.csv
│   │   ├── c++_repos.csv
│   │   ├── go_repos.csv
│   │   ├── java_repos.csv
│   │   ├── javascript_repos.csv
│   │   ├── php_repos.csv
│   │   ├── python_repos.csv
│   │   ├── rust_repos.csv
│   │   └── typescript_repos.csv
│   │
│   ├── processed/
│   │   ├── cleaned_github_repos.csv
│   │   └── featured_github_repos.csv
│
├── plots/
│   │   ├── figure_1_language_popularity.png
│   │   ├── figure_2_time_activity.png
│   │   └── figure_3_distribution_analysis.png
│
├── scripts/
│   │   ├── 01_collect_github_data.py
│   │   ├── 02_merge_csvs.py
│   │   ├── 03_data_understanding.py
│   │   ├── 04_data_cleaning.py
│   │   ├── 05_feature_engineering.py
│   │   └── 06_eda_analysis.py
│
├── .env
├── .gitignore
└── README.md
```


---

## Conclusion
This project demonstrates how **Exploratory Data Analysis** can be effectively used to analyze large-scale GitHub repository data.

By examining popularity, engagement, and activity metrics, the project provides valuable insights into open-source development trends across multiple programming languages.

---

## Future Scope
- Predict repository popularity using machine learning models  
- Perform time-series analysis using historical GitHub data  
- Integrate Stack Overflow or GH Archive datasets  
- Build an interactive dashboard using Power BI or Streamlit  

---

## Author
**Mansi Unge**
