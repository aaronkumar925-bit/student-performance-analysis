# Student Performance Analytics

## Project Overview

This project analyzes student academic performance using Python, Pandas, and Matplotlib.

The analysis focuses on student marks, attendance, subject-wise performance, performance categories, and the relationship between attendance and academic results.

The project also demonstrates a basic data-cleaning workflow by identifying duplicate records and handling missing values.

## Objectives

- Analyze student academic performance
- Calculate average marks for each student
- Compare subject-wise performance
- Identify high and low-performing students
- Identify students who may require additional academic support
- Analyze the relationship between attendance and academic performance
- Detect and handle missing data
- Detect and remove duplicate records
- Create visualizations to communicate findings

## Technologies Used

- Python
- Pandas
- Matplotlib
- Git
- GitHub

## Dataset

The dataset contains information about 10 students, including:

- Student ID
- Name
- Gender
- Age
- Mathematics marks
- Science marks
- English marks
- Computer Science marks
- Attendance percentage

## Data Analysis

The project calculates and analyzes:

- Average marks for each student
- Average marks for each subject
- Highest-performing student
- Lowest-performing student
- Top 3 students
- Students requiring additional support
- Average attendance
- Correlation between attendance and average marks

## Data Cleaning

To simulate a realistic data-analysis workflow, the dataset was intentionally modified to contain data-quality issues.

The project introduced:

- A missing Science mark
- A duplicate student record

The data was then cleaned by:

1. Checking for missing values
2. Checking for duplicate records
3. Removing duplicate records
4. Filling the missing Science value using the subject mean
5. Recalculating average marks
6. Recalculating performance categories
7. Rechecking the dataset for remaining quality issues

## Performance Categories

Students were classified based on their average marks.

| Average Marks | Performance Category |
|---|---|
| 90 and above | Excellent |
| 80–89.99 | Good |
| 70–79.99 | Average |
| Below 70 | Needs Improvement |

## Visualizations

The project uses Matplotlib to visualize student performance.

The visualizations include:

- Attendance vs Academic Performance
- Subject-wise Average Marks
- Performance Category Distribution
- Student Performance Ranking

### Attendance vs Academic Performance

![Attendance vs Academic Performance](attendance%20vs%20marks.png)

The scatter plot shows the relationship between student attendance and average academic performance.

## Key Findings

- **Highest-performing student:** Ishita — average score of **96.75**
- **Lowest-performing student:** Vikram — average score of **58.50**
- **Top 3 students:** Ishita, Ananya, and Sneha
- **Highest-performing subject:** Computer Science — average score of **85.8**
- **Lowest-performing subject:** Mathematics — average score of **76.8**
- **Students identified for additional support:** Arjun and Vikram
- **Average attendance:** **83.2%**
- **Attendance vs average marks correlation:** **0.99**

The dataset shows a strong positive relationship between attendance and academic performance.

However, this dataset is small and created for analytical practice. Therefore, the correlation should **not** be interpreted as proof that attendance causes higher academic performance or generalized to a larger student population.

## Project Structure

```text
student-performance-analysis/
│
├── analysis.py
├── students.csv
├── students_cleaned.csv
├── attendance vs marks.png
└── README.md
```

## Conclusion

This project demonstrates a complete introductory data-analysis workflow using Python.

It covers:

- Data loading
- Data exploration
- Statistical analysis
- Data cleaning
- Missing-value handling
- Duplicate detection
- Performance classification
- Correlation analysis
- Data visualization
- Interpretation of analytical results

The project provides a foundation for future data-science projects involving larger datasets, exploratory data analysis, predictive analytics, and machine learning.
