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
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Logout"]')
    WELCOME_BACK_ALERT_DIV = (By.XPATH, '//div[@class="alert-success" and text()=" Welcome back! "]')
    GOOBYE_ALERT_DIV = (By.XPATH, '//div[@class="alert-success" and text()=" GOOD BYE!! "]') 



    """ Page Actions """

    """use this function to login in to the website"""
    def do_login(self, username, password):
        
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        self.is_element_enabled(self.WELCOME_BACK_ALERT_DIV)

    """check if the login button is visible"""
    def is_login_button_visible(self):

        return self.is_element_enabled(self.LOGIN_BUTTON)

    """ use this function to logout of your yelp camp account"""
    def do_logout(self):

        self.do_click(self.LOGOUT_BUTTON)
        self.is_element_enabled(self.GOOBYE_ALERT_DIV)
        
    """ verify that you logged in by seeing whether the welcome back divider is visible"""
    def is_welcome_back_alert_visible(self):
        
        return self.is_element_enabled(self.WELCOME_BACK_ALERT_DIV)

    """ verify that you logged out by seeing whether the  good bye alert div is visible"""
    def is_good_bye_div_visible(self):

        return self.is_element_enabled(self.GOOBYE_ALERT_DIV)
    
