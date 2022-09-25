import pytest

from Config.config import Config
from Pages.yelpCampLoginPage import yelpCampLoginPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
from TestCases.configtest import init_driver



class Test_yelpCampLoginPage(yelpCampBaseTest):

    def test_login_button_visible(self):
        self.yelpCampLoginPage = yelpCampLoginPage(init_driver().get(yelpCampLoginPage.LOGIN_URL))
        flag = self.yelpCampLoginPage.is_login_button_visible()
        assert flag

    def test_login(self):
        self.yelpCampLoginPage = yelpCampLoginPage(init_driver().get(yelpCampLoginPage.LOGIN_URL))
        self.yelpCampLoginPage.do_login(Config.USERNAME,Config.PASSWORD)


"""
Example run in Windows Terminal

python -m pytest TestCases/test_yelpCampLoginPage.py

"""