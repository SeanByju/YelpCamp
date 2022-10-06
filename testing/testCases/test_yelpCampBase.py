import pytest
import unittest


from Pages.yelpCampBasePage import yelpCampBasePage


@pytest.mark.usefixtures("init_driver")
class yelpCampBaseTest(unittest.TestCase):

    pass

