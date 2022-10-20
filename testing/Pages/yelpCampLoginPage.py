# page object for login page

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

        print("\n this is the page that you are looking at after clicking the login in button: \n")

        print(self.driver.find_element(By.XPATH, "//main").text)

        # return the driver and initiate a campgrounds page object
        return self.driver
        


    """check if the login button is visible"""
    def is_login_button_visible(self):

        return self.is_element_visible(self.LOGIN_BUTTON[0], self.LOGIN_BUTTON[1])

    
