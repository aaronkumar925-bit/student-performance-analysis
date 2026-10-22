# Student Performance Analytics

## Project Overview

This project analyzes student academic performance using Python and Pandas.

The analysis explores student marks, attendance, subject performance, performance categories, and the relationship between attendance and academic performance.

The project also demonstrates basic data cleaning techniques such as handling missing values and removing duplicate records.

## Objectives

- Analyze student academic performance
- Calculate individual student averages
- Compare average performance across subjects
- Identify the top-performing students
- Identify students who may need academic support
- Analyze attendance and academic performance
- Detect missing values and duplicate records
- Clean and export the dataset
- Create visualizations using Matplotlib

## Technologies Used

- Python
- Pandas
- Matplotlib
- Spyder
- Anaconda

## Dataset

The dataset contains information about:

- Student ID
- Name
- Gender
- Age
- Attendance
- Mathematics marks
- Science marks
- English marks
- Computer Science marks

## Data Analysis

The project calculates:

- Average marks for each student
- Average marks for each subject
- Top 3 students
- Students requiring academic support
- Performance categories
- Attendance-performance correlation

## Data Cleaning

The project demonstrates:

- Missing value detection
- Missing value replacement using mean imputation
- Duplicate record detection
- Duplicate removal
- Recalculation of derived values after cleaning

## Visualizations

The project includes:

1. Attendance vs Average Marks scatter plot
2. Average Performance by Subject bar chart
3. Student Performance Category chart
4. Student Performance Ranking chart

## Key Findings

- Computer Science has the highest average subject score in the dataset.
- Ishita is the highest-performing student based on average marks.
- Vikram has the lowest average performance.
- Students with lower attendance generally show lower academic performance in this dataset.
- The dataset demonstrates a strong positive correlation between attendance and average marks.

## Important Note

The dataset used in this project is a small educational dataset created for analysis and demonstration purposes.

The observed correlation between attendance and marks should not be interpreted as proof that attendance directly causes higher academic performance.

## Project Structure

```text
student-performance-analysis/
│
├── analysis.py
├── students_cleaned.csv
└── README.md

## Key Findings

- **Highest-performing student:** Ishita — average score of **96.75**
- **Lowest-performing student:** Vikram — average score of **58.50**
- **Top 3 students:** Ishita, Ananya, and Sneha
- **Highest-performing subject:** Computer Science — average of **85.8**
- **Lowest-performing subject:** Mathematics — average of **76.8**
- **Students identified for additional support:** Arjun and Vikram
- **Average attendance:** **83.2%**
- **Attendance vs. average marks correlation:** **0.99**

The analysis suggests a strong positive relationship between attendance and academic performance in this dataset. However, the dataset is small and created for analytical practice, so the correlation should not be interpreted as proof of causation or generalized to a larger student population.
