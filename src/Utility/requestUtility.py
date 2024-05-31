import json
import logging

import requests

class Request_API(object):
    def __init__(self):
        self.baseUrl = "http://ask-stage.portnov.com/api/v1"


    def POST_request(self, endpoint, payload, header=None):
        if not header:
            header = {"Content-Type": "application/json"}
        url = self.baseUrl + endpoint
        result = requests.post(url=url, data=json.dumps(payload), headers=header)

        # import pdb; pdb.set_trace()

        return result.json()



