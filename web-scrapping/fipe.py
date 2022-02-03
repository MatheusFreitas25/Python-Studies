import requests
import pandas as pd
from datetime import date, datetime
import dateutil.parser as dtparse


url_base = 'http://veiculos.fipe.org.br/api/veiculos/'
url_date = f'{url_base}ConsultarTabelaDeReferencia'
url_brand = f'{url_base}ConsultarMarcas'
url_vehicles = f'{url_base}ConsultarModelos'
url_model = f'{url_base}ConsultarAnoModelo'
url_price = f'{url_base}ConsultarValorComTodosParametros'


def request_func(url, body_request):
    request_result = requests.post(url, data=body_request)
    return request_result.json()


request_date_result = requests.post(url_date)
if request_date_result.status_code == 200:
    request_date_result = request_date_result.json()
    last_month_code = request_date_result[0]['Codigo']
else:
    raise ValueError('Status_code != 200.')

# 1 = carros 2 = motos 3 = caminhões e retorna as marcas

vehicle_type = 1
brand_names = []
brand_list = {}

brand_body_request = {'codigoTabelaReferencia': last_month_code, 'codigoTipoVeiculo': vehicle_type}

request_brand_result = request_func(url_brand, brand_body_request)

brand_code = [r['Value'] for r in request_brand_result]

cars_by_brand = {}

for brand_code_value in brand_code:
    vehicle_code = []

    vehicle_body_request = {"codigoTabelaReferencia": last_month_code,
                            "codigoTipoVeiculo": vehicle_type,
                            "codigoMarca": brand_code_value
                            }

    request_vehicle_result = request_func(url_vehicles, vehicle_body_request)
    request_vehicle_result = request_vehicle_result['Modelos']
    cars_by_brand[brand_code_value] = [r['Value'] for r in request_vehicle_result]

cars_infos = []
df = pd.DataFrame()
index = 0

for brand in cars_by_brand.keys():
    for vehicle in cars_by_brand[brand]:
        list_aux = []
        model_body_request = {
                              "codigoTabelaReferencia": last_month_code,
                              "codigoTipoVeiculo": vehicle_type,
                              "codigoMarca": brand,
                              "codigoModelo": vehicle
                            }

        model_vehicle_result = request_func(url_model, model_body_request)
        for values in model_vehicle_result:
            car_year = values['Value']

            cars_infos = {
                          f"codigoTabelaReferencia": last_month_code,
                          "codigoTipoVeiculo": vehicle_type,
                          "codigoMarca": brand,
                          "ano": car_year,
                          "codigoTipoCombustivel": car_year.split('-')[1],
                          "anoModelo": car_year.split('-')[0],
                          "codigoModelo": vehicle,
                          "tipoConsulta": 'tradicional'
                        }

            price_vehicle_result = request_func(url_price, cars_infos)

            price_vehicle_result['Valor'] = price_vehicle_result['Valor'].replace("R$", "").strip()

            price_vehicle_result["DataConsulta"] = dtparse.parse(
                price_vehicle_result["DataConsulta"], fuzzy=True
            ).isoformat()

            print(price_vehicle_result)