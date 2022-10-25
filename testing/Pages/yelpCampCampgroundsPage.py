# page object for campgrounds page

from Pages.Locator import Locator
from selenium.webdriver.common.by import By

from Config.config import Config
from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampCampgroundsPage(yelpCampBasePage):


    """ By locators """
    WELCOME_BACK_ALERT_DIV = (By.XPATH, Locator.WELCOME_BACK_ALERT_DIV)
    GOODBYE_ALERT_DIV = (By.XPATH, Locator.GOODBYE_ALERT_DIV)
    MAP_CANVAS = (By.XPATH, Locator.MAP_CANVAS)
    ONE_STAR_RATE_LABEL = (By.XPATH, Locator.ONE_STAR_RATE_LABEL)
    TWO_STAR_RATE_LABEL = (By.XPATH, Locator.TWO_STAR_RATE_LABEL)
    THREE_STAR_RATE_LABEL = (By.XPATH, Locator.THREE_STAR_RATE_LABEL)
    FOUR_STAR_RATE_LABEL = (By.XPATH, Locator.FOUR_STAR_RATE_LABEL)
    FIVE_STAR_RATE_LABEL = (By.XPATH, Locator.FIVE_STAR_RATE_LABEL)
    DESCRIPTION_TEXTAREA = (By.XPATH, Locator.DESCRIPTION_TEXTAREA)
    SUBMIT_REVIEW_BUTTON = (By.XPATH, Locator.SUBMIT_REVIEW_BUTTON)
    LEAVE_A_REVIEW_HEADER = (By.XPATH, Locator.LEAVE_A_REVIEW_HEADER)
    EDIT_ATAG = (By.XPATH, Locator.EDIT_ATAG)
    DELETE_CAMPGROUND_BUTTON = (By.XPATH, Locator.DELETE_CAMPGROUND_BUTTON)
    VIEW_FIRST_CAMPGROUND_BUTTON = (By.XPATH, Locator.VIEW_FIRST_CAMPGROUND_BUTTON)
    USERNAME_REVIEW_SEARCH = (By.XPATH, Locator.USERNAME_REVIEW_SEARCH)
    REVIEW_IS_NOT_DEFINED_TAG = (By.XPATH, Locator.REVIEW_IS_NOT_DEFINED_TAG)
    DELETE_CAMPGROUND_SUCCESS_DIV = (By.XPATH, Locator.DELETE_CAMPGROUND_SUCCESS_DIV)
    ADD_NEW_CAMPGROUND_SUCCESS_DIV = (By.XPATH, Locator.ADD_NEW_CAMPGROUND_SUCCESS_DIV)
    CAMPGROUND_NAME_INPUT = (By.XPATH, Locator.CAMPGROUND_NAME_INPUT)
    CAMPGROUND_LOCATION_INPUT = (By.XPATH, Locator.CAMPGROUND_LOCATION_INPUT)
    CHOOSE_FILES_BUTTON = (By.XPATH, Locator.CHOOSE_FILES_BUTTON)
    CAMPGROUND_PRICE = (By.XPATH, Locator.CAMPGROUND_PRICE)
    CAMPGROUND_DESCRIPTION = (By.XPATH, Locator.CAMPGROUND_DESCRIPTION)
    SUBMIT_NEW_CAMPGROUND_BUTTON = (By.XPATH, Locator.SUBMIT_NEW_CAMPGROUND_BUTTON)
    CANCEL_ATAG = (By.XPATH, Locator.CANCEL_ATAG)
    WELCOME_BACK_ALERT_DIV_NAME = "welcome_back_alert_div"
    GOODBYE_ALERT_DIV_NAME = "goodbye_alert_div"
    MAP_CANVAS_NAME = "map_canvas"
    ONE_STAR_RATE_LABEL_NAME = "one_star_rate_label"
    TWO_STAR_RATE_LABEL_NAME = "two_star_rate_label"
    THREE_STAR_RATE_LABEL_NAME = "three_star_rate_label"
    FOUR_STAR_RATE_LABEL_NAME = "four_star_rate_label"
    FIVE_STAR_RATE_LABEL_NAME = "five_star_rate_label"
    DESCRIPTION_TEXTAREA_NAME = "description_textarea "
    SUBMIT_REVIEW_BUTTON_NAME = 'submit_review_button'
    LEAVE_A_REVIEW_HEADER_NAME = 'leave_review_header'
    EDIT_ATAG_NAME = "edit_campground_atag"
    DELETE_CAMPGROUND_BUTTON_NAME = "delete_campground_button"
    VIEW_FIRST_CAMPGROUND_BUTTON_NAME = "view_first_campground_button"
    USERNAME_REVIEW_SEARCH_NAME = ""
    REVIEW_IS_NOT_DEFINED_TAG_NAME = "review_undefined_div"
    DELETE_CAMPGROUND_SUCCESS_DIV_NAME = "review_undefined_div"
    ADD_NEW_CAMPGROUND_SUCCESS_DIV_NAME = "add_new_campground_success_div"
    CAMPGROUND_NAME_INPUT_NAME = "campground_name_input"
    CAMPGROUND_LOCATION_INPUT_NAME = "campground_location_input"
    CHOOSE_FILES_BUTTON_NAME = "campground_file_input"
    CAMPGROUND_PRICE_NAME = "campground_price"
    CAMPGROUND_DESCRIPTION_NAME = "campground_description"
    SUBMIT_NEW_CAMPGROUND_BUTTON_NAME = "submit_new_campground_button"
    CANCEL_ATAG_NAME = "cancel_new_campground"


    def getWelcomeBackAlertDiv(self):

        return self.WELCOME_BACK_ALERT_DIV


    def getGoodbyeAlertDiv(self):

        return self.GOODBYE_ALERT_DIV

    def getMapCanvas(self):

        return self.MAP_CANVAS

    def getOneStarRateLabel(self):

        return self.ONE_STAR_RATE_LABEL

    def getTwoStarLabel(self):

        return self.TWO_STAR_RATE_LABEL

    def getThreeStarLabel(self):

        return self.THREE_STAR_RATE_LABEL

    def getFourStarLabel(self):

        return self.FOUR_STAR_RATE_LABEL

    def getFiveStarLabel(self):

        return self.FIVE_STAR_RATE_LABEL

    def getDescriptionTextarea(self):

        return self.DESCRIPTION_TEXTAREA

    def getSubmitReviewButton(self):

        return self.SUBMIT_REVIEW_BUTTON

    def getLeaveAReviewButton(self):

        return self.LEAVE_A_REVIEW_HEADER

    def getEditATag(self):

        return self.EDIT_ATAG

    def getDeleteCampgroundButton(self):

        return self.DELETE_CAMPGROUND_BUTTON

    def getViewFirstCampgroundButton(self):

        return self.VIEW_FIRST_CAMPGROUND_BUTTON

    def getUsernameReviewSearch(self):

        return self.USERNAME_REVIEW_SEARCH

    def getReviewIsNotDefinedTag(self):

        return self.REVIEW_IS_NOT_DEFINED_TAG

    def getDeleteCampgroundSuccessDiv(self):

        return self.DELETE_CAMPGROUND_SUCCESS_DIV

    def getAddNewCampgroundsSuccessDiv(self):

        return self.ADD_NEW_CAMPGROUND_SUCCESS_DIV

    def getCampgroundNameInput(self):

        return self.CAMPGROUND_NAME_INPUT

    def getCampgroundLocationInput(self):

        return self.CAMPGROUND_LOCATION_INPUT

    def getChooseFilesButton(self):

        return self.CHOOSE_FILES_BUTTON

    def getCampgroundPrice(self):

        return self.CAMPGROUND_PRICE

    def getCampgroundDescription(self):

        return self.SUBMIT_NEW_CAMPGROUND_BUTTON

    def getCancelAtag(self):

        return self.CANCEL_ATAG



    """
    REVIEW_DESCRIPTION_IDENTIFIER = (By.XPATH, '//h5[@class="card-title" and text()="'+ Config.REVIEW_DESCRIPTION +'"]')
    REVIEW_CARD_REVIEWER_IDENTIFIER = (By.XPATH, 'card-subtitle')
    REVIEW_CARD_RATING = (By.XPATH, '//p[contains(text(),"'+Config.REVIEW_STAR_RATING+'")]')
    """


            
    """ verify that login was successful by checking if the mapbox canvs and logout buttons are visible"""
    """ note: could use the welcome back alert as a verifier as well but it is only usable with accounts that have already been created"""
    """ and you're logging back in. """
    
    """
    def is_welcome_back_alert_visible(self):

        
        return self.is_element_visible(self.WELCOME_BACK_ALERT_DIV[0], self.WELCOME_BACK_ALERT_DIV[1])
    """



    """ verify that you logged in by seeing whether the map canvas is visible """
    """
    def is_mapbox_canvas_visible(self):


        return self.is_element_visible(self.MAP_CANVAS[0], self.MAP_CANVAS[1])
    """



    """ verify that you logged out by seeing whether the  good bye alert div is visible"""
    """
    def is_good_bye_div_visible(self):


        return self.is_element_visible(self.GOODBYE_ALERT_DIV[0], self.GOODBYE_ALERT_DIV[1])


    def is_delete_campground_success_div_visible(self):


        return self.is_element_visible(self.DELETE_CAMPGROUND_SUCCESS_DIV[0], self.DELETE_CAMPGROUND_SUCCESS_DIV[1])
        
    


    # this is only visible at this time because the site is currently not deleting reviews when it is deleting a website. reviews need ot be deleted as well
    def is_review_not_defined_visible(self):

        return self.is_element_visible(self.REVIEW_IS_NOT_DEFINED_TAG[0], self.REVIEW_IS_NOT_DEFINED_TAG[1])




    def is_submit_new_campground_button_visible(self):

        return self.is_element_visible(self.SUBMIT_NEW_CAMPGROUND_BUTTON[0], self.SUBMIT_NEW_CAMPGROUND_BUTTON[1])

    """


    """ logout and veirfy that you logged out successfully"""
    """
    def do_logout_and_verify(self):

        
        self.do_logout()


        
        self.is_element_visible(self.GOODBYE_ALERT_DIV[0], self.GOODBYE_ALERT_DIV[1])

        
        
        return self
    """



    """ use this method to write a review of a campsite"""
    """
    def write_review(self, stars, review):

        # give a star reating to your review
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

        # write the description for your review
        self.do_send_keys_and_verify(self.DESCRIPTION_TEXTAREA[0], self.DESCRIPTION_TEXTAREA[1], review)

        # click the submit reivew button
        self.do_click_and_verify(self.SUBMIT_REVIEW_BUTTON[0], self.SUBMIT_REVIEW_BUTTON[1])
        
        return self.driver
    """



    
    """ verify that the review was added """
    """ verify by compiling a list of all of the review cards that match the input desription """
    """ then get the name of the reviewer and the star rating inputs and determine if the expected elements that contain these pieces of text exist on the review card """
    """ if the reviewer and star rating exist, you found the review you are searching for"""
    """
    def search_review(self, stars, review, reviewer):

        review_list = self.driver.find_elements(By.XPATH, '//h5[contains(text(),"'+review+'")]/parent::div')

        for webelement in review_list:
            
            reviewer_webelement = webelement.find_element(By.XPATH, '//h6[contains(text(),"'+reviewer+'")]')
            
            data_rating_web_element = webelement.find_element(By.XPATH, '//p[contains(text(),"Rated: '+stars+' stars")]')
            

            if (data_rating_web_element.text == "Rated: "+stars+" stars") and (reviewer_webelement.text == "By: "+reviewer):
                
                print("the text matched")

                return True
            
            else:

                continue

        return False
    """


    """delete a reveiw from a campground"""
    """
    def delete_campground(self, campground_name):
        
        "locate the button where you can view that campsite's subpage"
        self.do_click_and_verify, '//a[contains(text(),"View '+campground_name+'")]'), "view_campground")

        "click the edit button"
        self.do_click_and_verify(self.EDIT_ATAG[0], self.EDIT_ATAG[1])


        "click the delete button"
        self.do_click_and_verify(self.DELETE_CAMPGROUND_BUTTON[0], self.DELETE_CAMPGROUND_BUTTON[1])


        return self.driver
    """




    
    """ verify that the campground was added by checking the add new campground success div element is now visible """
    """
    def verify_add_campground(self):


        return self.is_element_visible(self.ADD_NEW_CAMPGROUND_SUCCESS_DIV[0], self.ADD_NEW_CAMPGROUND_SUCCESS_DIV[1])
        
    """




    """ verify that the welcome back alert div is visible """
    """
    def is_welcome_back_alert_div_visible(self):


        return self.is_element_visible(self.WELCOME_BACK_ALERT_DIV[0], self.WELCOME_BACK_ALERT_DIV[1])
        
    """


    """ add campground to account"""
    """ adjust add campground to include inputs for campground information """
    """
    def add_campground(self, name, location, image, price, description):
        

        
        self.do_send_keys_and_verify(self.CAMPGROUND_NAME_INPUT[0],self.CAMPGROUND_NAME_INPUT[1], name)


        
        self.do_send_keys_and_verify(self.CAMPGROUND_LOCATION_INPUT[0], self.CAMPGROUND_LOCATION_INPUT[1], location)



        self.do_send_keys_and_verify(self.CHOOSE_FILES_BUTTON[0], self.CHOOSE_FILES_BUTTON[1], image)


        
        self.do_send_keys_and_verify(self.CAMPGROUND_PRICE[0], self.CAMPGROUND_PRICE[1], price)


        
        self.do_send_keys_and_verify(self.CAMPGROUND_DESCRIPTION[0], self.CAMPGROUND_DESCRIPTION[1], description)


        
        self.do_click_and_verify(self.SUBMIT_NEW_CAMPGROUND_BUTTON[0], self.SUBMIT_NEW_CAMPGROUND_BUTTON[1])


        # return the new state of the campgrounds page since it has transisitioned after the submit button
        return self.driver
    """
    
