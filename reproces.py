import pandas as pd
import gzip
import json
import datetime
import numpy as np
import boto3

rental_file = pd.read_csv(f"/Users/cliente/Desktop/rental10.csv")
dw_file = pd.read_csv(f"/Users/cliente/Desktop/dw10.csv")
df_new = pd.DataFrame(columns=rental_file.columns)
df_final = pd.DataFrame()
list_rental = []
list_dw = []
content = []

for values in rental_file['issue_id']:
    list_rental.append(values)

for dw_value in dw_file['issue_id']:
    list_dw.append(dw_value)

for count_dw, value_dw in enumerate(list_dw):
    for count_rental, value_rental in enumerate(list_rental):
        if value_rental == value_dw:
            list_rental.pop(count_rental)

for id in list_rental:
    df_data = df_new.append(rental_file[rental_file['issue_id'] == id])
    df_data = df_data.reset_index()
    data = df_data['updated_at'][0]
    print(type(data))
    df_metadata = pd.DataFrame({"timestamp": [data],
                                "record-type": ["data"],
                                "operation": ["load"],
                                "partition-key-type": ["schema-table"],
                                "schema-name": ["""rental"""],
                                "table-name": ["Fines"],
                                "transaction-id": [""]})

    df_data = df_data.fillna('')
    df_data =df_data.drop(columns='index')
    df_final = df_final.append(pd.DataFrame({'data': df_data.to_dict('records'), 'metadata': df_metadata.to_dict('records')}))


df_final = df_final.to_dict('records')

kinesis = boto3.client("kinesis")

def record_to_kinesis_request(record: dict) -> dict:
    return [{
        "Data": json.dumps(record),
        "PartitionKey": str(abs(hash(json.dumps(record)))),
    }]

for record in df_final:
    kinesis.put_records(Records=record_to_kinesis_request(record), StreamName="cdc_stream")
