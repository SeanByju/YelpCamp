import pytest

from Pages.yelpCampRegisterPage import yelpCampRegisterPage
from test_yelpCampBase import yelpCampBaseTest
from Pages.yelpCampRegisterPage import yelpCampRegisterPage

class Test_yelpCampRegisterPage(yelpCampBaseTest):

    def test_register_button_visible(self):
        self.yelpCampRegisterPage = yelpCampRegisterPage(self.driver)
        flag = self.yelpCampRegisterPage.is_register_button_visible()
        assert flag
