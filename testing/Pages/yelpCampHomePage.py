"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""

import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from datetime import datetime as dt
from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage



"""This is the parent of all pages"""
"""It contains all of the generic methods and utiilties for all pages"""


class yelpCampHomePage(yelpCampBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    """ locators for home page web elements """
    VIEW_CAMPGROUNDS_BUTTON = ((By.XPATH, '//a[contains(text(),"View Campgrounds")]'), 'view_campgrounds_button')



    """ get to the campgrounds page by clicking the view campgrounds button"""
    def click_view_campgrounds_button(self):

        self.do_click_and_verify(self.VIEW_CAMPGROUNDS_BUTTON[0], self.VIEW_CAMPGROUNDS_BUTTON[1])

        # returnt he driver an put it into a campgrounds page object
        return self.driver



    