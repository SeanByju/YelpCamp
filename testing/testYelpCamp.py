#

from selenium import webdriver


class testYelpCamp():

    def __init__(self,app,driverPath):
        driver = "" 
        if app == "Chrome":
            driver = webdriver.Chrome(driverPath)
        elif app == "Firefox":
            driver = webdriver.Firefox(driverPath)
        elif app== "Edge":
            driver = webdriver.Edge(driverPath)

