import pytest


from Pages.yelpCampBasePage import yelpCampBasePage


@pytest.mark.usefixtures("init_driver")
class yelpCampBaseTest(yelpCampBasePage):

    pass

