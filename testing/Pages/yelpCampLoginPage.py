# page object for login page


import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage


class yelpCampLoginPage(yelpCampBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    """ By locators """
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')
    LOGIN_URL = Config.BASE_URL+"/login"


    """ Page Actions """

    """use this funcntion to login in to the website"""
    def do_login(self, username, password):
        
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    """check if the login button is visible"""
    def is_login_button_visible(self):

        return self.is_element_enabled(self.LOGIN_BUTTON)

