"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime as dt
import time

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampNewCampgroundPage(yelpCampBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    """ By locators """
    CAMPGROUND_NAME_INPUT = ((By.ID), "title")
    CAMPGROUND_LOCATION_INPUT = ((By.ID),"location")
    CHOOSE_FILES_BUTTON = ((By.ID), "image")
    CAMPGROUND_PRICE = ((By.ID), "price")
    CAMPGROUND_DESCRIPTION = ((By.ID), "description")
    SUBMIT_BUTTON = ((),"")
    CANCEL_ATAG = ((),"")

    """ add campground to account"""
    def add_campground(self):
        pass
