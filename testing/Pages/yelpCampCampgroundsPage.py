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
    LOGOUT_BUTTON = ((By.XPATH, '//a [contains(text(),\"Logout")]'),"logout_button")
    WELCOME_BACK_ALERT_DIV = ((By.XPATH, '//div[contains(text(),\"Welcome back!")]'),"welcome_back_alert_div")
    GOODBYE_ALERT_DIV = ((By.XPATH, '//div[contains(text(),\"GOOD BYE!!")]'),"goodbye_alert_div")
    MAP_CANVAS = ((By.CLASS_NAME, 'mapboxgl-canvas'),"map_canvas")

            
    """ verify that you logged in by seeing whether the welcome back divider is visible"""
    def is_welcome_back_alert_visible(self):
        
        return self.is_element_enabled(self.WELCOME_BACK_ALERT_DIV[0])

    """ verify that you logged in by seeing whether the map canvas is visible """
    def is_mapbox_canvas_visible(self):

        return self.is_element_enabled(self.MAP_CANVAS[0])

    """ verify that you logged out by seeing whether the  good bye alert div is visible"""
    def is_good_bye_div_visible(self):

        return self.is_element_enabled(self.GOODBYE_ALERT_DIV[0])
    
    
    """ use this function to logout of your yelp camp account"""
    def do_logout(self):

        self.do_click_and_verify(self.LOGOUT_BUTTON[0], self.LOGOUT_BUTTON[1])
        self.is_element_enabled(self.GOODBYE_ALERT_DIV[0])

    
