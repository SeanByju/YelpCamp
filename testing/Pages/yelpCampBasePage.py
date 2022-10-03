from turtle import clear
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


"""This is the parent of all pages"""
"""It contains all of the generic methods and utiilties for all pages"""


class yelpCampBasePage:

    def __init__(self,driver):

        self.driver = driver


    def do_click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()
    
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_loactor):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_loactor))
        return element.text

    def is_element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)




    def get_home_nav_button(self):

        self.is_element_enabled((By.XPATH, '//nav//a[text()="Home"]'))

    def get_campgrounds_nav_button(self):

        self.is_element_enabled(By.XPATH,'//nav//a[text()="Campgrounds"]')

    def get_login_nav_button(self):

        self.is_element_enabled(By.XPATH,'//nav//a[text()="Login"]')

    def get_register_button(self):

        self.is_element_enabled(By.XPATH,'//nav//a[text()="Register"]')
    
    
    