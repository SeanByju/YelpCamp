#

from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime



class testYelpCamp():

    def setup(self,app,driverPath):
        self.driver = "" 
        if app == "Chrome":
            self.driver = webdriver.Chrome(driverPath)
        elif app == "Firefox":
            self.driver = webdriver.Firefox(driverPath)
        elif app== "Edge":
            self.driver = webdriver.Edge(driverPath)
        
        self.driver.get("https://morning-savannah-46253.herokuapp.com/")

    def teardown(self):
        if self.driver:
            self.driver.quit()

    # web elements (move to web element file later)

    
    

