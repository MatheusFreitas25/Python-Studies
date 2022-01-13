import zlib
import os
import time
import json
import base64
from datetime import datetime
import logging
from typing import Any, Dict, Iterable

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def fix_coordinates(record: dict) -> dict:
    logger.debug(record)
    return {
        "metadata": record["metadata"],
        "data": {
            **record["data"],
            "coordenadas": {
                "lat": record["data"]["coordenadas"]["coordinates"][1],
                "long": record["data"]["coordenadas"]["coordinates"][0],
            },
        },
    }


def format_coordinates_records(records: dict):
    return [fix_coordinates(record) for record in records]
