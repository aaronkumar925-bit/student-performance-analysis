# Student Performance Analytics

## Project Overview

This project analyzes student academic performance using Python and Pandas. It explores marks, attendance, performance categories, and relationships between attendance and academic results.

The project also demonstrates data cleaning by identifying duplicate records and handling missing values.

## Objectives

- Analyze student academic performance
- Calculate average marks for each student
- Compare subject-wise performance
- Identify high and low-performing students
- Analyze the relationship between attendance and marks
- Clean missing and duplicate data
- Visualize important findings

## Technologies Used

- Python
- Pandas
- Matplotlib
- Git & GitHub

## Dataset

The dataset contains student information including:

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

The analysis calculates:

- Average marks for each student
- Subject-wise average marks
- Highest-performing student
- Lowest-performing student
- Top 3 students
- Students requiring additional academic support
- Average attendance
- Correlation between attendance and academic performance

## Data Cleaning

To demonstrate a realistic data-analysis workflow, the dataset was intentionally modified to contain:

- A missing Science mark
- A duplicate student record

The project then:

1. Identified missing values
2. Identified duplicate records
3. Removed duplicate records
4. Filled the missing Science mark using the subject mean
5. Recalculated student averages
6. Recalculated performance categories

## Performance Categories

Students were classified based on their average marks:

| Average Marks | Category |
|---|---|
| 90 and above | Excellent |
| 80–89.99 | Good |
| 70–79.99 | Average |
| Below 70 | Needs Improvement |

## Visualizations

The project includes visualizations for:

- Attendance vs Academic Performance
- Subject-wise Average Marks
- Performance Category Distribution
- Student Performance Ranking

### Attendance vs Academic Performance

![Attendance vs Academic Performance](attendance_vs_marks.png)

## Key Findings

- **Highest-performing student:** Ishita — average score of **96.75**
- **Lowest-performing student:** Vikram — average score of **58.50**
- **Top 3 students:** Ishita, Ananya, and Sneha
- **Highest-performing subject:** Computer Science — average of **85.8**
- **Lowest-performing subject:** Mathematics — average of **76.8**
- **Students identified for additional support:** Arjun and Vikram
- **Average attendance:** **83.2%**
- **Attendance vs. average marks correlation:** **0.99**

The analysis shows a strong positive relationship between attendance and academic performance in this dataset.

However, the dataset is small and created for analytical practice, so the correlation should **not** be interpreted as proof that attendance causes higher marks or generalized to a larger student population.

## Project Structure

```text
student-performance-analysis/
│
├── analysis.py
├── students.csv
├── students_cleaned.csv
├── attendance_vs_marks.png
└── README.md
```

## Conclusion

This project demonstrates a complete beginner-to-intermediate data analysis workflow using Python and Pandas. It covers data loading, exploratory analysis, data cleaning, statistical analysis, visualization, and interpretation of results.

The project provides a foundation for developing more advanced data science projects involving larger datasets, predictive analytics, and machine learning.
