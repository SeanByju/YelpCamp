import unittest
import pytest

from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# from conftest import init_driver
from Config.config import Config
from selenium.webdriver.common.by import By


# @pytest.mark.usefixtures("init_driver")
class Test_yelpCampAddWithoutLogin(yelpCampBaseTest):

    # first test, login into your account and verify you logged in
    @pytest.mark.xfail(condition= lambda: True, reason = "you should not be able to access the new campgrounds page since you are not logged in. if it fails, good")
    def test_1_fail_add_campground(self):

        self.yelpCampBasePage = yelpCampBasePage(self.driver)

        # note: do not have accesss to see the new campgrounds button from the home page
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.yelpCampBasePage.nav_to_campgrounds_page())


        self.yelpCampCampgroundsPage.nav_to_new_campgrounds_page()


        flag = self.yelpCampCampgroundsPage.is_submit_new_campground_button_visible()


        assert flag




    def test_2_is_submit_new_campground_button_visible(self):


        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)


        flag = self.yelpCampLoginPage.is_must_be_signed_in_alert_div_visible()


        assert flag
