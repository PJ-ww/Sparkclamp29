from pipeline.ingest import ingest_excel
from pipeline.validate import validate_data
from pipeline.transform import transform_data
from pipeline.publish import publish_data
from pipeline.analytics import create_analytics
from pipeline.rag_prepare import prepare_rag
from pipeline.audit import write_audit

RUN_ID = "RUN001"
BUSINESS_DATE = "2026-06-29"
INPUT_FILE = "data/input/thammasat_workshop_dataset.xlsx"

try:

    # -----------------------------
    # 1. Ingest
    # -----------------------------
    source_count = ingest_excel(
        input_file=INPUT_FILE,
        business_date=BUSINESS_DATE,
        run_id=RUN_ID
    )

    # -----------------------------
    # 2. Validate
    # -----------------------------
    rejected_count = validate_data()

    # -----------------------------
    # 3. Transform
    # -----------------------------
    transform_data()

    # -----------------------------
    # 4. Publish
    # -----------------------------
    loaded_count = publish_data()

    # -----------------------------
    # 5. Analytics
    # -----------------------------
    create_analytics()

    # -----------------------------
    # 6. Prepare RAG
    # -----------------------------
    prepare_rag()

    # -----------------------------
    # 7. Audit
    # -----------------------------
    write_audit(
        run_id=RUN_ID,
        business_date=BUSINESS_DATE,
        status="SUCCESS",
        source_count=source_count,
        loaded_count=loaded_count,
        rejected_count=rejected_count,
        error_message=""
    )

    print("\n========== PIPELINE SUCCESS ==========")

except Exception as e:

    write_audit(
        run_id=RUN_ID,
        business_date=BUSINESS_DATE,
        status="FAILED",
        source_count=0,
        loaded_count=0,
        rejected_count=0,
        error_message=str(e)
    )

    print("\n========== PIPELINE FAILED ==========")
    print(e)