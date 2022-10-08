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

    """ logout and veirfy that you logged out successfully"""
    def do_logout_and_verify(self):
        self.do_logout()
        self.is_element_enabled(self.GOODBYE_ALERT_DIV[0])

    def write_review(self, stars, review):
        pass
        

    
    
    

    
