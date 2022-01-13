import datetime
import boto3
import json
import os
from typing import Any, Dict


s3 = boto3.client("s3")
kinesis = boto3.client("kinesis")


def get_output_payload(data_dict, metadata, table_name, schema_name):
    data = {"data": data_dict, "metadata": metadata}
    return [
        {
            "Data": bytes(json.dumps(data), "utf-8"),
            "PartitionKey": schema_name + table_name,
        }
    ]


def get_metadata(table, schema):
    return {
        "timestamp": f"{datetime.datetime.now():%Y-%m-%dT%H:%M:%S.%fZ}",
        "record-type": "data",
        "operation": "update",
        "partition-key-type": "schema-table",
        "schema-name": schema,
        "table-name": table,
        "transaction-id": "",
    }


def format_response_payload(record, table_name, schema_name):
    metadata_dict = get_metadata(table_name, schema_name)

    if "updated_at" in record.keys():
        metadata_dict["timestamp"] = record["updated_at"]
    if "metadata.operation" in record.keys():
        metadata_dict["operation"] = record["metadata.operation"]
        record.pop("metadata.operation")

    return get_output_payload(record, metadata_dict, table_name, schema_name)


def send_stream_to_kinesis(records):
    kinesis.put_records(
        StreamName=os.environ["KINESIS_INGESTION_API"],
        Records=records,
    )


def send_to_kinesis_s3(message: Dict[str, Any]) -> None:
    source = message["source"]
    rows = (
        message["row_process"]
        if "data" not in message["row_process"].keys()
        else message["row_process"]["data"]
    )

    result = format_response_payload(
        rows,
        message["end_point"],
        source,
    )

    send_stream_to_kinesis(result)
