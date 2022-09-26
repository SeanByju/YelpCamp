import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.config import Config

"""
@pytest.fixture(params=["chrome","firefox","edge"],scope="class")
def init_driver(request):
    if request == "chrome":
        web_driver = webdriver.Chrome(Config.CHROME_DRIVER_EXECUTABLE_PATH)
    if request == "firefox":
        web_driver = webdriver.Firefox(Config.FIREFOX_DRIVER_EXECUTABLE_PATH)
    if request == "edge":
        web_driver = webdriver.Edge(Config.EDGE_DRIVER_EXECUTABLE_PATH)
    
    request.cls.driver = web_driver
    
    web_driver.implicitly_wait(5)

    return web_driver
    
    yield
    web_driver.close()
"""

def init_driver(request="chrome"):
    if request == "chrome":
        web_driver = webdriver.Chrome(Config().CHROME_DRIVER_EXECUTABLE_PATH)
    if request == "firefox":
        web_driver = webdriver.Firefox(Config().FIREFOX_DRIVER_EXECUTABLE_PATH)
    if request == "edge":
        web_driver = webdriver.Edge(Config().EDGE_DRIVER_EXECUTABLE_PATH)
    
    web_driver.implicitly_wait(5)

    return web_driver

