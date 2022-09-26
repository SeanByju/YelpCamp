# class file will store all the locator and methos of the home page

from selenium import By

from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampHomePage(yelpCampBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_nav_button(self):

        self.driver.find_element(By.XPATH,'//nav//a[text()="Home"]')

    def get_campgrounds_nav_button(self):

        self.driver.find_element(By.XPATH,'//nav//a[text()="Campgrounds"]')

    def get_login_nav_button(self):

        self.driver.find_element(By.XPATH,'//nav//a[text()="Login"]')

    def get_register_button(self):

        self.driver.find_element(By.XPATH,'//nav//a[text()="Register"]')


