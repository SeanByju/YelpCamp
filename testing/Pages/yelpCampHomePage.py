# class file will store all the locator and methos of the home page

from selenium import By

from Pages.yelpCampBasePage import yelpCampBasePage

class yelpCampHomePage(yelpCampBasePage):

    def get_home_nav_button(self):

        driver.find_element(By.XPATH,'//a[text()="Home"]')

    def get_campgrounds_nav_button(self):

        driver.find_element(By.XPATH,'//a[text()="Campgrounds"]')

    def get_login_nav_button(self):

        driver.find_element(By.XPATH,'//a[text()="Login"]')

    def get_register_button(self):

        driver.find_element(By.XPATH,'//a[text()="Register"]')

