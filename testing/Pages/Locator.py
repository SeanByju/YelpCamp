""" this is the page where all of the elmeents that you will be able to find on any page in the yelpCamp webapp will be located """
from Config.config import Config


class Locator:

    """ Base Page """
    NAV_HOME_ATAG = '//a[text()="Home"]'
    NAV_CAMPGROUNDS_ATAG = '//nav//a[text()="Campgrounds"]'
    NAV_NEW_CAMPGROUNDS_ATAG = '//nav//a[text()="New Campground"]'
    NAV_LOGIN_ATAG = '//nav//a[text()="Login"]'
    NAV_LOGOUT_ATAG = '//nav//a[text()="Logout"]'
    NAV_REGISTER_ATAG = '//nav//a[text()="Register"]'

    
    """ Home Page  """
    VIEW_CAMPGROUNDS_BUTTON =  '//a[contains(text(),"View Campgrounds")]'


    """ Login Page """
    LOGIN_USERNAME_INPUT = '//input[@id="username"]'
    LOGIN_PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//button[text()="Login"]' 
    MUST_BE_SIGNED_IN_ALERT_DIV = '//div[contains(text(),"you must be signed in")]'

    
    """ Campgrounds Page """
    WELCOME_BACK_ALERT_DIV = '//div[contains(text(),"Welcome back!")]'
    GOODBYE_ALERT_DIV = '//div[contains(text(),"GOOD BYE!!")]'
    MAP_CANVAS = '//canvas[@class="mapboxgl-canvas"]'
    ONE_STAR_RATE_LABEL ='//label[@for="first-rate1"]'
    TWO_STAR_RATE_LABEL ='//label[@for="first-rate2"]'
    THREE_STAR_RATE_LABEL ='//label[@for="first-rate3"]'
    FOUR_STAR_RATE_LABEL ='//labe[@for="first-rate4"]'
    FIVE_STAR_RATE_LABEL ='//label[@for="first-rate5"]'
    DESCRIPTION_TEXTAREA = '//textarea[@id="body"]'
    SUBMIT_REVIEW_BUTTON = '//button[text()="Submit"]'
    LEAVE_A_REVIEW_HEADER = '//h2[contains(text(),"Leave a Review")]'
    EDIT_ATAG = '//a[contains(text(),"Edit")]'
    DELETE_CAMPGROUND_BUTTON ='//button[text()="Delete Campground"]'
    VIEW_FIRST_CAMPGROUND_BUTTON = '//a[contains(text(),"View My First Camp")]'
    USERNAME_REVIEW_SEARCH ='//div[contains(text(),"'+Config.USERNAME+'")]'
    REVIEW_IS_NOT_DEFINED_TAG = '//h4[contains(text(),"Review is not defined")]'
    DELETE_CAMPGROUND_SUCCESS_DIV = '//div[contains(text(),"Successfully deleted campground!")]'
    ADD_NEW_CAMPGROUND_SUCCESS_DIV = '//div[contains(text(),"Successfully made a new campground!")]'
    CAMPGROUND_NAME_INPUT = '//input[@id="title"]'
    CAMPGROUND_LOCATION_INPUT = '//input[@id="location"]'
    CHOOSE_FILES_BUTTON = '//input[@id="image"]'
    CAMPGROUND_PRICE = '//input[@id="price"]'
    CAMPGROUND_DESCRIPTION = '//textarea[@id="description"]'
    SUBMIT_NEW_CAMPGROUND_BUTTON = '//button[contains(text(),"Submit")]'
    CANCEL_ATAG ='//a[text()="Cancel"]'

    def makeUsernameReviewSearch(self, username):

        return '//div[contains(text(),"'+username+'")]'



    """ Register Page """
    REGISTER_USERNAME_INPUT = '//input[@id="username"]'
    REGISTER_PASSWORD_INPUT = '//input[@id="password"]'
    REGISTER_EMAIL_INPUT = '//input[@id="email"]'
    REGISTER_BUTTON = '//button[text()="Register"]'
