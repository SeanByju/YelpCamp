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
    ONE_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate1"]'),"one_star_rate_label")
    TWO_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate2"] '),"two_star_rate_label")
    THREE_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate3"]'),"three_star_rate_label")
    FOUR_STAR_RATE_LABEL = ((By.XPATH,'//labe[@for="first-rate4"]'),"four_star_rate_label")
    FIVE_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate5"]'),"five_star_rate_label")
    DESCRIPTION_TEXTAREA = ((By.ID, "body"),"description_textarea ")
    SUBMIT_REVIEW_BUTTON = ((By.XPATH, '//button[text()="Submit"]'), 'submit_review_button')
    """
    REVIEW_DESCRIPTION_IDENTIFIER = (By.XPATH, '//h5[@class="card-title" and text()="'+ Config.REVIEW_DESCRIPTION +'"]')
    REVIEW_CARD_REVIEWER_IDENTIFIER = (By.CLASS_NAME, 'card-subtitle')
    REVIEW_CARD_RATING = (By.XPATH, '//p[contains(text(),"'+Config.REVIEW_STAR_RATING+'")]')
    """


            
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

    """ use this method to write a review of a campsite"""
    def write_review(self, stars, review):
        
        self.do_click_and_verify(self.FIVE_STAR_RATE_LABEL[0], self.FIVE_STAR_RATE_LABEL[1])
        self.do_send_keys_and_verify(self.DESCRIPTION_TEXTAREA[0], self.DESCRIPTION_TEXTAREA[1], )
        self.do_click_and_verify(self.SUBMIT_REVIEW_BUTTON[0], self.SUBMIT_REVIEW_BUTTON[1])
    
    """ verify that the review was added """
    """ verify by compiling a list of all of the review cards that match the input desription """
    """ then get the name of the reviewer and the star rating inputs and determine if the expected elements that contain these pieces of text exist on the review card """
    """ if the reviewer and star rating exist, you found the review you are searching for"""
    def search_review(self, stars, review, reviewer):

        review_list = self.driver.find_elements(review[0], review[1])

        for i in range(0, len(review_list)):

            review_parent_card = review_list[i].find_element_by_xpath("..")
            reviewer = review_parent_card.find_element_by_xpath(reviewer[0], reviewer[1])
            data_rating = review_parent_card.find_element_by_xpath(stars[0], stars[1])

            if data_rating and reviewer:

                return True
            
            else:

                continue

        return False
    

    
