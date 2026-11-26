# 🎓 Student Performance Analysis Dashboard

## 📌 Project Overview
This project explores how student habits relate to exam performance. It uses Python and SQL to prepare the data, Seaborn and Matplotlib to visualize it, and Power BI to build an interactive dashboard.

## 📂 Dataset
* **File:** `StudentPerformanceFactors.csv`
* **Size:** 6,607 student records and 20 columns
* **Columns analyzed:** `Hours_Studied`, `Sleep_Hours`, `Physical_Activity`, `Exam_Score`

## 🛠️ Tech Stack
* **Python:** Pandas, Matplotlib, Seaborn
* **SQL:** SQLite (in-memory database)
* **Power BI:** Interactive dashboard

## ⚙️ Workflow
1. Load the CSV file with Pandas.
2. Store it in an in-memory SQLite table.
3. Select the required columns with a SQL query.
4. Plot study hours, sleep hours and physical activity against exam score.
5. Export `Cleaned_Student_Data_for_PowerBI.csv` for the Power BI dashboard.

## 📊 Dashboard Preview
![Power BI Dashboard](./interactive%20dashboard.png)

The dashboard includes a scatter plot of study hours and exam score, an average exam score card, and filters for study hours and sleep hours.

## 🔍 Key Findings
| Factor | Correlation with exam score |
|---|---|
| Hours studied | 0.45 (moderate positive) |
| Physical activity | 0.03 (almost none) |
| Sleep hours | -0.02 (almost none) |

* The average exam score is **67.24**.
* Correlation shows a relationship, not proof of cause.

## 🚀 How to Run
```bash
git clone https://github.com/MSanjeevkrishna/-Student-Performance-Analysis-Dashboard.git student-performance
cd student-performance
pip install pandas matplotlib seaborn
python analysis.py
```
