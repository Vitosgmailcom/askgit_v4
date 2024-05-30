
from src.Utility.request import Request_API


class Autorization_API:
    def __init__(self):
        self.API_call = Request_API()

    def sign_in(self):
        return self.API_call.POST_request()
