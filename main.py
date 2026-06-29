from pipeline.ingest import ingest_excel

ingest_excel(
    input_file="data/input/thammasat_workshop_dataset.xlsx",
    business_date="2026-06-29",
    run_id="RUN001"
)