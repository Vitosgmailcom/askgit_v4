import json
import logging

import allure
import requests

class Request_API(object):
    def __init__(self):
        self.baseUrl = "http://ask-stage.portnov.com/api/v1"


    def POST_request(self, endpoint, payload, header=None, expected_status_code=200, **kwargs):
        if not header:
            header = {"Content-Type": "application/json"}
        url = self.baseUrl + endpoint
        result = requests.post(url=url, data=json.dumps(payload), headers=header)
        status_code = result.status_code
        with allure.step(f"Status code: {status_code}"):
            assert status_code == int(expected_status_code), (f"Expected status code: {expected_status_code}, "
                                                          f"but API returned {status_code}")
        # import pdb; pdb.set_trace()

        return result.json()



