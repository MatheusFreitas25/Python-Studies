import base64
import json
import os
import datetime
from datetime import timedelta

try:
    import dynamodb_connect
except:
    import utils.lambda_layers.dynamodb_connect.src.python.dynamodb_connect as dynamodb_connect

table = dynamodb_connect.DynamoConnect(os.environ["DYNAMODB_CONTROL"])


def decode_message(message):
    try:
        decoded_message = json.loads(base64.b64decode(message["body"]))
    except Exception:
        if isinstance(message["body"], str):
            decoded_message = json.loads(
                message["body"]
                .replace('"S ', '\\"S ')
                .replace('"W/', '\\"W/')
                .replace("\n", "  ")
                .replace("\r", "")
            )
        else:
            decoded_message = json.loads(message["body"])
    return decoded_message


def get_configs(end_point):
    return table.scan_table("end_point", f"{end_point}")["Items"][0]


def update_datetime(dt_start, dt_end, row):
    row["start_date"] = (
        dt_start if dt_start is not None else row.get("end_date", None)
    )
    row["end_date"] = (
        dt_end
        if dt_end is not None
        else (datetime.datetime.now() - timedelta(hours=3)).strftime(
            row["date_format"]
        )
    )

    table.put_item(Item=row)
