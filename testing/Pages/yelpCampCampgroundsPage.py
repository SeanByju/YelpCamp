# page object for campgrounds page

import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampCampgroundsPage(yelpCampBasePage):

    """ inherit driver initializer """
    def __init__(self, driver):
        super().__init__(driver)


    """ By locators """
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Logout"]')
    WELCOME_BACK_ALERT_DIV = (By.XPATH, '//div[text()="Welcome back!"]')
    GOOBYE_ALERT_DIV = (By.XPATH, '//div[@class="alert-success" and text()=" GOOD BYE!! "]') 
    MAP_CANVAS = (By.CLASS_NAME, 'mapboxgl-canvas')

            
    """ verify that you logged in by seeing whether the welcome back divider is visible"""
    def is_welcome_back_alert_visible(self):
        
        return self.is_element_enabled(self.WELCOME_BACK_ALERT_DIV)

    """ verify that you logged in by seeing whether the map canvas is visible """
    def is_mapbox_canvas_visible(self):

        return self.is_element_enabled(self.MAP_CANVAS)

    """ verify that you logged out by seeing whether the  good bye alert div is visible"""
    def is_good_bye_div_visible(self):

        return self.is_element_enabled(self.GOOBYE_ALERT_DIV)
    
    
    """ use this function to logout of your yelp camp account"""
    def do_logout(self):

        self.do_click(self.LOGOUT_BUTTON)
        self.is_element_enabled(self.GOOBYE_ALERT_DIV)

    
