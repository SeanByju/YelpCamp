import pytest

from Pages.yelpCampRegisterPage import test_yelpCampRegisterPage
from TestCases.test_yelpCampBase import yelpCampBaseTest
from testing.Pages.yelpCampRegisterPage import yelpCampRegisterPage

class Test_yelpCampRegisterPage(yelpCampBaseTest):

    def test_register_link_visible(self):
        self.yelpCampRegisterPage = yelpCampRegisterPage(self.driver)
        self.yelpCampRegisterPage.is_register_button_visible()
