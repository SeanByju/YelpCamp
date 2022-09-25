# base page object will hold all of the elements that are shared on all of the pages in
# yelpCamp 


from faulthandler import is_enabled
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class yelpCampBasePage:

    
    def __init__(self, driver):
        
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(by_locator).click())
    
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_loactor):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_loactor))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 5).until(EC.title_is(title))
        return self.driver.title



    def get_home_nav_button(self):

        self.is_enabled((By.XPATH, '//nav//a[text()="Home"]'))

    def get_campgrounds_nav_button(self):

        self.is_enabled(By.XPATH,'//nav//a[text()="Campgrounds"]')

    def get_login_nav_button(self):

        self.is_enabled(By.XPATH,'//nav//a[text()="Login"]')

    def get_register_button(self):

        self.is_enabled(By.XPATH,'//nav//a[text()="Register"]')
    
    
    def is_register_button_visible(self):
        
        return is_enabled((By.XPATH,'//nav//a[text()="Register"]'))