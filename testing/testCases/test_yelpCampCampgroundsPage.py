import pytest


from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
from configtest import init_driver
from Config.config import Config

@pytest.mark.usefixtures("init_driver")
class Test_yelpCampCampgroundsPage(yelpCampBaseTest):

    def test_welcome_back(self):
        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)
        yelpCampCampgroundsPage = self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD)
        print(self.driver.current_url)
        yelpCampCampgroundsPage.is_welcome_back_alert_visible()

    """
    def test_logout(self):
            driver = self.driver
            self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(driver)
            self.yelpCampCampgroundsPage.do_logout()
            flag = self.yelpCampCampgroundsPage.is_good_bye_div_visible()
            assert flag
    """

