import requests
import pandas as pd
import numpy as np

url_date = 'http://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia'
url_brand = 'http://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas'
url_vehicles = 'http://veiculos.fipe.org.br/api/veiculos/ConsultarModelos'
url_model = 'http://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModelo'
url_price = 'http://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'

df = pd.DataFrame()

request_date_result = requests.post(url_date)
if request_date_result.status_code == 200:
    request_date_result = request_date_result.json()
    last_month_code = request_date_result[0]['Codigo']
else:
    raise ValueError('Status_code != 200.')

# #  1 = carros 2 = motos 3 = caminhões e retorna as marcas

vehicle_type = 1
brand_names = []
brand_code = []
brand_list = {}

brand_body_request = {f'codigoTabelaReferencia': {last_month_code}, 'codigoTipoVeiculo': {vehicle_type}}

request_brand_result = requests.post(url_brand, data=brand_body_request)
request_brand_result = request_brand_result.json()
brand_names = [r['Label'] for r in request_brand_result]
brand_code = [r['Value'] for r in request_brand_result]
brand_list = dict(zip(brand_names, brand_code))

cars_by_brand = {}

for brand_code_value in brand_code:
    vehicle_code = []

    vehicle_body_request = {f"codigoTabelaReferencia": {last_month_code},
                            "codigoTipoVeiculo": {vehicle_type},
                            "codigoMarca": {brand_code_value}
                            }

    request_vehicle_result = requests.post(url_vehicles, data=vehicle_body_request)
    request_vehicle_result = request_vehicle_result.json()['Modelos']
    cars_by_brand[f'{brand_code_value}'] = [r['Value'] for r in request_vehicle_result]

cars_infos = []
list_aux_2 = []

for brand in cars_by_brand.keys():
    for vehicle in cars_by_brand[brand]:
        list_aux = []
        model_body_request = {
                              f"codigoTabelaReferencia": {last_month_code},
                              "codigoTipoVeiculo": {vehicle_type},
                              "codigoMarca": {brand},
                              "codigoModelo": {vehicle}
                            }

        model_vehicle_result = requests.post(url_model, data=model_body_request)
        model_vehicle_result = model_vehicle_result.json()

        for values in model_vehicle_result:
            list_aux_2.append(values['Value'].split('-')[0])
            list_aux_2.append(values['Value'].split('-')[1])

        list_aux.append(last_month_code)
        list_aux.append(vehicle_type)
        list_aux.append(brand)
        list_aux.append(values['Value'])
        list_aux.append(values['Value'].split('-')[1])
        list_aux.append(values['Value'].split('-')[0])
        list_aux.append(vehicle)
        list_aux.append('tradicional')
        cars_infos.append(list_aux)

for index in range(len(cars_infos)):
    price_body_request = {
                          f"codigoTabelaReferencia": {cars_infos[index][0]},
                          "codigoTipoVeiculo": {cars_infos[index][1]},
                          "codigoMarca": {int(cars_infos[index][2])},
                          "ano": cars_infos[index][3],
                          "codigoTipoCombustivel": cars_infos[index][4],
                          "anoModelo": int(cars_infos[index][5]),
                          "codigoModelo": cars_infos[index][6],
                          "tipoConsulta": cars_infos[index][7]
                        }

    price_vehicle_result = requests.post(url_price, data=price_body_request)
    price_vehicle_result = price_vehicle_result.json()

    if index == 0:
        df = pd.DataFrame(columns=price_vehicle_result.keys())

    df = df.append(price_vehicle_result, ignore_index=True)
print(df)
