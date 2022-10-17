"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
import allure
from datetime import datetime as dt
import time

from Config.config import Config


"""This is the parent of all pages"""
"""It contains all of the generic methods and utiilties for all pages"""


class yelpCampBasePage:

    def __init__(self,driver):

        self.driver = driver
        """
        time_now = dt.now().strftime(Config.global_strftime)
        time.sleep(10)
        driver.get_screenshot_as_file("init_driver_"+time_now+".png")
        """

    """ Base Web elements"""
    NAV_HOME_ATAG = ((By.XPATH, '//a[text()="Home"]'), "nav_home_atag")
    NAV_CAMPGROUNDS_ATAG = ((By.XPATH,'//nav//a[text()="Campgrounds"]'), "nav_campgrounds_atag")
    NAV_NEW_CAMPGROUNDS_ATAG = ((By.XPATH, '//nav//a[text()="New Campground"]'), "nav_new_campground_atag")
    NAV_LOGIN_ATAG = ((By.XPATH,'//nav//a[text()="Login"]'), "nav_login_atag")
    NAV_LOGOUT_ATAG = ((By.XPATH, '//nav//a[text()="Logout"]'),"nav_logout_atag")
    NAV_REGISTER_ATAG = ((By.XPATH, '//nav//a[text()="Register"]'),"nav_register_atag")


    """ Base Page Actions"""


    # get current url
    def get_curr_url(self):

        return self.driver.current_url


    # set current url
    def set_curr_url(self,url):

        self.driver.get(url)


    # click web elements
    def do_click(self, by_locator):

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()
    

    # click web elements and take screenshots before and after so you can visually verify what actions occured
    def do_click_and_verify(self, by_locator, element_name):

        # initialize action chains object
        actions = AC(self.driver)        

        # move to the element
        actions.move_to_element(WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)))

        # get the timestamp before clicking your web element
        time_now = dt.now().strftime(Config.global_strftime)
        
        # attach a screenshot of the state of the webpage before clicking the intended web element
        allure.attach(self.driver.get_screenshot_as_png(), name = time_now+"_before_click_"+element_name+"_"+Config.browser+".png", attachment_type=allure.attachment_type.PNG)

        # do the click action
        self.do_click(by_locator)

        # wait for the webpage to adjust after clicking your input web element
        time.sleep(10)

        # get the timestamp after waiting for the webpage to adjust after clicking your web element
        time_now = dt.now().strftime(Config.global_strftime)

        # attach a screenshot of the state of the webpage after clicking the intended web element
        allure.attach(self.driver.get_screenshot_as_png(), name= time_now+"_after_click_"+element_name+"_"+Config.browser+".png", attachment_type=allure.attachment_type.PNG)
        
        
    # send keys to web elements
    def do_send_keys(self, by_locator, text):

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # send keys to web elements and take screenshots before and after the action is taken
    def do_send_keys_and_verify(self, by_locator, element_name,  text):
        
        # initialize action chains object
        actions = AC(self.driver)        

        # move to the element
        actions.move_to_element(WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)))

        # get the current time to accurately log the screenshot
        time_now = dt.now().strftime(Config.global_strftime)
        
        # attach a screenshot of the state of the webpage before clicking the intended web element
        allure.attach(self.driver.get_screenshot_as_png(), name = time_now+"_before_send_keys_"+element_name+"_"+Config.browser+".png", attachment_type=allure.attachment_type.PNG)
        
        # do the send keys action
        self.do_send_keys(by_locator, text)

        # wait for the webpage to adjust after clicking your input web element
        time.sleep(10)

        # get the timestamp after waiting for the webpage to adjust after clicking your web element
        time_now = dt.now().strftime(Config.global_strftime)

        # attach a screenshot of the state of the webpage after clicking the intended web element
        allure.attach(self.driver.get_screenshot_as_png(), name= time_now+"_after_send_keys_"+element_name+"_"+Config.browser+".png", attachment_type=allure.attachment_type.PNG)
        
    # get the text of a web element
    def get_element_text(self, by_locator):
        
        # initialize action chains object
        actions = AC(self.driver)        

        # move to the element
        actions.move_to_element(by_locator)

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        
        return element.text

    # verify is a webelement is visible
    def is_element_visible(self, by_locator, element_name):

        # initialize action chains object
        actions = AC(self.driver)        

        # move to the element
        actions.move_to_element(WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)))

        # get the current time to accurately log the screenshot
        time_now = dt.now().strftime(Config.global_strftime)
        
        # attach a screenshot of the state of the webpage before clicking the intended web element
        allure.attach(self.driver.get_screenshot_as_png(), name = time_now+"_before_check_visible_"+element_name+"_"+Config.browser+".png", attachment_type=allure.attachment_type.PNG)

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

        # get the timestamp after waiting for the webpage to adjust after clicking your web element
        time_now = dt.now().strftime(Config.global_strftime)

        # attach a screenshot of the state of the webpage after clicking the intended web element
        allure.attach(self.driver.get_screenshot_as_png(), name= time_now+"_after_check_visible_"+element_name+"_"+Config.browser+".png", attachment_type=allure.attachment_type.PNG)

        # return the boolean of whether the element is visible
        return bool(element)


    """ see if base page elements are enabled """


    # verify whether the login nav button is visible
    def is_login_nav_button_enabled(self):

        return self.is_element_visible(self.NAV_LOGIN_ATAG[0], self.NAV_LOGIN_ATAG[1])
        

    # verify whether the logout out nav button is visible
    def is_logout_nav_button_enabled(self):

        return self.is_element_visible(self.NAV_LOGOUT_ATAG[0], self.NAV_LOGOUT_ATAG[1])
        

    # use this function to logout of your yelp camp account
    def do_logout(self):

        self.do_click_and_verify(self.NAV_LOGOUT_ATAG[0], self.NAV_LOGOUT_ATAG[1])


    # navigate to the yelpCamp base page (also calle d the home page on the website)
    def nav_to_base_page(self):

        self.do_click_and_verify(self.NAV_HOME_ATAG[0], self.NAV_HOME_ATAG[1])

   
    # nav to the login page by clicking the login nav button, it's possible to also set_curr_url to login page
    def nav_to_login_page(self):
        
        self.do_click_and_verify(self.NAV_LOGIN_ATAG[0], self.NAV_LOGIN_ATAG[1])


    # nav to the yelCamp campgrounds page
    def nav_to_campgrounds_page(self):
        
        self.do_click_and_verify(self.NAV_CAMPGROUNDS_ATAG[0], self.NAV_CAMPGROUNDS_ATAG[1])


    # nav to the yelpCamp new campgrounds page
    def nav_to_new_campgrounds_page(self):

        self.do_click_and_verify(self.NAV_NEW_CAMPGROUNDS_ATAG[0],self.NAV_NEW_CAMPGROUNDS_ATAG[1])


    # nav to the yelpCamp register page
    def nav_to_register_page(self):

        self.do_click_and_verify(self.NAV_REGISTER_ATAG[0], self.NAV_REGISTER_ATAG[1])

