import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# 1. Setup SQL Database in memory
conn = sqlite3.connect(':memory:') # Creates a temporary database
df_raw = pd.read_csv("StudentPerformanceFactors.csv")

# 2. Push the CSV data into a SQL Table
df_raw.to_sql('students', conn, index=False, if_exists='replace')

# 3. Use SQL to "Query" the data back into Python
query = """SELECT Hours_Studied, Attendance, Sleep_Hours, Physical_Activity, Exam_Score
FROM students WHERE Exam_Score <= 100"""
df = pd.read_sql_query(query, conn)

# 3. Create the Student Habits Dashboard
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Impact of Student Habits on Academic Performance', fontsize=16)

# Plot 1: Study Hours
sns.scatterplot(ax=axes[0], data=df, x='Hours_Studied', y='Exam_Score', alpha=0.3, color='blue')
axes[0].set_title('Study Hours vs. Score')

# Plot 2: Sleep Hours
sleep_avg = df.groupby('Sleep_Hours')['Exam_Score'].mean().reset_index()
sns.lineplot(ax=axes[1], data=sleep_avg, x='Sleep_Hours', y='Exam_Score', marker='o', color='purple')
axes[1].set_title('Sleep Hours vs. Average Score')

# Plot 3: Physical Activity
sns.barplot(ax=axes[2], data=df, x='Physical_Activity', y='Exam_Score', palette='magma')
axes[2].set_title('Physical Activity vs. Average Score')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
print(df.corr()['Exam_Score'].round(2))

# 4. Export for Power BI
df.to_csv("Cleaned_Student_Data_for_PowerBI.csv", index=False)
print("File exported! Now open this in Power BI to create your interactive dashboard.")