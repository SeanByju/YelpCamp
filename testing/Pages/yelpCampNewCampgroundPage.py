"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""

from selenium import webdriver
from distutils.command.config import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime as dt
import time

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage

class yelpCampNewCampgroundPage(yelpCampBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    """ By locators """
    CAMPGROUND_NAME_INPUT = ((By.ID, "title"), "campground_name_input")
    CAMPGROUND_LOCATION_INPUT = ((By.ID,"location"),"campground_location_input")
    CHOOSE_FILES_BUTTON = ((By.ID,"image"),"campground_file_input")
    CAMPGROUND_PRICE = ((By.ID, "price"),"campground_price")
    CAMPGROUND_DESCRIPTION = ((By.ID, "description"), "campground_description")
    SUBMIT_NEW_CAMPGROUND_BUTTON = ((By.XPATH, '//button[contains(text(),"Submit")]'),"submit_new_campground_button")
    CANCEL_ATAG = ((By.XPATH,'//a[text()="Cancel"]'),"cancel_new_campground")

    """ Page Actions"""

    """ add campground to account"""
    """ adjust add campground to include inputs for campground information """
    
    def add_campground(self):
        
        print("campground name input starts")
        self.do_send_keys_and_verify(self.CAMPGROUND_NAME_INPUT[0],self.CAMPGROUND_NAME_INPUT[1], Config.CAMPGROUND_NAME)
        
        print("campground location input starts")
        self.do_send_keys_and_verify(self.CAMPGROUND_LOCATION_INPUT[0], self.CAMPGROUND_LOCATION_INPUT[1], Config.CAMPGROUND_LOCATION)
        
        print("choose file input starts")

        
        print("initial click passed")


        self.do_send_keys_and_verify(self.CHOOSE_FILES_BUTTON[0], self.CHOOSE_FILES_BUTTON[1], Config.UPLOAD_IMAGE)
        
        print("campground price input starts")
        self.do_send_keys_and_verify(self.CAMPGROUND_PRICE[0], self.CAMPGROUND_PRICE[1], Config.CAMPGROUND_PRICE)
        
        print("campground description input starts")
        self.do_send_keys_and_verify(self.CAMPGROUND_DESCRIPTION[0], self.CAMPGROUND_DESCRIPTION[1], Config.CAMPGROUND_DESCRIPTION)
        
        print("click submit button")
        self.do_click_and_verify(self.SUBMIT_NEW_CAMPGROUND_BUTTON[0], self.SUBMIT_NEW_CAMPGROUND_BUTTON[1])
        
        """
        "test finding the submit button"
        self.driver.find_element(By.XPATH,'').click()
        """


        return yelpCampCampgroundsPage(self.driver)
        

    # return the new campground page
    def click_new_campgrounds_atag(self):

        self.do_click_and_verify(self.NEW_CAMPGROUNDS_BUTTON[0], self.NEW_CAMPGROUNDS_BUTTON[1])

        return yelpCampNewCampgroundPage(self.driver)

    def delete_campground(self):

        self.do_click_and_verify()



        """
        input_tags = self.driver.find_elements(By.TAG_NAME,'input')
        for web_element in input_tags:
            print(web_element.get_attribute("id"))
        
        print("C:\\Users\\Owner\\Documents\\Programming\\YelpCamp\\testing\\Resources\Images\\redwood-forrest-1.jpg")
        print(self.driver.find_element(By.ID,"image").send_keys())
        """