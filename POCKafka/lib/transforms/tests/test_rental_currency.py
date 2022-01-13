import unittest
import transforms.rental_currency as format_currency
import json, base64


class TestFormatNumber(unittest.TestCase):
    def test_parse_currency(self):
        input_data = "2020"
        self.assertEqual(
            format_currency.parse_currency(input_data), input_data
        )

        input_data = 2020
        self.assertEqual(format_currency.parse_currency(input_data), 20.20)

    def test_parse_record(self):
        input_data = {
            "Records": [{"amount_reference": 2020, "name": "test"}],
        }

        self.assertEqual(
            format_currency.parse_record(input_data, []), input_data
        )

    def test_format_currency_records(self):
        input_data = [
            {
                "amount_reference": 2020,
                "amount": 1222,
                "discount": 3300,
                "name": "test",
            }
        ]
        output_data = [
            {
                "amount_reference": 20.2,
                "amount": 12.22,
                "discount": 33.0,
                "name": "test",
            }
        ]

        self.assertEqual(
            format_currency.format_currency_records(
                input_data, "amount,amount_reference,discount".split(",")
            ),
            output_data,
        )
