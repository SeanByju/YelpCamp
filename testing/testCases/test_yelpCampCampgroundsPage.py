""" test yelpCamp camporgrounds page functions"""

import pytest
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# note: even though init driver is called only as a fixture, it still needs to be imported
from configtest import init_driver
from Config.config import Config

@pytest.mark.usefixtures("init_driver")
class Test_yelpCampCampgroundsPage(yelpCampBaseTest):

    def test_login_and_verify(self):
        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)
        yelpCampCampgroundsPage = self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD)
        """ verify that login was successful by checking if the mapbox canvs and logout buttons are visible"""
        """ note: could use the welcome back alert as a verifier as well but it is only usable with accounts that have already been created"""
        """ and you're logging back in. """
        flag = yelpCampCampgroundsPage.is_welcome_back_alert_visible()
        assert flag

    # must be loggeed in to add a campground
    def test_add_campground(self):
        self.yelpCampCampgroundsPage = yelpCampLoginPage(self.driver)

        
    
    def test_logout_and_verify(self):
        driver = self.driver
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(driver)
        self.yelpCampCampgroundsPage.do_logout()
        flag = self.yelpCampCampgroundsPage.is_good_bye_div_visible()
        assert flag
    

