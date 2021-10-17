import unittest

import login_data
from login_functionality import LoginPage


class TestLogin(unittest.TestCase):
    
    login_page = None

    def test_successful_login(self):
        self.login_page.page_login_logic(login_data.username, login_data.password)
        self.assertEqual(True, self.login_page.check_logout_button_exists())

    def test_unsuccessful_login(self):
        self.login_page.page_login_logic(login_data.username, '')
        self.assertEqual(False, self.login_page.check_logout_button_exists())

    @classmethod
    def setUpClass(cls):
        cls.login_page = LoginPage()

    @classmethod
    def tearDownClass(cls):
        cls.login_page = None


if __name__ == '__main__':
    unittest.main()
