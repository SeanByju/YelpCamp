""" test yelpCamp camporgrounds page functions"""

import pytest

from Pages.yelpCampBasePage import yelpCampBasePage
"""
from requests import delete
"""
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# note: even though init driver is called only as a fixture, it still needs to be imported
from conftest import init_driver
from Config.config import Config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_dummy(yelpCampBaseTest):
    
    def test_dummy(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver.get("https://morning-savannah-46253.herokuapp.com/")

        self.driver.implicitly_wait(60)

        self.driver.delete_all_cookies()

        self.yelpCampBasePage = yelpCampBasePage(self.driver)

        self.yelpCampBasePage.nav_to_login_page()

        self.yelpCampBasePage.nav_to_home_page()

        self.yelpCampBasePage.nav_to_campgrounds_page()

        self.yelpCampBasePage.nav_to_register_page()

        self.driver.close()

        self.driver.quit()