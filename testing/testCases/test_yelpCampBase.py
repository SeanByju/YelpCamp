import pytest

@pytest.mark.usefixtures("init_driver")
class yelpCampBaseTest:
    
    USERNAME = "test"
    PASSWORD = "test"