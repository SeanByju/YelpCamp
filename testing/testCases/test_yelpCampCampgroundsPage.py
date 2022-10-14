""" test yelpCamp camporgrounds page functions"""

import pytest
"""
from requests import delete
"""
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from Pages.yelpCampNewCampgroundPage import yelpCampNewCampgroundPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# note: even though init driver is called only as a fixture, it still needs to be imported
from configtest import init_driver
from Config.config import Config



@pytest.mark.usefixtures("init_driver")
class Test_yelpCampCampgroundsPage(yelpCampBaseTest):

    """ first test, login into your account and verify you logged in """
    def test_1_login_and_verify(self):
        print("initiate login and verify test")
        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)
        self.yelpCampCampgroundsPage = self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD)
        """ verify that login was successful by checking if the mapbox canvs and logout buttons are visible"""
        """ note: could use the welcome back alert as a verifier as well but it is only usable with accounts that have already been created"""
        """ and you're logging back in. """
        flag = self.yelpCampCampgroundsPage.is_welcome_back_alert_visible()
        """
        print(self.yelpCampCampgroundsPage.get_element_text(self.yelpCampCampgroundsPage.VIEW_FIRST_CAMPGROUND_BUTTON[0]))
        """
        assert flag

    
    # must be loggeed in to add a campground
    def test_2_add_campground(self):
        self.yelpCampNewCampgroundPage = yelpCampNewCampgroundPage(self.driver)
        self.yelpCampNewCampgroundPage = self.yelpCampNewCampgroundPage.click_new_campgrounds_atag()
        self.yelpCampNewCampgroundPage.add_campground()
    

    def test_3_write_review(self):
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)
        self.yelpCampCampgroundsPage.write_review(Config.REVIEW_STAR_RATING, Config.REVIEW_DESCRIPTION)
        self.yelpCampCampgroundsPage.do_click_and_verify(self.yelpCampCampgroundsPage.CAMPGROUNDS_NAV_BUTTON[0], self.yelpCampCampgroundsPage.CAMPGROUNDS_NAV_BUTTON[1])
        
        


    def test_4_delete_campground(self):
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)
        self.yelpCampCampgroundsPage.delete_campground(Config.CAMPGROUND_NAME)




    def test_5_logout_and_verify(self):
        print("initiate logout and verify test")
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)
        self.yelpCampCampgroundsPage.do_logout()
        flag = self.yelpCampCampgroundsPage.is_good_bye_div_visible()
        assert flag
    

