import pytest
import logging as log

@pytest.mark.health
def test_healthcheck():
    log.info("Hello World")


