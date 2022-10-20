# page object for registeration page

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampRegisterPage(yelpCampBasePage):
    
    """ By locators"""
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    EMAIL = (By.ID, "email")
    REGISTER_BUTTON = (By.XPATH, '//nav//a[text()="Register"]')

    """ constructor of the page class """
    def __init__(self, driver):
        
        super().__init__(driver)

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