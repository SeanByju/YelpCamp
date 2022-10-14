# page object for campgrounds page

from selenium.webdriver.common.by import By

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampCampgroundsPage(yelpCampBasePage):

    """ inherit driver initializer """
    def __init__(self, driver):
        super().__init__(driver)


    """ By locators """
    WELCOME_BACK_ALERT_DIV = ((By.XPATH, '//div[contains(text(),\"Welcome back!")]'),"welcome_back_alert_div")
    GOODBYE_ALERT_DIV = ((By.XPATH, '//div[contains(text(),"GOOD BYE!!")]'),"goodbye_alert_div")
    MAP_CANVAS = ((By.CLASS_NAME, 'mapboxgl-canvas'),"map_canvas")
    ONE_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate1"]'),"one_star_rate_label")
    TWO_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate2"] '),"two_star_rate_label")
    THREE_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate3"]'),"three_star_rate_label")
    FOUR_STAR_RATE_LABEL = ((By.XPATH,'//labe[@for="first-rate4"]'),"four_star_rate_label")
    FIVE_STAR_RATE_LABEL = ((By.XPATH,'//label[@for="first-rate5"]'),"five_star_rate_label")
    DESCRIPTION_TEXTAREA = ((By.ID, "body"),"description_textarea ")
    SUBMIT_REVIEW_BUTTON = ((By.XPATH, '//button[text()="Submit"]'), 'submit_review_button')
    LEAVE_A_REVIEW_HEADER = ((By.XPATH, '//h2[contains(text(),"Leave a Review")]'), 'leave_review_header')
    EDIT_ATAG = ((By.XPATH,'//a[contains(text(),"Edit")]'), 'edit_campground_atag')
    DELETE_CAMPGROUND_BUTTON = ((By.XPATH,'//button[text()="Delete Campground"]'), 'delete_campground_button')
    VIEW_FIRST_CAMPGROUND_BUTTON = ((By.XPATH, '//a[contains(text(),"View My First Camp")]'), 'view_first_campground_button')

    
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

        """ give a star reating to your review """
        match stars:
            case "5":
                self.do_click_and_verify(self.FIVE_STAR_RATE_LABEL[0],self.FIVE_STAR_RATE_LABEL[1])
            case "4":
                self.do_click_and_verify(self.FOUR_STAR_RATE_LABEL[0],self.FOUR_STAR_RATE_LABEL[1])
            case "3":
                self.do_click_and_verify(self.THREE_STAR_RATE_LABEL[0], self.THREE_STAR_RATE_LABEL[1])
            case "2":
                self.do_click_and_verify(self.TWO_STAR_RATE_LABEL[0], self.TWO_STAR_RATE_LABEL[1])
            case "1":
                self.do_click_and_verify(self.ONE_STAR_RATE_LABEL[0],self.ONE_STAR_RATE_LABEL[1])

        """wriet the description for your review"""
        self.do_send_keys_and_verify(self.DESCRIPTION_TEXTAREA[0], self.DESCRIPTION_TEXTAREA[1], review)

        """ click the submit reivew button"""
        self.do_click_and_verify(self.SUBMIT_REVIEW_BUTTON[0], self.SUBMIT_REVIEW_BUTTON[1])

        """return to the campgrounds page of the webpage after submitting"""
        self.do_click_and_verify(self.CAMPGROUNDS_NAV_BUTTON[0], self.CAMPGROUNDS_NAV_BUTTON[1])



    
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


    """delete a reveiw from a campground"""
    def delete_campground(self, campground_name):
        
        "locate the button where you can view that campsite's subpage"
        self.do_click_and_verify((By.XPATH, '//a[contains(text(),"'+campground_name+'")]'), "view_campground")

        "click the edit button"
        self.do_click_and_verify(self.EDIT_ATAG[0], self.EDIT_ATAG[1])

        "click the delete button"
        self.do_click_and_verify(self.DELETE_CAMPGROUND_BUTTON[0], self.DELETE_CAMPGROUND_BUTTON[1])

    


    
