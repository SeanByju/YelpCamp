# page object for registeration page


from selenium.webdriver.common.by import By

from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.Locator import Locator

class yelpCampRegisterPage(yelpCampBasePage):
    
    """ By locators"""
    USERNAME = (By.XPATH, Locator.REGISTER_USERNAME_INPUT)
    PASSWORD = (By.XPATH, Locator.REGISTER_PASSWORD_INPUT)
    EMAIL = (By.XPATH, Locator.REGISTER_EMAIL_INPUT)
    REGISTER_BUTTON = (By.XPATH, Locator.REGISTER_BUTTON)
    USERNAME_NAME = "register_username"
    PASSWORD_NAME = "register_password"
    EMAIL_NAME = "register_email"
    REGISTER_BUTTON_NAME = "register_button"


    """ Page Actions """

    def do_register(self, username, email, password):

        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.REGISTER_BUTTON)

        # return the driver and initiate a campgrounds page object
        return self.driver


    def is_register_button_visible(self):
        
        return super().is_element_visible(self.REGISTER_BUTTON[0], self.REGISTER_BUTTON[1])