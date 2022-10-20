import pytest

from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
from conftest import init_driver
from Config.config import Config

@pytest.mark.usefixtures("init_driver")
class Test_yelpCampLoginPage(yelpCampBaseTest):

    # first test, login into your account and verify you logged in
    def test_1_login_and_verify(self):

        self.yelpCampBasePage = yelpCampBasePage(self.driver)


        self.yelpCampLoginPage = yelpCampLoginPage(self.yelpCampBasePage.nav_to_login_page())


        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD))

        
        flag = self.yelpCampCampgroundsPage.is_welcome_back_alert_div_visible()


        assert flag

    

"""
Example run in Windows Terminal

python -m pytest TestCases/test_yelpCampLoginPage.py

"include html report"
python -m pytest TestCases/test_yelpCampLoginPage.py -v --html=./Reports/yelpCampTestReport.html

"""