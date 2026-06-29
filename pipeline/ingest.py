import pandas as pd

def ingest_excel(input_file, business_date, run_id):
    df = pd.read_excel(input_file)

    print(df.head())
    print(df.info())

    output_path = "output/raw_workshop_data.csv"
    df.to_csv(output_path, index=False)

    print("Raw layer created")

    return len(df)