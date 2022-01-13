import unittest
from unittest.mock import patch
import transforms.base as bt
import transforms.fleet_coordinates as fleet_coordinates

import uuid
import os
import base64
import json


def get_record():
    return {
        "metadata": {
            "schema-name": "fleet_tracking",
            "table-name": "tracking",
            "timestamp": "2020-01-01 12:00:00",
        },
        "data": {
            "id_equipamento": 4634516168,
            "veiculo": 7864,
            "placa": "ABJ2C54",
            "cliente": "KOVI TECNOLOGIA LTDA ",
            "data_posicao": {"$date": "2020-08-04T12:42:07.000Z"},
            "data_chegada": {"$date": "2020-08-04T12:42:08.111Z"},
            "velocidade": 0,
            "alim_ext": 12.342,
            "bateria": 4.108,
            "coordenadas": {
                "type": "Point",
                "coordinates": [-46.6734726, -23.6393355],
            },
            "altitude": 711.87,
            "heading": 7,
            "hodometro": 20533.856,
            "gps_status": True,
            "rssi": -87,
            "eventCode": 11,
            "ignicao": False,
            "DriverId": "00000000",
            "DeltaTempoExcessoVelocidade": 0,
            "bloqueio": False,
            "vin": "9BWDG45U3LT040078",
        },
    }


class TestFleetCoordinates(unittest.TestCase):
    def test_fix_coordinates(self):
        inp = get_record()
        out = fleet_coordinates.fix_coordinates(inp)
        self.assertEqual(
            out["data"]["coordenadas"]["lat"],
            inp["data"]["coordenadas"]["coordinates"][1],
        )
        self.assertEqual(
            out["data"]["coordenadas"]["long"],
            inp["data"]["coordenadas"]["coordinates"][0],
        )

    @patch("botocore.client.BaseClient._make_api_call")
    def test_handler(self, mock_client):
        inp = get_record()
        fleet_coordinates.format_coordinates_records(inp)
