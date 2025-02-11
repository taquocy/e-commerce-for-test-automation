import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page_v2 import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Read configuration and initialize browser setup once for all tests."""
        config = configparser.ConfigParser()
        config.read("config.ini")
        cls.login_url = config["app"]["login_url"]
        cls.driver = BrowserSetup.get_driver()

    def setUp(self):
        """Navigate to the login page before each test."""
        self.driver.get(self.login_url)

    def login(self, username, password):
        """Reusable method to handle login."""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

    def test_valid_login_with_admin_account(self):
        """Test valid login with admin account."""
        self.login("superadmin@gmail.com", "admin123")
        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    def test_invalid_login_with_wrong_password(self):
        """Test login with incorrect password."""
        self.login("superadmin@gmail.com", "wrong_password")
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_invalid_login_with_wrong_email(self):
        """Test login with incorrect email."""
        self.login("wrong_email@gmail.com", "admin123")
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_empty_login_fields(self):
        """Test login with empty fields."""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.click_login()
        self.assertEqual(
            "Ban chua nhap dia chi email", login_page.get_email_error_message()
        )
        self.assertEqual(
            "Ban chua nhap mat khau", login_page.get_password_error_message()
        )

    def test_invalid_email_format(self):
        """Test login with invalid email format."""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("213123")
        login_page.click_login()
        self.assertEqual(
            "Định dạng phải có '@' trong chuỗi", login_page.get_email_error_message()
        )

    def test_password_minimum_length(self):
        """Test login with a password less than 16 characters."""
        self.login("test@gmail.com", "12345678")
        password_error = LoginPage(self.driver).get_password_error_message()
        self.assertEqual("Yeu cau toi thieu 16 ky tu", password_error)

    def test_email_minimum_length(self):
        """Test login with an email less than 6 characters."""
        self.login("a@b.c", "validpassword1234")
        email_error = LoginPage(self.driver).get_email_error_message()
        self.assertEqual("Email phai co toi thieu 6 ky tu", email_error)

    def test_login_with_whitespace_email(self):
        """Test login with email containing leading and trailing whitespaces."""
        self.login("  superadmin@gmail.com  ", "admin123")
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_login_with_special_characters_in_password(self):
        """Test login with special characters in the password."""
        self.login("superadmin@gmail.com", "@dm!n#123$")
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_login_with_case_sensitive_email(self):
        """Test login with case-sensitive email."""
        self.login("SuperAdmin@gmail.com", "admin123")
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_login_with_sql_injection_attempt(self):
        """Test login with SQL injection attempt in username."""
        self.login("' OR 1=1; --", "admin123")
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_login_with_password_containing_whitespace(self):
        """Test login with password containing leading or trailing whitespace."""
        self.login("superadmin@gmail.com", " admin123 ")
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_login_with_maximum_password_length(self):
        """Test login with maximum allowed password length."""
        max_length_password = "a" * 64  # Assuming 64 characters as the max length
        self.login("superadmin@gmail.com", max_length_password)
        error_message = LoginPage(self.driver).get_error_message()
        self.assertIn("Invalid credentials", error_message)

    @classmethod
    def tearDownClass(cls):
        """Quit the browser after all tests."""
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
