from logging import config
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.config import Config
import time

subpage = "login"
getBrowser = "chrome"

@pytest.fixture(scope="class")
def init_driver(request):
    
    """
    if getBrowser == "chrome":
    """
    _driver = webdriver.Chrome(Config.CHROME_DRIVER_EXECUTABLE_PATH)
        # pass
    """
    if getBrowser == "firefox":
        # web_driver = webdriver.Firefox(Config.FIREFOX_DRIVER_EXECUTABLE_PATH)
        pass
    if getBrowser == "edge":
        #_driver = webdriver.Edge(Config.EDGE_DRIVER_EXECUTABLE_PATH)
        pass
    """

    _driver.get("https://morning-savannah-46253.herokuapp.com/"+subpage)

    _driver.implicitly_wait(60)

    request.cls.driver = _driver
  
    yield request.cls.driver

    time.sleep(2)

    request.cls.driver.quit()


"""
@pytest.fixture(params=["chrome","firefox","edge"],scope="class")
"""

"""
@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request="chrome"):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path = Config.CHROME_DRIVER_EXECUTABLE_PATH)
    
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path = Config.FIREFOX_DRIVER_EXECUTABLE_PATH)
    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path = Config.EDGE_DRIVER_EXECUTABLE_PATH)
    
    request.cls.driver = web_driver
    
    web_driver.implicitly_wait(10)
    
    yield
    
    web_driver.close()
"""


