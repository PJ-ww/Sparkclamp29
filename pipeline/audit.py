import pandas as pd
from pathlib import Path
from datetime import datetime
import os


def write_audit(
    run_id,
    business_date,
    status,
    source_count,
    loaded_count,
    rejected_count,
    error_message=""
):

    audit_folder = "data/audit"
    audit_file = f"{audit_folder}/batch_audit.csv"

    Path(audit_folder).mkdir(
        parents=True,
        exist_ok=True
    )

    end_time = datetime.now()

    audit_data = {

        "run_id": run_id,

        "business_date": business_date,

        "start_time": end_time,

        "end_time": end_time,

        "status": status,

        "source_count": source_count,

        "loaded_count": loaded_count,

        "rejected_count": rejected_count,

        "error_message": error_message

    }

    df = pd.DataFrame([audit_data])

    if os.path.exists(audit_file):

        old = pd.read_csv(audit_file)

        df = pd.concat(
            [old, df],
            ignore_index=True
        )

    df.to_csv(
        audit_file,
        index=False
    )

    print("Audit Saved")
