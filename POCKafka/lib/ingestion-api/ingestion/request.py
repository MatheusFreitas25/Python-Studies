import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def request_post(payload, token_id, url):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(token_id),
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except requests.exceptions.HTTPError as errh:
        logger.error("Http Error:", errh)
    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        logger.error("Error: Something Else", err)
