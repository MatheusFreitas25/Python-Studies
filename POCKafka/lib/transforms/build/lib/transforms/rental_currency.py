import logging
from typing import Any, Dict, Iterable

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def parse_currency(arg):
    return arg / 100 if isinstance(arg, float) or isinstance(arg, int) else arg


def parse_record(record: dict, fields):
    return {
        key: parse_currency(value) if key in fields else value
        for key, value in record.items()
    }


def format_currency_records(
    records: Iterable[Dict[str, Any]], fields
) -> Iterable[Dict[str, Any]]:
    return [parse_record(record, fields) for record in records]
