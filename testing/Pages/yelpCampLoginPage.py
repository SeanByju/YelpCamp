# page object for login page

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampLoginAPage(yelpCampBasePage):

    """ By locators """
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')

    def __init__(self, driver):
        
        super().__init__(driver)


    """ Page Actions """

    def is_username_input_visible(self):
        
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.USERNAME))

    def do_login(self, username, password):
        
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    

    
