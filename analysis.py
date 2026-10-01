
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student_performance.csv")

# Basic EDA
print("First Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# Detailed Analysis
print("\nAverage Study Hours:")
print(df["Study_Hours"].mean())

print("\nAverage Attendance:")
print(df["Attendance_Percentage"].mean())

print("\nAverage Exam Score:")
print(df["Exam_Score"].mean())

# Correlation Analysis
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True).round(2))

# Top 5 Students
print("\nTop 5 Students:")
print(df.nlargest(5, "Exam_Score"))

# ---------------------------------
# TASK 3: DATA VISUALIZATION
# ---------------------------------

# Chart 1: Study Hours vs Exam Score
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Exam_Score"])
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.tight_layout()
plt.savefig("study_hours_vs_exam_score.png", dpi=300)
plt.show()
plt.close()

# Chart 2: Attendance vs Exam Score
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Attendance_Percentage"],
    df["Exam_Score"]
)
plt.title("Attendance vs Exam Score")
plt.xlabel("Attendance Percentage")
plt.ylabel("Exam Score")
plt.grid(True)
plt.tight_layout()
plt.savefig("attendance_vs_exam_score.png", dpi=300)
plt.show()
plt.close()

# Chart 3: Exam Score Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Exam_Score"], bins=5, edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("exam_score_distribution.png", dpi=300)
plt.show()
plt.close()

# Chart 4: Performance Level
df["Performance_Level"] = pd.cut(
    df["Exam_Score"],
    bins=[0, 49, 74, 100],
    labels=[
        "Needs Improvement",
        "Average",
        "Excellent"
    ]
)

average_scores = df.groupby(
    "Performance_Level",
    observed=False
)["Exam_Score"].mean()

plt.figure(figsize=(8, 5))
average_scores.plot(kind="bar")
plt.title("Average Exam Score by Performance Level")
plt.xlabel("Performance Level")
plt.ylabel("Average Exam Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("performance_level.png", dpi=300)
plt.show()
plt.close()

print("\nAll charts saved successfully!")