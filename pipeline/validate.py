import pandas as pd


def validate_data():

    raw_file = "output/raw_workshop_data.csv"
    df = pd.read_csv(raw_file)

    errors = []

    rejected_count = 0

    # ==========================
    # Required Columns
    # ==========================

    required_columns = [
        "entity_id",
        "student_no",
        "snapshot_date",
        "gpa",
        "credit_earned",
        "expected_salary_thb"
    ]

    for column in required_columns:

        if column not in df.columns:

            raise Exception(f"Missing required column : {column}")

    # ==========================
    # Null Check
    # ==========================

    for column in ["entity_id", "student_no"]:

        invalid = df[column].isnull().sum()

        if invalid > 0:

            errors.append(f"{column} NULL = {invalid}")

            rejected_count += invalid

    # ==========================
    # Duplicate entity_id
    # ==========================

    duplicate_entity = df["entity_id"].duplicated().sum()

    if duplicate_entity > 0:

        errors.append(
            f"Duplicate entity_id = {duplicate_entity}"
        )

        rejected_count += duplicate_entity

    # ==========================
    # Duplicate Business Key
    # entity_id + snapshot_date
    # ==========================

    duplicate_business = df.duplicated(
        subset=[
            "entity_id",
            "snapshot_date"
        ]
    ).sum()

    if duplicate_business > 0:

        errors.append(
            f"Duplicate Business Key = {duplicate_business}"
        )

        rejected_count += duplicate_business

    # ==========================
    # GPA
    # ==========================

    df["gpa"] = pd.to_numeric(
        df["gpa"],
        errors="coerce"
    )

    invalid_gpa = df[
        (df["gpa"] < 0)
        | (df["gpa"] > 4)
        | (df["gpa"].isna())
    ]

    if len(invalid_gpa) > 0:

        errors.append(
            f"Invalid GPA = {len(invalid_gpa)}"
        )

        rejected_count += len(invalid_gpa)

    # ==========================
    # Credit
    # ==========================

    df["credit_earned"] = pd.to_numeric(
        df["credit_earned"],
        errors="coerce"
    )

    invalid_credit = df[
        (df["credit_earned"] < 0)
        | (df["credit_earned"].isna())
    ]

    if len(invalid_credit) > 0:

        errors.append(
            f"Invalid Credit = {len(invalid_credit)}"
        )

        rejected_count += len(invalid_credit)

    # ==========================
    # Salary
    # ==========================

    df["expected_salary_thb"] = pd.to_numeric(
        df["expected_salary_thb"],
        errors="coerce"
    )

    invalid_salary = df[
        (df["expected_salary_thb"] <= 0)
        | (df["expected_salary_thb"].isna())
    ]

    if len(invalid_salary) > 0:

        errors.append(
            f"Invalid Salary = {len(invalid_salary)}"
        )

        rejected_count += len(invalid_salary)

    # ==========================
    # Snapshot Date
    # ==========================

    snapshot = pd.to_datetime(
        df["snapshot_date"],
        errors="coerce"
    )

    invalid_date = snapshot.isna().sum()

    if invalid_date > 0:

        errors.append(
            f"Invalid Snapshot Date = {invalid_date}"
        )

        rejected_count += invalid_date

    # ==========================
    # Summary
    # ==========================

    print("=" * 50)
    print("DATA QUALITY REPORT")
    print("=" * 50)

    print(f"Total Records : {len(df)}")
    print(f"Rejected      : {rejected_count}")

    if len(errors) == 0:

        print("Validation Status : PASSED")

    else:

        print("Validation Status : FAILED")

        for error in errors:

            print("-", error)

    print("=" * 50)

    return rejected_count


if __name__ == "__main__":

    validate_data()
