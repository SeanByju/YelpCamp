import pytest


from Pages.yelpCampLoginPage import yelpCampLoginPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
from configtest import init_driver
from Config.config import Config

@pytest.mark.usefixtures("init_driver")
class Test_yelpCampLoginPage(yelpCampBaseTest):

    def test_login_button_visible(self):
        driver = self.driver
        self.yelpCampLoginPage = yelpCampLoginPage(driver)
        flag = self.yelpCampLoginPage.is_login_button_visible()
        assert flag

    def test_login(self):
        driver = self.driver
        self.yelpCampLoginPage = yelpCampLoginPage(driver)
        self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD)
        flag = self.yelpCampLoginPage.is_welcome_back_alert_visible()
        assert flag

    def test_logout(self):
        driver = self.driver
        self.yelpCampLoginPage = yelpCampLoginPage(driver)
        self.yelpCampLoginPage.do_logout()
        flag = self.yelpCampLoginPage.is_good_bye_div_visible()


"""
Example run in Windows Terminal

python -m pytest TestCases/test_yelpCampLoginPage.py

"include html report"
python -m pytest TestCases/test_yelpCampLoginPage.py -v --html=./Reports/yelpCampTestReport.html

"""