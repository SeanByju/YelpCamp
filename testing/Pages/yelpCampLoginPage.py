# page object for login page

from selenium.webdriver.common.by import By

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.Locator import Locator


class yelpCampLoginPage(yelpCampBasePage):

    """ By locators """
    USERNAME_INPUT = (By.XPATH, Locator.LOGIN_USERNAME_INPUT)
    PASSWORD_INPUT = (By.XPATH, Locator.LOGIN_PASSWORD_INPUT)
    LOGIN_BUTTON = (By.XPATH, Locator.LOGIN_BUTTON)
    LOGIN_URL = Config.BASE_URL+"/login"
    MUST_BE_SIGNED_IN_ALERT_DIV_NAME = (By.XPATH, Locator.MUST_BE_SIGNED_IN_ALERT_DIV)
    USERNAME_INPUT_NAME = "username_input"
    PASSWORD_INPUT_NAME = "password_input"
    LOGIN_BUTTON_NAME = "login_button"
    MUST_BE_SIGNED_IN_ALERT_DIV_NAME = "must_be_signed_in_alert_div"
    


    """ Page Actions """
    
    def getUsernameInput(self):

        return self.USERNAME_INPUT

    def getPasswordInput(self):

        return self.PASSWORD_INPUT

    def getLoginButton(self):

        return self.LOGIN_BUTTON

    def getMustBeSignedInAlertDiv(self):

        return self.MUST_BE_SIGNED_IN_ALERT_DIV


    """use this function to login in to the website"""
    def do_login(self, username, password):
        
        self.do_send_keys_and_verify(self.USERNAME_INPUT[0],self.USERNAME_INPUT[1], username)

        self.do_send_keys_and_verify(self.PASSWORD_INPUT[0],self.PASSWORD_INPUT[1], password)
        
        self.do_click_and_verify(self.LOGIN_BUTTON[0], self.LOGIN_BUTTON[1])

        # return the driver and initiate a campgrounds page object
        return self.driver
        


    """check if the login button is visible"""
    def is_login_button_visible(self):

        return self.is_element_visible(self.LOGIN_BUTTON[0], self.LOGIN_BUTTON[1])

    
    # the "you must be signed in" div is visible when you try to make a new campground but are not signed in so this verifies that this is the case
    def is_must_be_signed_in_alert_div_visible(self):

        return self.is_element_visible(self.MUST_BE_SIGNED_IN_ALERT_DIV[0], self.MUST_BE_SIGNED_IN_ALERT_DIV[1])

    
