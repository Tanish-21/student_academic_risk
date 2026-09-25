from pathlib import Path
import sqlite3

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def process_student_data():
    # Read Excel files using project-relative paths so it works from any launch folder.
    attendance = pd.read_excel(DATA_DIR / "attendance.xlsx")
    assignments = pd.read_excel(DATA_DIR / "assignments.xlsx")
    quiz = pd.read_excel(DATA_DIR / "quiz.xlsx")

    # Merge data
    merged = pd.merge(attendance, assignments, on="Roll No.", how="outer")
    merged = pd.merge(merged, quiz, on="Roll No.", how="outer")

    # Rename columns
    merged = merged.rename(columns={
        "Roll No.": "student_id",
        "Names": "student_name",
        "ATTENDENCE": "attendance",
        "ASSIGNMENT SCORE": "assignment_score",
        "MID SCORE": "mid_score",
    })

    # Normalize numeric values and handle missing entries safely.
    for column in ["attendance", "assignment_score", "mid_score"]:
        merged[column] = pd.to_numeric(merged[column], errors="coerce").fillna(0).round(2)

    merged["attendance"] = merged["attendance"].round(0).astype(int)
    merged["assignment_score"] = merged["assignment_score"].round(0).astype(int)
    merged["mid_score"] = merged["mid_score"].round(0).astype(int)

    #name null student name as unknown
    merged["student_name"] = merged["student_name"].fillna("Unknown")

    # Convert scores to percentages
    merged["assignment_percentage"] = (merged["assignment_score"] / 20) * 100
    merged["mid_percentage"] = (merged["mid_score"] / 20) * 100

    # Calculate overall score
    merged["overall_score"] = (
        merged["attendance"] * 0.30
        + merged["assignment_percentage"] * 0.30
        + merged["mid_percentage"] * 0.40
    )

    # Calculate risk level
    def calculate_risk(score):
        if score < 50:
            return "High Risk"
        elif score < 65:
            return "Medium Risk"
        else:
            return "Low Risk"

    merged["risk_level"] = merged["overall_score"].apply(calculate_risk)

    # Calculate risk reasons
    def get_risk_reason(row):
        reasons = []

        if row["attendance"] < 75:
            reasons.append("Low Attendance")

        if row["assignment_percentage"] < 50:
            reasons.append("Low Assignment Score")

        if row["mid_percentage"] < 50:
            reasons.append("Low Mid-term Score")

        if not reasons:
            return "No major risk"

        return ", ".join(reasons)

    merged["risk_reason"] = merged.apply(get_risk_reason, axis=1)

    # Save CSV and SQLite database to the project root.
    merged.to_csv(BASE_DIR / "student_risk_analysis.csv", index=False)

    connection = sqlite3.connect(BASE_DIR / "student_risk.db")
    merged.to_sql("student_risk", connection, if_exists="replace", index=False)
    connection.close()

    return merged