import pytest

""" Fixture for initiate driver"""
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

""" Or from chrome setup fixture"""
@pytest.mark.usefixtures("setup")
class BaseTest:
    pass
