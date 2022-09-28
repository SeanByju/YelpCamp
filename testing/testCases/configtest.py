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

"""
@pytest.fixture(params=["chrome","firefox","edge"],scope="class")
"""

@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path = Config.CHROME_DRIVER_EXECUTABLE_PATH)
    """
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path = Config.FIREFOX_DRIVER_EXECUTABLE_PATH)
    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path = Config.EDGE_DRIVER_EXECUTABLE_PATH)
    """
    request.cls.driver = web_driver
    
    web_driver.implicitly_wait(10)
    
    yield
    
    web_driver.close()
