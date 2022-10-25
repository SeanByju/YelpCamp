"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""

from selenium.webdriver.common.by import By
from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.Locator import Locator



"""This is the parent of all pages"""
"""It contains all of the generic methods and utiilties for all pages"""


class yelpCampHomePage(yelpCampBasePage):
    

    """ locators for home page web elements """
    VIEW_CAMPGROUNDS_BUTTON = (By.XPATH, Locator.VIEW_CAMPGROUNDS_BUTTON)
    VIEW_CAMPGROUNDS_BUTTON_NAME = "view_campgrounds_button"





    