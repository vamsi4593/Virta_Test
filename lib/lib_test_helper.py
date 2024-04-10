import json
import logging
import random

from config import BASE_URI
from lib.api_request import APIRequest

logger = logging.getLogger(__name__)


class Helper:
    def __init__(self):
        self.base_url = BASE_URI
        self.request = APIRequest()

    def verify_version(self, station, command_value):
        bool_value = False
        data = {'command': command_value}
        response = self.request.post(f'{self.base_url}{station}', data)
        logger.info('Verifying the response status code')
        if response.status_code == 200:
            logger.info('Verifying the version')
            if response.text != "":
                rsp_data = json.loads(response.text)
                if float(rsp_data["result"]) >= 1.6:
                    bool_value = True
        return bool_value

    def verify_interval(self, station, command_value):
        bool_value = False
        data = {'command': command_value}
        response = self.request.post(f'{self.base_url}{station}', data)
        print(f'interval response is {response}')
        logger.info('Verifying the response status code')
        if response.status_code == 200:
            logger.info('Verifying the interval')
            if response.text != "":
                rsp_data = json.loads(response.text)
                if 1 <= rsp_data["result"] <= 60:
                    bool_value = True
        return bool_value

    def set_value(self, station, command_value, n_value=None):
        if n_value is None:
            n_values = [1, 2, 5, 10, 13]
            pay_load = random.choice(n_values)
        else:
            pay_load = n_value
        bool_value = False
        data = {'command': command_value, 'payload': pay_load}
        print(f'pay load is {pay_load}')
        response = self.request.post(f'{self.base_url}{station}', data)
        print(f'interval response is {response}')
        logger.info('Verifying the response status code')
        if response.status_code == 200:
            logger.info('Verifying the response result')
            if response.text != "":
                rsp_data = json.loads(response.text)
                if isinstance(pay_load,str):
                    if rsp_data["result"] == "FAILED":
                        bool_value = True
                if isinstance(pay_load,int):
                    if 1 < pay_load < 10:
                        if rsp_data["result"] == "OK":
                            bool_value = True
                    else:
                        if rsp_data["result"] == "FAILED":
                            bool_value = True
        return bool_value
