
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(GeckoDriverManager().install())
    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    