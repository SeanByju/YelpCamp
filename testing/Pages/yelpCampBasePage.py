# 

from curses import echo
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located())
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 5).until(EC.title_is(title))
        return self.driver.title
