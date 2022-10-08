
class Config:

    CHROME_DRIVER_EXECUTABLE_PATH = "Drivers/chromedriver.exe"
    FIREFOX_DRIVER_EXECUTABLE_PATH = "Drivers/geckodriver.exe"
    EDGE_DRIVER_EXECUTABLE_PATH = "Drivers/msedgedriver.exe"

    """ login page inputs """
    BASE_URL = "https://morning-savannah-46253.herokuapp.com"
    USERNAME = "testmatthewanderson"
    PASSWORD = "testmatthewanderson"

    """ new campground inputs """
    CAMPGROUND_NAME = "Redwoods Site"
    CAMPGROUND_LOCATION = "San Francisco, CA"
    UPLOAD_IMAGE = ""
    CAMPGROUND_PRICE = "100"
    CAMPGROUND_DESCRIPTION = " test description"


    global_strftime = "%d-%m-%Y_%H-%M-%S"
    screenshot_path = "Reports/screenshots/"


    