# page object for login page

import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage


class yelpCampLoginPage(yelpCampBasePage):

    """inherit driver initializer"""
    def __init__(self, driver):
        super().__init__(driver)

    """ By locators """
    USERNAME_INPUT = ((By.ID, "username"), "username_input")
    PASSWORD_INPUT = ((By.ID, "password"), "password_input")
    LOGIN_BUTTON = ((By.XPATH, '//button[text()="Login"]'), "login_button")
    LOGIN_URL = Config.BASE_URL+"/login"
    


    """ Page Actions """

    """use this function to login in to the website"""
    def do_login(self, username, password):
        
        self.do_send_keys_and_verify(self.USERNAME_INPUT[0],self.USERNAME_INPUT[1], username)
        self.do_send_keys_and_verify(self.PASSWORD_INPUT[0],self.PASSWORD_INPUT[1], password)
        self.do_click_and_verify(self.LOGIN_BUTTON[0], self.LOGIN_BUTTON[1])
        return yelpCampCampgroundsPage(self.driver)

    """check if the login button is visible"""
    def is_login_button_visible(self):

        return self.is_element_enabled(self.LOGIN_BUTTON[0])

    
