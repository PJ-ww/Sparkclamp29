python
import pandas as pd
from pathlib import Path


def create_analytics():

    trusted_file = "data/trusted/trusted_student_snapshot.csv"

    df = pd.read_csv(trusted_file)

    Path("data/analytics").mkdir(
        parents=True,
        exist_ok=True
    )

    summary = []

    # ==========================
    # Total Student
    # ==========================

    summary.append({
        "Metric": "Total Student",
        "Value": len(df)
    })

    # ==========================
    # Average GPA
    # ==========================

    summary.append({
        "Metric": "Average GPA",
        "Value": round(df["gpa"].mean(), 2)
    })

    # ==========================
    # Average Salary
    # ==========================

    summary.append({
        "Metric": "Average Expected Salary",
        "Value": round(df["expected_salary_thb"].mean(), 2)
    })

    # ==========================
    # International Student
    # ==========================

    summary.append({
        "Metric": "International Student",
        "Value": df["is_international"].sum()
    })

    summary_df = pd.DataFrame(summary)

    summary_df.to_csv(
        "data/analytics/analytics_student_summary.csv",
        index=False
    )

    # Campus Summary

    campus = (
        df.groupby("campus")
        .size()
        .reset_index(name="student_count")
    )

    campus.to_csv(
        "data/analytics/campus_summary.csv",
        index=False
    )

    # Faculty Summary

    faculty = (
        df.groupby("faculty_or_school")
        .size()
        .reset_index(name="student_count")
    )

    faculty.to_csv(
        "data/analytics/faculty_summary.csv",
        index=False
    )

    # Career Interest

    career = (
        df.groupby("career_interest")
        .size()
        .reset_index(name="student_count")
    )

    career.to_csv(
        "data/analytics/career_interest_summary.csv",
        index=False
    )

    print("Analytics Success")


if __name__ == "__main__":

    create_analytics()
