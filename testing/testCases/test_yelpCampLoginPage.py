import pytest

from Pages.yelpCampLoginPage import yelpCampLoginPage
from TestCases.test_yelpCampBase import yelpCampBaseTest

class Test_yelpCampLoginPage(yelpCampBaseTest):
    

    def test_signup_link_visible(self):
        self.yelpCampLoginPage = yelpCampLoginPage(self.driver)
        self.yelpCampLoginPage.is_register_button_visible()

    