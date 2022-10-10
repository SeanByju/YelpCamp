"""yelpCamp page object holds all of the web elements and actions that can be used on all yelpcamp pages"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    HOME_NAV_BUTTON = ((By.XPATH, '//nav//a[text()="Home"]'), "home_nav_button")
    CAMPGROUNDS_NAV_BUTTON = ((By.XPATH,'//nav//a[text()="Campgrounds"]'), "campgrounds_nav_button")
    NEW_CAMPGROUNDS_BUTTON = ((By.XPATH, '//nav//a[text()='), "new_campground_nav_button")
    LOGIN_NAV_BUTTON = ((By.XPATH,'/nav/a[text()="Login"]'), "login_nav_button")
    LOGOUT_BUTTON = ((By.XPATH, '//a[contains(text(),\"Logout")]'),"logout_button")
    REGISTER_BUTTON = ((By.XPATH, '//button[text()="Register"]'))


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
        time_now = dt.now().strftime(Config.global_strftime)
        before_screenshot = self.driver.save_screenshot(Config.screenshot_path+element_name+"_before_"+time_now+".png")
        print(before_screenshot)
        self.do_click(by_locator)
        time.sleep(10)
        time_now = dt.now().strftime(Config.global_strftime)
        after_screenshot = self.driver.save_screenshot(Config.screenshot_path+element_name+"_after_"+time_now+".png")
        print(after_screenshot)
        
    # send keys to web elements
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # send keys to web elements and take screenshots before and after the action is taken
    def do_send_keys_and_verify(self, by_locator, element_name,  text):
        time_now = dt.now().strftime(Config.global_strftime)
        before_screenshot =self.driver.save_screenshot(Config.screenshot_path+element_name+"_before_"+time_now+".png")
        print(before_screenshot)
        self.do_send_keys(by_locator, text)
        time.sleep(10)
        time_now = dt.now().strftime(Config.global_strftime)
        after_screenshot = self.driver.save_screenshot(Config.screenshot_path+element_name+"_after_"+time_now+".png")
        print(after_screenshot)
        
    # get the text of a web element
    def get_element_text(self, by_loactor):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_loactor))
        return element.text

    # verify is a webelement is visible
    def is_element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    """ see if base page elements are enabled """

    # verify whether you can see the campgrounds nav button
    def is_campgrounds_nav_button(self):

        return bool(self.is_element_enabled())

    # verify whether the login nav button is visible
    def is_login_nav_button_enabled(self):

        element =  self.is_element_enabled((By.LINK_TEXT,"Login"))
        return bool(element)

    # verify whether the logout out nav button is visible
    def is_logout_nav_button_enabled(self):

        element =  self.is_element_enabled((By.LINK_TEXT,"Logout"))
        return bool(element)
    
    # return the home nav button web element
    def get_home_nav_button(self):

        return self.is_element_enabled(self.HOME_NAV_BUTTON[0])

    # return the login nav button web element
    def get_login_nav_button(self):

        return self.is_element_enabled()
        
    # return the register button web element
    def get_register_button(self):

        return self.is_element_enabled((By.XPATH,'//nav//a[text()="Register"]'))

    # nav to the login page by clicking the login nav button, it's possible to also set_curr_url to login page
    def nav_to_login(self):

        self.do_click_and_verify(self.LOGIN_NAV_BUTTON[0], self.LOGIN_NAV_BUTTON[1])


    # use this function to logout of your yelp camp account
    def do_logout(self):

        self.do_click_and_verify(self.LOGOUT_BUTTON[0], self.LOGOUT_BUTTON[1])

    # return the 
    def click_new_campgrounds_atag(self):

        return self.do_click_and_verify(self.NEW_CAMPGROUNDS_BUTTON[0], self.NEW_CAMPGROUNDS_BUTTON[1])

    

