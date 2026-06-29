import pandas as pd

df = pd.read_csv("output/raw_workshop_data.csv")

# ลบช่องว่างชื่อคอลัมน์
df.columns = df.columns.str.strip().str.lower()

# ลบข้อมูลซ้ำ
df = df.drop_duplicates()

# แทนค่า Missing
df = df.fillna("")

df.to_csv("output/trusted_student_snapshot.csv", index=False)

print("Trusted layer created")