import json
import logging

import requests

class Request_API(object):
    def __init__(self):
        self.baseUrl = "http://ask-stage.portnov.com/api/v1"
        # self.payload = {
        #     "email": "testuser_erqh@gmail.com",
        #     "password": "Password1"
        #     }
        self.endpoint = "/sign-in"
        self.url = self.baseUrl + self.endpoint

    def POST_request(self, endpoint=None, payload=None, header=None):
        if not header:
            header = {"Content-Type": "application/json"}
        payload = dict()
        payload['email'] = "testuser_erqh@gmail.com"
        payload['password'] = "Password1"
        response = requests.post(url=self.baseUrl, data=json.dumps(payload), headers=header)
        logging.debug(response)
        logging.info(self.url)
        logging.info(payload)
        import pdb; pdb.set_trace()


        return response.json()


