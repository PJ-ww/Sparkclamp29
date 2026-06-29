import pandas as pd
from pathlib import Path


def transform_data():

    # อ่านข้อมูลจาก Raw Layer
    df = pd.read_csv("data/raw/raw_workshop_data.csv")

    # ==========================
    # Trim ช่องว่างของข้อความ
    # ==========================
    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    # ==========================
    # แปลง GPA
    # ==========================
    df["gpa"] = pd.to_numeric(
        df["gpa"],
        errors="coerce"
    )

    # ==========================
    # แปลง Credit
    # ==========================
    df["credit_earned"] = pd.to_numeric(
        df["credit_earned"],
        errors="coerce"
    )

    # ==========================
    # แปลง Salary
    # ==========================
    df["expected_salary_thb"] = pd.to_numeric(
        df["expected_salary_thb"],
        errors="coerce"
    )

    # ==========================
    # แปลง Year
    # ==========================
    df["year_of_study"] = pd.to_numeric(
        df["year_of_study"],
        errors="coerce"
    )

    # ==========================
    # แปลงวันที่
    # ==========================
    df["snapshot_date"] = pd.to_datetime(
        df["snapshot_date"],
        errors="coerce"
    )

    df["batch_date"] = pd.to_datetime(
        df["batch_date"],
        errors="coerce"
    )

    # ==========================
    # แปลง True / False
    # ==========================
    df["is_international"] = (
        df["is_international"]
        .astype(str)
        .str.upper()
        .map({
            "TRUE": True,
            "FALSE": False
        })
    )

    # ==========================
    # สร้างโฟลเดอร์
    # ==========================
    Path("data/staging").mkdir(
        parents=True,
        exist_ok=True
    )

    # ==========================
    # บันทึก Staging Layer
    # ==========================
    df.to_csv(
        "data/staging/stg_student_snapshot.csv",
        index=False
    )

    print("Transform Complete")


if __name__ == "__main__":
    transform_data()