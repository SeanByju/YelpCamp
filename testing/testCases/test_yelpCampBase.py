""" This is the where your test setup and repeatable test functions that are usable by all test cases reside """

""" ************ IMPORTANT *****************"""
""" SELENIUM EXECUTES FUNCTIONS IN THE TEST CLASS IN ALPHABETICAL ORDER, NOT BY THE ORDER OF HOW YOU WRITE THE SCRIPTS"""

import pytest
import time
import allure
from Config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from datetime import datetime as dt
from TestCases.conftest import setup

@pytest.mark.usefixtures("setup")
class yelpCampBaseTest:
    
    
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
    def do_click_and_report(self, by_locator, element_name):

        # move to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)))

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
    def do_send_keys_and_report(self, by_locator, element_name,  text):
        
        # move to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)))

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

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

        # move to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        
        return element.text

    # verify is a webelement is visible
    def is_element_visible(self, by_locator, element_name):

        # move to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)))

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

