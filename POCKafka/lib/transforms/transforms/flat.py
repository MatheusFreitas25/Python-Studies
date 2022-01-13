#
# Copyright (c) 2020 Team Analytics <analytics@kovi.us>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

import re
import json
import uuid
from itertools import groupby
from datetime import datetime
from typing import Dict, List, Any, Iterable


def fix_type(obj: Any) -> Any:
    if not isinstance(obj, str):
        return obj
    try:
        aux = json.loads(obj)
    except:
        aux = None

    return aux if isinstance(aux, list) or isinstance(aux, dict) else obj


regex_preceded_by_array = (
    r"((?<=(\[\d{1}\]))"  # preceded by 1 digit
    r"|(?<=(\[\d{2}\]))"  # or 2 digits
    r"|(?<=(\[\d{3}\]))"  # or 3 digits
    r"|(?<=(\[\d{4}\]))"  # or 4 digits
    r"|(?<=(\[\d{5}\])))"  # or 5 digits
)


def flatten_object(obj, current_result={}, root_name="$") -> Dict[str, Any]:
    obj = fix_type(obj)
    if isinstance(obj, dict):
        return flatten_dict(
            obj, current_result=current_result, root_name=root_name
        )
    if isinstance(obj, list):
        return flatten_list(
            obj, current_result=current_result, root_name=root_name
        )
    return {
        **current_result,
        **{
            re.sub(
                (
                    regex_preceded_by_array + r"\." r"(?=(\[\d+\]))"
                ),  # a dot "."
                ".value.",
                re.sub(
                    (regex_preceded_by_array + "$"),
                    ".value",
                    root_name,
                ),
            ): obj
        },
    }


def flatten_dict(dict_like: dict, current_result, root_name):
    for key in dict_like.keys():
        value = dict_like[key]
        current_result = flatten_object(
            value, current_result, f"{root_name}.{key}"
        )
    return current_result


def flatten_list(list_like: list, current_result, root_name):
    for index, value in enumerate(list_like):
        current_result = flatten_object(
            value,
            current_result=current_result,
            root_name=f"{root_name}.[{index}]",
        )
    return current_result


def format_timestamp(timestamp):
    if timestamp is None:
        return datetime.utcnow().isoformat(" ", "seconds")

    try:
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    except:
        return timestamp


def inflate_rows(
    flattened: Dict[str, Any], current_result: List[Dict[str, Any]] = []
) -> List[Dict[str, Any]]:
    def key_to_subtable(key: str) -> str:
        return re.split(
            (regex_preceded_by_array + r"\."),
            key,
            1,
        )[0]

    row = {}
    reference = str(uuid.uuid4())

    flattened["metadata.timestamp"] = format_timestamp(
        flattened.get("metadata.timestamp")
    )

    schema_name = flattened.get("metadata.schema-name", "no-name")
    root_table_name = flattened.get("metadata.table-name", "no-name")
    timestamp = flattened.get("metadata.timestamp")

    for key, subtable_rows in groupby(
        sorted(flattened.keys()), key_to_subtable
    ):
        subtable_rows = list(subtable_rows)
        if (len(subtable_rows) == 1) and key == subtable_rows[0]:
            row[key] = flattened[key]
        else:
            index = int(re.search(r"(?<=\.\[)\d+(?=\](\]|$))", key).group(0))
            row["metadata.ingestion-id"] = reference
            data = {
                f"{field}".replace(key + ".", ""): flattened[field]
                for field in subtable_rows
            }
            subtable_name = (
                root_table_name + "." + re.sub(r"\.\[\d+\]", "", key)
            )
            current_result = inflate_rows(
                {
                    **{
                        "index": index,
                        root_table_name: reference,
                        "metadata.schema-name": schema_name,
                        "metadata.table-name": subtable_name,
                        "metadata.timestamp": timestamp,
                    },
                    **data,
                },
                current_result=current_result,
            )

    current_result.append(row)

    return current_result


def add_parent_attributes(records):
    attributes = {}

    for record in records:
        if "." not in record["metadata.table-name"]:
            if "metadata.operation" in record:
                attributes["metadata.operation"] = record["metadata.operation"]

            if "metadata.ingestion-id" in record:
                attributes["metadata.parent-id"] = record[
                    "metadata.ingestion-id"
                ]

    if len(attributes) > 0:
        for record in records:
            if "." in record["metadata.table-name"]:
                if "metadata.operation" in attributes:
                    record["metadata.operation"] = attributes[
                        "metadata.operation"
                    ]
                if "metadata.parent-id" in attributes:
                    record["metadata.parent-id"] = attributes[
                        "metadata.parent-id"
                    ]

    return records


def parse_record(record, fields_to_ignore):
    filterByKey = lambda keys: {
        f"{x.lower()}": record["data"][x]
        for x in keys
        if x in record["data"].keys()
    }
    transform_records = filterByKey(
        [key for key in record["data"].keys() if key not in fields_to_ignore]
    )

    ignored_records = {
        f"$.{x}": record["data"][x]
        for x in fields_to_ignore
        if x in record["data"].keys()
    }

    result = inflate_rows(
        {
            key[2:]: value
            for (key, value) in {
                **flatten_object(transform_records),
                **ignored_records,
                **flatten_object({"metadata": record["metadata"]}),
            }.items()
        },
        [],
    )

    return add_parent_attributes(result)


def flatten_records(
    records: Iterable[Dict[str, Any]], fields_to_ignore=[]
) -> Iterable[Dict[str, Any]]:
    return sum(
        [parse_record(record, fields_to_ignore) for record in records], []
    )
