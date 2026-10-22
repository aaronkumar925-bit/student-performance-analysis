import pandas as pd
import matplotlib.pyplot as plt

from io import StringIO

# -----------------------------
# 1. CREATE THE DATASET
# -----------------------------

csv_data = """Student_ID,Name,Gender,Age,Attendance,Math,Science,English,Computer_Science
S001,Aarav,M,19,92,88,91,85,95
S002,Diya,F,18,85,76,82,89,90
S003,Rahul,M,19,78,65,70,72,75
S004,Ananya,F,18,96,94,92,95,98
S005,Arjun,M,20,68,55,61,64,70
S006,Meera,F,19,89,84,87,91,93
S007,Karan,M,18,74,69,73,68,77
S008,Sneha,F,19,91,90,88,94,96
S009,Vikram,M,20,62,51,58,60,65
S010,Ishita,F,18,97,96,95,97,99"""

data = pd.read_csv(StringIO(csv_data))

# -----------------------------
# 2. BASIC INFORMATION
# -----------------------------

print("===== DATASET =====")
print(data)

print("\n===== DATASET SHAPE =====")
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

print("\n===== COLUMN NAMES =====")
print(data.columns.tolist())

# -----------------------------
# 3. SUBJECT ANALYSIS
# -----------------------------

subjects = ["Math", "Science", "English", "Computer_Science"]

# Calculate average marks
data["Average_Marks"] = data[subjects].mean(axis=1)

print("\n===== STUDENT AVERAGES =====")
print(data[["Student_ID", "Name", "Average_Marks"]])

# -----------------------------
# 4. SUBJECT AVERAGES
# -----------------------------

print("\n===== SUBJECT AVERAGES =====")

for subject in subjects:
    average = data[subject].mean()
    print(subject, ":", round(average, 2))

# -----------------------------
# 5. HIGHEST PERFORMER
# -----------------------------

highest_student = data.loc[data["Average_Marks"].idxmax()]

print("\n===== TOP PERFORMER =====")
print("Name:", highest_student["Name"])
print("Average:", round(highest_student["Average_Marks"], 2))

# -----------------------------
# 6. LOWEST PERFORMER
# -----------------------------

lowest_student = data.loc[data["Average_Marks"].idxmin()]

print("\n===== LOWEST PERFORMER =====")
print("Name:", lowest_student["Name"])
print("Average:", round(lowest_student["Average_Marks"], 2))

# -----------------------------
# 7. ATTENDANCE ANALYSIS
# -----------------------------

print("\n===== ATTENDANCE =====")
print("Average attendance:", round(data["Attendance"].mean(), 2))

# -----------------------------
# 8. ATTENDANCE VS MARKS
# -----------------------------

correlation = data["Attendance"].corr(data["Average_Marks"])

print("\n===== ATTENDANCE VS MARKS =====")
print("Correlation:", round(correlation, 2))



# -----------------------------
# 9. VISUALIZE ATTENDANCE VS MARKS
# -----------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    data["Attendance"],
    data["Average_Marks"]
)

plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Attendance vs Average Marks")

plt.grid(True)

plt.show()

plt.figure(figsize=(8, 5))

plt.scatter(
    data["Attendance"],
    data["Average_Marks"],
    s=80
)

plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Relationship Between Attendance and Academic Performance")

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()
plt.savefig("attendance_vs_marks.png")
# -----------------------------
# 10. SUBJECT PERFORMANCE CHART
# -----------------------------

subject_averages = data[subjects].mean()

plt.figure(figsize=(8, 5))

plt.bar(subject_averages.index, subject_averages.values)

plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Average Performance by Subject")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.show()
# -----------------------------
# 11. TOP 3 STUDENTS
# -----------------------------

top_3 = data.sort_values(
    by="Average_Marks",
    ascending=False
).head(3)

print("\n===== TOP 3 STUDENTS =====")
print(top_3[["Student_ID", "Name", "Average_Marks"]])
# -----------------------------
# 12. STUDENTS NEEDING SUPPORT
# -----------------------------

support_students = data[data["Average_Marks"] < 70]

print("\n===== STUDENTS NEEDING SUPPORT =====")
print(support_students[["Student_ID", "Name", "Average_Marks", "Attendance"]])
# -----------------------------
# 13. PERFORMANCE CATEGORIES
# -----------------------------

def performance_category(mark):
    if mark >= 90:
        return "Excellent"
    elif mark >= 80:
        return "Good"
    elif mark >= 70:
        return "Average"
    else:
        return "Needs Improvement"


data["Performance_Category"] = data["Average_Marks"].apply(
    performance_category
)

print("\n===== PERFORMANCE CATEGORIES =====")
print(data[["Name", "Average_Marks", "Performance_Category"]])
# -----------------------------
# 14. PERFORMANCE CATEGORY CHART
# -----------------------------

category_counts = data["Performance_Category"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    category_counts.index,
    category_counts.values
)

plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.title("Student Performance Categories")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.show()
# -----------------------------
# 15. INTERPRET ATTENDANCE CORRELATION
# -----------------------------

if correlation >= 0.7:
    interpretation = "Strong positive relationship"
elif correlation >= 0.4:
    interpretation = "Moderate positive relationship"
elif correlation >= 0:
    interpretation = "Weak positive relationship"
elif correlation >= -0.4:
    interpretation = "Weak negative relationship"
elif correlation >= -0.7:
    interpretation = "Moderate negative relationship"
else:
    interpretation = "Strong negative relationship"

print("\n===== CORRELATION INTERPRETATION =====")
print("Correlation:", round(correlation, 2))
print("Interpretation:", interpretation)
# -----------------------------
# 16. DATA QUALITY CHECK
# -----------------------------

print("\n===== DATA QUALITY CHECK =====")

print("Missing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())

print("\nData types:")
print(data.dtypes)
# -----------------------------
# 17. INTRODUCE DATA PROBLEMS
# -----------------------------

data.loc[2, "Science"] = None

data = pd.concat(
    [data, data.iloc[[4]]],
    ignore_index=True
)

print("\n===== AFTER INTRODUCING DATA PROBLEMS =====")

print("Missing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())
# -----------------------------
# 18. REMOVE DUPLICATES
# -----------------------------

data = data.drop_duplicates()

print("\n===== AFTER REMOVING DUPLICATES =====")
print("Duplicate rows:", data.duplicated().sum())
# -----------------------------
# 19. HANDLE MISSING VALUES
# -----------------------------

science_average = data["Science"].mean()

data["Science"] = data["Science"].fillna(science_average)

print("\n===== AFTER HANDLING MISSING VALUES =====")
print("Missing Science values:", data["Science"].isnull().sum())
print("Value used:", round(science_average, 2))
# -----------------------------
# 20. RECALCULATE AVERAGES
# -----------------------------

data["Average_Marks"] = data[subjects].mean(axis=1)

print("\n===== UPDATED STUDENT AVERAGES =====")
print(data[["Student_ID", "Name", "Average_Marks"]])
# -----------------------------
# 21. UPDATE PERFORMANCE CATEGORIES
# -----------------------------

data["Performance_Category"] = data["Average_Marks"].apply(
    performance_category
)

print("\n===== UPDATED PERFORMANCE CATEGORIES =====")
print(data[["Name", "Average_Marks", "Performance_Category"]])


# -----------------------------
# 22. UPDATE TOP 3 STUDENTS
# -----------------------------

top_3 = data.sort_values(
    by="Average_Marks",
    ascending=False
).head(3)

print("\n===== UPDATED TOP 3 STUDENTS =====")
print(top_3[["Student_ID", "Name", "Average_Marks"]])


# -----------------------------
# 23. UPDATE LOW PERFORMERS
# -----------------------------

support_students = data[data["Average_Marks"] < 70]

print("\n===== STUDENTS NEEDING SUPPORT =====")
print(
    support_students[
        ["Student_ID", "Name", "Average_Marks", "Attendance"]
    ]
)


# -----------------------------
# 24. UPDATED SUBJECT AVERAGES
# -----------------------------

subject_averages = data[subjects].mean()

print("\n===== UPDATED SUBJECT AVERAGES =====")

for subject in subjects:
    print(subject, ":", round(subject_averages[subject], 2))


# -----------------------------
# 25. UPDATED ATTENDANCE CORRELATION
# -----------------------------

correlation = data["Attendance"].corr(
    data["Average_Marks"]
)

print("\n===== UPDATED ATTENDANCE VS MARKS =====")
print("Correlation:", round(correlation, 2))


# -----------------------------
# 26. CORRELATION INTERPRETATION
# -----------------------------

if correlation >= 0.7:
    interpretation = "Strong positive relationship"
elif correlation >= 0.4:
    interpretation = "Moderate positive relationship"
elif correlation >= 0:
    interpretation = "Weak positive relationship"
elif correlation >= -0.4:
    interpretation = "Weak negative relationship"
elif correlation >= -0.7:
    interpretation = "Moderate negative relationship"
else:
    interpretation = "Strong negative relationship"

print("\n===== CORRELATION INTERPRETATION =====")
print("Correlation:", round(correlation, 2))
print("Interpretation:", interpretation)


# -----------------------------
# 27. FINAL DATA QUALITY CHECK
# -----------------------------

print("\n===== FINAL DATA QUALITY CHECK =====")

print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())


# -----------------------------
# 28. FINAL DATASET
# -----------------------------

print("\n===== FINAL CLEAN DATASET =====")
print(data)
# -----------------------------
# 29. STUDENT PERFORMANCE RANKING
# -----------------------------

ranking = data.sort_values(
    by="Average_Marks",
    ascending=True
)

plt.figure(figsize=(9, 6))

plt.barh(
    ranking["Name"],
    ranking["Average_Marks"]
)

plt.xlabel("Average Marks")
plt.ylabel("Student")
plt.title("Student Performance Ranking")

plt.grid(axis="x", alpha=0.3)

plt.tight_layout()

plt.show()
# -----------------------------
# 30. EXPORT CLEAN DATASET
# -----------------------------

data.to_csv(
    "students_cleaned.csv",
    index=False
)

print("\nClean dataset saved as students_cleaned.csv")


