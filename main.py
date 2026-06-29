from pipeline.ingest import ingest_excel
from pipeline.validate import validate_data
from pipeline.transform import transform_data
from pipeline.publish import publish_data
from pipeline.audit import write_audit

run_id = "RUN001"
business_date = "2026-06-29"

try:

    source_count = ingest_excel(
        input_file="data/input/thammasat_workshop_dataset.xlsx",
        business_date=business_date,
        run_id=run_id
    )

    rejected = validate_data()

    transform_data()

    loaded = publish_data()

    write_audit(
        run_id=run_id,
        business_date=business_date,
        status="SUCCESS",
        source_count=source_count,
        loaded_count=loaded,
        rejected_count=rejected
    )

except Exception as e:

    write_audit(
        run_id=run_id,
        business_date=business_date,
        status="FAILED",
        source_count=0,
        loaded_count=0,
        rejected_count=0,
        error_message=str(e)
    )