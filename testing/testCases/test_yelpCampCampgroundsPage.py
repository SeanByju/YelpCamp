""" test yelpCamp camporgrounds page functions"""

import pytest
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from Pages.yelpCampNewCampgroundPage import yelpCampNewCampgroundPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# note: even though init driver is called only as a fixture, it still needs to be imported
from configtest import init_driver
from Config.config import Config



@pytest.mark.usefixtures("init_driver")
class Test_yelpCampCampgroundsPage(yelpCampBaseTest):

    def test_1_login_and_verify(self):
        print("initiate login and verify test")
        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)
        self.yelpCampCampgroundsPage = self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD)
        """ verify that login was successful by checking if the mapbox canvs and logout buttons are visible"""
        """ note: could use the welcome back alert as a verifier as well but it is only usable with accounts that have already been created"""
        """ and you're logging back in. """
        flag = self.yelpCampCampgroundsPage.is_welcome_back_alert_visible()
        assert flag

    """
    # must be loggeed in to add a campground
    def test_2_add_campground(self):
        print("initiate add campground test")
        self.yelpCampNewCampgroundPage = yelpCampNewCampgroundPage(self.driver)
        self.yelpCampNewCampgroundPage = self.yelpCampNewCampgroundPage.click_new_campgrounds_atag()
        self.yelpCampNewCampgroundPage.add_campground()
    """

    def test_write_review(self):
        pass

    def test_3_delete_campground(self):
        pass
    
    """
    def test_4_logout_and_verify(self):
        print("initiate logout and verify test")
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)
        self.yelpCampCampgroundsPage.do_logout()
        flag = self.yelpCampCampgroundsPage.is_good_bye_div_visible()
        assert flag
    """

