import logging
from typing import Any, Dict, Iterable
import re
import datetime
import dateutil.parser as dtparse

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def remove_null_values(input_dict):
    for key, value in list(input_dict.items()):
        if input_dict[key] is None or input_dict[key] == "":
            input_dict.pop(key)
        elif (
            key == "wg_country_code"
            or key == "wl_time_attended"
            or key == "wl_attended_date"
            or key == "wu_call_cost"
            or key == "metadata.TaskAttributes.integrationZendesk"
            or key == "referral"
            or key == "issue_state"
            or key == "checklist.whip_lot_url"
            or key
            == "info.last_close_booking_checklist.info.last_preventive_km.odometer"
            or key == "info.last_preventive_km.odometer"
            or key == "checklist.traveled_km_since_last_preventive.data"
            or "metadata.TaskAttributes" in key
            or "attributes." in key.lower()
            or key == "title"
            or key == "result"
            or key == "fiscal_number"
            or key == "end"
            or key == "solicitation.respostaaceita.parceiro.cnh"
            or key == "solicitation.atendimento.veiculo.modelo"
        ):
            input_dict[key] = str(input_dict[key])

    return input_dict


def rental_date(record, key):
    return (
        True
        if record["metadata.schema-name"] == "rental"
        and (key[-3:] == "_at" or "_limit" == key[-6:])
        else False
    )


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
        "value",  # field on pipefy
        "ws_ticket_id",
        "text",
        "payload.Body",
        "payload.CurrentInput",
        "metadata.TaskAttributes.integrationZendesk",
        "license_number",
        "new_value",  # field on pipefy
        "referral",
        "Authorisation_Code",
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


def validate_year(arg):
    return arg.year > 1900 and arg.year < 2100


def reboqueme_date(record, key, arg):
    return (
        safe_parse_time_reboqueme(arg)
        if record["metadata.schema-name"] == "reboqueme"
        else arg
    )


def safe_parse_time_reboqueme(arg):

    if (not isinstance(arg, str)) or len(arg) <= 8:
        return arg

    try:
        return dtparse.parse(arg, dayfirst=True).isoformat()
    except:
        return arg


def safe_parse_time(arg, must_be_date):
    if (not must_be_date) and ((not isinstance(arg, str)) or len(arg) <= 8):
        return arg

    try:
        if "Date(" in arg:
            arg = re.search("\((.+?)\)", arg).group(1)
            date_formatted = datetime.datetime.fromtimestamp(
                int(arg) / 1000
            )  # using the local timezone
        else:
            date_formatted = dtparse.parse(str(arg))
        if validate_year(date_formatted):
            return date_formatted.isoformat()
        else:
            return None if must_be_date else arg
    except:
        return None if must_be_date else arg


def parse_datetimes(record: dict):
    record_fixed_date = {}
    for key, value in record.items():
        must_be_date = rental_date(record, key)

        value = reboqueme_date(record, key, value)

        record_fixed_date[key] = (
            safe_parse_time(value, must_be_date)
            if not string_column(record, key)
            and "metadata.taskattributes" not in key.lower()
            else value
        )

    return remove_null_values(record_fixed_date)


def format_date_records(
    records: Iterable[Dict[str, Any]]
) -> Iterable[Dict[str, Any]]:
    return [parse_datetimes(record) for record in records]
