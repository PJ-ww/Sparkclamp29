import pandas as pd

# อ่าน Excel
df = pd.read_excel("data/thammasat_workshop_dataset.xlsx")

print(df.head())
print(df.info())

# Export Raw
df.to_csv("output/raw_workshop_data.csv", index=False)

print("Raw layer created")