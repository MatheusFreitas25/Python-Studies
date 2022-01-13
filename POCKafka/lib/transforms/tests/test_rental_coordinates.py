import unittest
import datetime
import transforms.rental_coordinates as format_coordinates
import transforms.week as format_week_days
import json, base64


class TestFormatCoordinates(unittest.TestCase):
    def test_split_arg(self):
        self.assertEqual(
            format_coordinates.split_arg("-53.9947289,-150.91829182", ","),
            [-53.9947289, -150.91829182],
        )

    def test_validate_latlong(self):
        self.assertEqual(format_coordinates.validate_latlong([-100, -150]), [])
        self.assertEqual(
            format_coordinates.validate_latlong([-50, -120]), [-50, -120]
        )

    def test_parse_record(self):
        input_data = [
            {
                "address_latlong": "-23.8983710, -89.9273910",
                "name": "Test lat long",
                "discount": 3300,
            },
            {
                "address_latlong": "0x0000000001010000004A65E5F27A613340867DF1FBEDC458C0",
                "address_latlong_text": "POINT(19.3807823 -99.0770254)",
            },
            {
                "address_latlong": "0x0000000001010000004A65E5F27A613340867DF1FBEDC458C0"
            },
        ]
        fields_to_transform = ["address_latlong"]
        self.assertEqual(
            format_coordinates.format_coordinates_records(
                input_data, fields_to_transform
            ),
            input_data,
        )

    def test_format_coordinates_records(self):
        input_data = [
            {
                "address_latlong": "-23.8983710, -89.9273910",
                "name": "Test lat long",
                "discount": 3300,
            },
            {
                "address_latlong": "0x0000000001010000004A65E5F27A613340867DF1FBEDC458C0",
                "address_latlong_text": "POINT(19.3807823 -99.0770254)",
            },
            {
                "address_latlong": "0x0000000001010000004A65E5F27A613340867DF1FBEDC458C0"
            },
        ]
        output_data = [
            {
                "name": "Test lat long",
                "discount": 3300,
                "latitude": -23.8983710,
                "longitude": -89.9273910,
            },
            {
                "address_latlong_text": "POINT(19.3807823 -99.0770254)",
                "latitude": 19.3807823,
                "longitude": -99.0770254,
            },
            {"latitude": 19.3807823, "longitude": -99.0770254},
        ]
        fields_to_transform = ["address_latlong"]

        self.assertEqual(
            format_coordinates.format_coordinates_records(
                input_data, fields_to_transform
            ),
            output_data,
        )
