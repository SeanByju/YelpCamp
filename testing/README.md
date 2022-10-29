# Yelp Camp Automation

This subfolder project allows you to use the selenium webriver and Python programming language to run tests automatically for the purpose of improving the Yelp Camp website.
URL: https://morning-savannah-46253.herokuapp.com/

## What packages are in this project?
In order to run the automation, it uses the following libraries:
Selenium: automates your web browser and allows you to write test scripts.
Pytest: provides features to parameterize and assert your test functions and connect to allure for test reporting more seemlessly.
Allure: write test reports.

```bash
python -m pytest --alluredir=Reports_LoginPage_10-27-2022/ TestCases/test_yelpCampLoginPage.py -s -v
```


## Demo
The demo will allow you to open the website, login, and logout of the website

```python

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

# pytest allow you to form your testcases with test object classes and individual units as your
# pytest runs your test functions alphanumerically so I set up the test functions with numbers before their names
class Test_demo(yelpCampBaseTest):

    
    def test_demo(self):

        # 1. Create page objects of the webpages you will neavigate through.

        basePage = yelpCampBasePage()
        
                
        loginPage = yelpCampLoginPage()
        
        
        campgroundsPage = yelpCampCampgroundsPage()

        # 2. Navigate from the home page to the login page.
        
        
        self.do_click_and_verify(basePage.NAV_LOGIN_ATAG, basePage.NAV_LOGIN_ATAG_NAME)


        # 3. Verify that you successfully logged in by verifying that the welcome back div is visible on the campgrounds page.
        

        try:
            
            if EC.visibility_of_element_located(loginPage.LOGIN_BUTTON):
            
                print("You successfully navigated to the login page!")
        
        except Exception as error:
            
            print(error+" You failed to login.")


        # 4. Enter your Login credentials and submit
        
        
        self.do_send_keys_and_verify(loginPage.USERNAME_INPUT, loginPage.USERNAME_INPUT_NAME, Config.USERNAME)
        
        
        
        self.do_send_keys_and_verify(loginPage.PASSWORD_INPUT, loginPage.PASSWORD_INPUT_NAME, Config.PASSWORD)
        


        self.do_click_and_verify(loginPage.LOGIN_BUTTON, loginPage.LOGIN_BUTTON_NAME)
        
        
        # 5. Verify that you logged in by checking that you navigated to the campgrounds page after logging in


        try:
            
            if WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.WELCOME_BACK_ALERT_DIV)):
            
                print("You successfully logged in!")
        
        except Exception as error:
            
            print(str(error)+" You failed to login.")

        
        # 6. Logout

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(campgroundsPage.NAV_LOGOUT_ATAG)).click()


```


Use the venv folder to set up your environment without having to install the libraries on your computer. (Set your directory to the testing folder for simplicity). Use either of these methods to run the environment

### 1. Run as cmd.exe
```bash
(source)\venv\Scripts\activate.bat

```
### 2. Run through powershell
```bash
(source)\venv\Scripts\Activate.ps1
```