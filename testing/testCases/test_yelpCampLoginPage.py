import pytest


from Pages.yelpCampLoginPage import yelpCampLoginPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
from configtest import init_driver_indirect
from Config.config import Config


class Test_yelpCampLoginPage(yelpCampBaseTest):

    def test_login_button_visible(self):
        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)
        flag = self.yelpCampLoginPage.is_login_button_visible()
        assert flag

    def test_login(self):
        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)
        self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD)


"""
Example run in Windows Terminal

python -m pytest TestCases/test_yelpCampLoginPage.py

"""