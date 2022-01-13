import unittest
from transforms.base import RecordBatch as RecordBatch
import transforms.flat as flattening


def input_data():
    return {
        "field1": "value1",
        "field2": "value2",
        "field5.[0].value.[0].example": "value5",
        "field5.[0].value.[1].example": "value6",
        "field5.[1].value.[0].example": "value8",
        "field5.[1].value.[1].example": "value9",
        "field6.[0].value.[0].example1.[0].value.[0].value": "value15",
        "field6.[0].value.[0].example1.[0].value.[1].value": "value12",
        "metadata.schema-name": "test-schema",
        "metadata.table-name": "root",
        "metadata.timestamp": "2020-04-29T22:39:14.243966Z",
    }


class TestFlattening(unittest.TestCase):
    def test_ignore_records(self):
        ingested_at = "2020-06-16T23:07:33.243966Z"
        payload = [
            {
                "data": {
                    "field1": "value1",
                    "field2": {"field11": "value3", "field12": "value"},
                },
                "metadata": {
                    "schema-name": "schema",
                    "table-name": "table",
                    "timestamp": ingested_at,
                },
            },
            {
                "data": {"field3": [{"field31": 123}, {"field31": 456}]},
                "metadata": {
                    "schema-name": "schema",
                    "table-name": "table2",
                    "timestamp": ingested_at,
                },
            },
        ]
        response = flattening.flatten_records(payload, ["field2"])

        self.assertEqual(
            response[0]["field2"],
            payload[0]["data"]["field2"],
        )

    def test_flatten_records(self):
        ingested_at = "2020-06-16T23:07:33.243966Z"
        payload = [
            {
                "data": {
                    "field1": "value1",
                    "field2": {"field11": "value3", "field12": "value"},
                },
                "metadata": {
                    "schema-name": "schema",
                    "table-name": "table",
                    "timestamp": ingested_at,
                },
            },
            {
                "data": {"field3": [{"field31": 123}, {"field31": 456}]},
                "metadata": {
                    "schema-name": "schema",
                    "table-name": "table2",
                    "timestamp": ingested_at,
                },
            },
        ]
        response = flattening.flatten_records(payload, [])
        self.assertEqual(response[1]["metadata.table-name"], "table2.field3")
