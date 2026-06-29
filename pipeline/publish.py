import pandas as pd
from pathlib import Path


def publish_data():

    staging_file = "data/staging/stg_student_snapshot.csv"
    trusted_file = "data/trusted/trusted_student_snapshot.csv"

    # อ่านข้อมูลจาก Staging
    df = pd.read_csv(staging_file)

    # สร้างโฟลเดอร์ Trusted ถ้ายังไม่มี
    Path("data/trusted").mkdir(
        parents=True,
        exist_ok=True
    )

    # ==========================
    # Remove Duplicate
    # ==========================
    df = df.drop_duplicates(
        subset=[
            "entity_id",
            "snapshot_date"
        ],
        keep="last"
    )

    # ==========================
    # Sort Data
    # ==========================
    df = df.sort_values(
        by=[
            "entity_id",
            "snapshot_date"
        ]
    )

    # ==========================
    # Publish Trusted Layer
    # ==========================
    df.to_csv(
        trusted_file,
        index=False
    )

    print("Publish Success")
    print(f"Trusted Records : {len(df)}")

    return len(df)


if __name__ == "__main__":
    publish_data()