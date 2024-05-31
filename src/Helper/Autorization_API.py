
from src.Utility.requestUtility import Request_API


class Autorization_API:
    def __init__(self):
        self.API_call = Request_API()

    def sign_in_existing_user(self, expected_status_code=None):
        endpoint = "/sign-in"
        payload = dict()
        payload['email'] = "testuser_erqh@gmail.com"
        payload['password'] = "Password1"
        result = self.API_call.POST_request(endpoint=endpoint, payload=payload, expected_status_code=expected_status_code)
        return result


