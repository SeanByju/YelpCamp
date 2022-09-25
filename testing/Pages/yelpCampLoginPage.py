# page object for login page

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.yelpCampBasePage import yelpCampBasePage
from Config.config import Config



class yelpCampLoginPage(yelpCampBasePage):

    """ By locators """
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')
    LOGIN_URL = Config.BASE_URL+"/login"

    """ constructor of the page class """
    def __init__(self, driver):
        
        super().__init__(driver)


    """ Page Actions """


    def do_login(self, username, password):
        
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def is_login_button_visible(self):

        return self.is_element_enabled(self.LOGIN_BUTTON)

    

    
