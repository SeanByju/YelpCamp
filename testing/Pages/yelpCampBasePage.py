""""""
from selenium.webdriver import ActionChains
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
        time_now = dt.now().strftime(Config.global_strftime)
        driver.save_screenshot("init_driver_"+time_now+".png")

    """ Base Page Actions"""

    def do_click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()
    

    def do_click_and_verify(self, by_locator, element_name):
        time_now = dt.now().strftime(Config.global_strftime)
        self.driver.get_screenshot_as_file(element_name+"_before_"+time_now+".png")
        self.do_click(by_locator)
        time.sleep(10)
        time_now = dt.now().strftime(Config.global_strftime)
        self.driver.get_screenshot_as_file(element_name+"_after_"+time_now+".png")
        


    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def do_send_keys_and_verify(self, by_locator, element_name):
        time_now = dt.now().strftime(Config.global_strftime)
        self.driver.get_screenshot_as_file(element_name+"_before_"+time_now+".png")
        self.do_send_keys(by_locator)
        time.sleep(10)
        time_now = dt.now().strftime(Config.global_strftime)
        self.driver.get_screenshot_as_file(element_name+"_after_"+time_now+".png")
        

    def get_element_text(self, by_loactor):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_loactor))
        return element.text

    def is_element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    """ see if base page elements are enabled """
    def get_home_nav_button(self):

        return self.is_element_enabled((By.XPATH, '//nav//a[text()="Home"]'))

    def is_campgrounds_nav_button(self):

        return self.is_element_enabled((By.XPATH,'//nav//a[text()="Campgrounds"]'))

    def get_login_nav_button(self):

        return self.is_element_enabled((By.XPATH,'/nav/a[text()="Login"]'))
        

    def get_register_button(self):

        return self.is_element_enabled((By.XPATH,'//nav//a[text()="Register"]'))
    

    def is_login_nav_button_enabled(self):

        element =  self.is_element_enabled((By.LINK_TEXT,"Login"))
        return bool(element)

    def is_logout_nav_button_enabled(self):

        element =  self.is_element_enabled((By.LINK_TEXT,"Logout"))
        return bool(element)
    