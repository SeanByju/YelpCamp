""" test yelpCamp camporgrounds page functions"""

import pytest
"""
from requests import delete
"""
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# note: even though init driver is called only as a fixture, it still needs to be imported
from conftest import init_driver
from Config.config import Config


# add the init_driver fixture so you can add your set up and teardown functions
@pytest.mark.usefixtures("init_driver")
class Test_yelpCampCampgroundsPage(yelpCampBaseTest):


    # first test, login into your account and verify you logged in
    def test_1_login_and_verify(self):

        self.yelpCampBasePage = yelpCampBasePage(self.driver)


        self.yelpCampLoginPage = yelpCampLoginPage(self.yelpCampBasePage.nav_to_login_page())


        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD))

        
        flag = self.yelpCampCampgroundsPage.is_welcome_back_alert_div_visible()


        assert flag

    
    # must be loggeed in to add a campground
    def test_2_add_campground(self):

        
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)

        
        self.yelpCampCampgroundsPage.nav_to_new_campgrounds_page()

        
        self.yelpCampCampgroundsPage.add_campground(Config.CAMPGROUND_NAME, Config.CAMPGROUND_LOCATION, Config.UPLOAD_IMAGE, Config.CAMPGROUND_PRICE, Config.CAMPGROUND_DESCRIPTION)


        flag = self.yelpCampCampgroundsPage.verify_add_campground()

        
        assert flag



    def test_3_write_review(self):

        
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)

        
        self.yelpCampCampgroundsPage.write_review(Config.REVIEW_STAR_RATING, Config.REVIEW_DESCRIPTION)


        flag = self.yelpCampCampgroundsPage.search_review(Config.REVIEW_STAR_RATING, Config.REVIEW_DESCRIPTION, Config.USERNAME)


        self.yelpCampCampgroundsPage.nav_to_campgrounds_page()
        
        
        assert flag
        


    def test_4_delete_campground_with_review(self):

        
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)
        
        
        self.yelpCampCampgroundsPage.delete_campground(Config.CAMPGROUND_NAME)

        
        flag = self.yelpCampCampgroundsPage.is_review_not_defined_visible()


        assert flag




    def test_5_logout_and_verify(self):

        
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)
        
        
        self.yelpCampCampgroundsPage.do_logout()

        
        flag = self.yelpCampCampgroundsPage.is_good_bye_div_visible()
        
        
        assert flag