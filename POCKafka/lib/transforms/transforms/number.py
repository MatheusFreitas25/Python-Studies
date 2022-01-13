import logging
from typing import Any, Dict, Iterable

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def adyen_parser_number(arg):
    try:
        arg = float(arg)
        return arg
    except Exception:
        return arg


def parse_number(arg):
    return arg * 1.0 if isinstance(arg, int) else arg


def string_column(record, key):
    columns = [
        "description",
        "address_city",
        "address_country",
        "address_neighborhood",
        "address_postal_code",
        "address_state",
        "address_street_details",
        "address_street_name",
        "address_street_number",
        "garage_address_text.city",
        "garage_address_text.neighborhood",
        "garage_address_text.postal_code",
        "garage_address_text.state",
        "garage_address_text.street_details",
        "garage_address_text.street_name",
        "garage_address_text.street_number",
        "garage_address.city",
        "garage_address.neighborhood",
        "garage_address.postal_code",
        "garage_address.state",
        "garage_address.street_details",
        "garage_address.street_name",
        "garage_address.street_number",
        "wg_country_code",
        "wl_time_attended",
        "wl_attended_date",
        "wu_call_cost",
        "valorFaturaReembolso",
        "titulos.valorFaturaReembolso",
        "valorTitulo",
        "titulos.valorTitulo",
        "ws_ticket_id",
        "text",
        "payload.Body",
        "payload.CurrentInput",
        "metadata.TaskAttributes.integrationZendesk",
        "new_value",  # field on pipefy
        "referral",
        "EmpresaID",
        "OrdemDeServicoID",
        "ProdutoID" "Authorisation_Code",
        "Modification_Reference",
        "Shopper_PAN",
        "Acquirer_Reference",
        "Shopper_Reference",
        "Shopper_Name",
        "Billing_House_Number__Name",
        "Billing_Street",
        "Billing_Postal_Code__ZIP",
        "CB_Reason_Code",
        "version",
        "internal_comments",
        "payload.Attributes.proxied",
        "issue_state",
        "checklist.whip_lot_url",
        "info.last_close_booking_checklist.info.last_preventive_km.odometer",
        "info.last_preventive_km.odometer",
        "checklist.traveled_km_since_last_preventive.data",
        "title",
        "result",
        "fiscal_number",
        "end",
        "solicitation.atendimento.veiculo.modelo",
        "solicitation.respostaaceita.parceiro.cnh",
    ]

    return True if key in columns else False


def remove_null_values(input_dict):
    for key, value in list(input_dict.items()):
        if input_dict[key] is None or input_dict[key] == "":
            input_dict.pop(key)
        elif (
            key == "wg_country_code"
            or key == "wl_time_attended"
            or key == "wl_attended_date"
            or key == "wu_call_cost"
            or key == "referral"
            or key == "Authorisation_Code"
            or key == "checklist.whip_lot_url"
            or key
            == "info.last_close_booking_checklist.info.last_preventive_km.odometer"
            or key == "info.last_preventive_km.odometer"
            or key == "checklist.traveled_km_since_last_preventive.data"
            or "metadata.TaskAttributes" in key
            or "attributes." in key.lower()
            or key == "title"
            or key == "fiscal_number"
            or key == "result"
            or key == "end"
            or key == "solicitation.respostaaceita.parceiro.cnh"
            or key == "solicitation.atendimento.veiculo.modelo"
        ):
            input_dict[key] = str(input_dict[key])

    return input_dict


def check_adyen(record):
    print(record)
    if record["metadata.schema-name"] == "adyen":
        return True


def parse_record(record: dict):
    if check_adyen(record):
        record_formatted = {
            key: adyen_parser_number(value)
            if not string_column(record, key)
            else value
            for key, value in record.items()
        }

    else:
        record_formatted = {
            key: parse_number(value)
            if not string_column(record, key)
            and "metadata.taskattributes" not in key.lower()
            else value
            for key, value in record.items()
        }

    return remove_null_values(record_formatted)


def format_number_records(
    records: Iterable[Dict[str, Any]]
) -> Iterable[Dict[str, Any]]:
    return [parse_record(record) for record in records]
