import logging
from dataclasses import dataclass
import requests

logger = logging.getLogger(__name__)


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:
    def post(self, url, payload):
        try:
            response = requests.post(url,payload)
            return self.__get_responses(response)
        except TimeoutError:
            logger.error(f'Timed out while connecting to {url}')
        except ConnectionError:
            logger.error(f'Connection Error connecting to {url}')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )
