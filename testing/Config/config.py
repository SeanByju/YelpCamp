
class Config:

    """ options for browser include chrome, firefox, and edge"""
    browser = "firefox"

    "set the format for the screenshot that will be taken during the automation"
    global_strftime = "%d-%m-%Y_%H-%M-%S"

    """ login page inputs """
    BASE_URL = "https://morning-savannah-46253.herokuapp.com"
    USERNAME = "testmatthewanderson"
    PASSWORD = "testmatthewanderson"

    """ new campground inputs """
    CAMPGROUND_NAME = "Redwoods Site"
    CAMPGROUND_LOCATION = "San Francisco, CA"
    UPLOAD_IMAGE = "C:\\Users\\Owner\\Documents\\Programming\\YelpCamp\\testing\\Resources\Images\\redwood-forrest-1.jpg"
    CAMPGROUND_PRICE = "100"
    CAMPGROUND_DESCRIPTION = "test description"

    """ campgrounds review """
    REVIEW_DESCRIPTION = "test"
    REVIEW_STAR_RATING = "5"

