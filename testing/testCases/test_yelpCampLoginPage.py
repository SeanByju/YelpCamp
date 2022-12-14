
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
from Config.config import Config

# adjust the subpage to determine the url you are going to start your automation on
subpage = ""
# browser options include chrome, firefox, and edge
getBrowser = Config.browser


class Test_yelpCampLoginPage(yelpCampBaseTest):

    # first test, login into your account and verify you logged in
    def test_yelpCampLoginPage(self):
        

        """
        Functionality of this test case:

        1. Open on https://morning-savannah-46253.herokuapp.com/

        2. Navigate to the Login Page

        3. Check that you are on the Login Page

        4. Enter your Login credentials and submit

        5. Verify that you have signed in by checking for the Welcome Back div
        
        """

        """ 1. fixture that calls setup function in conftest used by the basetest class initializes the driver """

        """ 2. Navigate to the login page, initialize the base page object and use the getter in the object to find the nav_to_login web element and click it with custom clicking function"""


        basePage = yelpCampBasePage()
        
                
        loginPage = yelpCampLoginPage()
        
        
        campgroundsPage = yelpCampCampgroundsPage()
        
        
        self.do_click_and_report(basePage.NAV_LOGIN_ATAG, basePage.NAV_LOGIN_ATAG_NAME)



        """ 3. Verify that you successfully logged in by verifying that the welcome back div is visible on the campgrounds page. you need to initilaize a campgrounds page object to accomplish this"""


        try:
            
            if EC.visibility_of_element_located(loginPage.LOGIN_BUTTON):
            
                print("You successfully navigated to the login page!")
        
        except Exception as error:
            
            print(error+" You failed to login.")

        """ 4. Enter your Login credentials and submit """
        
        
        self.do_send_keys_and_report(loginPage.USERNAME_INPUT, loginPage.USERNAME_INPUT_NAME, Config.USERNAME)
        
        
        
        self.do_send_keys_and_report(loginPage.PASSWORD_INPUT, loginPage.PASSWORD_INPUT_NAME, Config.PASSWORD)
        
       
        self.do_click_and_report(loginPage.LOGIN_BUTTON, loginPage.LOGIN_BUTTON_NAME)
        

        
        try:
            
            if WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.WELCOME_BACK_ALERT_DIV)):
            
                print("You successfully logged in!")
        
        except Exception as error:
            
            print(str(error)+" You failed to login.")


