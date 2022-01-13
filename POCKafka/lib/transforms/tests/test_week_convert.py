from lib.transforms.transforms.week import format_week_days_records
import datetime


def test_format_weekly_days(self):
    d = datetime.date(2021, 8, 8)
    input_data = [
        {"data": d},
    ]
    output_data = [
        {"data": 0},
    ]
    fields_to_transform = ["data"]
    self.assertEqual(
        format_week_days_records(input_data, fields_to_transform),
        output_data,
    )
