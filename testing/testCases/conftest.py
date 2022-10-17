

import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.config import Config
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from datetime import datetime as dt


"adjust the subpage to determine the url you are going to start your automation on"
subpage = ""
""" browser options include chrome, firefox, and edge"""
getBrowser = Config.browser


@pytest.fixture(scope="class")
def init_driver(request):

    print("------------------------------setup-------------------------------")
    
    
    if getBrowser == "chrome":
        _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif getBrowser == "firefox":
        _driver = webdriver.Firefox(service= Service(GeckoDriverManager().install()))
        
    elif getBrowser == "edge":
        _driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        


    _driver.get("https://morning-savannah-46253.herokuapp.com/"+subpage)

    _driver.implicitly_wait(60)

    _driver.delete_all_cookies()

    time_now = dt.now().strftime(Config.global_strftime)
    
    allure.attach(_driver.get_screenshot_as_png(), name="init_driver_"+time_now+".png", attachment_type=allure.attachment_type.PNG)

    request.cls.driver = _driver
  
    yield request.cls.driver

    time.sleep(2)

    
    print("-----------------------------teardown-----------------------------")

    request.cls.driver.close()

    request.cls.driver.quit()

