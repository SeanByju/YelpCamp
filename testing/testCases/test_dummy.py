""" test yelpCamp camporgrounds page functions"""

import pytest
"""
from requests import delete
"""
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from Pages.yelpCampNewCampgroundPage import yelpCampNewCampgroundPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# note: even though init driver is called only as a fixture, it still needs to be imported
from configtest import init_driver
from Config.config import Config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_dummy(yelpCampBaseTest):
    
    def test_dummey(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver.get("https://morning-savannah-46253.herokuapp.com/campgrounds/62edfc449221806e44c9d6a9")

        self.driver.implicitly_wait(60)

        self.driver.delete_all_cookies()

        self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.driver)

        flag = self.yelpCampCampgroundsPage.search_review("5", 'Loved it here!', "boggitybog")

        self.driver.close()

        self.driver.quit()

        assert flag