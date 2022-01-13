from typing import Any, Dict, Iterable
import datetime


def convert_string_date_times(value):
    day_of_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    dict_days = dict(zip(day_of_week, range(len(day_of_week))))

    return dict_days[value]


def convert_timestamp_date_times(value):
    return 0 if value.isoweekday() == 7 else value.isoweekday()


def fix_field(value):
    if isinstance(value, datetime.date):
        return convert_timestamp_date_times(value)
    else:
        return convert_string_date_times(value)


def parse_record(record: dict, fields: list):
    return {
        key: fix_field(value) if key in fields else value
        for key, value in record.items()
    }


def format_week_days_records(
    records: Iterable[Dict[str, Any]], fields_weekly_to_transforms
) -> Iterable[Dict[str, Any]]:
    return [
        parse_record(record, fields_weekly_to_transforms) for record in records
    ]
