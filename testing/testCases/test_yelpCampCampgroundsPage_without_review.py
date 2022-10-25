""" test yelpCamp camporgrounds page functions"""
"""
1. Open up the yelpCamp webpage on the home page

2. Navigate to the login page

3. Login

4. Check for the welcome back alert div to verify that you logged in

5. Navigate to New Campgrounds Page

6. Add a new campground

7. verify that you added the campground 

8. Verify that you deleted the campground

9. Navigate back to the campgrounds page and logout


"""


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.yelpCampBasePage import yelpCampBasePage
from Pages.yelpCampLoginPage import yelpCampLoginPage
from Pages.yelpCampCampgroundsPage import yelpCampCampgroundsPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
# note: even though init driver is called only as a fixture, it still needs to be imported
# from Scripts.conftest import init_driver
from Config.config import Config


# add the init_driver fixture so you can add your set up and teardown functions
# @pytest.mark.usefixtures("init_driver")
class Test_yelpCampCampgroundsPageWithoutReview(yelpCampBaseTest):


    def test_yelpCampCampgroundsPageWithoutReview(self):
        
        basePage = yelpCampBasePage()
        

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(basePage.NAV_LOGIN_ATAG)).click()

        # self.do_click_and_verify(basePage.NAV_LOGIN_ATAG[0],basePage.NAV_LOGIN_ATAG[1])


        """ 3. Verify that you successfully logged in by verifying that the welcome back div is visible on the campgrounds page. you need to initilaize a campgrounds page object to accomplish this"""
        
                
        loginPage = yelpCampLoginPage()



        try:
            
            if EC.visibility_of_element_located(loginPage.LOGIN_BUTTON):
            
                print("You successfully navigated to the login page!")
        
        except Exception as error:
            
            print(error+" You failed to login.")

        """ 4. Enter your Login credentials and submit """
        
        
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loginPage.USERNAME_INPUT)).send_keys(Config.USERNAME)
        
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loginPage.PASSWORD_INPUT)).send_keys(Config.PASSWORD)
       
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loginPage.LOGIN_BUTTON)).click()
        

        
        
        # self.yelpCampCampgroundsPage = yelpCampCampgroundsPage(self.yelpCampLoginPage.do_login(Config.USERNAME, Config.PASSWORD))

        
        campgroundsPage = yelpCampCampgroundsPage()
        
        try:
            
            if EC.visibility_of_element_located(campgroundsPage.WELCOME_BACK_ALERT_DIV):
            
                print("You successfully logged in!")
        
        except Exception as error:
            
            print(str(error)+" You failed to login.")
            
            
        # navigate to the new campgrounds page
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.NAV_NEW_CAMPGROUNDS_ATAG)).click()
        
        # 6. add new campground
        
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.CAMPGROUND_NAME_INPUT)).send_keys(Config.CAMPGROUND_NAME)
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.CAMPGROUND_LOCATION_INPUT)).send_keys(Config.CAMPGROUND_LOCATION)
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.CHOOSE_FILES_BUTTON)).send_keys(Config.UPLOAD_IMAGE)
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.CAMPGROUND_PRICE)).send_keys(Config.CAMPGROUND_PRICE)
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.CAMPGROUND_DESCRIPTION)).send_keys(Config.CAMPGROUND_DESCRIPTION)
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.SUBMIT_NEW_CAMPGROUND_BUTTON)).click()


        # 7. Remove the campground
        
        # navigate back to the campgrounds page
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.NAV_CAMPGROUNDS_ATAG)).click()
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"View '+Config.CAMPGROUND_NAME+'")]'))).click()
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.EDIT_ATAG)).click()
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.DELETE_CAMPGROUND_BUTTON)).click()
        
        # 8. verify that the campground was deleted by seeing if the delete campground succes div is visible
        
        
        try:
            
            if EC.visibility_of_element_located(campgroundsPage.DELETE_CAMPGROUND_SUCCESS_DIV):
                
                print("You successfully deleted the campground!")
            
        except Exception as error:
            
            print(str(error)+" You failed to delete the campground.")
        
        
        
        # 9. Navigate back to the campground page and log out
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.NAV_CAMPGROUNDS_ATAG)).click()
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.NAV_LOGOUT_ATAG)).click()
        
        try:
            
            if EC.visibility_of_element_located(campgroundsPage.GOODBYE_ALERT_DIV):
                
                print("You successfully logged out!")
            
        except Exception as error:
            
            print(str(error)+" You failed to logout.")
        
        
    