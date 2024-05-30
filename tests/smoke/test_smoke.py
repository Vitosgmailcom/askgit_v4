from src.Helper.Autorization_API import Autorization_API

import pytest

@pytest.mark.smoke
def test_smoke():
    result = Autorization_API()
    result = result.sign_in()

    # import pdb; pdb.set_trace()



