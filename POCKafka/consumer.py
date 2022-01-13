from kafka import KafkaConsumer
import transforms.base as bt
from transforms.flat import flatten_records as flattening
from transforms.date import format_date_records as format_date
from transforms.number import format_number_records as format_number
from datetime import datetime
import ast
import json

TOPIC_NAME = 'meu-topico'

consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset='earliest', # where to start reading the messages at
    group_id='event-collector-group-1', # consumer group id
    bootstrap_servers=['3.95.64.58:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) # we deserialize our data from json
)

def consume_events():
    for records in consumer:
        records = bt.RecordBatch([records.value])
        save_dynamo = []
        try:
            save_dynamo = (
                records.apply(flattening).apply(format_date).apply(format_number)
            )

        except Exception as err:
            print(err)

        print(save_dynamo)
        # dict_records = ast.literal_eval(str(save_dynamo))
        # output_payload = json.dumps(dict_records, compress=True)
        # original_payload = json.dumps(list(consumer), to_encode=True, compress=True)

        # new_item = {
        #     "original_payload": original_payload,
        #     "output_payload": output_payload,
        #     "stage": "trusted",
        #     "modified_at": str(datetime.now()),
        # }

        #print(new_item)


if __name__ == '__main__':
    print("RODANDDOOOOO")
    consume_events()