from src.Helper.Autorization_API import Autorization_API

import pytest

class BaseTest:
    API_CALL: Autorization_API

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.API_CALL = Autorization_API()
