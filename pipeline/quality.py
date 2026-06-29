import pandas as pd

df = pd.read_csv("output/trusted/trusted_student_snapshot.csv")

print("Rows :", len(df))
print("Columns :", len(df.columns))
print("Duplicate :", df.duplicated().sum())
print("Missing")

print(df.isnull().sum())
assert df["entity_id"].notna().all()
assert df["student_no"].notna().all()