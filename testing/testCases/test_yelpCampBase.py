""" This is the where your test setup and repeatable test functions that are usable by all test cases reside """

""" ************ IMPORTANT *****************"""
""" SELENIUM EXECUTES FUNCTIONS IN THE TEST CLASS IN ALPHABETICAL ORDER, NOT BY THE ORDER OF HOW YOU WRITE THE SCRIPTS"""

from lib2to3.pgen2 import driver
import pytest
import time
import allure
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from datetime import datetime as dt
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampHomePage import yelpCampHomePage
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from Pages.yelpCampRegisterPage import yelpCampRegisterPage
from conftest import setup



@pytest.mark.usefixtures("setup")
class yelpCampBaseTest:
    
    
    """    
    def setUp(self):

        print("------------------------------setup-------------------------------")
        
        urllib3.disable_warnings(InsecureRequestWarning)

        if getBrowser == "chrome":
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        elif getBrowser == "firefox":
            self.driver = webdriver.Firefox(service= Service(GeckoDriverManager().install()))
            
        elif getBrowser == "edge":
            self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

        # declare all page object in basetest file


        self.driver.get(Config.BASE_URL+subpage)

        self.driver.set_page_load_timeout(30)

        self.driver.delete_all_cookies()
        
        self.driver.maximize_window()

        time_now = dt.now().strftime(Config.global_strftime)
    
        allure.attach(self.driver.get_screenshot_as_png(), name="init_driver_"+time_now+".png", attachment_type=allure.attachment_type.PNG)
 
    def tearDown(self):

        time.sleep(2)

        if (self.driver != None):
            print("------------------------------teardown-------------------------------")
            self.driver.close()
            self.driver.quit()
    """

    
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
    def do_send_keys_and_verify(self, by_locator, element_name,  text):
        
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

