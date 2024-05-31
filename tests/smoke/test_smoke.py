from tests.base_test import BaseTest

import pytest
import allure

@pytest.mark.smoke
class Test_smoke(BaseTest):

    @pytest.mark.smoke_sign_in
    @allure.title('Autorization API smoke test')
    def test_smoke(self):
        result = Test_smoke.API_CALL.sign_in_existing_user()
        # import pdb; pdb.set_trace()
        assert result['user']['active'] == True, f"Expected result is 'True' but API returned '{result['user']['active']}'"



