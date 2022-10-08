import pytest


from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
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
        flag1 = yelpCampCampgroundsPage.is_mapbox_canvas_visible()
        flag2 = yelpCampCampgroundsPage.is_logout_nav_button_enabled()
        yelpCampCampgroundsPage
        self.assertEqual(flag1,flag2)

    
    def test_logout_and_verify(self):
        driver = self.driver
        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(driver)
        self.yelpCampCampgroundsPage.do_logout()
        flag = self.yelpCampCampgroundsPage.is_good_bye_div_visible()
        assert flag
    

