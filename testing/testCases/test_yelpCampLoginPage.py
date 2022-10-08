import pytest


from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
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
        yelpCampCampgroundsPage = self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD) 
        flag = yelpCampCampgroundsPage.is_welcome_back_alert_visible()
        assert flag

    

"""
Example run in Windows Terminal

python -m pytest TestCases/test_yelpCampLoginPage.py

"include html report"
python -m pytest TestCases/test_yelpCampLoginPage.py -v --html=./Reports/yelpCampTestReport.html

"""