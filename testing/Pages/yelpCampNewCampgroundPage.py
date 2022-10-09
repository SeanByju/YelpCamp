"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""

from distutils.command.config import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime as dt
import time

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage
from testing.Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage

class yelpCampNewCampgroundPage(yelpCampBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    """ By locators """
    CAMPGROUND_NAME_INPUT = ((By.ID, "title"), "campground_name_input")
    CAMPGROUND_LOCATION_INPUT = ((By.ID,"location"),"campground_location_input")
    CHOOSE_FILES_BUTTON = ((By.ID, "image"),"choose_files_button")
    CAMPGROUND_PRICE = ((By.ID, "price"),"campground_price")
    CAMPGROUND_DESCRIPTION = ((By.ID, "description"), "campground_description")
    SUBMIT_NEW_CAMPGROUND_BUTTON = ((By.XPATH, '//button{text()="Submit"]'),"submit_new_campground_button")
    CANCEL_ATAG = ((By.XPATH,'//a[text()="Cancel"]'),"cancel_new_campground")

    """ Page Actions"""

    """ add campground to account"""
    def add_campground(self):
        
        self.do_send_keys_and_verify(self.CAMPGROUND_NAME_INPUT[0],self.CAMPGROUND_NAME_INPUT[1], Config.CAMPGROUND_NAME)
        self.do_send_keys_and_verify(self.CAMPGROUND_LOCATION_INPUT[0], self.CAMPGROUND_LOCATION_INPUT[1], Config.CAMPGROUND_LOCATION)
        self.do_send_keys_and_verify(self.CHOOSE_FILES_BUTTON[0], self.CHOOSE_FILES_BUTTON[1],Config.UPLOAD_IMAGE)
        self.do_send_keys_and_verify(self.CAMPGROUND_PRICE[0], self.CAMPGROUND_PRICE[1], Config.CAMPGROUND_PRICE)
        self.do_send_keys_and_verify(self.CAMPGROUND_DESCRIPTION[0], self.CAMPGROUND_DESCRIPTION[1], Config.CAMPGROUND_DESCRIPTION)
        self.do_click_and_verify(self.SUBMIT_NEW_CAMPGROUND_BUTTON[0], self.SUBMIT_NEW_CAMPGROUND_BUTTON[1])
        return yelpCampCampgroundsPage(self.driver)

