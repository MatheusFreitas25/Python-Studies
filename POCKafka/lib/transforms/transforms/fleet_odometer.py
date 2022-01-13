import logging
from typing import Any, Dict, Iterable
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_odometer_flag(record: Dict[str, Any], field: str) -> Dict[str, Any]:

    odometer_threshold = float(os.environ["ODOMETER_THRESHOLD"])

    if field in record.keys() and record[field] >= odometer_threshold:
        return {**record, "flag_odometer": 1.0}
    else:
        return record


def format_odometer_flag(
    records: Iterable[Dict[str, Any]], field
) -> Iterable[Dict[str, Any]]:
    return [create_odometer_flag(record["data"], field) for record in records]
