"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""


from selenium.webdriver.common.by import By
from datetime import datetime as dt
from Config.config import Config
from Pages.Locator import Locator


"""This is the parent of all pages"""
"""It contains all of the generic methods and utiilties for all pages"""


class yelpCampBasePage:


    """ Base Web elements"""
    NAV_HOME_ATAG = (By.XPATH, Locator.NAV_HOME_ATAG)
    NAV_CAMPGROUNDS_ATAG = (By.XPATH, Locator.NAV_CAMPGROUNDS_ATAG)
    NAV_NEW_CAMPGROUNDS_ATAG = (By.XPATH, Locator.NAV_NEW_CAMPGROUNDS_ATAG)
    NAV_LOGIN_ATAG = (By.XPATH, Locator.NAV_LOGIN_ATAG)
    NAV_LOGOUT_ATAG = (By.XPATH, Locator.NAV_LOGOUT_ATAG)
    NAV_REGISTER_ATAG = (By.XPATH, Locator.NAV_REGISTER_ATAG)
    NAV_HOME_ATAG_NAME = "nav_home_atag"
    NAV_CAMPGROUNDS_ATAG_NAME = "nav_campgrounds_atag"
    NAV_NEW_CAMPGROUNDS_ATAG_NAME = "nav_new_campground_atag"
    NAV_LOGIN_ATAG_NAME = "nav_login_atag"
    NAV_LOGOUT_ATAG_NAME = "nav_logout_atag"
    NAV_REGISTER_ATAG_NAME = "nav_register_atag"



    """ Base Page Actions"""

    def getNavHomeATag(self):

        return self.NAV_HOME_ATAG

    def getNavCampgroundsATag(self):

        return self.NAV_CAMPGROUNDS_ATAG
    
    def getNavLoginATag(self):

        return self.NAV_NEW_CAMPGROUNDS_ATAG

    def getNavLogoutATag(self):

        return self.NAV_LOGOUT_ATAG

    def getRegisterATag(self):

        return self.NAV_REGISTER_ATAG
    
    def getNavHomeATagName(self):

        return self.NAV_HOME_ATAG_NAME

    def getNavCampgroundsATagName(self):

        return self.NAV_CAMPGROUNDS_ATAG_NAME
    
    def getNavLoginATagName(self):

        return self.NAV_NEW_CAMPGROUNDS_ATAG_NAME

    def getNavLogoutATagName(self):

        return self.NAV_LOGOUT_ATAG_NAME

    def getRegisterATagName(self):

        return self.NAV_REGISTER_ATAG_NAME




    """ see if base page elements are enabled """


    # verify whether the login nav button is visible
    def is_login_nav_button_enabled(self):

        return self.is_element_visible(self.NAV_LOGIN_ATAG[0], self.NAV_LOGIN_ATAG[1])
        

    # verify whether the logout out nav button is visible
    def is_logout_nav_button_enabled(self):

        return self.is_element_visible(self.NAV_LOGOUT_ATAG[0], self.NAV_LOGOUT_ATAG[1])
        

    # use this function to logout of your yelp camp account
    def do_logout(self):

        self.do_click_and_report(self.NAV_LOGOUT_ATAG[0], self.NAV_LOGOUT_ATAG[1])

        # return the driver and initiate a campgrounds page object
        return self.driver


    # navigate to the yelpCamp base page (also calle d the home page on the website)
    def nav_to_home_page(self):

        self.do_click_and_report(self.NAV_HOME_ATAG[0], self.NAV_HOME_ATAG[1])

        # return the driver and initiatie a home page object 
        return self.driver

   
    # nav to the login page by clicking the login nav button, it's possible to also set_curr_url to login page
    def nav_to_login_page(self):
        
        self.do_click_and_report(self.NAV_LOGIN_ATAG[0], self.NAV_LOGIN_ATAG[1])

        # return the driver and initiate it into a login page object
        return self.driver



    # nav to the yelCamp campgrounds page
    def nav_to_campgrounds_page(self):
        
        self.do_click_and_report(self.NAV_CAMPGROUNDS_ATAG[0], self.NAV_CAMPGROUNDS_ATAG[1])

        # return the driver and initiate it into a campgrounds page object
        return self.driver



    # nav to the yelpCamp new campgrounds page
    def nav_to_new_campgrounds_page(self):

        self.do_click_and_report(self.NAV_NEW_CAMPGROUNDS_ATAG[0],self.NAV_NEW_CAMPGROUNDS_ATAG[1])

        # return the driver and initiate it into a new campgrounds object
        return self.driver



    # nav to the yelpCamp register page
    def nav_to_register_page(self):

        self.do_click_and_report(self.NAV_REGISTER_ATAG[0], self.NAV_REGISTER_ATAG[1])

        # return the driver and initiate it into a register page object
        return self.driver
