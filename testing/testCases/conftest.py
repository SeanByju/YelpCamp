

import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.config import Config
import time
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from datetime import datetime as dt


"adjust the subpage to determine the url you are going to start your automation on"
subpage = ""
""" browser options include chrome, firefox, and edge"""
getBrowser = Config.browser

@pytest.fixture(params=["chrome","firefox","edge"],scope="class")
def setup(request):

    # setup procedure
    
    print("------------------------------setup-------------------------------")
    
    urllib3.disable_warnings(InsecureRequestWarning)

    if request.param == "chrome":
        _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif request.param == "firefox":
        _driver = webdriver.Firefox(service= Service(GeckoDriverManager().install()))
        
    elif request.param == "edge":
        _driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    
    _driver.get(Config.BASE_URL+subpage)

    _driver.set_page_load_timeout(30)

    _driver.delete_all_cookies()
    
    _driver.maximize_window()

    time_now = dt.now().strftime(Config.global_strftime)

    allure.attach(_driver.get_screenshot_as_png(), name="init_driver_"+time_now+".png", attachment_type=allure.attachment_type.PNG)
  
    request.cls.driver = _driver      
  
    yield _driver

    # teardown procedure
    
    time.sleep(2)

    if (_driver != None):
        print("------------------------------teardown-------------------------------")
        _driver.close()
        _driver.quit()

    
