GitHub Repository Exploratory Data Analysis (EDA)
Project Overview

Open-source software development plays a critical role in modern technology, and GitHub is the largest platform hosting millions of repositories across diverse programming languages.
This project performs Exploratory Data Analysis (EDA) on GitHub repository data to uncover trends related to programming language popularity, repository activity, community engagement, and project maintenance.

The analysis is based on real-world data collected using the GitHub REST API and focuses on understanding how different programming languages perform across key repository metrics.

Problem Statement

With the rapid growth of open-source projects on GitHub, it becomes difficult to understand development trends, language popularity, and repository health using raw data alone.
This project aims to analyze GitHub repositories using data-driven techniques to extract meaningful insights and patterns that help in understanding open-source ecosystems.

Objectives

To collect and analyze GitHub repository data using the GitHub REST API

To compare popularity and engagement metrics across programming languages

To analyze repository activity and maintenance behavior

To visualize trends and correlations among repository features

To derive actionable insights from exploratory data analysis

Dataset Description

The dataset was collected using the GitHub REST API and consists of popular public repositories across multiple programming languages.

Number of repositories: ~5,000

Programming languages analyzed: C, C++, Python, Java, Go, Rust, PHP, JavaScript, TypeScript, C#

Data format: CSV

Key Attributes

Repository name

Programming language

Stargazers count

Forks count

Watchers count

Open issues count

Created date

Last updated date

Data Cleaning & Feature Engineering
Data Cleaning

Converted date columns to datetime format

Handled missing values where necessary

Ensured numerical consistency across metrics

Feature Engineering

The following derived features were created:

Repository Age (years) – time since repository creation

Days Since Last Update – measure of repository activity

Popularity Score – combined metric using stars, forks, and watchers

Engagement Ratio – forks-to-stars ratio

These features helped uncover deeper insights into repository popularity and engagement patterns.

Exploratory Data Analysis (EDA)

EDA was performed using statistical summaries and visualizations to explore trends, distributions, and relationships.

Analyses Performed

Programming language popularity analysis

Distribution analysis of stars and forks

Time-based analysis of repository creation and updates

Correlation analysis between repository metrics

Activity-based analysis of repositories

Visualizations were created using Matplotlib and Seaborn.

Key Insights

A small number of repositories account for a large proportion of total stars, indicating a highly skewed popularity distribution.

Some programming languages exhibit higher engagement ratios, suggesting deeper contributor involvement.

Actively maintained repositories tend to have higher popularity and community engagement.

Stars and forks show a strong positive correlation, indicating that popular repositories are more likely to attract contributions.

Tools & Technologies Used

Python

Pandas

Matplotlib

Seaborn

GitHub REST API

Project Structure
github-eda-project/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda_analysis.ipynb
├── scripts/
│   └── collect_github_data.py
├── README.md
└── requirements.txt

Conclusion

This project demonstrates how Exploratory Data Analysis can be effectively used to analyze large-scale GitHub repository data.
By examining popularity, engagement, and activity metrics, the project provides valuable insights into open-source development trends across multiple programming languages.

Future Scope

Predict repository popularity using machine learning models

Perform time-series analysis using historical GitHub data

Integrate Stack Overflow or GH Archive datasets

Build an interactive dashboard using Power BI or Streamlit

Author

Mansi Unge
